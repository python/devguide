.. _labels:
.. _gh-labels:

=============
GitHub Labels
=============

We're using labels on GitHub to categorize issues and pull requests.
Many labels are shared for both use cases, while some are dedicated
only to one. Below is a possibly inexhaustive list, but it should get
you going. For a full list, see `here <https://github.com/python/cpython/issues/labels>`_.


Type labels
===========

These labels are used to specify the type of issue:

* ``type-bug``: for unexpected behaviors, bugs, or errors (not hard crashes).
* ``type-crash``: for hard crashes of the interpreter, possibly with a
  core dump.
* ``type-feature``: for feature requests or enhancements.
* ``type-security``: for security issues.

Since most PRs have an associated issue, it is not necessary to apply these
labels to PRs


Component labels
================

These labels are mostly used to specify which :ref:`part of the codebase
<directory-structure>` is affected by the issue/PR:


* ``stdlib``: for standard library modules in the :file:`Lib` directory
  (written in Python).
* ``extension-modules``: for standard library modules in the :file:`Modules`
  directory (written in C).
* ``interpreter-core``: for changes related to the interpreter core in the
  :file:`Objects`, :file:`Python`, :file:`Grammar`, and :file:`Parser` dirs
  (written mostly in C).
* ``docs``: for documentation in the :file:`Doc` directory (written in
  reStructuredText), docstrings, and code comments.
* ``tests``: for tests in the :file:`Lib/test` directory (written in Python)
  and changes other related to tests, ``unittest``, or ``doctests``.


Expert labels
=============

These labels are used to specify the area of expertise required to address
the issue/PR.  This includes both specific modules/packages and generic
interest areas.

Adding these labels is also a way to notify the relevant experts, since
they are encouraged to subscribe to these labels.  Depending on the label,
this might also automatically add the issue to a GitHub project.

You can see the `full list of expert labels on GitHub
<https://github.com/python/cpython/labels?q=expert>`_.


OS labels
=========

These labels are used to specify which operating systems are affected.
Since most issues either affect all systems or are specific to Unix,
the only available labels are ``OS-windows``, ``OS-mac``, and ``OS-freebsd``.


Version labels
==============

These labels are used to indicate which versions of Python are affected.
The available version labels (with the form :samp:`3.{x}`) are updated
whenever new major releases are created or retired.


Other labels
============

* ``triaged``: for issue has been accepted as valid by a triager.
* ``easy``: for issues that are considered easy.
* ``build``/``performance``: for issues related respectively to the
  build process and performances.
* ``release-blocker``/``deferred-blocker``: for issues/PRs that, unless
  fixed, will hold the current or next release respectively.
* ``pending``: for issues/PRs that will be closed unless further feedback
  is provided.
* ``stale``: for issues/PRs that have been inactive for a while.
* ``sprint``: used for easier filtering of issues/PRs being worked on during
  official sprints.


Labels specific to PRs
======================

The following labels only apply to PRs.  They are either set automatically
by bots, or applied by humans to trigger specific bot behaviors.

* ``DO-NOT-MERGE``: for PRs that shouldn't be merged in their current state.
  It also prevents ``miss-islington`` from being able to automatically merge
  the PR.
* :samp:`needs backport to {X.Y}`: used to indicate which branches the PR should be
  backported to.  Once the PR is merged, ``miss-islington`` will automatically
  attempt to create backport PRs for the versions indicated by these labels.
  See also :ref:`the status of the Python branches <branchstatus>` for a list
  of branches and the type of PRs that can be backported to them.
* ``skip issue``: for trivial changes (such as typo fixes, comment changes,
  and section rephrases) that don't require a corresponding issue.
* ``skip news``: for PRs that don't need a NEWS entry.  The :ref:`news-entry`
  section covers in details in which cases the NEWS entry can be skipped.
* :samp:`awaiting *`: these labels are applied and used by ``bedevere`` to
  indicate the stage of a PR:

  * ``awaiting review``: the PR hasn't been reviewed and is waiting for a
    review.
  * ``awaiting core review``: a review by a core developer is needed.
  * ``awaiting changes``: a reviewer requested changes to proceed with the PR.
  * ``awaiting change review``: a review of the requested changes is needed.
  * ``awaiting merge``: the PR has been approved by a core developer and is
    ready to merge.

* ``test-with-buildbots``: used to test the latest commit with the buildbot
  fleet whenever more testing is required before merging.  This may take
  multiple hours to complete. Triagers can also stop a stuck build using
  the web interface.

