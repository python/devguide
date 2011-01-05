.. _runtests:

Running & Writing Tests
=======================

.. note::
    This document assumes you are working with the in-development version of
    Python. If you are not then some things presented here may not work as they
    may depend on new features not available in released versions of Python.

Running
-------

The shortest, simplest way of running the test suite is::

    ./python -m test

That will run the entire standard test suite (i.e., all tests that do not
consume a lot of resources) using the ``test.regrtest`` module (Python's test
runner which you can execute directly if you prefer).
To run **all** tests, you need to specify what
resources you are willing to have consumed. For those flags (and others which
can help debug various issues such as reference leaks), read the help text::

    ./python -m test -h

If you want to run a single test, simply specify the test name as an argument::

    ./python -m test test_abc

Finally, if you want to run tests under a more strenuous set of settings, you
can run test as::

    ./python -bb -E -Wd -m test -j2 -r -w

The various extra flags passed to Python cause it to be much stricter about
various things (the ``-Wd`` flag should be ``-We`` at some point, but the test
suite has not reached a point where all warnings have been dealt with and so we
cannot guarantee that a bug-free Python will properly complete a test run with
``-We``). The flags to the test runner cause it to run faster but also
more randomly which is also a stricter way to run tests thanks to possible
assumptions in test order or state that may have been made. It also causes
failures to run again to see if it a transient failure or a consistent one.


Writing
-------

XXX
