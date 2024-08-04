.. _extension-modules:
.. _extensions:

==================================
Standard library extension modules
==================================

In this section, we are interested in extending the CPython project with
an :term:`extension module`. We will not explain how to write the module
in C but rather explain how to configure the project and make it compile.

Some modules in the standard library, such as :mod:`datetime` or :mod:`pickle`,
have identical implementations in C and Python; the C implementation, when
available, is expected to improve performance (such extension modules are
commonly referred to as *accelerator modules*).

Other modules mainly implemented in Python may import a C helper extension
providing implementation details (for instance, the :mod:`csv` module uses
the internal :mod:`!_csv` module defined in :cpy-file:`Modules/_csv.c`).

For writing an extension module in C, we prefer to give you some links
where you can read good documentation:

* https://docs.python.org/dev/c-api/
* https://docs.python.org/dev/extending/
* :pep:`399`
* https://pythonextensionpatterns.readthedocs.io/en/latest/

Classifying extension modules
=============================

Extension modules can be classified into two categories:

* A *built-in* extension module is a module built and shipped with
  the Python interpreter. A built-in module is *statically* linked
  into the interpreter, thereby lacking a :attr:`__file__` attribute.

  .. seealso:: :data:`sys.builtin_module_names` --- names of built-in modules.

  Built-in modules are built with the :c:macro:`!Py_BUILD_CORE_BUILTIN`
  macro defined.

* A *shared* (or *dynamic*) extension module is built as a shared library
  (``.so`` or ``.dll`` file) and is *dynamically* linked into the interpreter.

  In particular, the module's :attr:`__file__` attribute contains the path
  to the ``.so`` or ``.dll`` file.

  Shared modules are built with the :c:macro:`!Py_BUILD_CORE_MODULE`
  macro defined. Using the :c:macro:`!Py_BUILD_CORE_BUILTIN` macro
  instead causes an :exc:`ImportError` when importing the module.

.. note::

   Informally, built-in extension modules can be regarded as *required*
   while shared extension modules are *optional* in the sense that they
   might be supplied, overridden or disabled externally.

   Usually, accelerator modules are built as *shared* extension modules,
   especially if they already have a pure Python implementation.

According to :pep:`399`, *new* extension modules MUST provide a working and
tested pure Python implementation, unless a special dispensation is given.
Please ask the :github:`Steering Council <python/steering-council>` if such
dispensation is needed.

Adding an extension module to CPython
=====================================

Assume that the standard library contains a pure Python module :mod:`!foo`
together with the following :func:`!foo.greet` function:

.. code-block:: python
   :caption: Lib/foo.py

   def greet():
       return "Hello World!"

Instead of using the Python implementation of :func:`!foo.greet`, we want to
use its corresponding C implementation exposed in some :mod:`!_foo` module
written in C. Ideally, we want to modify :cpy-file:`!Lib/foo.py` as follows:

.. code-block:: python
   :caption: Lib/foo.py

   try:
       # use the C implementation if possible
       from _foo import greet
   except ImportError:
       # fallback to the pure Python implementation
       def greet():
           return "Hello World!"

.. note::

   Accelerator modules should *never* be imported directly, whence the
   convention is to mark them as private implementation details with the
   underscore prefix (namely, :mod:`!_foo` in this example).

In order to incorporate the accelerator module, we need to determine:

- where to place the extension module source code in the CPython project tree,
- which files to modify in order to compile the CPython project, and
- which ``Makefile`` rules to invoke at the end.

Updating the CPython project tree
---------------------------------

Usually, accelerator modules are added in the :cpy-file:`Modules` directory of
the CPython project. If more than one file is needed for the extension module,
it is more convenient to create a sub-directory in :cpy-file:`Modules`.

For our extension module :mod:`!_foo`, we consider the following working tree:

- :ref:`Modules/_foo/_foomodule.c` --- the extension module implementation.
- :ref:`Modules/_foo/helper.h` --- the extension helpers declarations.
- :ref:`Modules/_foo/helper.c` --- the extension helpers implementations.

By convention, the source file containing the extension module implementation
is called ``<NAME>module.c``, where ``<NAME>`` is the name of the module that
will be later imported (in our case :mod:`!_foo`). In addition, the directory
containing the implementation should also be named similarly.