.. TODO: delete most of what follows, since it seems specific for bpo.
   Some things are still relevant, and should be moved elsewhere.

Title
-----
A brief description of the issue. Review whether the title is too generic or
specifies an incorrect term or library.

(Optional) Add a prefix at the start of the title to indicate the module, e.g.
IDLE, doc, or asyncio.

Type
----
Describes the type of issue.  If an issue does not fit within any
specific type, please do not set a type.

+----------------+----------------------------------------------------------+
|      Type      |                       Description                        |
+================+==========================================================+
| behavior       | Unexpected behavior, result, or exception.  Most bugs    |
|                | will have this type. This group also includes compile    |
|                | errors, and crashers.                                    |
+----------------+----------------------------------------------------------+
| enhancement    | Issues that propose the addition of new functionality,   |
|                | such as new functions, classes, modules, or even new     |
|                | arguments for existing functions. Also used for          |
|                | improvements in the documentation, test suite and        |
|                | other refactorings. A good place to discuss enhancements |
|                | prior to filing an issue is `python-ideas`_ mailing      |
|                | list.                                                    |
+----------------+----------------------------------------------------------+
| performance    | Situations where too much time is necessary to complete  |
|                | the task. For example, a common task now takes           |
|                | significantly longer to complete. This group also        |
|                | includes resource usage (e.g. too much memory needed)    |
|                | issues.                                                  |
+----------------+----------------------------------------------------------+
| security       | Issues that might have security implications. Report     |
|                | security vulnerabilities using the procedure found in    |
|                | the `Reporting security issues in Python`_ page on the   |
|                | python.org website.                                      |
+----------------+----------------------------------------------------------+

Stage
-----
A needed next action to advance the issue.  The *stage* on GitHub issues is
determined by presence of a linked PR and whether the issue is still open
or closed. It is the PR that holds code review-related labels.

Components
----------
The area or Python library affected by the issue. A single issue can apply
multiple component labels.

One or more components may be selected for an issue:

+-------------------+------------------------------------------------------+
|     Component     |                     Description                      |
+===================+======================================================+
| Documentation     | The documentation in Doc_ (source used to build HTML |
|                   | docs for https://docs.python.org/).                  |
+-------------------+------------------------------------------------------+
| Extension Modules | C modules in Modules_.                               |
+-------------------+------------------------------------------------------+
| Interpreter Core  | The interpreter core.                                |
|                   | The built-in objects in `Objects`_, the `Python`_,   |
|                   | `Grammar`_ and `Parser`_ dirs.                       |
+-------------------+------------------------------------------------------+
| Library (Lib)     | Python modules in Lib_.                              |
+-------------------+------------------------------------------------------+
| Tests             | The unittest framework in `Lib/unittest`_            |
|                   | The doctest framework `Lib/doctest.py`_.             |
|                   | The CPython tests in `Lib/test`_.                    |
|                   | The test runner in `Lib/test/regrtest.py`_.          |
|                   | The test support utilities in `Lib/test/support`_.   |
+-------------------+------------------------------------------------------+

Versions
--------
The known versions of Python that the issue affects and should be fixed for.

Thus if an issue for a new feature is assigned for e.g., Python 3.8 but is not
applied before Python 3.8.0 is released, this label should be updated to say
``python-3.9`` as the version and drop ``python-3.8``.

Priority
--------
What is the severity and urgency?

+------------------+--------------------------------------------------------+
| Priority         | Description                                            |
+==================+========================================================+
| normal           | The default value for most issues filed.               |
+------------------+--------------------------------------------------------+
| deferred blocker | The issue will not hold up the next release, *n*. It   |
|                  | will be promoted to a *release blocker* for the        |
|                  | following release, *n+1*.                              |
+------------------+--------------------------------------------------------+
| release blocker  | The issue **must** be fixed before *any* release is    |
|                  | made, e.g., will block the next release even if it is  |
|                  | an alpha release.                                      |
+------------------+--------------------------------------------------------+

As a guideline, whether a bug is a *release blocker* for the current
:ref:`release schedule <branchstatus>` is decided by the release manager.
Triagers may recommend this priority and should notify the release manager by
tagging them in a comment using ``@username``. If needed, consult the
:ref:`release schedule <branchstatus>` and the release's associated PEP for the
release manager's name.

Keywords
--------
Various informational flags about the issue. Multiple values are possible.

+---------------+------------------------------------------------------------+
|    Keyword    |                        Description                         |
+===============+============================================================+
| easy          | Fixing the issue should not take longer than a day for     |
|               | someone new to contributing to Python to solve.            |
+---------------+------------------------------------------------------------+

Nosy List
---------
A list of people who may be interested in an issue.

This used to be a feature of the old issue tracker. On GitHub issues the
same effect is achieved by tagging people in a comment using ``@username``.

It is acceptable to tag someone to if you think the issue should be brought to
their attention. Use the :ref:`experts` to know who wants to be added to the
nosy list for issues targeting specific areas.

If you want to subscribe yourself to an issue, click the *🔔 Subscribe*
button in the sidebar. Similarly, if you were tagged by somebody else but
decided this issue is not for you, you might click the *🔕 Unsubscribe*
button in the sidebar.

Assignees
---------
Who is expected to take the next step in resolving the issue.

It is acceptable to assign an issue to someone if the issue cannot move
forward without their help, e.g., they need to make a technical decision to
allow the issue to move forward. Also consult the :ref:`experts` as certain
stdlib modules should always be assigned to a specific person.

Note that in order to assign an issue to someone, that person **must** be
a team member, likely a Triager or a core developer.

Dependencies
------------
The issue requires the listed issue(s) to be resolved first before it can move
forward. This is achieved using checkbox lists in the initial issue description
comment. Long story short, if you add this::

    - [x] #739
    - [ ] https://github.com/octo-org/octo-repo/issues/740
    - [ ] Add delight to the experience when all tasks are complete :tada:

then those will become sub-tasks on the given issue. Moreover, GitHub will
automatically mark a task as complete if the other referenced issue is
closed.

More details in the `official GitHub documentation
<https://docs.github.com/en/issues/tracking-your-work-with-issues/about-task-lists>`_.

Superseder
----------
The issue is a duplicate of the listed issue(s). To make GitHub mark
an issue as duplicate, write "Duplicate of #xxxx" in a comment.

Status
------

+---------------+------------------------------------------------------------+
|    Status     |                        Description                         |
+===============+============================================================+
| open          | Issue is not resolved.                                     |
+---------------+------------------------------------------------------------+
| closed        | The issue has been resolved (somehow).                     |
+---------------+------------------------------------------------------------+

Linked pull requests
--------------------
A link might be added manually using the cog icon next to this field.
Most commonly though, if the PR includes "Fixes #xxx" in its description,
the link will be added automatically.

Generating Special Links in a Comment
=====================================
Using the following abbreviations in a comment will automatically generate
a link to relevant web pages.

+-------------------------------------------------------------+-------------------------------------------------------+
| Comment abbreviation                                        | Description                                           |
+=============================================================+=======================================================+
| ``#<number>``,                                              | Links to the tracker issue or PR ``<number>`` (they   |
| ``GH-<number>``                                             | share the same sequence of integers on GitHub).       |
+-------------------------------------------------------------+-------------------------------------------------------+
| ``BPO-<number>``                                            | Links to the old bug tracker at bugs.python.org.      |
+-------------------------------------------------------------+-------------------------------------------------------+
| a 10-, 11-, 12-, or 40-digit hex ``<number>``               | Indicates a Git changeset identifier and              |
|                                                             | generates a link to changeset ``<number>`` on GitHub. |
+-------------------------------------------------------------+-------------------------------------------------------+

.. _Doc: https://github.com/python/cpython/tree/main/Doc/
.. _Grammar: https://github.com/python/cpython/tree/main/Grammar/
.. _Lib: https://github.com/python/cpython/tree/main/Lib/
.. _Lib/doctest.py: https://github.com/python/cpython/blob/main/Lib/doctest.py
.. _Lib/test: https://github.com/python/cpython/tree/main/Lib/test/
.. _Lib/test/regrtest.py: https://github.com/python/cpython/blob/main/Lib/test/regrtest.py
.. _Lib/test/support: https://github.com/python/cpython/tree/main/Lib/test/support/
.. _Lib/unittest: https://github.com/python/cpython/tree/main/Lib/unittest/
.. _Modules: https://github.com/python/cpython/tree/main/Modules/
.. _Objects: https://github.com/python/cpython/tree/main/Objects/
.. _Parser: https://github.com/python/cpython/tree/main/Parser/
.. _Python: https://github.com/python/cpython/tree/main/Python/
.. _Reporting security issues in Python: https://www.python.org/dev/security/
.. _python-ideas: https://mail.python.org/mailman3/lists/python-ideas.python.org
