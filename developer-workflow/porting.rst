.. _porting:

============================
Porting and platform support
============================

The Python interpreter runs on an underlying *platform* -- the operating system
(for example, Linux, Windows or macOS), processor (like Intel/AMD, ARM),
C compiler and library, and other "lower level" details.

CPython is *officially supported* on several platforms, on which the core team
has adequate knowledge and resources to test releases and fix bugs.
See :pep:`11` for details.

Other platforms are unsupported *by the core team*, but might be supported
by others -- as a volunteer project, by a company that wants Python on "their"
system, or just as a one-off experiment.
See :pep:`11#unsupported-platforms` for the policy on merging code for
unsupported platforms into the main CPython repository.


.. _ports:

Ports and contacts
==================

The table below lists relevant third-party projects,
their maintainers, and links to information that's relevant when triaging
platform-specific issues.

It is OK to @mention the listed GitHub usernames to draw maintainers' attention
or request their opinion on platform-specific issues.
Maintainers must only be listed with their permission, and they may remove
themselves at any time.

Third-party projects should only be listed if they benefit substantially
more people than the maintainer(s).
Officially supported platforms are included when there are relevant links
to show, or to group similar platforms.

Links should be for the port specifically (not the platform itself),
and relevant for porting work and fixing platform-specific issues
(no homepage/marketing links).

* **AIX**: :github-user:`ayappanec`
* **Linux** [t1]_

  * Fedora: :github-user:`hroncok`, :github-user:`befeleme`; see
    `Config & patches <https://src.fedoraproject.org/rpms/python3.15/tree/rawhide>`_,
    `Bugs <https://bugzilla.redhat.com/buglist.cgi?bug_status=NEW&bug_status=ASSIGNED&classification=Fedora&columnlist=product%2Ccomponent%2Cassigned_to%2Cbug_status%2Cshort_desc%2Cchangeddate%2Cbug_severity&f1=component&o1=regexp&order=status%2C%20assigned_to%2C%20id%2C%20&product=Fedora&product=Fedora%20EPEL&query_format=advanced&v1=python3%5C..%2A>`__,
    `Maintenance guide <https://hackmd.io/9f64YNIZTCy0ZzKb5wKtqQ?view>`__
  * Debian: :github-user:`stefanor`, :github-user:`doko42`; see
    `Config & patches <https://salsa.debian.org/cpython-team/python3/-/tree/master/debian/patches>`_,
    `Bugs <https://bugs.debian.org/cgi-bin/pkgreport.cgi?src=python3.15>`__,
    `Wiki <https://wiki.debian.org/Python>`__
  * Alpine: see
    `Config & patches <https://github.com/alpinelinux/aports/tree/master/main/python3>`_
* **macOS** [t1]_: :gh-python-team:`macos-team`, :github-user:`freakboy3742`;
  see
  `Limitations <https://docs.python.org/3/library/intro.html#mobile-platforms>`__,
  `Usage <https://docs.python.org/3/library/intro.html#mobile-platforms>`__,
  :cpy-file:`Platforms/Apple`
* Mobile platforms: see
  `Limitations <https://docs.python.org/3/library/intro.html#mobile-platforms>`__

  * **Android** [t3]_: :github-user:`mhsmith`; see
    `Usage <https://docs.python.org/3/using/android.html>`__,
    :cpy-file:`Platforms/Android`
  * **iOS** [t3]_: :github-user:`freakboy3742`, :github-user:`ned-deily`; see
    `Usage <https://docs.python.org/3/using/ios.html>`__,
    :cpy-file:`Platforms/Apple`

* **Solaris**/OpenIndiana: :github-user:`jcea`, :github-user:`kulikjak`
* **WebAssembly**: see `Limitations <https://docs.python.org/3/library/intro.html#webassembly-platforms>`__

  * WASI [t2]_: see :cpy-file:`WASI <Platforms/WASI>`
  * Emscripten [t3]_: :github-user:`pmp-p`, :github-user:`rdb`, :github-user:`rth`; see
    :cpy-file:`emscripten <Platforms/emscripten>`

    * Pyodide: :github-user:`hoodmane`, :github-user:`ryanking13`, :github-user:`agriyakhetarpal`

* **Windows** [t1]_: :gh-python-team:`windows-team`, :github-user:`pfmoore`; see
  `Usage <https://docs.python.org/3/using/windows.html>`__,
  :cpy-file:`PC`,
  :cpy-file:`PCbuild`
* **Cross-Platform**:

  * conda-forge: see
    `Recipe <https://github.com/conda-forge/python-feedstock/tree/main/recipe>`_

.. [t1] Specific variants have official :pep:`Tier 1 support <11#tier-1>`
.. [t2] Specific variants have official :pep:`Tier 2 support <11#tier-2>`
.. [t3] Specific variants have official :pep:`Tier 3 support <11#tier-3>`


Porting to a new platform
=========================

Porting CPython to an entirely new platform is an adventure.
If you try it, consider keeping notes -- and updating this guide, if you
find something that might be relevant to others.
Since each platform is different, this guide can only give you a
few rough tips.

The first step is to familiarize yourself with the development toolchain on
the platform in question, notably the C compiler. Make sure you can compile and
run a hello-world program using the target compiler.

Next, learn how to compile and run the Python interpreter on a platform to
which it has already been ported; preferably Unix, but Windows will
do, too. The build process for Python, in particular the ``Makefile`` in the
source distribution, will give you a hint on which files to compile
for Python. Not all source files are relevant: some are platform-specific,
and others are only used in emergencies (for example,
:cpy-file:`Python/getopt.c`).

It is not recommended to start porting Python without at least a medium-level
understanding of your target platform; how it is generally used, how to
write platform-specific apps, and so on. Also, some Python knowledge is required, or
you will be unable to verify that your port is working correctly.

On systems with a UNIX shell, run the included :cpy-file:`configure` script.
This should generate all required files, including a :file:`Makefile`.
If it does not, you will need to debug it (or reimplement it).
Note that the script is generated from :cpy-file:`configure.ac` using GNU
Autotools.
(CPython pins a specific version for reproducibility, but other versions may
work fine.)

The main files that ``configure`` generates -- and which you might want to
check -- are:

* A :file:`pyconfig.h` file tailored for your platform.
  If you need to create this manually, start with :cpy-file:`pyconfig.h.in`,
  read the comments, and turn on definitions that apply to your platform.
* A :file:`config.c` file, which lists the built-in modules you support.
  Until you get dynamic extension loading to work, all compiled modules
  you need to import will need to be listed here.
  The file is generated from :cpy-file:`Modules/config.c.in`.
* A :file:`Makefile` with instructions to put everything together.
  If one isn't generated, try compiling all the ``*.c`` files, and fix the
  errors -- or omit files that don't look important.
  For example, forget about the ``posix`` module
  (:cpy-file:`Modules/posixmodule.c`) in the beginning: don't compile it,
  and comment it out of the :file:`config.c` file.

Keep working on it until you get a ``>>>`` prompt.  You may have to disable the
importing of ``site.py`` by passing the ``-S`` option. When you have a prompt,
bang on it until it executes very simple Python statements.

At some point you will want to use the ``os`` module; this is the time to start
thinking about what to do with the ``posix`` module.  It is okay to simply
comment out functions in the ``posix`` module that cause problems; the
remaining ones will be quite useful.
You can use the same approach for other modules too, of course.

Before you are done, it is highly recommended to run the Python regression test
suite, as described in :ref:`runtests`.
You will probably need to skip tests that do not make sense; for inspiration
look at how that's done for the WASI platform.
