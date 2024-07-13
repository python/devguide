.. _extension-modules:
.. _extensions:

==================================
Standard library extension modules
==================================

In this section, we could explain how to write a CPython extension with the
C language, but the topic can take a complete book. We will however explain
how to add a new extension module to the standard library, e.g., a module
responsible for accelerating some parts of the library.

For writing a CPython extension itself, we prefer to give you some links
where you can read a very good documentation.

Read the following references:

* https://docs.python.org/dev/c-api/
* https://docs.python.org/dev/extending/
* :pep:`399`
* https://pythonextensionpatterns.readthedocs.io/en/latest/

=====================================
Adding an extension module to CPython
=====================================

In this section, we assume that the extension module to be added
does not rely on external dependencies and is not a frozen module.

Let us assume that the standard library has the :mod:`!foo` module
which contains some function :func:`!foo.bar`:

.. code-block:: python

   def bar():
       return "Hello World!"

Instead of using the Python implementation of :func:`!foo.bar`, we want to
use its C implementation that we would have written somewhere else. Ideally,
we want to modify ``foo.py`` as follows:

.. code-block:: python

   try:
       # use the C implementation if possible
       from _foo import bar
   except ImportError:
       # fallback to the pure Python implementation
       def bar():
           return "Hello World!"

Some modules in the standard library are implemented both in C and in Python,
such as :mod:`functools` or :mod:`io`, and the C implementation should offer
improved performances when available (such modules are usually referred to as
*accelerator modules*). In our example, we need to

- determine where the extension module is to be placed;
- determine which files to modify in order to compile the project;
- determine which Makefile rules to invoke in the end.

In general, accelerator modules are added in the ``Modules/`` directory
of the CPython project. If more than one file is needed for the extension
module, it is convenient to create a sub-directory in ``Modules/`` and place
the files inside it. For instance,

.. code-block:: c

   // Modules/foo/foomodule.h: file containing shared prototypes

   #ifndef FOOMODULE_H
   #define FOOMODULE_H

   #include "Python.h"

   typedef struct {
       /* ... */
   } foomodule_state;

   static inline foomodule_state *
   get_foomodule_state(PyObject *module)
   {
       void *state = PyModule_GetState(module);
       assert(state != NULL);
       return (foomodule_state *)state;
   }

   /* helper implemented somewhere else */
   extern PyObject *_Py_fast_bar();

   #endif // FOOMODULE_H

The actual implementation of the module is in the corresponding ``.c`` file:

.. code-block:: c

   // Modules/foo/foomodule.c

   #include "foomodule.h"
   #include "clinic/foomodule.c.h"

   /* Functions for the module's state */
   static int
   foomodule_exec(PyObject *module)
   {
       // imports, static attributes, exported classes, etc
       return 0;
   }

   static int
   foomodule_traverse(PyObject *m, visitproc visit, void *arg)
   {
       foomodule_state *st = get_foomodule_state(m);
       // call Py_VISIT() on the state attributes
       return 0;
   }

   static int
   foomodule_clear(PyObject *m)
   {
       foomodule_state *st = get_foomodule_state(m);
       // call Py_CLEAR() on the state attributes
       return 0;
   }

   static void
   foomodule_free(void *m) {
       (void)foomodule_clear((PyObject *)m);
   }

   /* Implementation of publicly exported functions */

   /*[clinic input]
   module foo
   [clinic start generated code]*/
   /*[clinic end generated code: output=... input=...]*/

   /*[clinic input]
   foo.bar -> object

   [clinic start generated code]*/
   static PyObject *
   foo_bar_impl(PyObject *module)
   /*[clinic end generated code: output=... input=...]*/
   {
       return _Py_fast_bar();
   }

   /* Exported module's data */

   static PyMethodDef foomodule_methods[] = {
       FOO_BAR_METHODDEF  // this becomes available after running 'make clinic'
       {NULL, NULL}
   };

   static struct PyModuleDef_Slot foomodule_slots[] = {
       {Py_mod_exec, foomodule_exec}, // foomodule_exec may be NULL if the state is trivial
       {Py_mod_multiple_interpreters, Py_MOD_PER_INTERPRETER_GIL_SUPPORTED},
       {Py_mod_gil, Py_MOD_GIL_NOT_USED},
       {0, NULL},
   };

   static struct PyModuleDef foomodule = {
       PyModuleDef_HEAD_INIT,
       .m_name = "_foo",
       .m_doc = "some doc",               // or NULL if not needed
       .m_size = sizeof(foomodule_state),
       .m_methods = foomodule_methods,
       .m_slots = foomodule_slots,
       .m_traverse = foomodule_traverse,  // or NULL if the state is trivial
       .m_clear = foomodule_clear,	      // or NULL if the state is trivial
       .m_free = foomodule_free,		  // or NULL if the state is trivial
   };

   PyMODINIT_FUNC
   PyInit_foo(void)
   {
       return PyModuleDef_Init(&_foomodule);
   }

