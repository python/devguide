.. _setup-building:
.. _setup:

==================
Setup and building
==================

.. raw:: html

    <script>
    document.addEventListener('DOMContentLoaded', function() {
      activateTab(getOS());
    });
    </script>

.. highlight:: console

These instructions cover how to get a working copy of the source code and a
compiled version of the CPython interpreter (CPython is the version of Python
available from https://www.python.org/). It also gives an overview of the
directory structure of the CPython source code.

Alternatively, if you have `Docker <https://www.docker.com/>`_ installed you
might want to use `our official images
<https://gitlab.com/python-devs/ci-images/blob/main/README.md>`_.  These
contain the latest releases of several Python versions, along with Git head,
and are provided for development and testing purposes only.

.. seealso::

   The :ref:`quick-reference` gives brief summary of the process from
   installing Git to submitting a pull request.

.. _vcsetup:

Install Git
===========

CPython is developed using `Git <https://git-scm.com>`_ for version control. The Git
command line program is named ``git``; this is also used to refer to Git
itself. Git is easily available for all common operating systems.

- **Install**

  As the CPython repo is hosted on GitHub, please refer to either the
  `GitHub setup instructions <https://docs.github.com/en/get-started/getting-started-with-git/set-up-git>`_
  or the `Git project instructions <https://git-scm.com>`_ for step-by-step
  installation directions. You may also want to consider a graphical client
  such as `TortoiseGit <https://tortoisegit.org/>`_ or
  `GitHub Desktop <https://desktop.github.com/>`_.

- **Configure**

  Configure :ref:`your name and email <set-up-name-email>` and create
  `an SSH key <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>`_
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

You will only need to execute these steps once per machine:

1. Go to https://github.com/python/cpython.

2. Press :guilabel:`Fork` on the top right.

3. When asked where to fork the repository, choose to fork it to your username.

4. Your fork will be created at :samp:`https://github.com/{<username>}/cpython`.

5. Clone your GitHub fork (replace ``<username>`` with your username)::

      $ git clone git@github.com:<username>/cpython.git

   (You can use both SSH-based or HTTPS-based URLs.)

.. Step 6 and 7 are are duplicated in bootcamp as well.
   Please update these steps in both places.

6. Add an ``upstream`` remote, then configure ``git``
   to pull ``main`` from ``upstream`` and always push to ``origin``::

      $ cd cpython
      $ git remote add upstream https://github.com/python/cpython
      $ git config --local branch.main.remote upstream
      $ git remote set-url --push upstream git@github.com:<your-username>/cpython.git

7. Verify that your setup is correct::

      $ git remote -v
      origin  git@github.com:<your-username>/cpython.git (fetch)
      origin  git@github.com:<your-username>/cpython.git (push)
      upstream        https://github.com/python/cpython (fetch)
      upstream        git@github.com:<your-username>/cpython.git (push)
      $ git config branch.main.remote
      upstream

For more information about these commands see
:ref:`Git Bootcamp and Cheat Sheet <git-boot-camp>`.

If you did everything correctly, you should now have a copy of the code
in the ``cpython`` directory and two remotes that refer to your own GitHub fork
(``origin``) and the official CPython repository (``upstream``).

.. XXX move the text below in pullrequest

If you want a working copy of an already-released version of Python,
that is, a version in :ref:`maintenance mode <maintbranch>`, you can checkout
a release branch. For instance, to checkout a working copy of Python 3.8,
do ``git switch 3.8``.

You will need to re-compile CPython when you do such an update.

Do note that CPython will notice that it is being run from a working copy.
This means that if you edit CPython's source code in your working copy,
changes to Python code will be picked up by the interpreter for immediate
use and testing.  (If you change C code, you will need to recompile the
affected files as described below.)

Patches for the documentation can be made from the same repository; see
:ref:`documenting`.

.. _install-pre-commit:

Install pre-commit as a Git hook
--------------------------------

To make sure your code is linted correctly, we recommend setting up
`pre-commit <https://pre-commit.com#installation>`_ as a Git hook::

   $ pre-commit install --allow-missing-config
   pre-commit installed at .git/hooks/pre-commit

Now pre-commit will run automatically on ``git commit``.

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

.. seealso:: The effects of various configure and build flags are documented in
   the `Python configure docs <https://docs.python.org/dev/using/configure.html>`_.

.. _unix-compiling:

Unix
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

Configuration is typically::

   $ ./configure --with-pydebug

More flags are available to ``configure``, but this is the minimum you should
do to get a pydebug build of CPython.

.. note::
   You might need to run ``make clean`` before or after re-running ``configure``
   in a particular build directory.

Once ``configure`` is done, you can then compile CPython with::

   $ make -s -j2

This will build CPython with only warnings and errors being printed to
stderr and utilize up to 2 CPU cores. If you are using a multi-core machine
with more than 2 cores (or a single-core machine), you can adjust the number
passed into the ``-j`` flag to match the number of cores you have (or if your
version of Make supports it, you can use ``-j`` without a number and Make
will not limit the number of steps that can run simultaneously.).

At the end of the build you should see a success message, followed
by a list of extension modules that haven't been built because their
dependencies were missing:

.. code-block:: none

   The necessary bits to build these optional modules were not found:
   _gdbm
   To find the necessary bits, look in configure.ac and config.log.

   Checked 106 modules (31 built-in, 74 shared, 0 n/a on macosx-13.4-arm64, 0 disabled, 1 missing, 0 failed on import)

If the build failed and you are using a C89 or C99-compliant compiler,
please open a bug report on the `issue tracker`_.

If you decide to :ref:`build-dependencies`, you will need to re-run both
``configure`` and ``make``.

.. _mac-python.exe:

Once CPython is done building you will then have a working build
that can be run in-place; ``./python`` on most machines (and what is used in
all examples), ``./python.exe`` wherever a case-insensitive filesystem is used
(for example, on macOS by default), in order to avoid conflicts with the ``Python``
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
^^^^^

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


Optimization
^^^^^^^^^^^^

If you are trying to improve CPython's performance, you will probably want
to use an optimized build of CPython. It can take a lot longer to build CPython
with optimizations enabled, and it's usually not necessary to do so. However,
it's essential if you want accurate benchmark results for a proposed performance
optimization.

For an optimized build of Python, use
``configure --enable-optimizations --with-lto``.
This sets the default make targets up to enable Profile Guided Optimization (PGO)
and may be used to auto-enable Link Time Optimization (LTO) on some platforms.
See :option:`python:--enable-optimizations` and :option:`python:--with-lto`
to learn more about these options.

.. code:: console

   $ ./configure --enable-optimizations --with-lto

.. _windows-compiling:

Windows
-------

.. note:: If you are using the Windows Subsystem for Linux (WSL),
   :ref:`clone the repository <checkout>` from a native Windows shell program
   like PowerShell or the ``cmd.exe`` command prompt,
   and use a build of Git targeted for Windows,
   for example, the `Git for Windows download from the official Git website`_.
   Otherwise, Visual Studio will not be able to find all the project's files
   and will fail the build.

For a concise step by step summary of building Python on Windows,
you can read `Victor Stinner's guide`_.

All supported versions of Python can be built
using Microsoft Visual Studio 2017 or later.
You can download and use any of the free or paid versions of `Visual Studio`_.

When installing it, select the :guilabel:`Python development` workload
and the optional :guilabel:`Python native development tools` component
to obtain all of the necessary build tools.
You can find Git for Windows on the :guilabel:`Individual components` tab
if you don't already have it installed.

.. note:: If you want to build MSI installers, be aware that the build toolchain
   for them has a dependency on the Microsoft .NET Framework Version 3.5
   (which may not be included on recent versions of Windows, such as Windows 10).
   If you are building on a recent Windows version, use the Control Panel
   (:menuselection:`Programs --> Programs and Features --> Turn Windows Features on or off`)
   and ensure that the entry
   :guilabel:`.NET Framework 3.5 (includes .NET 2.0 and 3.0)` is enabled.

Your first build should use the command line to ensure any external dependencies
are downloaded:

.. code-block:: batch

   PCbuild\build.bat -c Debug

The above command line build uses the ``-c Debug`` argument
to build in the ``Debug`` configuration,
which enables checks and assertions helpful for developing Python.
By default, it builds in the ``Release`` configuration
and for the 64-bit ``x64`` platform rather than 32-bit ``Win32``;
use ``-c`` and ``-p`` to control build config and platform, respectively.

After this build succeeds, you can open the ``PCbuild\pcbuild.sln`` solution
in the Visual Studio IDE to continue development, if you prefer.
When building in Visual Studio,
make sure to select build settings that match what you used with the script
(the :guilabel:`Debug` configuration and the :guilabel:`x64` platform)
from the dropdown menus in the toolbar.

.. note::

   If you need to change the build configuration or platform,
   build once with the ``build.bat`` script set to those options first
   before building with them in VS to ensure all files are rebuilt properly,
   or you may encounter errors when loading modules that were not rebuilt.

   Avoid selecting the ``PGInstrument`` and ``PGUpdate`` configurations,
   as these are intended for PGO builds and not for normal development.

You can run the build of Python you've compiled with:

.. code-block:: batch

   PCbuild\amd64\python_d.exe

See the `PCBuild readme`_ for more details on what other software is necessary
and how to build.

.. _Victor Stinner's guide: https://web.archive.org/web/20220907075854/https://cpython-core-tutorial.readthedocs.io/en/latest/build_cpython_windows.html
.. _Visual Studio: https://visualstudio.microsoft.com/
.. _PCBuild readme: https://github.com/python/cpython/blob/main/PCbuild/readme.txt
.. _Git for Windows download from the official Git website: https://git-scm.com/download/win


.. _wasi-compiling:

WASI
----

WASI_ is a system interface standard for WebAssembly_. Through a combination of
C compilers that can target WebAssembly and `wasi-libc`_ providing
POSIX-compatible shims for WASI, it's possible for CPython to run on a WASI
host/runtime as a *guest*.

.. note::

   The instructions below assume a Unix-based OS due to cross-compilation for
   CPython being designed for ``./configure`` / ``make``.

To build for WASI, you will need to cross-compile CPython. This requires a C
compiler just like building for :ref:`Unix <unix-compiling>` as well as:

1. A C compiler that can target WebAssembly (for example, `WASI SDK`_)
2. A WASI host/runtime (for example, Wasmtime_)

All of this is provided in the :ref:`devcontainer <using-codespaces>`. You can
also use what's installed in the container as a reference of what versions of
these tools are known to work.

.. note::

   CPython has only been verified with the above tools for WASI. Using
   other compilers, hosts, or WASI versions *should* work, but the above tools
   and their versions specified in the container are tested via a
   :ref:`buildbot <buildbots>`.

Building for WASI requires doing a cross-build where you have a *build* Python
to help produce a WASI build of CPython (technically it's a "host x host"
cross-build because the build Python is also the target Python while the host
build is the WASI build). This means you effectively build CPython twice: once
to have a version of Python for the build system to use and another that's the
build you ultimately care about (that is, the build Python is not meant for use by
you directly, only the build system).

The easiest way to get a debug build of CPython for WASI is to use the
``Tools/wasm/wasi.py build`` command (which should be run w/ a recent version of
Python you have installed on your machine):

.. code-block:: shell

   $ python3 Tools/wasm/wasi.py build --quiet -- --config-cache --with-pydebug

That single command will configure and build both the build Python and the
WASI build in ``cross-build/build`` and ``cross-build/wasm32-wasi``,
respectively.

You can also do each configuration and build step separately; the command above
is a convenience wrapper around the following commands:

.. code-block:: shell

   $ python Tools/wasm/wasi.py configure-build-python --quiet -- --config-cache --with-pydebug
   $ python Tools/wasm/wasi.py make-build-python --quiet
   $ python Tools/wasm/wasi.py configure-host --quiet -- --config-cache
   $ python Tools/wasm/wasi.py make-host --quiet

.. note::

   The ``configure-host`` command infers the use of ``--with-pydebug`` from the
   build Python.

Running the separate commands after ``wasi.py build`` is useful if you, for example, only want to
run the ``make-host`` step after making code changes.

Once everything is complete, there will be a
``cross-build/wasm32-wasi/python.sh`` helper file which you can use to run the
``python.wasm`` file (see the output from the ``configure-host`` subcommand):

.. code-block:: shell

   $ cross-build/wasm32-wasi/python.sh --version

You can also use ``Makefile`` targets and they will work as expected thanks to
the ``HOSTRUNNER`` environment variable having been set to a similar value as
used in ``python.sh``:

.. code-block:: shell

   $ make -C cross-build/wasm32-wasi test

.. note::

   WASI uses a *capability-based* security model. This means that the WASI host
   does not give full access to your machine unless you tell it to. This
   also means things like files can end up being mapped to a different path
   inside the WASI host. So, if you try passing a file path to
   ``python.wasm``/ ``python.sh``, it needs to match the path **inside** the
   WASI host, not the path on your machine (much like using a container).

.. _WASI: https://wasi.dev
.. _wasi-libc: https://github.com/WebAssembly/wasi-libc
.. _WASI SDK: https://github.com/WebAssembly/wasi-sdk
.. _wasmtime: https://wasmtime.dev
.. _WebAssembly: https://webassembly.org

iOS
---

Compiling Python for iOS requires a macOS machine, on a recent version of macOS,
running a recent version of Xcode. Apple expects developers to keep their
operating systems and tools up-to-date; if your macOS version is more than one
major release out of date, or your Xcode version is more than a couple of minor
versions out of date, you'll likely encounter difficulties. It is not possible
to compile for iOS using Windows or Linux as a build machine.

A complete build for Python on iOS requires compiling CPython four times: once for
macOS; then once for each of the three underlying platforms used by iOS:

* An ARM64 device (an iPhone or iPad);
* An ARM64 simulator running on a recent macOS machine; and
* An x86_64 simulator running on older macOS machine.

The macOS build is required because building Python involves running some Python
code. On a normal desktop build of Python, you can compile a Python interpreter
and then use that interpreter to run Python code. However, the binaries produced
for iOS won't run on macOS, so you need to provide an external Python
interpreter. From the root of a CPython code checkout, run the following::

   $ ./configure --prefix=$(pwd)/cross-build/macOS
   $ make -j4 all
   $ make install

This will build and install Python for macOS into the ``cross-build/macOS``
directory.

The CPython build system can compile a single platform at a time. It is possible
to *test* a single platform at a time; however, for distribution purposes, you
must compile all three, and merge the results. See the `iOS README
<https://github.com/python/cpython/blob/main/iOS/README.rst#merge-thin-frameworks-into-fat-frameworks>`__
for details on this merging process.

The following instructions will build CPython for iOS with all extensions
enabled, provided you have installed the build dependencies XZ, BZip2, OpenSSL
and libFFI in subfolders of the ``cross-build`` folder. See :ref:`the iOS
section on installing build dependencies <build-dependencies>` for details on
how to obtain these dependencies. These dependencies are all strictly optional,
however, including libFFI is *highly* recommended, as it is required by the
:py:mod:`ctypes` module which is used on iOS to support accessing native system APIs.

.. tab:: ARM64 device

   .. code-block:: console

      $ export PATH="$(pwd)/iOS/Resources/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin"
      $ ./configure \
            LIBLZMA_CFLAGS="-I$(pwd)/cross-build/iphoneos.arm64/xz/include" \
            LIBLZMA_LIBS="-L$(pwd)/cross-build/iphoneos.arm64/xz/lib -llzma" \
            BZIP2_CFLAGS="-I$(pwd)/cross-build/iphoneos.arm64/bzip2/include" \
            BZIP2_LIBS="-L$(pwd)/cross-build/iphoneos.arm64/bzip2/lib -lbz2" \
            LIBFFI_CFLAGS="-I$(pwd)/cross-build/iphoneos.arm64/libffi/include" \
            LIBFFI_LIBS="-L$(pwd)/cross-build/iphoneos.arm64/libffi/lib -lffi" \
            --with-openssl="$(pwd)/cross-build/iphoneos.arm64/openssl" \
            --host=arm64-apple-ios12.0 \
            --build=arm64-apple-darwin \
            --with-build-python=$(pwd)/cross-build/macOS/bin/python3.13 \
            --enable-framework
      $ make -j4 all
      $ make install

.. tab:: ARM64 simulator

   .. code-block:: console

      $ export PATH="$(pwd)/iOS/Resources/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin"
      $ ./configure \
            LIBLZMA_CFLAGS="-I$(pwd)/cross-build/iphonesimulator.arm64/xz/include" \
            LIBLZMA_LIBS="-L$(pwd)/cross-build/iphonesimulator.arm64/xz/lib -llzma" \
            BZIP2_CFLAGS="-I$(pwd)/cross-build/iphonesimulator.arm64/bzip2/include" \
            BZIP2_LIBS="-L$(pwd)/cross-build/iphonesimulator.arm64/bzip2/lib -lbz2" \
            LIBFFI_CFLAGS="-I$(pwd)/cross-build/iphonesimulator.arm64/libffi/include" \
            LIBFFI_LIBS="-L$(pwd)/cross-build/iphonesimulator.arm64/libffi/lib -lffi" \
            --with-openssl="$(pwd)/cross-build/iphonesimulator.arm64/openssl" \
            --host=arm64-apple-ios12.0-simulator \
            --build=arm64-apple-darwin \
            --with-build-python=$(pwd)/cross-build/macOS/bin/python3.13 \
            --enable-framework
      $ make -j4 all
      $ make install

.. tab:: x86-64 simulator

   .. code-block:: console

      $ export PATH="$(pwd)/iOS/Resources/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin"
      $ ./configure \
            LIBLZMA_CFLAGS="-I$(pwd)/cross-build/iphonesimulator.x86_64/xz/include" \
            LIBLZMA_LIBS="-L$(pwd)/cross-build/iphonesimulator.x86_64/xz/lib -llzma" \
            BZIP2_CFLAGS="-I$(pwd)/cross-build/iphonesimulator.x86_64/bzip2/include" \
            BZIP2_LIBS="-L$(pwd)/cross-build/iphonesimulator.x86_64/bzip2/lib -lbz2" \
            LIBFFI_CFLAGS="-I$(pwd)/cross-build/iphonesimulator.x86_64/libffi/include" \
            LIBFFI_LIBS="-L$(pwd)/cross-build/iphonesimulator.x86_64/libffi/lib -lffi" \
            --with-openssl="$(pwd)/cross-build/iphonesimulator.x86_64/openssl" \
            --host=x86_64-apple-ios12.0-simulator \
            --build=arm64-apple-darwin \
            --with-build-python=$(pwd)/cross-build/macOS/bin/python3.13 \
            --enable-framework
      $ make -j4 all
      $ make install

These instructions modify your ``PATH`` before the build. As iOS and macOS share
a hardware architecture (ARM64), it is easy for a macOS ARM64 binary to be
accidentally linked into your iOS build. This is especially common when Homebrew
is present on the build system. The most reliable way to avoid this problem is
to remove any potential source of other libraries from your ``PATH``.

However, the ``PATH`` is not completely bare --- it includes the
``iOS/Resources/bin`` folder. This folder contains a collection of scripts that
wrap the invocation of the Xcode :program:`xcrun` tool, removing user- and
version-specific paths from the values encoded in the :py:mod:`sysconfig`
module. Copies of these scripts are included in the final build products.

Once this build completes, the ``iOS/Frameworks`` folder will contain a
``Python.framework`` that can be used for testing.

To run the test suite on iOS, complete a build for a *simulator* platform,
ensure the path modifications from the build are still in effect, and run::

   $ make testios

The full test suite takes approximately 12 minutes to run on a 2022 M1 MacBook
Pro, plus a couple of extra minutes to build the testbed application and boot
the simulator. There will be an initial burst of console output while the Xcode
test project is compiled; however, while the test suite is running, there is no
console output or progress. This is a side effect of how Xcode operates when
executed at the command line. You should see an iOS simulator appear during the
testing process; the simulator will booth to an iOS landing screen, the testbed
app will be installed, and then started. The screen of the simulator will be
black while the test suite is running. When the test suite completes, success or
failure will be reported at the command line. In the case of failure, you will
see the full log of CPython test suite output.

You can also run the test suite in Xcode itself. This is required if you want to
run on a physical device; it is also the easiest approach if you need to run a
single test, or a subset of tests. See the `iOS README
<https://github.com/python/cpython/blob/main/iOS/README.rst#debugging-test-failures>`__
for details.

.. _build-dependencies:
.. _deps-on-linux:
.. _macOS and OS X:
.. _macOS:

Install dependencies
====================

This section explains how to install additional extensions (for example, ``zlib``)
on Linux, macOS and iOS.

.. tab:: Linux

   For Unix-based systems, we try to use system libraries whenever available.
   This means optional components will only build if the relevant system headers
   are available. The best way to obtain the appropriate headers will vary by
   distribution, but the appropriate commands for some popular distributions
   are below.

   On **Fedora**, **RHEL**, **CentOS** and other ``dnf``-based systems::

      $ sudo dnf install dnf-plugins-core  # install this to use 'dnf builddep'
      $ sudo dnf builddep python3


   On **Debian**, **Ubuntu**, and other ``apt``-based systems, try to get the
   dependencies for the Python you're working on by using the ``apt`` command.

   First, make sure you have enabled the source packages in the sources list.
   You can do this by adding the location of the source packages, including
   URL, distribution name and component name, to ``/etc/apt/sources.list``.
   Take Ubuntu 22.04 LTS (Jammy Jellyfish) for example::

      $ deb-src http://archive.ubuntu.com/ubuntu/ jammy main

   Alternatively, uncomment lines with ``deb-src`` using an editor, for
   example::

      $ sudo nano /etc/apt/sources.list

   For other distributions, like Debian, change the URL and names to correspond
   with the specific distribution.

   Then you should update the packages index::

      $ sudo apt-get update

   Now you can install the build dependencies via ``apt``::

      $ sudo apt-get build-dep python3
      $ sudo apt-get install pkg-config

   If you want to build all optional modules, install the following packages and
   their dependencies::

      $ sudo apt-get install build-essential gdb lcov pkg-config \
            libbz2-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev \
            libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev \
            lzma lzma-dev tk-dev uuid-dev zlib1g-dev libmpdec-dev

   Note that Debian 12 and Ubuntu 24.04 do not have the ``libmpdec-dev`` package.  You can safely
   remove it from the install list above and the Python build will use a bundled version.

.. tab:: macOS

   For **macOS systems** (versions 10.9+),
   the Developer Tools can be downloaded and installed automatically;
   you do not need to download the complete Xcode application.

   If necessary, run the following::

      $ xcode-select --install

   This will also ensure that the system header files are installed into
   ``/usr/include``.

   .. _Homebrew: https://brew.sh

   .. _MacPorts: https://www.macports.org

   Also note that macOS does not include several libraries used by the Python
   standard library, including ``libzma``, so expect to see some extension module
   build failures unless you install local copies of them.  As of OS X 10.11,
   Apple no longer provides header files for the deprecated system version of
   OpenSSL which means that you will not be able to build the ``_ssl`` extension.
   One solution is to install these libraries from a third-party package
   manager, like Homebrew_ or MacPorts_, and then add the appropriate paths
   for the header and library files to your ``configure`` command.

   .. tab:: Homebrew

      For **Homebrew**, install dependencies using ``brew``::

         $ brew install pkg-config openssl@3 xz gdbm tcl-tk mpdecimal

      .. tab:: Python 3.13+

         For Python 3.13 and newer::

            $ GDBM_CFLAGS="-I$(brew --prefix gdbm)/include" \
               GDBM_LIBS="-L$(brew --prefix gdbm)/lib -lgdbm" \
               ./configure --with-pydebug \
                           --with-system-libmpdec \
                           --with-openssl="$(brew --prefix openssl@3)"

      .. tab:: Python 3.11-3.12

         For Python 3.11 and 3.12::

            $ GDBM_CFLAGS="-I$(brew --prefix gdbm)/include" \
               GDBM_LIBS="-L$(brew --prefix gdbm)/lib -lgdbm" \
               ./configure --with-pydebug \
                           --with-openssl="$(brew --prefix openssl@3)"

      .. tab:: Python 3.8-3.10

         For Python 3.8, 3.9, and 3.10::

            $ CPPFLAGS="-I$(brew --prefix gdbm)/include -I$(brew --prefix xz)/include" \
               LDFLAGS="-L$(brew --prefix gdbm)/lib -L$(brew --prefix xz)/lib" \
               ./configure --with-pydebug \
                           --with-openssl="$(brew --prefix openssl@3)" \
                           --with-tcltk-libs="$(pkg-config --libs tcl tk)" \
                           --with-tcltk-includes="$(pkg-config --cflags tcl tk)"

   .. tab:: MacPorts

      For **MacPorts**, install dependencies using ``port``::

         $ sudo port install pkgconfig openssl xz gdbm tcl tk +quartz mpdecimal

      .. tab:: Python 3.13+

         For Python 3.13 and newer::

            $ GDBM_CFLAGS="-I$(dirname $(dirname $(which port)))/include" \
               GDBM_LIBS="-L$(dirname $(dirname $(which port)))/lib -lgdbm" \
               ./configure --with-pydebug \
                           --with-system-libmpdec

      .. tab:: Python 3.11-3.12

         For Python 3.11 and 3.12::

            $ GDBM_CFLAGS="-I$(dirname $(dirname $(which port)))/include" \
               GDBM_LIBS="-L$(dirname $(dirname $(which port)))/lib -lgdbm" \
               ./configure --with-pydebug

   And finally, run ``make``::

      $ make -s -j2

   There will sometimes be optional modules added for a new release which
   won't yet be identified in the OS-level build dependencies. In those cases,
   just ask for assistance in the *Core Development* category on :ref:`help-discourse`.

   Explaining how to build optional dependencies on a Unix-based system without
   root access is beyond the scope of this guide.

   For more details on various options and considerations for building, refer
   to the `macOS README
   <https://github.com/python/cpython/blob/main/Mac/README.rst>`_.

   .. _clang: https://clang.llvm.org/
   .. _ccache: https://ccache.dev/

   .. note:: While you need a C compiler to build CPython, you don't need any
      knowledge of the C language to contribute!  Vast areas of CPython are
      written completely in Python: as of this writing, CPython contains slightly
      more Python code than C.

.. tab:: Windows

   On Windows, extensions are already included and built automatically.

.. tab:: iOS

   As with CPython itself, the dependencies for CPython must be compiled for
   each of the hardware architectures that iOS supports. Consult the
   documentation for `XZ <https://xz.tukaani.org/xz-utils/>`__, `bzip2
   <https://sourceware.org/bzip2/>`__, `OpenSSL <https://www.openssl.org>`__ and
   `libffi <https://github.com/libffi/libffi>`__ for details on how to configure
   the project for cross-platform iOS builds.

   Alternatively, the `BeeWare Project <https://beeware.org>`__ maintains a
   `project for building iOS dependencies
   <https://github.com/beeware/cpython-apple-source-deps>`__, and distributes
   `pre-compiled binaries
   <https://github.com/beeware/cpython-apple-source-deps/releases>`__ for each
   of the dependencies. If you use this project to build the dependencies
   yourself, the subfolders of the ``install`` folder can be used to configure
   CPython. If you use the pre-compiled binaries, you should unpack each tarball
   into a separate folder, and use that folder as the configuration target.

.. _regenerate_configure:

Regenerate ``configure``
========================

If a change is made to Python which relies on some POSIX system-specific
functionality (such as using a new system call), it is necessary to update the
:cpy-file:`configure` script to test for availability of the functionality.
Python's :file:`configure` script is generated from :cpy-file:`configure.ac`
using `GNU Autoconf <https://www.gnu.org/software/autoconf/>`_.

After editing :file:`configure.ac`, run ``make regen-configure`` to generate
:file:`configure`, :cpy-file:`pyconfig.h.in`, and :cpy-file:`aclocal.m4`.
When submitting a pull request with changes made to :file:`configure.ac`,
make sure you also commit the changes in the generated files.

Python's :file:`configure.ac` script requires a specific version of
GNU Autoconf.
For Python 3.12 and newer, GNU Autoconf v2.71 is required.
For Python 3.11 and earlier, GNU Autoconf v2.69 is required.

The recommended and by far the easiest way to regenerate :file:`configure` is::

   $ make regen-configure

This will use Podman or Docker to do the regeneration with the proper version
of GNU Autoconf.

If you cannot (or don't want to) use ``make regen-configure``,
install the :program:`autoconf-archive` and :program:`pkg-config` utilities,
and make sure the :file:`pkg.m4` macro file located in the appropriate
:program:`aclocal` location::

   $ ls $(aclocal --print-ac-dir) | grep pkg.m4

.. note::

   Running :program:`autoreconf` is not the same as running :program:`autoconf`.
   For example, running :program:`autoconf` by itself will not regenerate
   :file:`pyconfig.h.in`.
   :program:`autoreconf` runs :program:`autoconf` and a number of other tools
   repeatedly as appropriate.

.. _build_troubleshooting:

Regenerate the ABI dump
=======================

Maintenance branches (not ``main``) have a special file located in
``Doc/data/pythonX.Y.abi`` that allows us to know if a given Pull Request
affects the public ABI. This file is used by the GitHub CI in a check
called ``Check if the ABI has changed`` that will fail if a given Pull Request
has changes to the ABI and the ABI file is not updated.

This check acts as a fail-safe and **doesn't necessarily mean that the Pull
Request cannot be merged**. When this check fails you should add the relevant
release manager to the PR so that they are aware of the change and they can
validate if the change can be made or not.

.. important::
   ABI changes are allowed before the first release candidate. After the first release
   candidate, all further releases must have the same ABI for ensuring compatibility
   with native extensions and other tools that interact with the Python interpreter.
   See the documentation about the :ref:`release candidate <rc>` phase.

When the PR check fails, the associated run will have the updated ABI file
attached as an artifact. After release manager approval, you can download and
add this file into your PR to pass the check.

You can regenerate the ABI file by yourself by invoking the ``regen abidump``
Make target. Note that for doing this you need to regenerate the ABI file in
the same environment that the GitHub CI uses to check for it. This is because
different platforms may include some platform-specific details that make the
check fail even if the Python ABI is the same. The easier way to regenerate
the ABI file using the same platform as the CI uses is by using Docker::

   # In the CPython root:
   $ docker run -v$(pwd):/src:Z -w /src --rm -it ubuntu:22.04 \
       bash /src/.github/workflows/regen-abidump.sh

Note that the ``ubuntu`` version used to execute the script matters and
**must** match the version used by the CI to check the ABI. See the
``.github/workflows/build.yml`` file for more information.

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

Editors and tools
=================

Python is used widely enough that practically all code editors have some form
of support for writing Python code. Various coding tools also include Python
support.

For editors and tools which the core developers have felt some special comment
is needed for coding *in* Python, see :ref:`resources`.

.. _build-directory-structure:

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
     Mac-specific code (for example, using IDLE as a macOS application).

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
     CPython interpreter.

``Python``
     The code that makes up the core CPython runtime. This includes the
     compiler, eval loop and various built-in modules.

``Tools``
     Various tools that are (or have been) used to maintain Python.


.. _issue tracker: https://github.com/python/cpython/issues


.. _using-codespaces:

Contribute using GitHub Codespaces
==================================

.. _codespaces-whats-codespaces:

What is GitHub Codespaces?
--------------------------

If you'd like to start contributing to CPython without needing to set up a local
developer environment, you can use
`GitHub Codespaces <https://github.com/features/codespaces>`_.
Codespaces is a cloud-based development environment offered by GitHub that
allows developers to write, build, test, and debug code directly within their
web browser or in Visual Studio Code (VS Code).

To help you get started, CPython contains a
`devcontainer folder <https://github.com/python/cpython/tree/main/.devcontainer>`_
with a JSON configuration file that provides consistent and versioned codespace
configurations for all users of the project. It also contains a Dockerfile that
allows you to set up the same environment but locally in a Docker container if
you'd prefer to use that directly.

.. _codespaces-create-a-codespace:

Create a CPython codespace
--------------------------

Here are the basic steps needed to contribute a patch using Codespaces.
You first need to navigate to the
`CPython repo <https://github.com/python/cpython>`_ hosted on GitHub.

Then you will need to:

1. Press the ``,`` key to launch the codespace setup screen for the current
   branch (alternatively, click the green :guilabel:`Code` button and choose
   the ``codespaces`` tab and then press the
   green :guilabel:`Create codespace on main` button).
2. A screen should appear that lets you know your codespace is being set up.
   (Note: Since the CPython devcontainer is provided, codespaces will use the
   configuration it specifies.)
3. A `web version of VS Code <https://vscode.dev/>`_ will open inside your web
   browser, already linked up with your code and a terminal to the remote
   codespace where CPython and its documentation have already been built.
4. Use the terminal with the usual Git commands to create a new branch, commit
   and push your changes once you're ready!

If you close your repository and come back later you can always resume your
codespace by navigating to the CPython repo, selecting the codespaces tab and
selecting your most recent codespaces session. You should then be able to pick
up from where you left off!

.. _codespaces-use-locally:

Use Codespaces locally
----------------------

On the bottom left side of the codespace screen you will see a green or grey
square that says :guilabel:`Codespaces`. You can click this for additional
options. If you prefer working in a locally installed copy of VS Code you can
select the option ``Open in VS Code``. You will still be working on the remote
codespace instance, thus using the remote instance's compute power. The compute
power may be a much higher spec than your local machine which can be helpful.


.. TODO: add docker instructions