One could imagine having more files, or no helper files at all. Here,
we wanted to illustrate a simple example without making it too trivial. If
the extension module does not require additional files, it may directly be
placed in :cpy-file:`Modules` as ``Modules/_foomodule.c``.

.. code-block:: c
   :caption: Modules/_foo/helper.h
   :name: Modules/_foo/helper.h

   #ifndef _FOO_HELPER_H
   #define _FOO_HELPER_H

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
   extern PyObject *
   _Py_greet_fast(void);

   #endif // _FOO_HELPER_H

.. tip::

   Functions or data that do not need to be shared across different C source
   files should be declared ``static`` to avoid exporting their symbols from
   ``libpython``.

   If symbols need to be exported, their names must start with ``Py`` or
   ``_Py``. This can be verified by ``make smelly``. For more details,
   please refer to the section on :ref:`Changing Python's C API <c-api>`.

.. code-block:: c
   :caption: Modules/_foo/helper.c
   :name: Modules/_foo/helper.c

   #include "_foomodule.h"

   PyObject *_Py_greet_fast(void) {
       return PyUnicode_FromString("Hello World!");
   }

.. code-block:: c
   :caption: Modules/_foo/_foomodule.c
   :name: Modules/_foo/_foomodule.c

   #include "helper.h"
   #include "clinic/_foomodule.c.h"

   /* Functions for the extension module's state */
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
   foo_greet_impl(PyObject *module)
   /*[clinic end generated code: output=... input=...]*/
   {
       return _Py_greet_fast();
   }

   /* Exported module's data */

   static PyMethodDef foomodule_methods[] = {
       // macro in 'clinic/_foomodule.c.h' after running 'make clinic'
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
       .m_name = "_foo",
       .m_doc = "some doc",               // or NULL if not needed
       .m_size = sizeof(foomodule_state),
       .m_methods = foomodule_methods,
       .m_slots = foomodule_slots,
       .m_traverse = foomodule_traverse,  // or NULL if the state is trivial
       .m_clear = foomodule_clear,        // or NULL if the state is trivial
       .m_free = foomodule_free,          // or NULL if the state is trivial
   };

   PyMODINIT_FUNC
   PyInit__foo(void)
   {
       return PyModuleDef_Init(&foomodule);
   }

.. tip::

   Recall that the ``PyInit_<NAME>`` function must be suffixed by the
   module name ``<NAME>`` used in import statements (here ``_foo``),
   and which usually coincides with :c:member:`PyModuleDef.m_name`.

   Other identifiers such as those used in :ref:`Argument Clinic <clinic>`
   inputs do not have such naming requirements.

Configuring the CPython project
-------------------------------

Now that we have implemented our extension module, we need to update some
configuration files in order to compile the CPython project on different
platforms.

Updating :cpy-file:`!Modules/Setup.{bootstrap,stdlib}.in`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Depending on whether the extension module is required to get a functioning
interpreter or not, we update :cpy-file:`Modules/Setup.bootstrap.in` or
:cpy-file:`Modules/Setup.stdlib.in`. In the former case, the extension
module is necessarily built as a built-in extension module.

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
   _foo _foo/_foomodule.c _foo/helper.c
   ...

The syntax is ``<NAME> <SOURCES>`` where ``<NAME>`` is the name of the
module used in :keyword:`import` statements and ``<SOURCES>`` is the list
of space-separated source files.

For other extension modules, update :cpy-file:`Modules/Setup.stdlib.in`
by adding the following line after the ``*@MODULE_BUILDTYPE@*`` marker
but before the ``*shared*`` marker:

.. code-block:: text
   :caption: :cpy-file:`Modules/Setup.stdlib.in`
   :emphasize-lines: 3

   *@MODULE_BUILDTYPE@*
   ...
   @MODULE__FOO_TRUE@_foo _foo/_foomodule.c _foo/helper.c
   ...
   *shared*

The ``@MODULE_<NAME_UPPER>_TRUE@<NAME>`` marker expects ``<NAME_UPPER>`` to
be the upper-cased form of ``<NAME>``, where ``<NAME>`` has the same meaning
as before (in our case, ``<NAME_UPPER>`` and ``<NAME>`` are ``_FOO`` and
``_foo`` respectively). The marker is followed by the list of source files.

If the extension module must be built as a *shared* module, put the
``@MODULE__FOO_TRUE@_foo`` line after the ``*shared*`` marker:

