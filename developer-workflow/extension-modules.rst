.. _extension-modules:
.. _extensions:

==================================
Standard library extension modules
==================================

In this section, we could explain how to write a CPython extension with the
C language, but the topic can take a complete book. We will however explain
how to add a new extension module to the standard library, for instance, a
module responsible for accelerating some parts of the library.

For writing a CPython extension itself, we prefer to give you some links
where you can read good documentation:

* https://docs.python.org/dev/c-api/
* https://docs.python.org/dev/extending/
* :pep:`399`
* https://pythonextensionpatterns.readthedocs.io/en/latest/

Adding an extension module to CPython
-------------------------------------

In this section, we assume that the extension module to be added
does not rely on external dependencies and is not a frozen module.

Let us assume that the standard library has the :mod:`!foo` module
which contains some function :func:`!foo.bar`:

.. code-block:: python

   def bar():
       return "Hello World!"

Instead of using the Python implementation of :func:`!foo.bar`, we want to
use its corresponding C implementation exposed as the :mod:`!_foo` module.
Ideally, we want to modify ``foo.py`` as follows:

.. code-block:: python

   try:
       # use the C implementation if possible
       from _foo import bar
   except ImportError:
       # fallback to the pure Python implementation
       def bar():
           return "Hello World!"

Some modules in the standard library are implemented both in C and in Python,
such as :mod:`decimal` or :mod:`io`, and the C implementation is expected
to improve performance when available (such modules are usually referred to as
*accelerator modules*). In our example, we need to:

- determine where to place the extension module;
- determine which files to modify in order to compile the project;
- determine which ``Makefile`` rules to invoke at the end.

Usually, accelerator modules are added in the :cpy-file:`Modules` directory of
the CPython project. If more than one file is needed for the extension
module, it is convenient to create a sub-directory in :cpy-file:`Modules`, and
place the files inside it. In our example, we will assume that we have
the following structure:

- ``Modules/foo/foomodule.h`` -- the shared prototypes for our mini-project.
- ``Modules/foo/foomodule.c`` -- the actual module's implementation.
- ``Modules/foo/helper.c``    -- some helper's implementation.

.. note::

   If ``Modules/foo/foomodule.c`` contains some Argument Clinic directives,
   the corresponding header file is written to ``Modules/foo/clinic/foomodule.c.h``.

The following code snippets illustrate the possible contents of the above files:

.. code-block:: c

   // Modules/foo/foomodule.h

   #ifndef FOO_FOOMODULE_H
   #define FOO_FOOMODULE_H

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

   /* Helper implemented somewhere else. */
   extern PyObject *_Py_fast_bar();

   #endif // FOO_FOOMODULE_H

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
       // the following macro is available in 'Modules/foo/clinic/foomodule.c.h'
       // after running 'make clinic'
       FOO_BAR_METHODDEF
       {NULL, NULL}
   };

   static struct PyModuleDef_Slot foomodule_slots[] = {
       {Py_mod_exec, foomodule_exec}, // 'foomodule_exec' may be NULL if the state is trivial
       {Py_mod_multiple_interpreters, Py_MOD_PER_INTERPRETER_GIL_SUPPORTED},
       {Py_mod_gil, Py_MOD_GIL_NOT_USED},
       {0, NULL},
   };

   static struct PyModuleDef foomodule = {
       PyModuleDef_HEAD_INIT,
       .m_name = "_foo",                  // name to use in 'import' statements
       .m_doc = "some doc",               // or NULL if not needed
       .m_size = sizeof(foomodule_state),
       .m_methods = foomodule_methods,
       .m_slots = foomodule_slots,
       .m_traverse = foomodule_traverse,  // or NULL if the state is trivial
       .m_clear = foomodule_clear,        // or NULL if the state is trivial
       .m_free = foomodule_free,          // or NULL if the state is trivial
   };

   PyMODINIT_FUNC
   PyInit_foo(void)
   {
       return PyModuleDef_Init(&_foomodule);
   }

In a separate file, we would have the implementation of ``_Py_fast_bar``:

.. code-block:: c

   // Modules/foo/helper.c

   #include "foomodule.h"

   PyObject *_Py_fast_bar() {
       return PyUnicode_FromString("Hello World!");
   }

