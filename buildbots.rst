.. _buildbots:

Continuous Integration
======================

To assert that there are no regressions in the :doc:`development and maintenance
branches <devcycle>`, Python has a set of dedicated machines (called *buildbots* or
*build slaves*) used for continuous integration.  They span a number of
hardware/operating system combinations.  Furthermore, each machine hosts
several *builders*, one per active branch: when a new change is pushed
to this branch on the public Mercurial repository, all corresponding builders
will schedule a new build to be run as soon as possible.

The build steps run by the buildbots are the following:

* Checkout of the source tree for the changeset which triggered the build
* Compiling Python
* Running the test suite using :ref:`strenuous settings <strenuous_testing>`
* Cleaning up the build tree

It is your responsibility, as a core developer, to check the automatic
build results after you push a change to the repository.  It is therefore
important that you get acquainted with the way these results are presented,
and how various kinds of failures can be explained and diagnosed.

Checking results of automatic builds
------------------------------------

There are two ways of visualizing recent build results:

* The Web interface for each branch at http://python.org/dev/buildbot/,
  where the so-called "waterfall" view presents a vertical rundown of recent
  builds for each builder.  When interested in one build, you'll have to
  click on it to know which changesets it corresponds to.

* The command-line ``bbreport.py`` client, which you can get from
  http://code.google.com/p/bbreport/. Installing it is trivial: just add
  the directory containing ``bbreport.py`` to your system path so that
  you can run it from any filesystem location.  For example, if you want
  to display the latest build results on the development ("default") branch,
  type::

      bbreport.py -q 3.x

Some buildbots are much faster than others.  Over time, you will learn which
ones produce the quickest results after a build, and which ones take the
longest time.

Also, when several changesets are pushed in a quick succession in the same
branch, it often happens that a single build is scheduled for all these
changesets.

Stability
---------

A subset of the buildbots are marked "stable".  They are taken into account
when making a new release.  The rule is that all stable builders must be free of
persistent failures when the release is cut.  It is absolutely **vital**
that core developers fix any issue they introduce on the stable buildbots,
as soon as possible.

This does not mean that other builders' test results can be taken lightly,
either.  Some of them are known for having platform-specific issues that
prevent some tests from succeeding (or even terminating at all), but
introducing additional failures should generally not be an option.

Flags-dependent failures
------------------------

Sometimes, while you have run the :doc:`whole test suite <runtests>` before
committing, you may witness unexpected failures on the buildbots.  One source
of such discrepancies is if different flags have been passed to the test runner
or to Python itself.  To reproduce, make sure you use the same flags as the
buildbots: they can be found out simply by clicking the **stdio** link for
the failing build's tests.  For example::

   ./python.exe -Wd -E -bb  ./Lib/test/regrtest.py -uall -rwW

.. note::
   Running ``Lib/test/regrtest.py`` is exactly equivalent to running
   ``-m test``.

Ordering-dependent failures
---------------------------

Sometimes even the failure is subtler, as it relies on the order in which
the tests are run.  The buildbots *randomize* test order (by using the ``-r``
option to the test runner) to maximize the probability that potential
interferences between library modules are exercised; the downside is that it
can make for seemingly sporadic failures.

The ``--randseed`` option makes it easy to reproduce the exact randomization
used in a given build.  Again, open the ``stdio`` link for the failing test
run, and check the beginning of the test output proper.

Let's assume, for the sake of example, that the output starts with::

   ./python -Wd -E -bb Lib/test/regrtest.py -uall -rwW
   == CPython 3.3a0 (default:22ae2b002865, Mar 30 2011, 13:58:40) [GCC 4.4.5]
   ==   Linux-2.6.36-gentoo-r5-x86_64-AMD_Athlon-tm-_64_X2_Dual_Core_Processor_4400+-with-gentoo-1.12.14 little-endian
   ==   /home/buildbot/buildarea/3.x.ochtman-gentoo-amd64/build/build/test_python_29628
   Testing with flags: sys.flags(debug=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=0, no_user_site=0, no_site=0, ignore_environment=1, verbose=0, bytes_warning=2, quiet=0)
   Using random seed 2613169
   [  1/353] test_augassign
   [  2/353] test_functools

You can reproduce the exact same order using::

   ./python -Wd -E -bb -m test -uall -rwW --randseed 2613169

It will run the following sequence (trimmed for brevity)::

   [  1/353] test_augassign
   [  2/353] test_functools
   [  3/353] test_bool
   [  4/353] test_contains
   [  5/353] test_compileall
   [  6/353] test_unicode

If this is enough to reproduce the failure on your setup, you can then
bisect the test sequence to look for the specific interference causing the
failure.  Copy and paste the test sequence in a text file, then use the
``--fromfile`` (or ``-f``) option of the test runner to run the exact
sequence recorded in that text file::

   ./python -Wd -E -bb -m test -uall -rwW --fromfile mytestsequence.txt

In the example sequence above, if ``test_unicode`` had failed, you would
first test the following sequence::

   [  1/353] test_augassign
   [  2/353] test_functools
   [  3/353] test_bool
   [  6/353] test_unicode

And, if it succeeds, the following one instead (which, hopefully, shall
fail)::

   [  4/353] test_contains
   [  5/353] test_compileall
   [  6/353] test_unicode

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
------------------

While we try to make the test suite as reliable as possible, some tests do
not reach a perfect level of reproducibility.  Some of them will sometimes
display spurious failures, depending on various conditions.  Here are common
offenders:

* Network-related tests, such as ``test_poplib``, ``test_urllibnet``, etc.
  Their failures can stem from adverse network conditions, or imperfect
  thread synchronization in the test code, which often has to run a
  server in a separate thread.

* Tests dealing with delicate issues such as inter-thread or inter-process
  synchronization, or Unix signals: ``test_multiprocessing``,
  ``test_threading``, ``test_subprocess``, ``test_threadsignals``.

When you think a failure might be transient, it is recommended you confirm by
waiting for the next build.  Still, even if the failure does turn out sporadic
and unpredictable, the issue should be reported on the bug tracker; even
better if it can be diagnosed and suppressed by fixing the test's implementation,
or by making its parameters - such as a timeout - more robust.


Custom builders
---------------

When working on a long-lived feature branch, or on a bugfix branch which
enables issue-specific debugging, you will probably want to test your
work on one or several buildbots.  Since your work is hosted in a distinct
repository, you can't trigger builds on the regular builders.  Instead,
you have to use one of the `custom builders
<http://www.python.org/dev/buildbot/all/waterfall?category=custom.stable&category=custom.unstable>`_.

When creating ("forcing") a build on a custom builder, you have to provide
at least two parameters:

* The repository path, relative to http://hg.python.org. For example,
  ``sandbox/myfixes`` if ``http://hg.python.org/sandbox/myfixes`` is the
  full path to the repository.

* The Mercurial id of the changeset you want to build.  To make things less
  tedious, we suggest you do your changes in a separate named branch: you can
  then supply the branch name instead of a specific changeset id.

If you are interested in the results of a specific test file only, we
recommend you change (temporarily, of course) the contents of the
``buildbottest`` clause in ``Makefile.pre.in``; or, for Windows builders,
the ``Tools/buildbot/test.bat`` and ``Tools/buildbot/test-amd64.bat``
scripts.

.. note::
   For security reasons, it is impossible to build repositories from outside
   the http://hg.python.org realm.