In a separate file, we would have the implementation of ``Py_fast_bar``:

.. code-block:: c

   // Modules/foo/helper.c

   #include "foomodule.h"

   PyObject *_Py_fast_bar() {
       return PyUnicode_FromString("Hello World!");
   }

Now, to summarize, we have the following files:

- ``Modules/foo/foomodule.h`` -- the shared prototypes for our mini-project.
- ``Modules/foo/foomodule.c`` -- the actual module's implementation.
- ``Modules/foo/helper.c``    -- some helper's implementation.

One could imagine having more ``.h`` files, or no ``helper.c`` file if it is
not needed. Here, we wanted to illustrate a simple example without making it
too trivial.

### Make the CPython project compile

Now that we have our files, we need to update the ``Makefile.pre.in`` file.
First, define the following the variables:

```makefile
FOO_H = Modules/foo/foomodule.h

FOO_OBJS =	\
	Modules/foo/foomodule.o \
	Modules/foo/helper.o
```

and place them somewhere in the file (usually where other variables of the
same kind are).

Then, add the following rule in the '# Special rules for object files' section:

```makefile
$(FOO_OBJS): $(FOO_H)
```

and the following rule in the dependencies section:

```makefile
MODULE_FOO_DEPS=$(srcdir)/Modules/foo/foomodule.h
```

.. note::

   The ``FOO_OBJS`` and ``FOO_H`` are not necessarily needed and the rule
   ``$(FOO_OBJS): $(FOO_H)`` could be hard-coded. Using Makefile variables
   is generally better if more than multiple files need to be compiled.

Finally, we need to modify the configuration for Windows platforms:

- Open ``PC/config.c`` and add the prototype:

  .. code-block:: c

     extern PyObject* PyInit_foo(void);

  and the entry ``{"foo", PyInit_foo}`` to ``_PyImport_Inittab``.

- Open ``PCbuild/pythoncore.vcxproj`` and add the following line to
  the ``ItemGroup`` containing the ``..\Modules\*.h`` files:

  .. code-block:: xml

     <ClInclude Include="..\Modules\foo\foomodule.h" />

  In addition, add the following lines to the ``ItemGroup`` containing
  the ``..\Modules\*.c`` files:

  .. code-block:: xml

     <ClCompile Include="..\Modules\foo\foomodule.c" />
     <ClCompile Include="..\Modules\foo\helper.c" />

- Open ``PCbuild/pythoncore.vcxproj.filters`` and add the following line to
  the ``ItemGroup`` containing the ``..\Modules\*.h`` files:

  .. code-block:: xml

     <ClInclude Include="..\Modules\foo\foomodule.h">
         <Filter>Modules\foo</Filter>
     </ClInclude>

  In addition, add the following lines to the ``ItemGroup`` containing
  the ``..\Modules\*.c`` files:

  .. code-block:: xml

     <ClCompile Include="..\Modules\foo\foomodule.c">
       <Filter>Modules\foo</Filter>
     </ClCompile>
     <ClCompile Include="..\Modules\foo\helper.c">
       <Filter>Modules\foo</Filter>
     </ClCompile>

Observe that ``.h`` files use ``<ClInclude ...>`` whereas ``.c`` files
use ``<ClCompile ...>`` tags.

### Compile the CPython project

Now that everything is in place, it remains to compile everything. To that
end, run the following commands:

.. code-block:: shell

   make regen-configure
   make regen-all
   make regen-stdlib-module-names

.. tip:: Use ``make -j12`` to speed-up the compilation.

- The ``make regen-configure`` step regenerates the configure script.

- The ``make regen-all`` is responsible for running Arguments Clinic,
  regenerating global objects, etc. It is useful to run when you do not
  know which files should be updated.

- The ``regen-stdlib-module-names`` updates the standard module names,
  making ``_foo`` discoverable and importable via ``import _foo``!

You can now compile the entire project by running the following commands:

.. code-block:: shell

   ./configure --with-pydebug
   make

#### Troubleshooting: ``make regen-configure`` does not work!

Since this rule requires Docker to be running and a Docker instance,
the following can be done on Linux platforms (systemctl-based):

.. code-block:: shell

   $ systemctl status docker        # is the docker service running?
   $ sudo systemctl start docker    # start it if not!
   $ sudo systemctl restart docker  # or restart it!

If docker complains about missing permissions, the following StackOverflow post
could be useful in solving the issue: `How to fix docker: permission denied
<https://stackoverflow.com/q/48957195/9579194>`_
