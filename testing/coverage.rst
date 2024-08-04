.. _coverage:

======================
Increase test coverage
======================

.. raw:: html

    <script>
    document.addEventListener('DOMContentLoaded', function() {
      activateTab(getOS());
    });
    </script>

Python development follows a practice that all semantic changes and additions
to the language and :abbr:`stdlib (standard library)` are accompanied by
appropriate unit tests. Unfortunately Python was in existence for a long time
before the practice came into effect. This has left chunks of the stdlib
untested which is not a desirable situation to be in.

A good, easy way to become acquainted with Python's code and to help out is to
help increase the test coverage for Python's stdlib. Ideally we would like to
have 100% coverage, but any increase is a good one. Do realize, though, that
getting 100% coverage is not always possible. There could be platform-specific
code that simply will not execute for you, errors in the output, etc. You can
use your judgement as to what should and should not be covered, but being
conservative and assuming something should be covered is generally a good rule
to follow.

Choosing what module you want to increase test coverage for can be done in a
couple of ways.
You can simply run the entire test suite yourself with coverage turned
on and see what modules need help. This has the drawback of running the entire
test suite under coverage measuring which takes some time to complete, but you
will have an accurate, up-to-date notion of what modules need the most work.

Another is to follow the examples below and simply see what
coverage your favorite module has. This is "stabbing in the dark", though, and
so it might take some time to find a module that needs coverage help.

Do make sure, though, that for any module you do decide to work on that you run
coverage for just that module. This will make sure you know how good the
explicit coverage of the module is from its own set of tests instead of from
implicit testing by other code that happens to use the module.


Common gotchas
==============

Please realize that coverage reports on modules already imported before coverage
data starts to be recorded will be wrong. Typically you can tell a module falls
into this category by the coverage report saying that global statements that
would obviously be executed upon import have gone unexecuted while local
statements have been covered. In these instances you can ignore the global
statement coverage and simply focus on the local statement coverage.

When writing new tests to increase coverage, do take note of the style of tests
already provided for a module (for example, whitebox, blackbox, etc.). As
some modules are primarily maintained by a single core developer they may have
a specific preference as to what kind of test is used (for example, whitebox) and
prefer that other types of tests not be used (for example, blackbox). When in doubt,
stick with whitebox testing in order to properly exercise the code.


Measuring coverage
==================

It should be noted that a quirk of running coverage over Python's own stdlib is
that certain modules are imported as part of interpreter startup. Those modules
required by Python itself will not be viewed as executed by the coverage tools
and thus look like they have very poor coverage (for example, the :py:mod:`stat`
module). In these instances the module will appear to not have any coverage of
global statements but will have proper coverage of local statements (for example,
function definitions will not be traced, but the function bodies will).
Calculating the coverage of modules in this situation will simply require
manually looking at what local statements were not executed.

Using coverage.py
-----------------

One of the most popular third-party coverage tools is `coverage.py`_ which
provides very nice HTML output along with advanced features such as
:ref:`branch coverage <branch_coverage>`. If you prefer to stay with tools only
provided by the stdlib then you can :ref:`use test.regrtest
<coverage_by_regrtest>`.


.. _install_coverage:

Install coverage
^^^^^^^^^^^^^^^^

By default, pip will not install into the in-development version of Python you
just built, and this built version of Python will not see packages installed
into your default version of Python. One option is to use a virtual environment
to install coverage.

.. tab:: Unix

    Run:

    .. code-block:: shell

        ./python -m venv ../cpython-venv
        source ../cpython-venv/bin/activate
        pip install coverage

.. tab:: macOS

    On :ref:`most <mac-python.exe>` macOS systems run:

    .. code-block:: shell

        ./python.exe -m venv ../cpython-venv
        source ../cpython-venv/bin/activate
        pip install coverage

.. tab:: Windows

    Run:

    .. code-block:: dosbatch

        python.bat -m venv ..\\cpython-venv
        ..\\cpython-venv\\Scripts\\activate.bat
        pip install coverage

You can now use python without the ./ for the rest of these instructions, as
long as your venv is activated. For more info on venv see `Virtual Environment
<https://docs.python.org/3/tutorial/venv.html>`_ documentation.

If this does not work for you for some reason, you should try using the
in-development version of coverage.py to see if it has been updated as needed.
To do this you should clone/check out the development version of coverage.py::

    git clone https://github.com/nedbat/coveragepy

You will need to use the full path to the installation.

Another option is to use an installed copy of coverage.py, if you already have
it. For this, you will again need to use the full path to that installation.

.. _coverage_usage:

Basic usage
^^^^^^^^^^^

