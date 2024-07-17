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

Assume that the standard library contains a pure Python module :mod:`!foo`
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
- which ``Makefile`` rules to invoke at the end.

Updating the CPython project tree
---------------------------------

Usually, accelerator modules are added in the :cpy-file:`Modules` directory of
the CPython project. If more than one file is needed for the extension module,
it is more convenient to create a sub-directory in :cpy-file:`Modules`.

For our extension, we will create the following files:

- ``Modules/_foo/_foomodule.h`` --- the shared prototypes for our mini-project.
- ``Modules/_foo/_foomodule.c`` --- the actual module's implementation.
- ``Modules/_foo/helper.c`` --- helpers implementation.

We deliberately named the mini-project directory and files with names distinct
from the actual Python module to import (whether it is the pure Python module
or its C implementation) to highlight the differences in configuration files.

.. note::

   If ``Modules/_foo/_foomodule.c`` contains Argument Clinic directives,
   ``make clinic`` creates the file ``Modules/_foo/clinic/_foomodule.c.h``.

The following code snippets illustrate the possible contents of the above files:

.. code-block:: c
   :caption: Modules/_foo/_foomodule.h

   #ifndef _FOO__FOOMODULE_H
   #define _FOO__FOOMODULE_H

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

   /* Helper used in Modules/_foo/_foomodule.c
    * but implemented in Modules/_foo/helper.c.
    */
   extern PyObject *_Py_greet_fast(void);

   #endif // _FOO__FOOMODULE_H

.. code-block:: c
   :caption: Modules/_foo/_foomodule.c

   #include "_foomodule.h"
   #include "clinic/_foomodule.c.h"

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
       // macro available in 'clinic/_foomodule.c.h' after running 'make clinic'
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

   Recall that the ``PyInit_<MODNAME>`` function must be suffixed by the *same*
   module name as that of :c:member:`PyModuleDef.m_name` (here, ``fastfoo``).
   The other identifiers or functions such as those used in Argument Clinic
   inputs or as local variables do not have such naming requirements.

.. code-block:: c
   :caption: Modules/_foo/helper.c

   #include "_foomodule.h"

   PyObject *_Py_greet_fast(void) {
       return PyUnicode_FromString("Hello World!");
   }

.. tip::

   Do not forget that symbols exported by ``libpython`` must start
   with ``Py`` or ``_Py``, which can be verified by ``make smelly``.

One could imagine having more ``.h`` files, or no ``helper.c`` file. Here,
we wanted to illustrate a simple example without making it too trivial. If
the extension module does not require additional files, it may directly be
placed in :cpy-file:`Modules` as ``Modules/_foomodule.c`` for instance.

Extension Modules Types
-----------------------

Extension modules can be classified into the following types:

* A *built-in* extension module is a module built and shipped with
  the Python interpreter. A built-in module is *statically* linked
  into the interpreter, thereby lacking a :attr:`__file__` attribute.

  .. seealso:: :data:`sys.builtin_module_names` --- names of built-in modules.

* A *shared* (or *dynamic*) extension module is built as a shared library
  (``.so`` or ``.dll`` file) and is *dynamically* linked into the interpreter.

  In particular, the module's :attr:`__file__` attribute contains the path
  to the ``.so`` or ``.dll`` file.

Built-in extension modules are part of the interpreter, while shared extension
modules might be supplied or overridden externally.

In particular, built-in extension modules do not need to have a pure Python
implementation but shared extension modules should have one in case the shared
library is not present on the system.

.. note::

   Usually, accelerator modules are built as *shared* extension modules,
   especially if they already have a pure Python implementation.

Make the CPython project compile
--------------------------------

Once we have our files, we need to update some configuration files.

Updating :cpy-file:`configure.ac`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Locate the ``SRCDIRS`` variable and add the following line:

  .. code-block:: text
     :caption: :cpy-file:`configure.ac`
     :emphasize-lines: 4

     AC_SUBST([SRCDIRS])
     SRCDIRS="\
     ...
     Modules/_foo \
     ..."

  .. note::

     This step is only needed when adding new source directories to
     the CPython project.

