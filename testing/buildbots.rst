.. _buildbots:

======================
Working with buildbots
======================

.. highlight:: bash

To assert that there are no regressions in the :ref:`development and maintenance
branches <devcycle>`, Python has a set of dedicated machines (called *buildbots*
or *build workers*) used for continuous integration.  They span a number of
hardware/operating system combinations.  Furthermore, each machine hosts
several *builders*, one per active branch: when a new change is pushed
to this branch on the public `GitHub repository <https://github.com/python/cpython>`__,
all corresponding builders will schedule a new build to be run as soon as possible.

The build steps run by the buildbots are the following:

* Check out the source tree for the change which triggered the build
* Compile Python
* Run the test suite using :ref:`strenuous settings <strenuous_testing>`
* Clean up the build tree

It is the responsibility of core team members to check the automatic
build results after they push a change to the repository.  It is therefore
important that they are acquainted with the way these results are presented,
and how various kinds of failures can be explained and diagnosed.


In case of trouble
==================

Please read this page in full. If your questions aren't answered here and you
need assistance with the buildbots, a good way to get help is to either:

* contact the ``python-buildbots@python.org`` mailing list where all buildbot
  worker owners are subscribed; or
* contact the release manager of the branch you have issues with.


Buildbot failures on pull requests
==================================

The ``bedevere-bot`` on GitHub will put a message on your merged Pull Request
if building your commit on a stable buildbot worker fails. Take care to
evaluate the failure, even if it looks unrelated at first glance.

Not all failures will generate a notification since not all builds are executed
after each commit. In particular, reference leaks builds take several hours to
complete so they are done periodically. This is why it's important for you to
be able to check the results yourself, too.


Triggering on pull requests
===========================

To trigger buildbots on a pull request you need to be a CPython triager or a
core team member. If you are not, ask someone to trigger them on your behalf.

The simplest way to trigger most buildbots on your PR is with the
:gh-label:`🔨 test-with-buildbots` and :gh-label:`🔨 test-with-refleak-buildbots`
labels. (See :ref:`github-pr-labels`.)

These will run buildbots on the most recent commit. If you want to trigger the
buildbots again on a later commit, you'll have to remove the label and add it
again.

If you want to test a pull request against specific platforms, you can trigger
one or more build bots by posting a comment that begins with:

.. code-block:: none

   !buildbot regex-matching-target

For example to run both the iOS and Android build bot, you can use:

.. code-block:: none

   !buildbot ios|android

bedevere-bot will post a comment indicating which build bots, if
any, were matched. If none were matched, or you do not have the
necessary permissions to trigger a request, it will tell you that too.

The ``!buildbot`` comment will also only run buildbots on the most recent
commit. To trigger the buildbots again on a later commit, you will have to
repeat the comment.


Checking results of automatic builds
====================================

The Web interface at https://buildbot.python.org/#/ has several ways of
visualizing recent build results:

* A `Waterfall View <https://buildbot.python.org/#/waterfall>`_
  that presents a vertical rundown of recent builds for each builder.
  When interested in one build, you'll have to
  click on it to know which commits it corresponds to.

* A `Console View <https://buildbot.python.org/#/console>`_,
  which works best on a wide, high resolution
  monitor.  Clicking on the colored circles will allow you to open a new page
  containing whatever information about that particular build is of interest to
  you.  You can also access builder information by clicking on the builder
  status bubbles in the top line.

* A `Release Status Dashboard <https://buildbot.python.org/#/release_status>`_
  that shows the status of stable buildbots for each active branch,
  summarizing whether the builds are ready for release.

Note that the buildbot web pages are often slow to load, be patient.

Some buildbots are much faster than others.  Over time, you will learn which
ones produce the quickest results after a build, and which ones take the
longest time.

Also, when several commits are pushed in a quick succession in the same
branch, it often happens that a single build is scheduled for all these
commits.


Stability
=========

A subset of the buildbots are marked as
`"stable" <https://buildbot.python.org/#/builders?tags=%2Bstable>`_.
They are taken into account when making a new release.
The rule is that all stable builders must be free of
persistent failures when the release is cut.  It is absolutely **vital**
that core team members fix or revert any issue they introduce on the stable
buildbots, as soon as possible.

This does not mean that other builders' test results can be taken lightly,
either.  Some of them are known for having platform-specific issues that
prevent some tests from succeeding (or even terminating at all), but
introducing additional failures should generally not be an option.


Flags-dependent failures
========================

