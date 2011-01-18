.. _setup:

Getting Set Up
==============

These instructions cover how to get a source checkout and a compiled version of
the CPython interpreter (CPython is the version of Python available from
http://www.python.org/). It will also tell you how to set up various code
editors. Finally, this document also gives an overview of the directory
structure of a CPython checkout.

.. contents::


Version Control Setup
---------------------

CPython is developed using `Subversion (commonly abbreviated SVN)
<http://subversion.tigris.org/>`_.
It is easily available for common Unix systems by way of the standard package
manager; under Windows, you might want to use the `TortoiseSVN
<http://tortoisesvn.net/>`_ graphical client.


Checking out the code
----------------------

One should always work from a checkout of the CPython source code. While it may
be tempting to work from the downloaded copy you already have installed on your
machine, it is very likely that you will be working from out-of-date code as
the Python core developers are constantly updating and fixing things in their
:abbr:`VCS`. It also means you will have better tool
support through the VCS as it will provide a diff tool, etc.

To get a read-only checkout of CPython's source, you need to checkout the source
code. To get a read-only checkout of
the in-development branch of Python (core developers should read XXX for a
read-write checkout), run::

    svn co http://svn.python.org/projects/python/branches/py3k

If you want a read-only checkout of an already-released version of Python,
i.e., a version in maintenance mode, run something like the following which
gets you a checkout for Python 3.1::

    svn co http://svn.python.org/projects/python/branches/release31-maint

To check out a version of Python other than 3.1, simply change the number in
the above URL to the major/minor version (e.g., ``release27-maint`` for Python
2.7).

Do note that CPython will notice that it is being run from a source checkout.
This means that it if you edit Python source code in your checkout the changes
will be picked up by the interpreter for immediate testing.


Compiling (for debugging)
-------------------------

CPython provides several compilation flags which help with debugging various
things. While all of the known flags can be in the ``Misc/SpecialBuilds.txt``
file, the most critical one is the ``Py_DEBUG`` flag which creates what is
known as a "pydebug" build. This flag turns on
various extra sanity checks which help catch common issues. You should always
develop under a pydebug build of CPython (only instance of when you shouldn't
is if you are taking performance measurements).


UNIX
''''

The basic steps for building Python for development is to configure it and
then compile it.

Configuration is typically::

  ./configure --with-pydebug

More flags are available to ``configure``, but this is the minimum you should
do. This will give you a debug version of Python along with the safety measure
of preventing you from accidentally installing your development version over
your system install.

Once ``configure`` is done, you can then compile Python.::

    make -s -j2

This will build Python with only warnings and errors being printed to
stderr and utilize up to 2 CPU cores. If you are using a multi-core machine
with more than 2 cores (or a single-core machine), you can adjust the number
passed into the ``-j`` flag to match the number of cores you have.

Once Python is done building you will then have a working build of Python
that can be run in-place; ``./python`` on most machines (and what is used in
all examples), ``./python.exe`` on OS X (when on a case-insensitive filesystem,
which is the default).


Windows
'''''''

For Microsoft Visual Studio 2008 (also named Visual C++ 9), the ``PCbuild``
directory contains the build files (for older versions of Visual Studio, see
the ``PC`` directory).  The full version of Visual Studio is not necessary
for common tasks; gratis versions from http://www.microsoft.com/express/ are
sufficient.

To build from the Visual Studio GUI, load the project files and press F7. Make
sure have chosen the "Debug" build first.

.. XXX: doesn't work
   If you want to build from the command line, you can run the
   ``build_env.bat`` file to get a terminal with proper environment variables.
   From that terminal, run::

       build.bat -c Debug

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
is needed for coding *in* Python, see the ``Misc`` directory and the
various ``README.*`` files. For tool/editor support geared specifically towards
coding *for* (C)Python itself, see :ref:`resources`.


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

