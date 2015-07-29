===============
Getting Started
===============

These instructions cover how to get a working copy of the source code and a
compiled version of the CPython interpreter (CPython is the version of Python
available from http://www.python.org/). It also gives an overview of the
directory structure of the CPython source code.

OpenHatch also has a great `setup guide`_ for Python for people who are
completely new to contributing to open source.

.. _setup guide: https://openhatch.org/wiki/Contributing_to_Python


.. _setup:

Getting Set Up
==============


.. _vcsetup:

Version Control Setup
---------------------

CPython is developed using `Mercurial <http://hg-scm.org/>`_. The Mercurial
command line program is named ``hg``; this is also used to refer to Mercurial
itself. Mercurial is easily available for common Unix systems by way of the
standard package manager; under Windows, you might want to use the
`TortoiseHg <http://tortoisehg.org/>`_ graphical client, but the build system
still prefers :file:`hg.exe` to be on your PATH.


.. _checkout:

Getting the Source Code
-----------------------

One should always work from a working copy of the CPython source code.
While it may
be tempting to work from the copy of Python you already have installed on your
machine, it is very likely that you will be working from out-of-date code as
the Python core developers are constantly updating and fixing things in their
:abbr:`VCS (version control system)`. It also means you will have better tool
support through the VCS as it will provide a diff tool, etc.

To get a working copy of the :ref:`in-development <indevbranch>` branch of
CPython (core developers use a different URL as outlined in :ref:`coredev`),
run::

    hg clone https://hg.python.org/cpython

If you want a working copy of an already-released version of Python,
i.e., a version in :ref:`maintenance mode <maintbranch>`, you can update your
working copy. For instance, to update your working copy to Python 3.4, do::

   hg update 3.4

You will need to re-compile CPython when you do such an update.

Do note that CPython will notice that it is being run from a working copy.
This means that if you edit CPython's source code in your working copy,
changes to Python code will be picked up by the interpreter for immediate
use and testing.  (If you change C code, you will need to recompile the
affected files as described below.)

Patches for the documentation can be made from the same repository; see
:ref:`documenting`.

.. _compiling:

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


.. _build-dependencies:

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

For UNIX based systems, we try to use system libraries whenever available.
This means optional components will only build if the relevant system headers
are available. The best way to obtain the appropriate headers will vary by
distribution, but the appropriate commands for some popular distributions
are below.

Fedora, Red Hat Enterprise Linux and other ``yum`` based systems::

   $ sudo yum install yum-utils
   $ sudo yum-builddep python3

Debian, Ubuntu and other ``apt`` based systems, try to get the dependencies for
the Python version that you're working on e.g.::

   $ sudo apt-get build-dep python3.4

If that package is not available for your system, try reducing the minor
version until you find a package that is available.

For Mac OS X systems, it is generally easiest to use the C compiler and other
development utilities provided by Apple's Xcode Developer Tools.  There are
specific versions supported by Apple for each major release of OS X.  For
current releases, Xcode is available as a no-cost download from Apple's App
Store.  Xcode versions for older releases are available through
`the Apple Developer web site <https://developer.apple.com/>`_.
Note that while the Xcode IDE application itself is not needed to build Python,
the development components packaged inside it may be.  You should also install
the Xcode Command Line Tools component to ensure build tools and system header
files are installed in their conventional locations (``/usr/bin`` and
``/usr/include``).  How the command line tools are installed varies by OS X
and Xcode release.  In earlier releases, there may be a separate installer
download.  For OS X 10.7 and 10.8, there is an option in the Xcode app
Preferences menu.  For OS X 10.9 (Mavericks), run the following::

    $ xcode-select --install

Also note that OS X does not include several libraries used by the Python
standard library, including ``libzma``, so expect to see some extension module
build failures unless you install local copies of them.

There will sometimes be optional modules added for a new release which
won't yet be identified in the OS level build dependencies. In those cases,
just ask for assistance on the core-mentorship list. If working on bug
fixes for Python 2.7, use ``python`` in place of ``python3`` in the above
commands.

Explaining how to build optional dependencies on a UNIX based system without
root access is beyond the scope of this guide.

.. _clang: http://clang.llvm.org/

.. note:: While you need a C compiler to build CPython, you don't need any
   knowledge of the C language to contribute!  Vast areas of CPython are
   written completely in Python: as of this writing, CPython contains slightly
   more Python code than C.


.. _unix-compiling:

UNIX
''''

The basic steps for building Python for development is to configure it and
then compile it.

Configuration is typically::

  ./configure --with-pydebug

More flags are available to ``configure``, but this is the minimum you should
do to get a pydebug build of CPython.

Once ``configure`` is done, you can then compile CPython with::

    make -s -j2

This will build CPython with only warnings and errors being printed to
stderr and utilize up to 2 CPU cores. If you are using a multi-core machine
with more than 2 cores (or a single-core machine), you can adjust the number
passed into the ``-j`` flag to match the number of cores you have.

Do take note of what modules were **not** built as stated at the end of your
build. More than likely you are missing a dependency for the module(s) that
were not built, and so you can install the dependencies and re-run both
``configure`` and ``make`` (if available for your OS).
Otherwise the build failed and thus should be fixed (at least with a bug being
filed on the `issue tracker`_).

.. _mac-python.exe:

Once CPython is done building you will then have a working build
that can be run in-place; ``./python`` on most machines (and what is used in
all examples), ``./python.exe`` wherever a case-insensitive filesystem is used
(e.g. on OS X by default), in order to avoid conflicts with the ``Python``
directory. There is normally no need to install your built copy
of Python! The interpreter will realize where it is being run from
and thus use the files found in the working copy.  If you are worried
you might accidentally install your working copy build, you can add
``--prefix=/tmp/python`` to the configuration step.  When running from your
working directory, it is best to avoid using the ``--enable-shared`` flag
to ``configure``; unless you are very careful, you may accidentally run
with code from an older, installed shared Python library rather than from
the interpreter you just built.

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


.. _windows-compiling:

Windows
'''''''

The `readme <https://hg.python.org/cpython/file/default/PCbuild/readme.txt>`_
included in the solution has more details, especially on what additional
software is required to build which parts of Python.

**Python 3.5** and later use Microsoft Visual Studio 2015.  You can download
and use any of the free or paid versions of `Visual Studio 2015
<https://www.visualstudio.com/>`_.

Python 3.3 and 3.4 use Microsoft Visual Studio 2010.  You can download
Microsoft Visual Studio 2010 Express with an `MSDN subscription
<https://msdn.microsoft.com/subscriptions/downloads>`_.
You'll also need to install the Visual Studio `Service Pack 1 (SP1)
<http://www.microsoft.com/en-us/download/details.aspx?id=23691>`_. If you
don't install this service pack, you may receive errors like the following
during linking: ``LINK : fatal error LNK1123: failure during conversion to
COFF: file invalid or corrupt``.

Most Python versions prior to 3.3 use Microsoft Visual Studio 2008.  You can
download Microsoft Visual C++ 2008 Express Edition with SP1
from a new location yet to be determined.

Regardless of Visual Studio version, the ``PCbuild`` directory of a source
checkout contains the build files for the Python version you are building.

To build from the command line, execute :file:`PCBuild\\build.bat`.  If you
have not previously done so, you can pass the ``-e`` option to download
external dependencies or invoke :file:`PCBuild\\get_externals.bat` directly. By
default, :file:`PCBuild\\build.bat` will produce a 32-bit release build. Pass
the ``-p x64`` option to produce a 64-bit build, and/or the ``-d`` option to
produce a debug build.

To build from the Visual Studio GUI, open the ``pcbuild.sln`` solution file
with Visual Studio.  Choose the :menuselection:`Build Solution` option
under the :menuselection:`Build` menu.  Be sure that "Debug" was chosen
as the active solution configuration (e.g. under
:menuselection:`Build --> Configuration Manager...`).

When building you may see a number of build errors related to missing
files or directories.  These do not necessarily mean that Python failed
to build.  If you prefer, you can exclude the offending projects from
the build process by unchecking them inside the
:menuselection:`Build --> Configuration Manager...` settings. You can
also use the script :file:`PCbuild\\get_externals.bat` to download missing
dependencies.

Once built you might want to set Python as a startup project. Pressing F5 in
Visual Studio, or choosing :menuselection:`Start Debugging` from the
:menuselection:`Debug` menu, will launch the interpreter.

.. _win-python.exe:

If you want to launch the compiled interpreter from the command-line, the
path varies according to the build.  For a 32-bit build in debug mode, you
have to invoke ``PCBuild\win32\python_d.exe``, for a 64-bit build in debug
mode, ``PCBuild\amd64\python_d.exe``.  If you are compiling in release mode
(which you shouldn't, in general), replace ``python_d.exe`` with
``python.exe``.  You can also invoke the most recently built interpreter using
``python.bat`` in the root of the source tree.

.. _build_troubleshooting:

Troubleshooting the build
-------------------------

This section lists some of the common problems that may arise during the
compilation of Python, with proposed solutions.

Avoiding re-creating auto-generated files
'''''''''''''''''''''''''''''''''''''''''

Under some circumstances you may encounter Python errors in scripts like
``Parser/asdl_c.py`` or ``Python/makeopcodetargets.py`` while running ``make``.
Python auto-generates some of its own code, and a full build from scratch needs
to run the auto-generation scripts. However, this makes the Python build require
an already installed Python interpreter; this can also cause version mismatches
when trying to build an old (2.x) Python with a new (3.x) Python installed, or
vice versa.

To overcome this problem, auto-generated files are also checked into the
Mercurial repository. So if you don't touch the auto-generation scripts, there's
no real need to auto-generate anything. However, as Mercurial doesn't preserve
timestamps well, a special build target ``touch`` was added (the ``touch``
build target is not designed for git clones and does not support them). Run::

    make touch

Before running the compilation ``make``. This will tweak the timestamps of the
auto-generated files in a way that makes it unnecessary to create them anew and
henceforth the compilation should not require an installed Python interpreter.

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
     See also :ref:`building-doc`.

``Grammar``
     Contains the :abbr:`EBNF (Extended Backus-Naur Form)` grammar file for
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
     Windows-specific code.

``PCbuild``
     Build files for the version of MSVC currently used for the Windows
     installers provided on python.org.

``Parser``
     Code related to the parser. The definition of the AST nodes is also kept
     here.

``Programs``
     Source code for C executables, including the main function for the
     CPython interpreter (in versions prior to Python 3.5, these files are
     in the Modules directory).

``Python``
     The code that makes up the core CPython runtime. This includes the
     compiler, eval loop and various built-in modules.

``Tools``
     Various tools that are (or have been) used to maintain Python.

