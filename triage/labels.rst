.. _gh-labels:

GitHub Labels
=============

We're using labels on GitHub to categorize issues and pull requests.
Many labels are shared for both use cases, while some are dedicated
only to one. Below is a possibly inexhaustive list, but it should get
you going. For a full list, see `here <https://github.com/python/cpython/issues/labels>`_.

General purpose labels
----------------------

type-behavior
    Used for issues/PRs that address unintentional behavior, but do not
    pose significant security concerns. Generally, bugfixes will be attached
    to a specific issue where the unintended behavior was first reported.

type-documentation
    Used for issues/PRs that exclusively involve changes to
    the documentation. Documentation includes ``*.rst`` files, docstrings,
    and code comments.

type-enhancement
    Used for issues/PRs that provide additional functionality
    or capabilities beyond the existing specifications.

type-performance
    Used for issues/PRs that provide performance optimizations.

type-security
    Used for issues/PRs that involve critical security issues. Less severe
    security concerns can instead use the type-bugfix label.

type-tests
    Used for issues/PRs that exclusively involve changes to the tests.

OS-Mac / OS-Windows
    Used for issues/PRs involving changes which only have an effect upon
    a specific operating system.

spam
    Used for issues/PRs that don't include enough eggs or bacon.

Labels specific to issues
-------------------------

Priority
^^^^^^^^

release-blocker
    The highest priority of an issue. If unaddressed, will cause the
    release manager to hold releasing a new version of Python.

deferred-blocker
    A release blocker that was pushed one or more releases into the
    future. Possibly a temporary workaround was employed, or the version
    of Python the issue is affecting is still in alpha or beta stages
    of development.

Component
^^^^^^^^^

library
    Used for issues involving Python modules in the ``Lib/`` dir.

docs
    Used for issues involving documentation in the ``Doc/`` dir.

interpreter-core
    Used for issues in interpreter core (``Objects/``, ``Python/``,
    ``Grammar/``, and ``Parser/`` dirs).

extension-modules
    Used for issues involving C modules in the ``Modules/`` dir.

tests
    Used for issues involving only Python's regression test suite, i.e.
    files in the ``Lib/test/`` dir.

Other
^^^^^

new
    Denotes that the issue hasn't been looked at by triagers or core
    developers yet.

easy
    Denotes that the issue is a good candidate for a newcomer to address.


Labels specific to PRs
----------------------

DO-NOT-MERGE
    Used on PRs to prevent miss-islington from being able
    to automatically merge the pull request. This label is appropriate when a PR
    has a non-trivial conflict with the branch it is being merged into.

expert-asyncio
    Used for PRs which involve changes to the asyncio module
    or other asynchronous frameworks that utilize it.

invalid
    Used manually for PRs that do not meet basic requirements and
    automatically added by bedevere when PR authors attempt to merge maintenance
    branches into the main branch. During events such as the October
    Hacktoberfest, this label will prevent the PR from counting toward the
    author's contributions.

needs backport to X.Y
    Used for PRs which are appropriate to backport to
    branches prior to main. Generally, backports to the maintenance branches
    are primarily bugfixes and documentation clarifications. Backports to the
    security branches are strictly reserved for PRs involving security fixes, such as
    crashes, privilege escalation, and DoS. The use of this label will cause
    miss-islington to attempt to automatically merge the PR into the branches
    specified.

skip issue
    Used for PRs which involve trivial changes, such as typo fixes,
    comment changes, and section rephrases. The majority of PRs require
    an issue to be attached to, but if there are no code changes and the
    section being modified retains the same meaning, this label might be
    appropriate.

skip news
    Similar to the skip issue label, this label is used for PRs which
    involve trivial changes, backports, or already have a relevant news entry
    in another PR. Any potentially impactful changes should have a
    corresponding news entry, but for trivial changes it's commonly at the
    discretion of the PR author if they wish to opt-out of making one.

sprint
    Used for PRs authored during an in-person sprint, such as
    at PyCon, EuroPython, or other official Python events. The label is
    used to prioritize the review of those PRs during the sprint.

