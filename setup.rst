.. _setup:

Getting Set Up
==============

These instructions cover how to get a working copy of the source code and a
compiled version of the CPython interpreter (CPython is the version of Python
available from http://www.python.org/). It also gives an overview of the
directory structure of the CPython source code.

.. contents::


Version Control Setup
---------------------

CPython is developed using `Mercurial (commonly abbreviated 'hg')
<http://hg-scm.org/>`_.
It is easily available for common Unix systems by way of the standard package
manager; under Windows, you might want to use the `TortoiseHg
<http://tortoisehg.org/>`_ graphical client.


.. _checkout:

Checking out the code
----------------------

One should always work from a working copy of the CPython source code.
While it may
be tempting to work from the copy of Python you already have installed on your
machine, it is very likely that you will be working from out-of-date code as
the Python core developers are constantly updating and fixing things in their
:abbr:`VCS`. It also means you will have better tool
support through the VCS as it will provide a diff tool, etc.

To get a read-only checkout of
the :ref:`in-development <indevbranch>` branch of Python, run::

    hg clone http://hg.python.org/cpython

If you want a read-only checkout of an already-released version of Python,
i.e., a version in :ref:`maintenance mode <maintbranch>`, run something
like the following which gets you a working copy of Python 3.1::

    hg clone http://hg.python.org/cpython#release-31maint

To check out a version of Python other than 3.1, simply change the number in
the above URL to the major/minor version (e.g., ``release27-maint`` for Python
2.7). You may also update a working copy to other branches of CPython by using
``hg update``.

Do note that CPython will notice that it is being run from a working copy.
This means that it if you edit CPython's source code in your working copy the
changes will be picked up by the interpreter for immediate use and testing.


Compiling (for debugging)
-------------------------

CPython provides several compilation flags which help with debugging various
things. While all of the known flags can be found in the
``Misc/SpecialBuilds.txt``
file, the most critical one is the ``Py_DEBUG`` flag which creates what is
known as a "pydebug" build. This flag turns on
various extra sanity checks which help catch common issues. The use of the flag
is so common that turning on the flag is a basic compile option.

You should always
develop under a pydebug build of CPython (the only instance of when you
shouldn't is if you are taking performance measurements). Even when working
only on pure Python code the pydebug build provides several useful checks that
one should not skip.


Build dependencies
''''''''''''''''''

The core CPython interpreter only needs a C compiler to be built; if
you get compile errors with a C89 or C99-compliant compiler, please `open a
bug report <http://bugs.python.org>`_.
However, some of the extension modules will need development headers
for additional libraries (such as the ``zlib`` library for compression).
Depending on what you intend to work on, you might need to install these
additional requirements so that the compiled interpreter supports the
desired features.

.. _clang: http://clang.llvm.org/

.. note:: While you need a C compiler to build CPython, you don't need any
   knowledge of the C language to contribute!  Vast areas of CPython are
   written completely in Python: as of this writing, CPython contains slightly
   more Python code than C.


UNIX
''''

The basic steps for building Python for development is to configure it and
then compile it.

Configuration is typically::

  ./configure --with-pydebug

More flags are available to ``configure``, but this is the minimum you should
do to get a pydebug build of CPython.

Once ``configure`` is done, you can then compile CPython.::

    make -s -j2

This will build CPython with only warnings and errors being printed to
stderr and utilize up to 2 CPU cores. If you are using a multi-core machine
with more than 2 cores (or a single-core machine), you can adjust the number
passed into the ``-j`` flag to match the number of cores you have.

Do take note of what modules were **not** built as stated at the end of your
build. More than likely you are missing a dependency for the module(s) that
were not built, and so you can install the dependencies and re-run ``make``
(if available for your OS).
Otherwise the build failed and thus should be fixed (at least with a bug being
filed on the `issue tracker`_).

Once CPython is done building you will then have a working build
that can be run in-place; ``./python`` on most machines (and what is used in
all examples), ``./python.exe`` on OS X (when on a case-insensitive filesystem,
which is the default). There is absolutely no need to install your built copy
of Python! The interpreter will realize where it is being run from
and thus use the files found in the working copy. If you are worried
you might accidentally install your working copy build, you can add
``--prefix=/dev/null`` to the configuration step.

.. _issue tracker: http://bugs.python.org


Clang
"""""

If you are using clang_ to build CPython, some flags you might want to set to
quiet some standard warnings which are specifically superfluous to CPython are
``-Wno-unused-value -Wno-empty-body -Qunused-arguments``. You can set your
``CFLAGS`` environment variable to these flags when running ``configure``.

If you are using LLVM 2.8, also use the ``-no-integrated-as`` flag in order to
build the :py:mod:`ctypes` module (without the flag the rest of CPython will
still build properly).


Windows
'''''''

For Microsoft Visual Studio 2008 (also named Visual C++ 9), the ``PCbuild``
directory contains the build files (for older versions of Visual Studio, see
the ``PC`` directory).  The full version of Visual Studio is not necessary
for common tasks; gratis versions from http://www.microsoft.com/express/ are
sufficient.

To build from the Visual Studio GUI, load the project files and press F7. Make
sure you have chosen the "Debug" build first.

Once built you might want to set Python as a startup project. Pressing F5 in
Visual Studio will launch the interpreter.

If you want to launch the compiled interpreter from the command-line, the
path varies according to the build.  For a 32-bit build in debug mode, you
have to invoke ``PCBuild\python_d.exe``, for a 64-bit build in debug mode,
``PCBuild\AMD64\python_d.exe``.  If you are compiling in release mode (which
you shouldn't, in general), replace ``python_d.exe`` with ``python.exe``.


Editors and Tools
=================

Python is used widely enough that practically all code editors have some form
of support for writing Python code. Various coding tools also include Python
support.

For editors and tools which the core developers have felt some special comment
is needed for coding *in* Python, see :ref:`resources`.


Directory Structure
===================

There are several top-level directories in the CPython source tree. Knowing what
each one is meant to hold will help you find where a certain piece of
functionality is implemented. Do realize, though, there are always exceptions to
every rule.

``Doc``
     The official documentation. This is what http://docs.python.org/ uses.
     To build the docs, see ``Doc/README.txt``.

``Grammar``
     Contains the :abbr:`EBNF (Extended Backus–Naur Form)` grammar file for
     Python.

``Include``
     Contains all interpreter-wide header files.

``Lib``
     The part of the standard library implemented in pure Python.

``Mac``
     Mac-specific code (e.g., using IDLE as an OS X application).

``Misc``
     Things that do not belong elsewhere. Typically this is varying kinds of
     developer-specific documentation.

``Modules``
     The part of the standard library (plus some other code) that is implemented
     in C.

``Objects``
     Code for all built-in types.

``PC``
     Windows-specific code along with build files for VC 6, 7, & 8 along with
     OS/2.

``PCbuild``
     Build files for VC 9 and newer.

``Parser``
     Code related to the parser. The definition of the AST nodes is also kept
     here.

``Python``
     The code that makes up the CPython interpreter. This includes the compiler,
     eval loop and various built-in modules.

``Tools``
     Various tools that are (or have been) used to maintain Python.

