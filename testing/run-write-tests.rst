.. _run-write-tests:
.. _runtests:

=========================
Running and writing tests
=========================

.. raw:: html

    <script>
    document.addEventListener('DOMContentLoaded', function() {
      activateTab(getOS());
    });
    </script>

.. note::

    This document assumes you are working from an
    :ref:`in-development <indevbranch>` checkout of Python. If you
    are not then some things presented here may not work as they may depend
    on new features not available in earlier versions of Python.

Running
=======

The shortest, simplest way of running the test suite is the following command
from the root directory of your checkout (after you have
:ref:`built Python <compiling>`):

.. tab:: Unix

    .. code-block:: shell

        ./python -m test

.. tab:: macOS

    .. code-block:: shell

        ./python.exe -m test

    This works on :ref:`most <mac-python.exe>` macOS systems.

.. tab:: Windows

    .. code-block:: dosbatch

        .\python.bat -m test

This will run the majority of tests, but exclude a small portion of them; these
excluded tests use special kinds of resources: for example, accessing the
Internet, or trying to play a sound or to display a graphical interface on
your desktop.  They are disabled by default so that running the test suite
is not too intrusive.  To enable some of these additional tests (and for
other flags which can help debug various issues such as reference leaks), read
the help text:

.. tab:: Unix

    .. code-block:: shell

        ./python -m test -h

.. tab:: macOS

    .. code-block:: shell

        ./python.exe -m test -h

.. tab:: Windows

    .. code-block:: dosbatch

        .\python.bat -m test -h

If you want to run a single test file, simply specify the test file name
(without the extension) as an argument.  You also probably want to enable
verbose mode (using ``-v``), so that individual failures are detailed:

.. tab:: Unix

    .. code-block:: shell

        ./python -m test -v test_abc

.. tab:: macOS

    .. code-block:: shell

        ./python.exe -m test -v test_abc

.. tab:: Windows

    .. code-block:: dosbatch

        .\python.bat -m test -v test_abc

To run a single test case, use the ``unittest`` module, providing the import
path to the test case:

.. tab:: Unix

    .. code-block:: shell

        ./python -m unittest -v test.test_abc.TestABC_Py

.. tab:: macOS

    .. code-block:: shell

        ./python.exe -m unittest -v test.test_abc.TestABC_Py

.. tab:: Windows

    .. code-block:: dosbatch

        .\python.bat -m unittest -v test.test_abc.TestABC_Py

Some test modules also support direct invocation,
which might be useful for IDEs and local debugging:

.. tab:: Unix

    .. code-block:: shell

        ./python Lib/test/test_typing.py

.. tab:: macOS

    .. code-block:: shell

        ./python.exe Lib/test/test_typing.py

.. tab:: Windows

    .. code-block:: dosbatch

        .\python.bat Lib/test/test_typing.py

But, there are several important notes:

1. This way of running tests exists only
   for local developer needs and is discouraged for anything else
2. Some modules do not support it at all. One example is ``test_importlib``.
   In other words: if some module does not have ``unittest.main()``, then
   most likely it does not support direct invocation.

If you have a multi-core or multi-CPU machine, you can enable parallel testing
using several Python processes so as to speed up things:

.. tab:: Unix

    .. code-block:: shell

        ./python -m test -j0

.. tab:: macOS

    .. code-block:: shell

        ./python.exe -m test -j0

.. tab:: Windows

    .. code-block:: dosbatch

        .\python.bat -m test -j0

.. _strenuous_testing:

Finally, if you want to run tests under a more strenuous set of settings, you
can run ``test`` as:

.. tab:: Unix

    .. code-block:: shell

        ./python -bb -E -Wd -m test -r -w -uall

.. tab:: macOS

    .. code-block:: shell

        ./python.exe -bb -E -Wd -m test -r -w -uall

.. tab:: Windows

    .. code-block:: dosbatch

        .\python.bat -bb -E -Wd -m test -r -w -uall

The various extra flags passed to Python cause it to be much stricter about
various things (the ``-Wd`` flag should be ``-W error`` at some point, but the
test suite has not reached a point where all warnings have been dealt with and
so we cannot guarantee that a bug-free Python will properly complete a test run
with ``-W error``). The ``-r`` flag to the test runner causes it to run tests in
a more random order which helps to check that the various tests do not interfere
with each other.  The ``-w`` flag causes failing tests to be run again to see
if the failures are transient or consistent.
The ``-uall`` flag allows the use of all available
resources so as to not skip tests requiring, for example, Internet access.

To check for reference leaks (only needed if you modified C code),
you can enable reference leak checking during testing using the ``-R`` flag.
For example, using the command::

    python -m test <test_name> -R :

This default setting performs a few initial warm-up runs to stabilize the reference count,
followed by additional runs to check for leaks.

If you want more control over the number of runs, you can specify ``warmups`` and ``repeats`` explicitly::

    python -m test <test_name> -R <warmups>:<repeats>

For instance, ``-R 3:2`` will first run the test 3 times to settle down the
reference count, and then run it 2 more times to check for leaks.

You can also execute the ``Tools/scripts/run_tests.py`` script as  found in a
CPython checkout. The script tries to balance speed with thoroughness. But if
you want the most thorough tests you should use the strenuous approach shown
above.

Locale support
--------------

Some tests require specific locales to run successfully. These locales are
often non-default, non-English, non-UTF-8 locales. If a necessary locale is
unavailable, the test is skipped or runs in the dry-run mode.
Additional locales that you may find helpful to set up on developer's machines
or buildbots include:

* ``en_US`` (``en_US.utf8``, ``en_US.iso88591``) --- the standard default
* ``de_DE`` (``de_DE.UTF-8``) or ``fr_FR`` (``fr_FR.utf8``, ``fr_FR.iso88591``,
  ``fr_FR.iso885915@euro``) --- common non-English locales
* ``tr_TR`` (``tr_TR.iso88599``) --- Turkish has different rules for upper/lower
  cases of "i" and "I".
* ``ps_AF`` --- used in ``test_decimal``

On Linux and macOS, the ``locale`` command can be used to list available
locales and change the settings. Environment variables ``LANG`` and those
prefixed with ``LC_`` can be used to set the locale.

Unexpected skips
----------------

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
=======

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

For tests of the C API, see Tests sections in :ref:`c-api`.


Benchmarks
==========

Benchmarking is useful to test that a change does not degrade performance.

`The Python Benchmark Suite <https://github.com/python/pyperformance>`_
has a collection of benchmarks for all Python implementations. Documentation
about running the benchmarks is in the `README.txt
<https://github.com/python/pyperformance/blob/main/README.rst>`_ of the repo.
