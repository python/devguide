.. _extension-modules:
.. _extensions:

==================================
Standard library extension modules
==================================

In this section, we are interested in extending the CPython project with
an :term:`extension module`. We will not explain how to write the module
in C but rather explain how to configure the project and make it compile.

For writing an extension module in C, we prefer to give you some links
where you can read good documentation:

* https://docs.python.org/dev/c-api/
* https://docs.python.org/dev/extending/
* :pep:`399`
* https://pythonextensionpatterns.readthedocs.io/en/latest/

Adding an extension module to CPython
=====================================

Assume that the standard library contains a pure Python module :mod:`foo`
together with the following :func:`!foo.greet` function:

.. code-block:: python

   def greet():
       return "Hello World!"

Instead of using the Python implementation of :func:`!foo.greet`, we want to
use its corresponding C implementation exposed in some :mod:`!fastfoo` module
written in C. Ideally, we want to modify ``foo.py`` as follows:

.. code-block:: python

   try:
       # use the C implementation if possible
       from fastfoo import greet
   except ImportError:
       # fallback to the pure Python implementation
       def greet():
           return "Hello World!"

Some modules in the standard library are implemented both in C and in Python,
such as :mod:`decimal` or :mod:`itertools`, and the C implementation is expected
to improve performance when available (such modules are commonly referred
to as *accelerator modules*). In our example, we need to determine:

- where to place the extension module source code in the CPython project tree;
- which files to modify in order to compile the CPython project;
- which :cpy-file:`!Makefile` rules to invoke at the end.

Updating the CPython project tree
---------------------------------

Usually, accelerator modules are added in the :cpy-file:`Modules` directory of
the CPython project. If more than one file is needed for the extension module,
it is more convenient to create a sub-directory in :cpy-file:`Modules`.

For our extension, we will create the following files:

- ``Modules/cfoo/foomodule.h`` --- the shared prototypes for our mini-project.
- ``Modules/cfoo/foomodule.c`` --- the actual module's implementation.
- ``Modules/cfoo/helper.c`` --- helpers implementation.

We deliberately named the mini-project directory and files with names distinct
from the actual Python module to import (whether it is the pure Python module
or its C implementation) to highlight the differences in configuration files.

.. note::

   If ``Modules/cfoo/foomodule.c`` contains Argument Clinic directives,
   ``make clinic`` creates the file ``Modules/cfoo/clinic/foomodule.c.h``.

The following code snippets illustrate the possible contents of the above files:

.. code-block:: c

   // Modules/cfoo/foomodule.h

   #ifndef CFOO_FOOMODULE_H
   #define CFOO_FOOMODULE_H

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

   /* Helper used in Modules/cfoo/foomodule.c
    * but implemented in Modules/cfoo/helper.c.
    */
   extern PyObject *_Py_greet_fast();

   #endif // CFOO_FOOMODULE_H


The actual implementation of the module is in the corresponding ``.c`` file:

.. code-block:: c

   // Modules/cfoo/foomodule.c

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

   /* Implementation of publicly exported functions. */

   /*[clinic input]
   module foo
   [clinic start generated code]*/
   /*[clinic end generated code: output=... input=...]*/

   /*[clinic input]
   foo.greet -> object

   [clinic start generated code]*/
   static PyObject *
   foo_greet(PyObject *module)
   /*[clinic end generated code: output=... input=...]*/
   {
       return _Py_greet_fast();
   }

   /* Exported module's data */

   static PyMethodDef foomodule_methods[] = {
       // macro available in 'clinic/foomodule.c.h' after running 'make clinic'
       FOO_GREET_METHODDEF
       {NULL, NULL}
   };

   static struct PyModuleDef_Slot foomodule_slots[] = {
       // 'foomodule_exec' may be NULL if the state is trivial
       {Py_mod_exec, foomodule_exec},
       {Py_mod_multiple_interpreters, Py_MOD_PER_INTERPRETER_GIL_SUPPORTED},
       {Py_mod_gil, Py_MOD_GIL_NOT_USED},
       {0, NULL},
   };

   static struct PyModuleDef foomodule = {
       PyModuleDef_HEAD_INIT,
       .m_name = "fastfoo",               // name to use in 'import' statements
       .m_doc = "some doc",               // or NULL if not needed
       .m_size = sizeof(foomodule_state),
       .m_methods = foomodule_methods,
       .m_slots = foomodule_slots,
       .m_traverse = foomodule_traverse,  // or NULL if the state is trivial
       .m_clear = foomodule_clear,        // or NULL if the state is trivial
       .m_free = foomodule_free,          // or NULL if the state is trivial
   };

   PyMODINIT_FUNC
   PyInit_fastfoo(void)
   {
       return PyModuleDef_Init(&foomodule);
   }