.. tip::

   Do not forget that symbols exported by ``libpython`` must start
   with ``Py`` or ``_Py``, which is verified via ``make smelly``.

One could imagine having more ``.h`` files, or no ``helper.c`` file if it is
not needed. Here, we wanted to illustrate a simple example without making it
too trivial.

Make the CPython project compile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that we have our files, we need to update the :cpy-file:`Makefile.pre.in` file.
First, define the following the variables:

.. code-block:: makefile

   FOO_H = Modules/foo/foomodule.h
   FOO_OBJS = Modules/foo/foomodule.o Modules/foo/helper.o

and place them in the **Modules** section where other pre-defined objects live such
as ``MODULE_OBJS`` and ``IO_OBJS``. Then, add the following rule in the section for
**Special rules for object files**:

.. code-block:: makefile

   $(FOO_OBJS): $(FOO_H)

and the following rule in the section for **Module dependencies and platform-specific files**:

.. code-block:: makefile

   MODULE_FOO_DEPS=$(srcdir)/Modules/foo/foomodule.h

.. note::

   The ``FOO_OBJS`` and ``FOO_H`` are not necessarily needed and the rule
   ``$(FOO_OBJS): $(FOO_H)`` could be hard-coded. Using Makefile variables
   is generally better if multiple files need to be compiled.

Finally, we need to modify the configuration for Windows platforms:

- Open :cpy-file:`PC/config.c` and add the prototype:

  .. code-block:: c

     extern PyObject* PyInit_foo(void);

  and the entry ``{"foo", PyInit_foo}`` to ``_PyImport_Inittab``.

- Open :cpy-file:`PCbuild/pythoncore.vcxproj` and add the following line to
  the ``<ItemGroup>`` containing the other ``..\Modules\*.h`` files:

  .. code-block:: xml

     <ClInclude Include="..\Modules\foo\foomodule.h" />

  In addition, add the following lines to the ``<ItemGroup>``
  containing the the other ``..\Modules\*.c`` files:

  .. code-block:: xml

     <ClCompile Include="..\Modules\foo\foomodule.c" />
     <ClCompile Include="..\Modules\foo\helper.c" />

- Open :cpy-file:`PCbuild/pythoncore.vcxproj.filters` and add the following line to
  the ``ItemGroup`` containing the the other ``..\Modules\*.h`` files:

  .. code-block:: xml

     <ClInclude Include="..\Modules\foo\foomodule.h">
         <Filter>Modules\foo</Filter>
     </ClInclude>

  In addition, add the following lines to the ``ItemGroup`` containing
  the the other ``..\Modules\*.c`` files:

  .. code-block:: xml

     <ClCompile Include="..\Modules\foo\foomodule.c">
       <Filter>Modules\foo</Filter>
     </ClCompile>
     <ClCompile Include="..\Modules\foo\helper.c">
       <Filter>Modules\foo</Filter>
     </ClCompile>

Observe that ``.h`` files use ``<ClInclude ...>`` whereas ``.c`` files
use ``<ClCompile ...>`` tags.

Compile the CPython project
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that everything is in place, it remains to compile the project:

.. code-block:: shell

   make regen-configure
   make regen-all
   make regen-stdlib-module-names

- The ``make regen-configure`` step regenerates the configure script.

- The ``make regen-all`` is responsible for running Arguments Clinic,
  regenerating global objects, etc. It is useful to run when you do not
  know which files should be updated.

- The ``regen-stdlib-module-names`` updates the standard module names,
  making ``_foo`` discoverable and importable via ``import _foo``.

You can now compile the entire project by running the following commands:

.. code-block:: shell

   ./configure --with-pydebug
   make

.. tip:: Use ``make -j12`` to speed-up compilation if you have enough CPU cores.

Troubleshooting
^^^^^^^^^^^^^^^

This section addresses common issues that you may face when following this tutorial.

``make regen-configure`` does not work!
.......................................

Since this rule requires Docker to be running and a Docker instance,
the following can be done on Linux platforms (``systemctl``-based):

.. code-block:: shell

   systemctl status docker         # is the docker service running?
   sudo systemctl start docker     # start it if not!
   sudo systemctl restart docker   # or restart it!

If Docker complains about missing permissions, this Stack Overflow post
could be useful in solving the issue: `How to fix docker: permission denied
<https://stackoverflow.com/q/48957195/9579194>`_.
