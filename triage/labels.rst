.. _labels:
.. _gh-labels:

=============
GitHub labels
=============

Triagers, core developers and bots can add labels on GitHub
to categorize issues and pull requests.
Many labels are shared for both use cases, while some are dedicated
only to one. Below is a possibly inexhaustive list, but it should get
you going. For a full list, see `here <https://github.com/python/cpython/issues/labels>`_.


.. _general-purpose-labels:
.. _Type:
.. _labels-type:

Type labels
===========

These labels are used to specify the type of issue:

* :gh-label:`type-bug`: for unexpected behaviors, bugs, or exceptions
  (not hard crashes).
* :gh-label:`type-crash`: for hard crashes of the interpreter, possibly with a
  core dump.
* :gh-label:`type-feature`: for feature requests or enhancements.
  Feature requests do not need :ref:`version labels <Version labels>`;
  it is implicit that features are added to the ``main`` branch only.
  The `Ideas Discourse category`_ can be used to discuss enhancements
  before filing an issue.
* :gh-label:`type-security`: for security issues.
  See also `Reporting security issues in Python`_.


.. _Component:
.. _labels-component:

Component labels
================

These labels are mostly used to specify which :ref:`part of the codebase
<build-directory-structure>` is affected by the issue/PR:

* :gh-label:`stdlib`: for standard library modules in the :cpy-file:`Lib`
  directory (written in Python).
* :gh-label:`extension-modules`: for standard library modules in the
  :cpy-file:`Modules` directory (written in C).
* :gh-label:`interpreter-core`: for changes related to the interpreter core in
  the :cpy-file:`Objects`, :cpy-file:`Python`, :cpy-file:`Grammar`,
  and :cpy-file:`Parser` dirs (written mostly in C).
* :gh-label:`docs`: for documentation in the :cpy-file:`Doc` directory
  (written in :ref:`reStructuredText <markup>`), docstrings, and code comments.
* :gh-label:`tests`: for tests in the :cpy-file:`Lib/test` directory
  (written in Python) and other changes related to tests, :mod:`unittest`,
  or :mod:`doctest`.

OS labels
=========

These labels are used to specify which operating systems are affected.
Since most issues either affect all systems or are specific to Unix,
the only available labels are :gh-label:`OS-windows`, :gh-label:`OS-mac`,
and :gh-label:`OS-freebsd`.


.. _Expert labels:
.. _Topic labels:

Topic labels
============

These labels are used to denote the specific topic area, if any, of
the issue/PR.  This includes both specific modules/packages and generic
interest areas.

Adding these labels is also a way to notify the relevant experts, since
they are encouraged to subscribe to them.  Depending on the label,
this might also automatically add the issue to a GitHub project.

You can see the `full list of topic labels on GitHub
<https://github.com/python/cpython/labels?q=topic>`_.


.. _Version labels:

Version labels
==============

These labels are used to indicate which versions of Python are affected.
The available version labels (with the form :samp:`3.{N}`) are updated
whenever new major releases are created or retired.

See also :ref:`the branch status page <branchstatus>`
for a list of active branches.


.. _Keywords:
.. _Other:
.. _Priority:
.. _labels-other:

Other labels
============

* :gh-label:`triaged`: for issue has been accepted as valid by a triager.
* :gh-label:`easy`: for issues that are considered easy.
* :gh-label:`build`/:gh-label:`performance`: for issues related
  to the build process or performance, respectively.
* :gh-label:`release-blocker`/:gh-label:`deferred-blocker`: for issues/PRs
  that, unless fixed, will hold the current or next release respectively.
  Triagers may set these labels for issues that must be fixed before a release,
  and the :ref:`branch's release manager <branchstatus>`
  will review them and determine if they indeed qualify,
  removing or retaining the label as appropriate.
* :gh-label:`pending`: for issues/PRs that will be closed unless further
  feedback is provided.
* :gh-label:`stale`: for issues/PRs that have been inactive for a while.
* :gh-label:`sprint`: for easier filtering of issues/PRs being worked on
  during official sprints.


.. _GitHub Labels for PRs:
.. _github-pr-labels:

Labels specific to PRs
======================

The following labels only apply to :ref:`Pull Requests <pullrequest>`.
They are either set automatically by bots, or added by humans
to trigger specific bot behaviors.

* :gh-label:`DO-NOT-MERGE`: for PRs that shouldn't be merged in their current
  state.  It also prevents `miss-islington`_ from being able to automatically
  merge the PR.
* :samp:`needs backport to {X.Y}`: used to indicate which branches the PR
  should be backported to.  Once the PR is merged, ``miss-islington`` will
  automatically attempt to create backport PRs for the versions indicated
  by these labels.
  See also :ref:`the status of the Python branches <branchstatus>` for a list
  of branches and the type of PRs that can be backported to them.
* :gh-label:`skip issue`: for trivial changes (such as typo fixes, comment
  changes, and section rephrases) that don't require a corresponding issue.
* :gh-label:`skip news`: for PRs that don't need a NEWS entry.
  The :ref:`news-entry` section covers in details in which cases the NEWS entry
  can be skipped.
* :gh-label:`test-with-buildbots`: used to test the latest commit with
  the :ref:`buildbot fleet <buildbots>` whenever more testing is required
  before merging.  This may take multiple hours to complete.
* :samp:`awaiting {action}`: these labels are applied and used by `bedevere`_
  to indicate the stage of a PR and should not be applied manually.


.. _Reporting security issues in Python: https://www.python.org/dev/security/
.. _Ideas Discourse category: https://discuss.python.org/c/ideas/6
.. _miss-islington: https://github.com/python/miss-islington
.. _bedevere: https://github.com/python/bedevere/#pr-state-machine
