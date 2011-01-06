.. _coverage:

Increase Test Coverage
======================

Python development follows a practice that all semantics changes and additions
to the language and :abbr:`stdlib (standard library)` are accompanied by
appropriate unit tests. Unfortunately Python was in existence for a long time
before the practice came into effect. This has left chunks of the stdlib
untested which is not a desirable situation to be in.

A good, easy way to become acquianted with Python's code and to help out is to
help increase the test coverage for Python's stdlib. Ideally we would like to
have 100% coverage, but any increase is a good one. Do realize, though, that
getting 100% coverage is not always possible. There could be platform-specific
code that simply will not execute for you, errors in the output, etc. You can
use your judgement as to what should and should not be covered, but being
conservative and assuming something should be covered is generally a good rule
to follow.

Choosing what module you want to increase test coverage can be done in a couple
of ways. A third-party website at http://coverage.livinglogic.de/ provides an
overall view of how good coverage is for various modules (you will want to
focus on those in the ``Lib`` directory as those are the pure Python modules
from Python's stdlib, and thus easier to work with than the C extension
modules). Another is to follow the examples below and simply see what kind of
coverage your favorite module has. This is "stabbing in the dark", though, and
so it might take some time to find a module that needs coverage help. Finally,
you can simply run the test suite yourself with coverage turned on and see what
modules need help. This has the drawback as the test suite takes some time to
complete when run under coverage measuring.


Using coverage.py
-----------------

One of the most popular third-party coverage tools is `coverage.py`_ which
provides very nice HTML output along with advanced features such as
:ref:`branch coverage <branch_coverage>`. If you prefer to stay with tools only
provided by the stdlib then that is possible to :ref:`using test.regrtest
<coverage_by_regrtest>`.

Because the in-development version of Python is bleeding-edge, it is possible
that the latest release version of coverage.py will not work. In that case you
should try using the in-development of coverage.py to see if it has been
updated as needed. To do this you should check out the development version of
coverage.py into your checkout of Python and make a symlink (or simply copy if
you prefer) the ``coverage`` subdirectory::

    hg clone https://bitbucket.org/ned/coveragepy
    ln -s coveragepy/coverage

Otherwise you can use the latest release of coverage.py. One option is to
download the source distribution of coverage.py and copy the ``coverage``
directory into your Python checkout. The other option is to use your checkout
copy of Python to install coverage.py (but use the ``--user`` flag to
Distutils!).

Regardless of how you installed coverage.py, the following should work::

    ./python -m coverage

Coverage.py will print out a little bit of helper text verifying that
everything is working.

To run the test suite under coverage.py, do the following::

    ./python -m coverage run --pylib Lib/test/regrtest.py

If you want to run only a single test, specify the module/package being tested
in the ``--source`` flag (so as to prune the coverage reporting to only the
module/package you are interested in) and then append the name of the test you
wish to run to the command::

    ./python -m coverage run --pylib --source=abc Lib/test/regrtest.py test_abc

To see the results of the coverage run, you can view a text-based report with::

    ./python -m coverage report

You can use the ``--show-missing`` flag to get a list of lines that were not
executed::

    ./python -m coverage report --show-missing

But one of the strengths of coverage.py is its HTML-based reports which lets
you visually see what lines of code were not tested::

    ./python -m coverage -d .coverage_html html

You can then open the ``.coverage_html/index.html`` file in a web browser to
view the coverage results in a nicely formatted page.


.. _branch_coverage:

Branch Coverage
'''''''''''''''

For the truly daring, you can use another powerful feature of coverage.py:
branch coverage. Testing every possible branch path through code, while a great
goal to strive for, is not as important of a goal as it is to get 100% line
coverage for the entire stdlib (for now).

If you decide to want to try to improve branch coverage, simply add the
``--branch`` flag to your coverage run::

    ./python -m coverage run --pylib --branch

This will lead to the report stating not only what lines were not covered, but
also what branch paths were not executed.


.. _coverage.py: http://nedbatchelder.com/code/coverage/


.. _coverage_by_regrtest:

Using test.regrtest
-------------------

XXX