* Find the section containing ``PY_STDLIB_MOD`` and ``PY_STDLIB_MOD_SIMPLE``
  usages and add the following line:

  .. code-block:: text
     :caption: :cpy-file:`configure.ac`
     :emphasize-lines: 3

     dnl always enabled extension modules
     ...
     PY_STDLIB_MOD_SIMPLE([fastfoo], [-I\$(srcdir)/Modules/_foo], [])
     ...

  The ``PY_STDLIB_MOD_SIMPLE`` macro takes as arguments:

  * the module name as specified by :c:member:`PyModuleDef.m_name`,
  * the compiler flags (CFLAGS), and
  * the linker flags (LDFLAGS).

  If the extension module may not be enabled or supported depending on the
  host configuration. use ``PY_STDLIB_MOD`` which takes as arguments:

  * the module name as specified by :c:member:`PyModuleDef.m_name`,
  * a boolean indicating whether the extension is **enabled** or not,
  * a boolean indicating whether the extension is **supported** or not,
  * the compiler flags (CFLAGS), and
  * the linker flags (LDFLAGS).

  For instance, enabling the ``fastfoo`` extension on Linux systems, but
  only providing support for 32-bit architecture is achieved as follows:

  .. code-block:: text
     :caption: :cpy-file:`configure.ac`
     :emphasize-lines: 2, 3

     PY_STDLIB_MOD([fastfoo],
                   [test "$ac_sys_system" = "Linux"],
                   [test "$ARCH_RUN_32BIT" = "true"],
                   [-I\$(srcdir)/Modules/_foo], [])

  More generally, the status of the extension is determined as follows:

      +-----------+-----------------+----------+
      | Enabled   | Supported       | Status   |
      +===========+=================+==========+
      | true      | true            | yes      |
      +-----------+-----------------+----------+
      | true      | false           | missing  |
      +-----------+-----------------+----------+
      | false     | true or false   | disabled |
      +-----------+-----------------+----------+

  The extension status is ``n/a`` if the extension is marked unavailable
  via the ``PY_STDLIB_MOD_SET_NA`` macro. To add an unavailable extension,
  find the usage of ``PY_STDLIB_MOD_SET_NA`` in :cpy-file:`configure.ac`
  and add the following line:

  .. code-block:: text
     :caption: :cpy-file:`configure.ac`
     :emphasize-lines: 4

     dnl Modules that are not available on some platforms
     AS_CASE([$ac_sys_system],
         ...
         [PLATFORM_NAME], [PY_STDLIB_MOD_SET_NA([fastfoo])],
         ...
     )

Updating :cpy-file:`Makefile.pre.in`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If needed, add the following line to the section for module dependencies:

.. code-block:: text
   :caption: :cpy-file:`Makefile.pre.in`
   :emphasize-lines: 4

   ##########################################################################
   # Module dependencies and platform-specific files
   ...
   MODULE_FASTFOO_DEPS=$(srcdir)/Modules/_foo/_foomodule.h
   ...

Updating MSVC project files
^^^^^^^^^^^^^^^^^^^^^^^^^^^

We describe the minimal steps for compiling on Windows using MSVC.

* Update :cpy-file:`PC/config.c`:

  .. code-block:: c
     :caption: :cpy-file:`PC/config.c`
     :emphasize-lines: 3, 8

     ...
     // add the entry point prototype
     extern PyObject* PyInit_fastfoo(void);
     ...
     // update the entry points table
     struct _inittab _PyImport_Inittab[] = {
        ...
        {"fastfoo", PyInit_fastfoo},
        ...
        {0, 0}
     };
     ...

* Update :cpy-file:`PCbuild/pythoncore.vcxproj`:

  .. code-block:: xml
     :caption: :cpy-file:`PCbuild/pythoncore.vcxproj`
     :emphasize-lines: 4, 11-12

     <!-- group with header files ..\Modules\<MODULE>.h -->
     <ItemGroup>
       ...
       <ClInclude Include="..\Modules\_foo\_foomodule.h" />
       ...
     </ItemGroup>

     <!-- group with source files ..\Modules\<MODULE>.c -->
     <ItemGroup>
       ...
       <ClCompile Include="..\Modules\_foo\_foomodule.c" />
       <ClCompile Include="..\Modules\_foo\helper.c" />
       ...
     </ItemGroup>

* Update :cpy-file:`PCbuild/pythoncore.vcxproj.filters`:

  .. code-block:: xml
     :caption: :cpy-file:`PCbuild/pythoncore.vcxproj.filters`
     :emphasize-lines: 4-6, 13-18

     <!-- group with header files ..\Modules\<MODULE>.h -->
     <ItemGroup>
       ...
       <ClInclude Include="..\Modules\_foo\_foomodule.h">
         <Filter>Modules\_foo</Filter>
       </ClInclude>
       ...
     </ItemGroup>

     <!-- group with source files ..\Modules\<MODULE>.c -->
     <ItemGroup>
       ...
       <ClCompile Include="..\Modules\_foo\_foomodule.c">
         <Filter>Modules\_foo</Filter>
       </ClCompile>
       <ClCompile Include="..\Modules\_foo\helper.c">
         <Filter>Modules\_foo</Filter>
       </ClCompile>
       ...
     <ItemGroup>