.. tip::

   Recall that the ``PyInit_<MODNAME>`` function must be suffixed by the same
   module name as defined by :c:member:`PyModuleDef.m_mod` (here, ``fastfoo``).
   The other identifiers or functions do not have such naming requirements.

In a separate file, we put the implementation of ``_Py_greet_fast``:

.. code-block:: c

   // Modules/cfoo/helper.c

   #include "foomodule.h"

   PyObject *_Py_greet_fast() {
       return PyUnicode_FromString("Hello World!");
   }

.. tip::

   Do not forget that symbols exported by ``libpython`` must start
   with ``Py`` or ``_Py``, which is verified via ``make smelly``.

One could imagine having more ``.h`` files, or no ``helper.c`` file if it is
not needed. Here, we wanted to illustrate a simple example without making it
too trivial. If the extension module does not require additional files, it
may directly be placed in :cpy-file:`Modules` as ``Modules/foomodule.c``.

Extension Modules Types
-----------------------

Extension modules can be classified into the following types:

- A *built-in* extension module is a module built and shipped with
  the Python interpreter.

  .. note::

     A built-in module is *statically* linked into the interpreter,
     and thereby lacks a :attr:`__file__` attribute.

  .. seealso:: :data:`sys.builtin_module_names`

- A *dynamic* (or *shared*) extension module is built as a *dynamic* library,
  and is *dynamically* linked into the Python interpreter.

  In particular, the corresponding ``.so`` or ``.dll`` file is described by the
  module's :attr:`__file__` attribute.

Built-in extension modules are part of the interpreter, while dynamic extension
modules might be supplied or overridden externally. In particular, the latter
provide a pure Python implementation in case of missing ``.so/.dll`` files.

Make the CPython project compile
--------------------------------

Now that we have our files, we first update :cpy-file:`configure.ac`:

1. Add a line ``Modules/cfoo`` in

   .. code-block:: configure

      AC_SUBST([SRCDIRS])
      SRCDIRS="\
      ...
      Modules/cfoo \
      ..."

   .. note::

      This step is only needed when adding new source directories to
      the CPython project.

2. Find the section containing ``PY_STDLIB_MOD_SIMPLE`` usages and
   add the following line:

   .. code-block:: configure

      PY_STDLIB_MOD_SIMPLE([fastfoo], [-I\$(srcdir)/Modules/cfoo], [])

   The ``PY_STDLIB_MOD_SIMPLE`` macro takes as arguments:

   - the module name as specified by :c:member:`PyModuleDef.m_mod`,
   - the compiler flags (CFLAGS), and
   - the linker flags (LDFLAGS).

Then, we update :cpy-file:`Makefile.pre.in` by adding to the
section **Module dependencies and platform-specific files**:

   .. code-block:: makefile

      MODULE_FASTFOO_DEPS=$(srcdir)/Modules/cfoo/foomodule.h

Additionally, we update the configuration files for Windows platforms:

- Open :cpy-file:`PC/config.c` and add the prototype:

  .. code-block:: c

     extern PyObject* PyInit_fastfoo(void);

  and update the :c:data:`!_PyImport_Inittab`:

  .. code-block:: c

     struct _inittab _PyImport_Inittab[] = {
        ...
        {"fastfoo", PyInit_fastfoo},
        ...
        {0, 0}
     };
     extern PyObject* PyInit_fastfoo(void);

- Open :cpy-file:`PCbuild/pythoncore.vcxproj` and add the following line to
  the ``<ItemGroup>`` containing the other ``..\Modules\*.h`` files:

  .. code-block:: xml

     <ClInclude Include="..\Modules\cfoo\foomodule.h" />

  In addition, add the following lines to the ``<ItemGroup>``
  containing the other ``..\Modules\*.c`` files:

  .. code-block:: xml

     <ClCompile Include="..\Modules\cfoo\foomodule.c" />
     <ClCompile Include="..\Modules\cfoo\helper.c" />