.. code-block:: text
   :caption: :cpy-file:`Modules/Setup.stdlib.in`
   :emphasize-lines: 4

   ...
   *shared*
   ...
   @MODULE__FOO_TRUE@_foo _foo/_foomodule.c _foo/helper.c

Updating :cpy-file:`configure.ac`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. add section about configuration variable afterwards

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
     PY_STDLIB_MOD_SIMPLE([_foo], [-I\$(srcdir)/Modules/_foo], [])
     ...

  The ``PY_STDLIB_MOD_SIMPLE`` macro takes as arguments:

  * the module name ``<NAME>`` used in :keyword:`import` statements,
  * the compiler flags (CFLAGS), and
  * the linker flags (LDFLAGS).

  If the extension module may not be enabled or supported depending on the
  host configuration, use the ``PY_STDLIB_MOD`` macro instead, which takes
  as arguments:

  * the module name ``<NAME>`` used in :keyword:`import` statements,
  * a boolean indicating whether the extension is **enabled** or not,
  * a boolean indicating whether the extension is **supported** or not,
  * the compiler flags (CFLAGS), and
  * the linker flags (LDFLAGS).

  For instance, enabling the :mod:`!_foo` extension on Linux platforms, but
  only providing support for 32-bit architecture, is achieved as follows:

  .. code-block:: text
     :caption: :cpy-file:`configure.ac`
     :emphasize-lines: 2, 3

     PY_STDLIB_MOD([_foo],
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
  by the ``PY_STDLIB_MOD_SET_NA`` macro. To mark an extension as unavailable,
  find the usages of ``PY_STDLIB_MOD_SET_NA`` in :cpy-file:`configure.ac` and
  add the following line:

  .. code-block:: text
     :caption: :cpy-file:`configure.ac`
     :emphasize-lines: 4

     dnl Modules that are not available on some platforms
     AS_CASE([$ac_sys_system],
         ...
         [PLATFORM_NAME], [PY_STDLIB_MOD_SET_NA([_foo])],
         ...
     )

.. tip::

   Consider reading the comments and configurations for existing modules
   in :cpy-file:`configure.ac` for guidance on adding new external build
   dependencies for extension modules that need them.

Updating :cpy-file:`Makefile.pre.in`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If needed, add the following line to the section for module dependencies:

.. code-block:: text
   :caption: :cpy-file:`Makefile.pre.in`
   :emphasize-lines: 4

   ##########################################################################
   # Module dependencies and platform-specific files
   ...
   MODULE__FOO_DEPS=$(srcdir)/Modules/_foo/helper.h
   ...

The ``MODULE_<NAME_UPPER>_DEPS`` variable follows the same naming
requirements as the ``@MODULE_<NAME_UPPER>_TRUE@<NAME>`` marker.

Updating MSVC project files
^^^^^^^^^^^^^^^^^^^^^^^^^^^

We describe the minimal steps for compiling on Windows using MSVC.

* Update :cpy-file:`PC/config.c`:

  .. code-block:: c
     :caption: :cpy-file:`PC/config.c`
     :emphasize-lines: 3, 8

     ...
     // add the entry point prototype
     extern PyObject* PyInit__foo(void);
     ...
     // update the entry points table
     struct _inittab _PyImport_Inittab[] = {
        ...
        {"_foo", PyInit__foo},
        ...
        {0, 0}
     };
     ...

  Each item in ``_PyImport_Inittab`` consists of the module name to import,
  here :mod:`!_foo`, together with the corresponding ``PyInit_*`` function
  correctly suffixed.

* Update :cpy-file:`PCbuild/pythoncore.vcxproj`:

  .. code-block:: xml
     :caption: :cpy-file:`PCbuild/pythoncore.vcxproj`
     :emphasize-lines: 4, 11-12

     <!-- group with header files ..\Modules\<MODULE>.h -->
     <ItemGroup>
       ...
       <ClInclude Include="..\Modules\_foo\helper.h" />
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
       <ClInclude Include="..\Modules\_foo\helper.h">
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


Compiling the CPython project
-----------------------------

Now that everything is in place, it remains to compile the project:

.. code-block:: shell

   make regen-configure
   ./configure
   make regen-all
   make regen-stdlib-module-names
   make

.. tip::

   Use ``make -j`` to speed-up compilation by utilizing as many CPU cores
   as possible or ``make -jN`` to allow at most *N* concurrent jobs.

* ``make regen-configure`` updates the :cpy-file:`configure` script.

* ``make regen-all`` is responsible for regenerating header files and
  invoking other scripts, such as :ref:`Argument Clinic <clinic>`.
  Execute this rule if you do not know which files should be updated.

* ``make regen-stdlib-module-names`` updates the standard module names, making
  :mod:`!_foo` discoverable and importable via ``import _foo``.

* The final ``make`` step is generally not needed since the previous ``make``
  invokations may completely rebuild the project, but it could be needed in
  some specific cases.

Troubleshooting
---------------

This section addresses common issues that you may face when following
this tutorial.

No rule to make target ``regen-configure``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This usually happens after running ``make distclean`` (which removes
the ``Makefile``). The solution is to regenerate the :cpy-file:`configure`
script as follows:

.. code-block:: shell

   ./configure            # for creating the 'Makefile' file
   make regen-configure   # for updating the 'configure' script
   ./configure            # for updating the 'Makefile' file

If missing, the :cpy-file:`configure` script can be regenerated
by executing :cpy-file:`Tools/build/regen-configure.sh`:

.. code-block:: shell

   ./Tools/build/regen-configure.sh     # create an up-to-date 'configure'
   ./configure                          # create an up-to-date 'Makefile'

``make regen-configure`` and missing permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since this rule requires `Docker <https://docs.docker.com/desktop>`_ to be
running, the following can be done on Linux platforms (``systemctl``-based):

.. code-block:: shell

   systemctl status docker          # is the Docker service running?
   sudo systemctl start docker      # start it if it is not
   sudo systemctl restart docker    # or restart it if the issue persists

If Docker complains about missing permissions, this Stack Overflow post
could be useful in solving the issue: `How to fix docker: permission denied
<https://stackoverflow.com/q/48957195/9579194>`_.

Once the Docker service is running, check that you have an `Ubuntu
$CONFIGURE_UBUNTU_VERSION$ image <https://hub.docker.com/_/ubuntu>`_,
or pull it if it is not case:

.. code-block:: shell

   # check for the Docker image presence
   docker images ubuntu:$CONFIGURE_UBUNTU_VERSION$
   # pull the Docker image if needed
   docker image pull ubuntu:$CONFIGURE_UBUNTU_VERSION$

.. tip::

   If the issue persists, you may try `podman <https://podman.io/>`_.
   The commands for listing or pulling an image are the same as ``docker``.

Missing ``Py_BUILD_CORE`` define when using internal headers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, the CPython :ref:`Stable ABI <stable-abi>` is exposed via
:code:`#include "Python.h"`. In some cases, this may be insufficient
and internal headers from :cpy-file:`Include/internal` are needed;
in particular, those headers require the :c:macro:`!Py_BUILD_CORE`
macro to be defined.

To that end, one should define the :c:macro:`!Py_BUILD_CORE_BUILTIN`
or the :c:macro:`!Py_BUILD_CORE_MODULE` macro depending on whether the
extension module is built-in or shared. Using either of the two macros
implies :c:macro:`!Py_BUILD_CORE` and gives access to CPython internals:

.. code-block:: c
   :caption: Definition of :c:macro:`!Py_BUILD_CORE_BUILTIN`

   #ifndef Py_BUILD_CORE_MODULE
   #  define Py_BUILD_CORE_BUILTIN 1
   #endif

.. code-block:: c
   :caption: Definition of :c:macro:`!Py_BUILD_CORE_MODULE`

   #ifndef Py_BUILD_CORE_BUILTIN
   #  define Py_BUILD_CORE_MODULE 1
   #endif

Tips
----

In this section, we give some tips for improving the quality of
extension modules meant to be included in the standard library.

Restricting to the Limited API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order for non-CPython implementations to benefit from new extension modules,
it is recommended to use the :ref:`Limited API <limited-c-api>`. Instead of
exposing the entire Stable ABI, define the :c:macro:`Py_LIMITED_API` macro
*before* the :code:`#include "Python.h"` directive:

.. code-block:: c
   :caption: Using the 3.13 Limited API.
   :emphasize-lines: 3, 6

   #include "pyconfig.h"    // Py_GIL_DISABLED
   #ifndef Py_GIL_DISABLED
   #  define Py_LIMITED_API 0x030d0000
   #endif

   #include "Python.h"

This makes the extension module non-CPython implementation-friendly by
removing the dependencies to CPython internals.
