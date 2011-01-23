.. _runtests:

Running & Writing Tests
=======================

.. note::
    This document assumes you are working from a checkout of Python. If you
    are not then some things presented here may not work as they may depend
    on new features not available in earlier versions of Python.

Running
-------

The shortest, simplest way of running the test suite is the following command
from the root directory of your checkout (after you have built Python)::

    ./python -m test

This will run the majority of tests, but exclude a small portion of them; these
excluded tests use special kinds of resources: for example, accessing the
Internet, or trying to play a sound or to display a graphical interface on
your desktop.  They are disabled by default so that running the test suite
is not too intrusive.  To enable some of these additional tests (and for
other flags which can help debug various issues such as reference leaks), read
the help text::

    ./python -m test -h

If you want to run a single test, simply specify the test name as an argument.
You also probably want to enable verbose mode (using ``-v``), so that individual
failures are detailed::

    ./python -m test -v test_abc

If you have a multi-core or multi-CPU machine, you can enable parallel testing
using several Python processes so as to speed up things::

   ./python -m test -j2

.. _strenuous_testing:

Finally, if you want to run tests under a more strenuous set of settings, you
can run ``test`` as::

    ./python -bb -E -Wd -m test -r -w -uall

The various extra flags passed to Python cause it to be much stricter about
various things (the ``-Wd`` flag should be ``-W error`` at some point, but the
test
suite has not reached a point where all warnings have been dealt with and so we
cannot guarantee that a bug-free Python will properly complete a test run with
``-W error``). The ``-r`` flag to the test runner causes it to run more randomly
which helps assert that the various tests don't interfere against each other.
The ``-w`` flag causes failures to run again to see if it a transient failure
or a consistent one. The ``-uall`` flag allows the user of all available
resources so as to not skip tests requiring, e.g., Internet access.


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