.. tip::

   Header files use ``<ClInclude>`` tags, whereas
   source files use ``<ClCompile>`` tags.

Updating :cpy-file:`!Modules/Setup.{bootstrap,stdlib}.in`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Depending on whether the extension module is required to get a functioning
interpreter or not, we update :cpy-file:`Modules/Setup.bootstrap.in` or
:cpy-file:`Modules/Setup.stdlib.in`. In the former case, the module is
necessarily built as a built-in module.

.. tip::

   For accelerator modules, :cpy-file:`Modules/Setup.stdlib.in` should be
   preferred over :cpy-file:`Modules/Setup.bootstrap.in`.

For built-in extension modules, update :cpy-file:`Modules/Setup.bootstrap.in`
by adding the following line after the ``*static*`` marker:

.. code-block:: text
   :caption: :cpy-file:`Modules/Setup.bootstrap.in`
   :emphasize-lines: 3

   *static*
   ...
   fastfoo _foo/_foomodule.c _foo/helper.c
   ...

For other extension modules, update :cpy-file:`Modules/Setup.stdlib.in`
by adding the following line after the ``*@MODULE_BUILDTYPE@*`` marker
but before the ``*shared*`` marker:

.. code-block:: text
   :caption: :cpy-file:`Modules/Setup.stdlib.in`
   :emphasize-lines: 3

   *@MODULE_BUILDTYPE@*
   ...
   @MODULE_FASTFOO_TRUE@fastfoo _foo/_foomodule.c _foo/helper.c
   ...
   *shared*

The ``@MODULE_<NAME>_TRUE@<name>`` marker expects ``<NAME>`` to be the
upper-cased module name ``<name>``. If the extension module must be built
as a *shared* module, put the ``@MODULE_FASTFOO_TRUE@fastfoo`` line after
the ``*shared*`` marker:

.. code-block:: text
   :caption: :cpy-file:`Modules/Setup.stdlib.in`
   :emphasize-lines: 4

   ...
   *shared*
   ...
   @MODULE_FASTFOO_TRUE@fastfoo _foo/_foomodule.c _foo/helper.c

Compile the CPython project
---------------------------

Now that everything is in place, it remains to compile the project:

.. code-block:: shell

   make regen-configure
   ./configure
   make regen-all
   make regen-stdlib-module-names
   make

.. tip::

   Use ``make -j12`` to speed-up compilation if you have enough CPU cores.

* ``make regen-configure`` updates the :cpy-file:`configure` script.

* ``make regen-all`` is responsible for regenerating header files and
  invoking other scripts, such as :ref:`Argument Clinic <clinic>`.
  Execute this rule if you do not know which files should be updated.

* ``regen-stdlib-module-names`` updates the standard module names, making
  :mod:`!fastfoo` discoverable and importable via ``import fastfoo``.

* The final ``make`` step is generally not needed since ``make regen-all``
  and ``make regen-stdlib-module-names`` may completely rebuild the project,
  but it could be needed in some specific cases.

Troubleshooting
---------------

This section addresses common issues that you may face when following this tutorial.

No rule to make target ``regen-configure``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This usually happens after running ``make distclean`` (which removes
the ``Makefile``). The solution is to regenerate :cpy-file:`configure`:

.. code-block:: shell

   ./configure            # for creating a Makefile
   make regen-configure   # for updating 'configure'
   ./configure            # for updating the Makefile

``make regen-configure`` does not work!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since this rule requires `Docker <https://docs.docker.com/desktop>`_ to be
running, the following can be done on Linux platforms (``systemctl``-based):

.. code-block:: shell

   systemctl status docker          # is the Docker service running?
   sudo systemctl start docker      # start it if it is not
   sudo systemctl restart docker    # or restart it if the issue persists

If Docker complains about missing permissions, this Stack Overflow post
could be useful in solving the issue: `How to fix docker: permission denied
<https://stackoverflow.com/q/48957195/9579194>`_.

Once the Docker service is running, check that you have an `Ubuntu 22.04 image
<https://hub.docker.com/_/ubuntu>`_, or pull it if it is not case:

.. code-block:: shell

   docker images ubuntu:22.04       # check for the Docker image presence
   docker image pull ubuntu:22.04   # or pull the image if needed
