.. _runtests:

Running & Writing Tests
=======================

.. note::

    This document assumes you are working from an
    :ref:`in-development <indevbranch>` checkout of Python. If you
    are not then some things presented here may not work as they may depend
    on new features not available in earlier versions of Python.

Running
-------

The shortest, simplest way of running the test suite is the following command
from the root directory of your checkout (after you have
:ref:`built Python <compiling>`)::

    ./python -m test

You may need to change this command as follows throughout this section.
On :ref:`most <mac-python.exe>` Mac OS X systems, replace :file:`./python`
with :file:`./python.exe`.  On Windows, use :file:`PCbuild\\python_d.exe` or
check the detailed :ref:`Windows instructions <win-python.exe>`.  If using
Python 2.7, replace ``test`` with ``test.regrtest``.

If you don't have easy access to a command line, you can run the test suite from
a Python or IDLE shell::

    >>> from test import autotest

This will run the majority of tests, but exclude a small portion of them; these
excluded tests use special kinds of resources: for example, accessing the
Internet, or trying to play a sound or to display a graphical interface on
your desktop.  They are disabled by default so that running the test suite
is not too intrusive.  To enable some of these additional tests (and for
other flags which can help debug various issues such as reference leaks), read
the help text::

    ./python -m test -h

If you want to run a single test file, simply specify the test file name
(without the extension) as an argument.  You also probably want to enable
verbose mode (using ``-v``), so that individual failures are detailed::

    ./python -m test -v test_abc

To run a single test case, use the ``unittest`` module, providing the import
path to the test case::

   ./python -m unittest -v test.test_abc.TestABC

If you have a multi-core or multi-CPU machine, you can enable parallel testing
using several Python processes so as to speed up things::

   ./python -m test -j0

If you are running a version of Python prior to 3.3 you must specify the number
of processes to run simultaneously (e.g. ``-j2``).

.. _strenuous_testing:

Finally, if you want to run tests under a more strenuous set of settings, you
can run ``test`` as::

    ./python -bb -E -Wd -m test -r -w -uall

The various extra flags passed to Python cause it to be much stricter about
various things (the ``-Wd`` flag should be ``-W error`` at some point, but the
test suite has not reached a point where all warnings have been dealt with and
so we cannot guarantee that a bug-free Python will properly complete a test run
with ``-W error``). The ``-r`` flag to the test runner causes it to run tests in
a more random order which helps to check that the various tests do not interfere
with each other.  The ``-w`` flag causes failing tests to be run again to see
if the failures are transient or consistent.
The ``-uall`` flag allows the use of all available
resources so as to not skip tests requiring, e.g., Internet access.

To check for reference leaks (only needed if you modified C code), use the
``-R`` flag.  For example, ``-R 3:2`` will first run the test 3 times to settle
down the reference count, and then run it 2 more times to verify if there are
any leaks.

You can also execute the ``Tools/scripts/run_tests.py`` script as  found in a
CPython checkout. The script tries to balance speed with thoroughness. But if
you want the most thorough tests you should use the strenuous approach shown
above.


Unexpected Skips
^^^^^^^^^^^^^^^^

Sometimes when running the test suite, you will see "unexpected skips"
reported. These represent cases where an entire test module has been
skipped, but the test suite normally expects the tests in that module to
be executed on that platform.

Often, the cause is that an optional module hasn't been built due to missing
build dependencies. In these cases, the missing module reported when the test
is skipped should match one of the modules reported as failing to build when
:ref:`compiling`.

In other cases, the skip message should provide enough detail to help figure
out and resolve the cause of the problem (for example, the default security
settings on some platforms will disallow some tests)


Writing
-------

Writing tests for Python is much like writing tests for your own code. Tests
need to be thorough, fast, isolated, consistently repeatable, and as simple as
possible. We try to have tests both for normal behaviour and for error
conditions.  Tests live in the ``Lib/test`` directory, where every file that
includes tests has a ``test_`` prefix.

One difference with ordinary testing is that you are encouraged to rely on the
:py:mod:`test.support` module. It contains various helpers that are tailored to
Python's test suite and help smooth out common problems such as platform
differences, resource consumption and cleanup, or warnings management.
That module is not suitable for use outside of the standard library.

When you are adding tests to an existing test file, it is also recommended
that you study the other tests in that file; it will teach you which precautions
you have to take to make your tests robust and portable.


Benchmarks
----------
Benchmarking is useful to test that a change does not degrade performance.

`The Grand Unified Python Benchmark Suite <https://hg.python.org/benchmarks/>`_
has a collection of benchmarks for all Python implementations. Documentation
about running the benchmarks is in the `README.txt
<https://hg.python.org/benchmarks/file/tip/README.txt>`_ of the benchmarks repo.