The following command will tell you if your copy of coverage works (substitute
``COVERAGEDIR`` with the directory where your clone exists, for example,
``../coveragepy``)::

    ./python COVERAGEDIR

Coverage.py will print out a little bit of helper text verifying that
everything is working. If you are using an installed copy, you can do the
following instead (note this must be installed using the built copy of Python,
such as by venv)::

    ./python -m coverage

The rest of the examples on how to use coverage.py will assume you are using a
cloned copy, but you can substitute the above and all instructions should still
be valid.

To run the test suite under coverage.py, do the following::

    ./python COVERAGEDIR run --pylib Lib/test/regrtest.py

To run only a single test, specify the module/package being tested
in the ``--source`` flag (so as to prune the coverage reporting to only the
module/package you are interested in) and then append the name of the test you
wish to run to the command::

    ./python COVERAGEDIR run --pylib --source=abc Lib/test/regrtest.py test_abc

To see the results of the coverage run, you can view a text-based report with::

    ./python COVERAGEDIR report

You can use the ``--show-missing`` flag to get a list of lines that were not
executed::

    ./python COVERAGEDIR report --show-missing

But one of the strengths of coverage.py is its HTML-based reports which let
you visually see what lines of code were not tested::

    ./python COVERAGEDIR html -i --include=`pwd`/Lib/* --omit="Lib/test/*,Lib/*/tests/*"

This will generate an HTML report in a directory named ``htmlcov`` which
ignores any errors that may arise and ignores modules for which test coverage is
unimportant (for example, tests, temp files, etc.). You can then open the
``htmlcov/index.html`` file in a web browser to view the coverage results along
with pages that visibly show what lines of code were or were not executed.


.. _branch_coverage:

Branch coverage
^^^^^^^^^^^^^^^

For the truly daring, you can use another powerful feature of coverage.py:
branch coverage. Testing every possible branch path through code, while a great
goal to strive for, is a secondary goal to getting 100% line
coverage for the entire stdlib (for now).

If you decide you want to try to improve branch coverage, simply add the
``--branch`` flag to your coverage run::

    ./python COVERAGEDIR run --pylib --branch <arguments to run test(s)>

This will lead to the report stating not only what lines were not covered, but
also what branch paths were not executed.


.. _coverage_by_regrtest:

Using test.regrtest
-------------------

If you prefer to rely solely on the stdlib to generate coverage data, you can
do so by passing the appropriate flags to :py:mod:`test` (along with
any other flags you want to)::

    ./python -m test --coverage -D `pwd`/coverage_data <test arguments>

Do note the argument to ``-D``; if you do not specify an absolute path to where
you want the coverage data to end up it will go somewhere you don't expect.


.. note::
    If you are running coverage over the entire test suite, make sure to
    add ``-x test_importlib test_runpy test_trace`` to exclude those tests as
    they trigger exceptions during coverage; see
    `python/cpython#54750 <https://github.com/python/cpython/issues/54750>`__ and
    `python/cpython#55200 <https://github.com/python/cpython/issues/55200>`__.

Once the tests are done you will find the directory you specified contains
files for each executed module along with which lines were executed how many
times.


Filing the issue
================
Once you have increased coverage,
you need to create an issue on the `issue tracker`_ and
submit a :ref:`pull request <pullrequest>`.


Measuring coverage of C code with gcov and lcov
===============================================

It's also possible to measure the function, line and branch coverage of
Python's C code. Right now only GCC with `gcov`_ is supported. In order to
create an instrumented build of Python with gcov, run:

.. tab:: Unix/macOS

    .. code-block:: shell

        make coverage

.. tab:: Windows

    .. code-block:: dosbatch

        .\make coverage

Then run some code and gather coverage data with the ``gcov`` command. In
order to create a HTML report you can install `lcov`_. The command:

.. tab:: Unix/macOS

    .. code-block:: shell

        make coverage-lcov

.. tab:: Windows

    .. code-block:: dosbatch

        .\make coverage-lcov

assembles coverage data, removes 3rd party and system libraries and finally
creates a report. You can skip both steps and just run:

.. tab:: Unix/macOS

    .. code-block:: shell

        make coverage-report

.. tab:: Windows

    .. code-block:: dosbatch

        .\make coverage-report

if you like to generate a coverage report for Python's stdlib tests. It takes
about 20 to 30 minutes on a modern computer.

.. note::

    Multiple test jobs may not work properly. C coverage reporting has only
    been tested with a single test process.

.. _issue tracker: https://github.com/python/cpython/issues
.. _gcov: https://gcc.gnu.org/onlinedocs/gcc/Gcov.html
.. _lcov: https://github.com/linux-test-project/lcov
.. _coverage.py: https://coverage.readthedocs.io/en/latest/