Sometimes, while you have run the :ref:`whole test suite <runtests>` before
committing, you may witness unexpected failures on the buildbots.  One source
of such discrepancies is if different flags have been passed to the test runner
or to Python itself.  To reproduce, make sure you use the same flags as the
buildbots: they can be found out simply by clicking the **stdio** link for
the failing build's tests.  For example::

   ./python.exe -W error -E -bb  ./Lib/test/regrtest.py -uall -rwW

.. note::
   Running ``Lib/test/regrtest.py`` is exactly equivalent to running
   ``-m test``.


Ordering-dependent failures
===========================

Sometimes the failure is even subtler, as it relies on the order in which
the tests are run.  The buildbots *randomize* test order (by using the ``-r``
option to the test runner) to maximize the probability that potential
interferences between library modules are exercised; the downside is that it
can make for seemingly sporadic failures.

The ``--randseed`` option makes it easy to reproduce the exact randomization
used in a given build.  Again, open the ``stdio`` link for the failing test
run, and check the beginning of the test output proper.

Let's assume, for the sake of example, that the output starts with:

.. code-block:: none
   :emphasize-lines: 9

   ./python -u -W error -bb -E -m test --slow-ci --timeout=2400 -j2 -u-cpu,-urlfetch,-network --junit-xml test-results.xml -j4 --dont-add-python-opts
   == CPython 3.15.0a6+ (heads/main:d625f7da33b, Feb 13 2026, 17:27:29) [GCC 12.2.0]
   == Linux-6.12.20+rpt-rpi-v8-aarch64-with-glibc2.36 little-endian
   == Python build: release
   == cwd: /home/stan/buildarea/3.x.stan-raspbian.nondebug/build/build/test_python_worker_181905Ã¦
   == CPU count: 4
   == encodings: locale=ISO-8859-1 FS=utf-8
   == resources: all,-cpu,-network,-urlfetch
   Using random seed: 1000348774
   0:00:00 load avg: 3.34 Run 500 tests in parallel using 4 worker processes (timeout: 40 min, worker timeout: 45 min)
   0:00:01 load avg: 3.34 [  1/500] test_colorsys passed
   0:00:01 load avg: 3.34 [  2/500] test_float passed

You can reproduce the exact same order using::

   ./python -W error -E -bb -m test -uall -rwW --randseed 1000348774

It will run the following sequence (trimmed for brevity):

.. code-block:: none

   [  1/500] test_colorsys
   [  2/500] test_float
   [  3/500] test.test_io.test_memoryio
   [  4/500] test_profile
   [  5/500] test_picklebuffer
   [  6/500] test_zipimport
   [  7/500] test_devpoll
   ...

If this is enough to reproduce the failure on your setup, you can then
bisect the test sequence to look for the specific interference causing the
failure.  Copy and paste the test sequence in a text file, then use the
``--fromfile`` (or ``-f``) option of the test runner to run the exact
sequence recorded in that text file::

   ./python -W error -E -bb -m test -uall -rwW --fromfile mytestsequence.txt

In the example sequence above, if ``test_zipimport`` had failed, you would
first test the following sequence:

.. code-block:: none

   [  1/500] test_colorsys
   [  2/500] test_float
   [  3/500] test.test_io.test_memoryio
   [  6/500] test_zipimport

And, if it succeeds, the following one instead (which, hopefully, shall
fail):

.. code-block:: none

   [  4/500] test_profile
   [  5/500] test_picklebuffer
   [  6/500] test_zipimport

Then, recursively, narrow down the search until you get a single pair of
tests which triggers the failure.  It is very rare that such an interference
involves more than **two** tests.  If this is the case, we can only wish you
good luck!

.. note::
   You cannot use the ``-j`` option (for parallel testing) when diagnosing
   ordering-dependent failures.  Using ``-j`` isolates each test in a
   pristine subprocess and, therefore, prevents you from reproducing any
   interference between tests.


Transient failures
==================

While we try to make the test suite as reliable as possible, some tests do
not reach a perfect level of reproducibility.  Some of them will sometimes
display spurious failures, depending on various conditions.  Here are common
offenders:

* Network-related tests, such as ``test_poplib``, ``test_urllibnet``, and so on.
  Their failures can stem from adverse network conditions, or imperfect
  thread synchronization in the test code, which often has to run a
  server in a separate thread.

* Tests dealing with delicate issues such as inter-thread or inter-process
  synchronization, or Unix signals: ``test_multiprocessing``,
  ``test_threading``, ``test_subprocess``, ``test_threadsignals``.

When you think a failure might be transient, it is recommended you confirm by
waiting for the next build.  Still, even if the failure does turn out sporadic
and unpredictable, the issue should be reported on the bug tracker; even
better if it can be diagnosed and suppressed by fixing the test's
implementation, or by making its parameters - such as a timeout - more robust.

.. seealso::
   :ref:`buildworker`