stale
    Used for PRs that include changes which are no longer relevant, or when the
    author hasn't responded to feedback in a long period of time, or when the
    reviewer is unresponsive. This label helps core developers quickly identify
    PRs that are candidates for closure or require a ping to the author or
    reviewer.

awaiting review
    Used for PRs that haven't been reviewed by anyone yet.

awaiting core review
    Used when the PR is authored by a core developer or when a non-core
    developer has reviewed the PR, even if they requested changes.
    Note that reviewers could have been added manually by a triager or core
    developer, or included automatically through use of the `CODEOWNERS
    <https://github.com/python/cpython/blob/main/.github/CODEOWNERS>`_
    file.

awaiting changes
    A reviewer required changes to proceed with the PR.

awaiting change review
    The PR author made requested changes, and they are waiting for review.

awaiting merge
    The PR has been approved by a core developer and is ready to merge.

test-with-buildbots
    Used on PRs to test the latest commit with the buildbot fleet. Generally for
    PRs with large code changes requiring more testing before merging. This
    may take multiple hours to complete. Triagers can also stop a stuck build
    using the web interface.


.. _github-pr-labels:

GitHub Labels for PRs
---------------------

An important component of triaging PRs for the CPython repo involves
appropriately categorizing them through the usage of labels. For this
purpose we're using :ref:`gh-labels`.

Applying labels for Issues
--------------------------

The major elements found in an issue report include:

* Classification (including *Title*) - Metadata that lets us categorize
  the issue. Apart from the *Title* field, we use some *type-*, *component-*, and
  *version-* specific labels.
* Process - These fields indicate the state of the issue and its progress
  toward resolution. The fields are *Status* (open/closed), *Assignees*,
  *Comment*, as well as *priority-* and *keyword-* specific labels.
* Messages
* History

Title
'''''
A brief description of the issue. Review whether the title is too generic or
specifies an incorrect term or library.

(Optional) Add a prefix at the start of the title to indicate the module, e.g.
IDLE, doc, or asyncio.

Type
''''
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
'''''
A needed next action to advance the issue.  The *stage* on GitHub issues is
determined by presence of a linked PR and whether the issue is still open
or closed. It is the PR that holds code review-related labels.

Components
''''''''''
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
''''''''
The known versions of Python that the issue affects and should be fixed for.

Thus if an issue for a new feature is assigned for e.g., Python 3.8 but is not
applied before Python 3.8.0 is released, this label should be updated to say
``python-3.9`` as the version and drop ``python-3.8``.

Priority
''''''''
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
''''''''
Various informational flags about the issue. Multiple values are possible.

+---------------+------------------------------------------------------------+
|    Keyword    |                        Description                         |
+===============+============================================================+
| easy          | Fixing the issue should not take longer than a day for     |
|               | someone new to contributing to Python to solve.            |
+---------------+------------------------------------------------------------+

Nosy List
'''''''''
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
'''''''''
Who is expected to take the next step in resolving the issue.

It is acceptable to assign an issue to someone if the issue cannot move
forward without their help, e.g., they need to make a technical decision to
allow the issue to move forward. Also consult the :ref:`experts` as certain
stdlib modules should always be assigned to a specific person.

Note that in order to assign an issue to someone, that person **must** be
a team member, likely a Triager or a core developer.

Dependencies
''''''''''''
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
''''''''''
The issue is a duplicate of the listed issue(s). To make GitHub mark
an issue as duplicate, write "Duplicate of #xxxx" in a comment.

Status
''''''

+---------------+------------------------------------------------------------+
|    Status     |                        Description                         |
+===============+============================================================+
| open          | Issue is not resolved.                                     |
+---------------+------------------------------------------------------------+
| closed        | The issue has been resolved (somehow).                     |
+---------------+------------------------------------------------------------+

Linked pull requests
''''''''''''''''''''
A link might be added manually using the cog icon next to this field.
Most commonly though, if the PR includes "Fixes #xxx" in its description,
the link will be added automatically.

Generating Special Links in a Comment
-------------------------------------
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
