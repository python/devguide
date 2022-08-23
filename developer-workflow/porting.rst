.. _porting:

=========================
Porting to a New Platform
=========================

The first step is to familiarize yourself with the development toolchain on
the platform in question, notably the C compiler. Make sure you can compile and
run a hello-world program using the target compiler.

Next, learn how to compile and run the Python interpreter on a platform to
which it has already been ported; preferably Unix, but Windows will
do, too. The build process for Python, in particular the ``Makefile`` in the
source distribution, will give you a hint on which files to compile
for Python.  Not all source files are relevant: some are platform-specific,
and others are only used in emergencies (e.g. ``getopt.c``).

It is not recommended to start porting Python without at least a medium-level
understanding of your target platform; i.e. how it is generally used, how to
write platform-specific apps, etc. Also, some Python knowledge is required, or
you will be unable to verify that your port is working correctly.

You will need a ``pyconfig.h`` file tailored for your platform.  You can
start with ``pyconfig.h.in``, read the comments, and turn on definitions that
apply to your platform.  Also, you will need a ``config.c`` file, which lists
the built-in modules you support.  Again, starting with
``Modules/config.c.in`` is recommended.

Finally, you will run into some things that are not supported on your
target platform.  Forget about the ``posix`` module in the beginning. You can
simply comment it out of the ``config.c`` file.

Keep working on it until you get a ``>>>`` prompt.  You may have to disable the
importing of ``site.py`` by passing the ``-S`` option. When you have a prompt,
bang on it until it executes very simple Python statements.

At some point you will want to use the ``os`` module; this is the time to start
thinking about what to do with the ``posix`` module.  It is okay to simply
comment out functions in the ``posix`` module that cause problems; the
remaining ones will be quite useful.

Before you are done, it is highly recommended to run the Python regression test
suite, as described in :ref:`runtests`.
