.. _triaging:

Triaging an Issue
=================

This section of the devguide documents the `issue tracker`_ for users
and developers.

Contributors with the Triager role on the `issue tracker`_ can triage issues
directly without any assistance.

Additionally, this section provides an overview of the Python triage team.

Python triage team
------------------

The Python triage team is a group dedicated towards improving workflow
efficiency through thoughtful review and triage of open issues and pull
requests. This helps contributors receive timely feedback and enables core
developers to focus on reviewed items which reduces their workload. The
expectations of this role expand upon the "Triager" role on the
`issue tracker`_. The responsibilities listed below are primarily centered
around the Python GitHub repositories. This extends beyond CPython, and, as
needed, to other repos such as devguide and core-workflow.

Responsibilities include:

* PR/issue management
    - Reviewing PRs
    - Assisting contributors
    - Notifying appropriate core developers
* Applying appropriate labels to PRs/Issues
    - Skip news
    - Skip issue
    - Good first issue
    - Other categorizations

Although triagers have the power to close PRs, they should generally not do so
without first consulting a core developer. By having triagers and core developers work together,
the author receives a careful consideration of their PR. This encourages future
contributions, regardless of whether their PR is accepted or closed.

Nonetheless, triagers should feel free to close a PR if they judge that the
chance of the PR being merged would be exceedingly low, even if substantial
revisions were made to the PR. This includes (but is not limited to) the
following:

* PRs proposing solely cosmetic changes
* PRs proposing changes to deprecated modules
* PRs that are no longer relevant. This includes:
    - PRs proposing fixes for bugs that can no longer be reproduced
    - PRs proposing changes that have been rejected by Python core developers
      elsewhere (e.g. in an issue or a PEP rejection notice)

If a triager has any doubt about whether to close a PR, they should consult a core
developer before taking any action.

Triagers can also make use of the ``invalid`` and ``stale`` labels to suggest that a
PR may be suitable for closure. For more information, see the
:ref:`GitHub PR labels <github-pr-labels>` section.

Note that it is of paramount importance to treat every contributor to the Python
project kindly and with respect. Regardless of whether they're entirely new
or a veteran core developer, they're actively choosing to voluntarily donate their
time towards the improvement of Python. As is the case with any member of
the Python Software Foundation, always follow the `PSF Code of Conduct`_.

Becoming a member of the Python triage team
-------------------------------------------

Any Python core developers are welcome to invite a Python contributor to the
Python triage team. Triagers will be responsible to handle not just issues, but
also pull requests, and even managing backports. A Python triager has access to
more repositories than just CPython.

Any existing active contributor to the Python repository on GitHub can
transition into becoming a Python triager. They can request this to any core
developer, and the core developer can pass the request to the `Python
organization admin
<https://devguide.python.org/devcycle/?highlight=organization%20admin#current-owners>`_
on GitHub. The request can be made confidentially via a DM in Discourse, or
publicly by opening an `issue in the core-workflow repository
<https://github.com/python/core-workflow/issues/new?template=triage_membership.md>`_.

For every new triager, it would be great to announce them in the python-committers
mailing list and core-workflow category in Discourse. `Example announcement
<https://discuss.python.org/t/abhilash-raj-has-been-granted-triage-role-on-github/2089>`_.

.. _github-pr-labels:

GitHub Labels for PRs
'''''''''''''''''''''

An important component of triaging PRs for the CPython repo involves
appropriately categorizing them through the usage of labels. For this
purpose we're using :doc:`gh-labels`.

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

As a guideline, whether a bug is a *release blocker* for the current `release
schedule`_ is decided by the release manager. Triagers may recommend this
priority and should notify the release manager by tagging them in a comment
using ``@username``. If needed, consult the `release schedule`_ and the
release's associated PEP for the release manager's name.

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

Checklist for Triaging
----------------------

* Read the issue comment(s).
* Review and set classification fields
    - Title: should be concise with specifics which are helpful to someone
      scanning a list of issue titles. (Optional, if possible) Add a
      prefix at the start of the title to indicate the module, e.g. IDLE,
      doc, or async.
    - Type
    - Stage
    - Components: multiple items may be set
    - Versions: set if known, leave blank if unsure. Multiple items may be set.
* Review and set process fields
    - Status
    - Superseder
    - Assignees
    - Nosy List
    - Priority
    - Keywords
* (Optional) Leave a brief comment about the proposed next action needed. If
  there is a long message list, a summary can be very helpful.


.. _CPython: https://github.com/python/cpython/
.. _Doc: https://github.com/python/cpython/tree/main/Doc/
.. _Grammar: https://github.com/python/cpython/tree/main/Grammar/
.. _Lib: https://github.com/python/cpython/tree/main/Lib/
.. _Lib/lib2to3: https://github.com/python/cpython/tree/main/Lib/lib2to3/
.. _Lib/ctypes: https://github.com/python/cpython/tree/main/Lib/ctypes/
.. _Lib/distutils: https://github.com/python/cpython/tree/main/Lib/distutils/
.. _Lib/doctest.py: https://github.com/python/cpython/blob/main/Lib/doctest.py
.. _Lib/idlelib: https://github.com/python/cpython/tree/main/Lib/idlelib/
.. _Lib/io.py: https://github.com/python/cpython/blob/main/Lib/io.py
.. _Lib/re.py: https://github.com/python/cpython/blob/main/Lib/re.py
.. _Lib/test: https://github.com/python/cpython/tree/main/Lib/test/
.. _Lib/test/regrtest.py: https://github.com/python/cpython/blob/main/Lib/test/regrtest.py
.. _Lib/test/support: https://github.com/python/cpython/tree/main/Lib/test/support/
.. _Lib/tkinter: https://github.com/python/cpython/tree/main/Lib/tkinter/
.. _Lib/unittest: https://github.com/python/cpython/tree/main/Lib/unittest/
.. _Lib/xml: https://github.com/python/cpython/tree/main/Lib/xml/
.. _Modules: https://github.com/python/cpython/tree/main/Modules/
.. _Modules/_io: https://github.com/python/cpython/tree/main/Modules/_io/
.. _Modules/_sre.c: https://github.com/python/cpython/blob/main/Modules/_sre.c
.. _Objects: https://github.com/python/cpython/tree/main/Objects/
.. _Objects/unicodeobject.c: https://github.com/python/cpython/blob/main/Objects/unicodeobject.c
.. _Parser: https://github.com/python/cpython/tree/main/Parser/
.. _Python: https://github.com/python/cpython/tree/main/Python/
.. _Tools: https://github.com/python/cpython/tree/main/Tools/
.. _Tools/demo: https://github.com/python/cpython/tree/main/Tools/demo/
.. _Developer's guide: https://github.com/python/devguide/
.. _GSoC: https://summerofcode.withgoogle.com/
.. _issue tracker: https://bugs.python.org
.. _GitHub pull requests: https://github.com/python/cpython/pulls
.. _Python source code repositories: https://github.com/python/cpython/
.. _Reporting security issues in Python: https://www.python.org/dev/security/
.. _python-ideas: https://mail.python.org/mailman3/lists/python-ideas.python.org
.. _release schedule: https://devguide.python.org/#status-of-python-branches
.. _PSF Code of Conduct: https://www.python.org/psf/conduct/
.. _PEP 3121: https://www.python.org/dev/peps/pep-3121/
