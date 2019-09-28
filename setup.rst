.. _setup:

===============
Getting Started
===============

.. highlight:: console

These instructions cover how to get a working copy of the source code and a
compiled version of the CPython interpreter (CPython is the version of Python
available from https://www.python.org/). It also gives an overview of the
directory structure of the CPython source code.

Alternatively, if you have `Docker <https://www.docker.com/>`_ installed you
might want to use `our official images
<https://gitlab.com/python-devs/ci-images/blob/master/README.md>`_.  These
contain the latest releases of several Python versions, along with git head,
and are provided for development and testing purposes only.

.. seealso::

   The :ref:`quick-reference` gives brief summary of the process from
   installing git to submitting a pull request.

.. _vcsetup:

Install ``git``
===============

CPython is developed using `git <https://git-scm.com>`_ for version control. The git
command line program is named ``git``; this is also used to refer to git
itself. git is easily available for all common operating systems.

- **Install**

  As the CPython repo is hosted on GitHub, please refer to either the
  `GitHub setup instructions <https://help.github.com/articles/set-up-git/>`_
  or the `git project instructions <https://git-scm.com>`_ for step-by-step
  installation directions. You may also want to consider a graphical client
  such as `TortoiseGit <https://tortoisegit.org/>`_ or
  `GitHub Desktop <https://desktop.github.com/>`_.

- **Configure**

  Configure :ref:`your name and email <set-up-name-email>` and create
  `an SSH key <https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/>`_
  as this will allow you to interact with GitHub without typing a username
  and password each time you execute a command, such as ``git pull``,
  ``git push``, or ``git fetch``.  On Windows, you should also
  :ref:`enable autocrlf <autocrlf>`.


.. _checkout:

Get the source code
===================

The CPython repo is hosted on GitHub. To get a copy of the source code you should
:ref:`fork the Python repository on GitHub <fork-cpython>`, :ref:`create a local
clone of your personal fork, and configure the remotes <clone-your-fork>`.

You will only need to execute these steps once:

1. Go to https://github.com/python/cpython.

2. Press :guilabel:`Fork` on the top right.

3. When asked where to fork the repository, choose to fork it to your username.

4. Your fork will be created at :samp:`https://github.com/{<username>}/cpython`.

5. Clone your GitHub fork (replace ``<username>`` with your username)::

      $ git clone git@github.com:<username>/cpython.git

   (You can use both SSH-based or HTTPS-based URLs.)

6. Configure an ``upstream`` remote::

      $ cd cpython
      $ git remote add upstream git@github.com:python/cpython.git

7. Verify that your setup is correct::

      $ git remote -v
      origin  git@github.com:<your-username>/cpython.git (fetch)
      origin  git@github.com:<your-username>/cpython.git (push)
      upstream        git@github.com:python/cpython.git (fetch)
      upstream        git@github.com:python/cpython.git (push)

If you did everything correctly, you should now have a copy of the code
in the ``cpython`` directory and two remotes that refer to your own GitHub fork
(``origin``) and the official CPython repository (``upstream``).

.. XXX move the text below in pullrequest

If you want a working copy of an already-released version of Python,
i.e., a version in :ref:`maintenance mode <maintbranch>`, you can checkout
a release branch. For instance, to checkout a working copy of Python 3.7,
do ``git checkout 3.7``.

You will need to re-compile CPython when you do such an update.

Do note that CPython will notice that it is being run from a working copy.
This means that if you edit CPython's source code in your working copy,
changes to Python code will be picked up by the interpreter for immediate
use and testing.  (If you change C code, you will need to recompile the
affected files as described below.)

Patches for the documentation can be made from the same repository; see
:ref:`documenting`.


.. _compiling:

Compile and build
=================

CPython provides several compilation flags which help with debugging various
things. While all of the known flags can be found in the
``Misc/SpecialBuilds.txt`` file, the most critical one is the ``Py_DEBUG`` flag
which creates what is known as a "pydebug" build. This flag turns on various
extra sanity checks which help catch common issues. The use of the flag is so
common that turning on the flag is a basic compile option.

You should always develop under a pydebug build of CPython (the only instance of
when you shouldn't is if you are taking performance measurements). Even when
working only on pure Python code the pydebug build provides several useful
checks that one should not skip.


.. _unix-compiling:

UNIX
----

The core CPython interpreter only needs a C compiler to be built,
however, some of the extension modules will need development headers
for additional libraries (such as the ``zlib`` library for compression).
Depending on what you intend to work on, you might need to install these
additional requirements so that the compiled interpreter supports the
desired features.

If you want to install these optional dependencies, consult the
:ref:`build-dependencies` section below.

If you don't need to install them, the basic steps for building Python
for development is to configure it and then compile it.

Configuration is typically:

.. code-block:: bash

   ./configure --with-pydebug

More flags are available to ``configure``, but this is the minimum you should
do to get a pydebug build of CPython.

Once ``configure`` is done, you can then compile CPython with:

.. code-block:: bash

   make -s -j2

This will build CPython with only warnings and errors being printed to
stderr and utilize up to 2 CPU cores. If you are using a multi-core machine
with more than 2 cores (or a single-core machine), you can adjust the number
passed into the ``-j`` flag to match the number of cores you have (or if your
version of Make supports it, you can use ``-j`` without a number and Make
will not limit the number of steps that can run simultaneously.).

At the end of the build you should see a success message, possibly followed
by a list of extension modules that haven't been built because their
dependencies were missing:

.. code-block:: none

   Python build finished successfully!
   The necessary bits to build these optional modules were not found:
   _bz2                  _dbm                  _gdbm
   _lzma                 _sqlite3              _ssl
   _tkinter              _uuid                 readline
   zlib
   To find the necessary bits, look in setup.py in detect_modules()
   for the module's name.

If the build failed and you are using a C89 or C99-compliant compiler,
please `open a bug report <https://bugs.python.org>`_.

If you decide to :ref:`build-dependencies`, you will need to re-run both
``configure`` and ``make``.

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


Clang
'''''

If you are using clang_ to build CPython, some flags you might want to set to
quiet some standard warnings which are specifically superfluous to CPython are
``-Wno-unused-value -Wno-empty-body -Qunused-arguments``. You can set your
``CFLAGS`` environment variable to these flags when running ``configure``.

If you are using clang_ with ccache_, turn off the noisy
``parentheses-equality`` warnings with the ``-Wno-parentheses-equality`` flag.
These warnings are caused by clang not  having enough information to detect
that extraneous parentheses in expanded macros are valid, because the
preprocessing is done separately by ccache.

If you are using LLVM 2.8, also use the ``-no-integrated-as`` flag in order to
build the :py:mod:`ctypes` module (without the flag the rest of CPython will
still build properly).


.. _windows-compiling:

Windows
-------

For a quick guide to building you can read `this documentation`_ from Victor
Stinner.

**Python 3.6** and later can use Microsoft Visual Studio 2017.  You can download
and use any of the free or paid versions of `Visual Studio 2017`_.

When installing Visual Studio 2017, select the **Python development** workload
and the optional **Python native development tools** component to obtain all of
the necessary build tools. If you do not already have git installed, you can
find git for Windows on the **Individual components** tab of the installer.

.. note:: If you want to build MSI installers, be aware that the build toolchain
  for them has a dependency on the Microsoft .NET Framework Version 3.5 (which
  may not be configured on recent versions of Windows, such as Windows 10). If
  you are building on a recent Windows version, use the Control Panel (Programs
  | Programs and Features | Turn Windows Features on or off) and ensure that the
  entry ".NET Framework 3.5 (includes .NET 2.0 and 3.0)" is enabled.

Your first build should use the command line to ensure any external dependencies
are downloaded:

.. code-block:: dosbatch

   PCBuild\build.bat

After this build succeeds, you can open the ``PCBuild\pcbuild.sln`` solution in
Visual Studio to continue development.

See the `readme`_ for more details on what other software is necessary and how
to build.

.. note:: **Python 2.7** uses Microsoft Visual Studio 2008, which is most easily
   obtained through an MSDN subscription.  To use the build files in the
   `PCbuild directory`_ you will also need Visual Studio 2010, see the `2.7
   readme`_ for more details.  If you have VS 2008 but not 2010 you can use the
   build files in the `PC/VS9.0 directory`_, see the `VS9 readme`_ for details.

.. note:: If you are using the Windows Subsystem for Linux (WSL), clone the
   repository from a native Windows terminal program like cmd.exe command prompt
   or PowerShell as well as use a build of git targeted for Windows, e.g., the
   official one from `<https://git-scm.com>`_. Otherwise, Visual Studio will
   not be able to find all the project's files and will fail the build.

.. _this documentation: https://cpython-core-tutorial.readthedocs.io/en/latest/build_cpython_windows.html
.. _Visual Studio 2017: https://www.visualstudio.com/
.. _readme: https://github.com/python/cpython/blob/master/PCbuild/readme.txt
.. _PCbuild directory: https://github.com/python/cpython/tree/2.7/PCbuild/
.. _2.7 readme: https://github.com/python/cpython/blob/2.7/PCbuild/readme.txt
.. _PC/VS9.0 directory: https://github.com/python/cpython/tree/2.7/PC/VS9.0/
.. _VS9 readme: https://github.com/python/cpython/blob/2.7/PC/VS9.0/readme.txt


.. _build-dependencies:

Install dependencies
====================

This section explains how to install additional extensions (e.g. ``zlib``)
on :ref:`Linux <deps-on-linux>` and :ref:`macOs/OS X <macOS>`.  On Windows,
extensions are already included and built automatically.

.. _deps-on-linux:

Linux
-----

For UNIX based systems, we try to use system libraries whenever available.
This means optional components will only build if the relevant system headers
are available. The best way to obtain the appropriate headers will vary by
distribution, but the appropriate commands for some popular distributions
are below.

On **Fedora**, **Red Hat Enterprise Linux** and other ``yum`` based systems::

   $ sudo yum install yum-utils
   $ sudo yum-builddep python3

On **Fedora** and other ``DNF`` based systems::

   $ sudo dnf install dnf-plugins-core  # install this to use 'dnf builddep'
   $ sudo dnf builddep python3

On **Debian**, **Ubuntu**, and other ``apt`` based systems, try to get the
dependencies for the Python you're working on by using the ``apt`` command.

First, make sure you have enabled the source packages in the sources list.
You can do this by adding the location of the source packages, including
URL, distribution name and component name, to ``/etc/apt/sources.list``.
Take Ubuntu Bionic for example::

   deb-src http://archive.ubuntu.com/ubuntu/ bionic main

For other distributions, like Debian, change the URL and names to correspond
with the specific distribution.

Then you should update the packages index::

   $ sudo apt-get update

Now you can install the build dependencies via ``apt``::

   $ sudo apt-get build-dep python3.6

If that package is not available for your system, try reducing the minor
version until you find a package that is available.


.. _MacOS:

macOS and OS X
--------------

For **macOS systems** (versions 10.12+) and **OS X 10.9 and later**,
the Developer Tools can be downloaded and installed automatically;
you do not need to download the complete Xcode application.

If necessary, run the following::

    $ xcode-select --install

This will also ensure that the system header files are installed into
``/usr/include``.

On **Mac OS X systems** (versions 10.0 - 10.7) and **OS X 10.8**, use the C
compiler and other development utilities provided by Apple's Xcode Developer
Tools. The Developer Tools are not shipped with Mac OS X.

For these **older releases (versions 10.0 - 10.8)**, you will need to download either the
correct version of the Command Line Tools, if available, or install them from the
full Xcode app or package for that OS X release.  Older versions may be
available either as a no-cost download through Apple's App Store or from
`the Apple Developer web site <https://developer.apple.com/>`_.

.. _Homebrew: https://brew.sh

.. _MacPorts: https://www.macports.org

Also note that OS X does not include several libraries used by the Python
standard library, including ``libzma``, so expect to see some extension module
build failures unless you install local copies of them.  As of OS X 10.11,
Apple no longer provides header files for the deprecated system version of
OpenSSL which means that you will not be able to build the ``_ssl`` extension.
One solution is to install these libraries from a third-party package
manager, like Homebrew_ or MacPorts_, and then add the appropriate paths
for the header and library files to your ``configure`` command.  For example,

with **Homebrew**::

    $ brew install openssl xz gdbm

and ``configure`` Python versions >= 3.7::

    ./configure --with-pydebug --with-openssl=$(brew --prefix openssl)

or ``configure`` Python versions < 3.7::

    $ CPPFLAGS="-I$(brew --prefix openssl)/include" \
      LDFLAGS="-L$(brew --prefix openssl)/lib" \
      ./configure --with-pydebug

and ``make``::

    $ make -s -j2

or **MacPorts**::

    $ sudo port install pkgconfig openssl xz gdbm

and ``configure``::

    $ CPPFLAGS="-I/opt/local/include" \
      LDFLAGS="-L/opt/local/lib" \
      ./configure --with-pydebug

and ``make``::

    $ make -s -j2

There will sometimes be optional modules added for a new release which
won't yet be identified in the OS level build dependencies. In those cases,
just ask for assistance on the core-mentorship list. If working on bug
fixes for Python 2.7, use ``python`` in place of ``python3`` in the above
commands.

Explaining how to build optional dependencies on a UNIX based system without
root access is beyond the scope of this guide.

.. _clang: https://clang.llvm.org/
.. _ccache: https://ccache.samba.org/

.. note:: While you need a C compiler to build CPython, you don't need any
   knowledge of the C language to contribute!  Vast areas of CPython are
   written completely in Python: as of this writing, CPython contains slightly
   more Python code than C.


.. _regenerate_configure:

Regenerate ``configure``
========================

If a change is made to Python which relies on some POSIX system-specific
functionality (such as using a new system call), it is necessary to update the
``configure`` script to test for availability of the functionality.

Python's ``configure`` script is generated from ``configure.ac`` using Autoconf.
Instead of editing ``configure``, edit ``configure.ac`` and then run
``autoreconf`` to regenerate ``configure`` and a number of other files (such as
``pyconfig.h``).

When submitting a patch with changes made to ``configure.ac``, you should also
include the generated files.

Note that running ``autoreconf`` is not the same as running ``autoconf``. For
example, ``autoconf`` by itself will not regenerate ``pyconfig.h.in``.
``autoreconf`` runs ``autoconf`` and a number of other tools repeatedly as is
appropriate.

Python's ``configure.ac`` script typically requires a specific version of
Autoconf.  At the moment, this reads: ``AC_PREREQ(2.69)``.

If the system copy of Autoconf does not match this version, you will need to
install your own copy of Autoconf.

.. _build_troubleshooting:

Troubleshoot the build
======================

This section lists some of the common problems that may arise during the
compilation of Python, with proposed solutions.

Avoid recreating auto-generated files
-------------------------------------

Under some circumstances you may encounter Python errors in scripts like
``Parser/asdl_c.py`` or ``Python/makeopcodetargets.py`` while running ``make``.
Python auto-generates some of its own code, and a full build from scratch needs
to run the auto-generation scripts. However, this makes the Python build require
an already installed Python interpreter; this can also cause version mismatches
when trying to build an old (2.x) Python with a new (3.x) Python installed, or
vice versa.

To overcome this problem, auto-generated files are also checked into the
Git repository. So if you don't touch the auto-generation scripts, there's
no real need to auto-generate anything.

Editors and Tools
=================

Python is used widely enough that practically all code editors have some form
of support for writing Python code. Various coding tools also include Python
support.

For editors and tools which the core developers have felt some special comment
is needed for coding *in* Python, see :ref:`resources`.


Directory structure
===================

There are several top-level directories in the CPython source tree. Knowing what
each one is meant to hold will help you find where a certain piece of
functionality is implemented. Do realize, though, there are always exceptions to
every rule.

``Doc``
     The official documentation. This is what https://docs.python.org/ uses.
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