- Open :cpy-file:`PCbuild/pythoncore.vcxproj.filters` and add the following
  line to the ``ItemGroup`` containing the other ``..\Modules\*.h`` files:

  .. code-block:: xml

     <ClInclude Include="..\Modules\cfoo\foomodule.h">
         <Filter>Modules\cfoo</Filter>
     </ClInclude>

  In addition, add the following lines to the ``ItemGroup`` containing
  the other ``..\Modules\*.c`` files:

  .. code-block:: xml

     <ClCompile Include="..\Modules\cfoo\foomodule.c">
       <Filter>Modules\cfoo</Filter>
     </ClCompile>
     <ClCompile Include="..\Modules\cfoo\helper.c">
       <Filter>Modules\cfoo</Filter>
     </ClCompile>

Observe that ``.h`` files use ``<ClInclude ...>`` whereas ``.c`` files
use ``<ClCompile ...>`` tags.

It remains to update :cpy-file:`Modules/Setup.bootstrap.in` if the module is
required to get a functioning interpreter (such module is *always* a built-in
module) or :cpy-file:`Modules/Setup.stdlib.in` otherwise (such module can be
built-in or dynamic).

.. note::

   Built-in modules do not need to have a pure Python implementation
   but optional extension modules should have one in case the shared
   library is not present on the system.

.. rubric:: For required extension modules (built-in)

Open :cpy-file:`Modules/Setup.bootstrap.in` and add the following line:

.. code-block:: text

   fastfoo cfoo/foomodule.c cfoo/helper.c

.. rubric:: For optional extension modules

Open :cpy-file:`Modules/Setup.stdlib.in` and add the following line:

.. code-block:: text

   @MODULE_FASTFOO_TRUE@fastfoo cfoo/foomodule.c cfoo/helper.c

The ``@MODULE_<NAME>_TRUE@<name>`` marker requires ``<NAME>``
to be the upper case form of the module name ``<name>``.

Compile the CPython project
---------------------------

Now that everything is in place, it remains to compile the project:

.. code-block:: shell

   ./Tools/build/regen-configure.sh
   ./configure --with-pydebug
   make regen-all
   make regen-stdlib-module-names
   make

.. tip::

   Use ``make -j12`` to speed-up compilation if you have enough CPU cores.

- Since the shipped version of :cpy-file:`configure` may not be up-to-date for
  the new extension module, ``./Tools/build/regen-configure.sh`` should always
  be executed first. This is equivalent to run ``make regen-configure`` but does
  not require to create a ``Makefile`` first.

  Alternatively, :cpy-file:`configure` can be regenerated as follows:

  .. code-block:: shell

     ./configure            # for creating a Makefile
     make regen-configure   # for updating 'configure'
     ./configure            # for updating the Makefile

- The ``./configure --with-pydebug`` step generates the new Makefile.

- The ``make regen-all`` is responsible for running Arguments Clinic,
  regenerating global objects, etc. It is useful to run when you do not
  know which files should be updated.

- The ``regen-stdlib-module-names`` updates the standard module names,
  making ``fastfoo`` discoverable and importable via ``import fastfoo``.

- The final ``make`` step is generally not needed since ``make regen-all``
  and ``make regen-stdlib-module-names`` may completely rebuild the project,
  but it could be needed in some specific cases.

Troubleshooting
---------------

This section addresses common issues that you may face when following this tutorial.

``make regen-configure`` does not work!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since this rule requires Docker to be running and a Docker instance,
the following can be done on Linux platforms (``systemctl``-based):

.. code-block:: shell

   systemctl status docker          # is the docker service running?
   sudo systemctl start docker      # start it if not!
   sudo systemctl restart docker    # or restart it!

If Docker complains about missing permissions, this Stack Overflow post
could be useful in solving the issue: `How to fix docker: permission denied
<https://stackoverflow.com/q/48957195/9579194>`_.

Once the Docker service is running, check if you have an `Ubuntu 22.04 image
<https://hub.docker.com/_/ubuntu>`_, or pull it if it is not case:

.. code-block:: shell

   docker images ubuntu:22.04       # check for the Docker image presence
   docker image pull ubuntu:22.04   # or pull the image if it does not exist!
