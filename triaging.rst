.. _triaging:

Triaging an Issue
=================

This section of the devguide documents the `issue tracker`_ for users
and developers.

Contributors with the Developer role on the `issue tracker`_ can triage issues
directly without any assistance.

Additionally, this section provides an overview of the Python triage team.

Python triage team
------------------

The Python triage team is a group dedicated towards improving workflow
efficiency through thoughtful review and triage of open issues and pull
requests. This helps contributors receive timely feedback and enables core 
developers to focus on reviewed items which reduces their workload. The 
expectations of this role expand upon the "Developer" role on the 
`issue tracker`_. The responsibilities listed below are primarily centered 
around the Python GitHub repositories. This extends beyond CPython, and, as 
needed, to other repos such as devguide and core-workflow.

Responsibilities include:

* PR/issue management
    - Renaming PRs
    - Reviewing PRs
    - Closing PRs and issues
    - Assisting contributors
    - Notifying appropriate core developers
* Applying appropriate labels to PRs/Issues
    - Skip news
    - Skip issue
    - Good first issue
    - Other categorizations

It is also of paramount importance to treat every contributor to the Python
project kindly and with respect. Regardless of whether they're entirely new
or a veteran core developer, they're actively choosing to voluntarily donate their
time towards the improvement of Python. As is the case with any member of
the Python Software Foundation, always follow the `PSF Code of Conduct`_.

.. note::

   Existing members with the "Developer" role on the `issue tracker`_ are welcome to
   self-nominate for triage team membership if they are interested.
   
GitHub Labels
''''''''''''''''

An important component of triaging PRs and issues involves appropriately 
categorizing them through the usage of labels. Here are several of the
common ones utilized by the Python triage team:

+-----------------------+----------------------------------------------------------------------------+
| Label                 | Description                                                                |
+-----------------------+----------------------------------------------------------------------------+
| needs backport to X.Y | Used for PRs which are appropriate to backport to branches prior to        |
|                       | master. Generally, backports to the maintenance branches are primarily     |
|                       | bugfixes and documentation clarifications. Backports to the security       |
|                       | branches are strictly reserved for PRs involving security fixes, such as   |
|                       | crashes, privilege escalation, and DoS.                                    |
+-----------------------+----------------------------------------------------------------------------+
| skip issue            | Used for PRs which involve trivial changes, such as typo fixes,            |
|                       | comment changes, and section rephrases. The majority of PRs require        |
|                       | an issue to be attached to, but if there are no code changes and the       |
|                       | section being modified retains the same meaning, this label might be       |
|                       | appropriate. It is also used commonly for backports.                       |
+-----------------------+----------------------------------------------------------------------------+
| skip news             | Used frequently in combination with the skip issue label for PRs that      |
|                       | involve trivial changes, backports, or already have a relevant news entry  |
|                       | in another PR. Any potentially impactful changes should have a             |
|                       | corresponding  news entry, but for trivial changes it's commonly at the    |
|                       | discretion of the PR author if they wish to opt-out of making one.         |
+-----------------------+----------------------------------------------------------------------------+

Fields in the Issue Tracker
---------------------------

The major elements found in an issue report include:

* Classification (including *Title*) - These fields categorize the issue.
  The fields include *Title*, *Type*, *Stage*, *Components*, and *Version*.
* Process - These fields indicate the state of the issue and its progress
  toward resolution. The fields are *Status*, *Resolution*, *Dependencies*,
  *Superseder*, *Assigned To*, *Nosy List*, *Priority*, *Keywords*, *Comment*,
  *File*, *File Description*, *Remote hg repo*, *GitHub PR*.
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
|                | will have this type.                                     |
+----------------+----------------------------------------------------------+
| compile error  | Errors reported by the compiler while compiling Python.  |
+----------------+----------------------------------------------------------+
| crash          | Hard crashes of the Python interpreter -- possibly with  |
|                | a core dump or a Windows error box.                      |
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
|                | significantly longer to complete.                        |
+----------------+----------------------------------------------------------+
| resource usage | Situations where too many resources (e.g. memory) are    |
|                | used.                                                    |
+----------------+----------------------------------------------------------+
| security       | Issues that might have security implications. Report     |
|                | security vulnerabilities using the procedure found in    |
|                | the `Reporting security issues in Python`_ page on the   |
|                | python.org website.                                      |
+----------------+----------------------------------------------------------+

Stage
'''''
A needed next action to advance the issue.  The *stage* needn't be set until
it is clear that the issue has been initially triaged and determined work
will be needed.

+---------------+----------------------------------------------------------+
|     Stage     |                       Description                        |
+===============+==========================================================+
| test needed   | The steps which are needed to reproduce the issue. The   |
|               | bug reporter should post a script, instructions, or      |
|               | example to help someone test or reproduce the issue.     |
+---------------+----------------------------------------------------------+
| needs patch   | A patch or pull request is needed to solve the problem   |
|               | (i.e. fixing the bug or adding the requested             |
|               | improvement).                                            |
+---------------+----------------------------------------------------------+
| patch review  | A patch or pull request exists, but it needs review.     |
|               | Any triager or core developer may do the review.         |
+---------------+----------------------------------------------------------+
| commit review | A triager performed a patch review and it looks good.    |
|               | This signals to core developers the patch or pull        |
|               | request needs a quick once-over to make sure nothing was |
|               | overlooked before committing it.                         |
+---------------+----------------------------------------------------------+
| resolved      | The issue is considered closed and addressed (e.g. patch |
|               | or pull request committed; expected behavior).           |
+---------------+----------------------------------------------------------+

Components
''''''''''
The area or Python library affected by the issue. This is a multi-select field.

Choosing certain components, such as `Documentation`, may cause the issue to
be auto-assigned, i.e. the issue tracker may automatically fill in the
`Assigned To`_ field after you press ``Submit changes``.

One or more components may be selected for an issue:

+-------------------+------------------------------------------------------+
|     Component     |                     Description                      |
+===================+======================================================+
| 2to3 (*2.x to*    | The 2to3 conversion tool in `Lib/lib2to3`_.          |
| *3 conversion*    |                                                      |
| *tool*)           |                                                      |
+-------------------+------------------------------------------------------+
| Build             | The build process.                                   |
+-------------------+------------------------------------------------------+
| ctypes            | The ctypes package in `Lib/ctypes`_.                 |
+-------------------+------------------------------------------------------+
| Demos and Tools   | The files in Tools_ and `Tools/demo`_.               |
+-------------------+------------------------------------------------------+
| Distutils         | The distutils package in `Lib/distutils`_.           |
+-------------------+------------------------------------------------------+
| Documentation     | The documentation in Doc_ (source used to build HTML |
|                   | docs for https://docs.python.org/).                  |
+-------------------+------------------------------------------------------+
| email             | The email package and related modules.               |
+-------------------+------------------------------------------------------+
| Extension Modules | C modules in Modules_.                               |
+-------------------+------------------------------------------------------+
| IDLE              | The `Lib/idlelib`_ package.                          |
+-------------------+------------------------------------------------------+
| Installation      | The installation process.                            |
+-------------------+------------------------------------------------------+
| Interpreter Core  | The interpreter core.                                |
|                   | The built-in objects in `Objects`_, the `Python`_,   |
|                   | `Grammar`_ and `Parser`_ dirs.                       |
+-------------------+------------------------------------------------------+
| IO                | The I/O system, `Lib/io.py`_ and `Modules/_io`_.     |
+-------------------+------------------------------------------------------+
| Library (Lib)     | Python modules in Lib_.                              |
+-------------------+------------------------------------------------------+
| Macintosh         | The Mac OS X operating system.                       |
+-------------------+------------------------------------------------------+
| Regular           | The `Lib/re.py`_ and `Modules/_sre.c`_ modules.      |
| Expressions       |                                                      |
+-------------------+------------------------------------------------------+
| Tests             | The unittest framework in `Lib/unittest`_            |
|                   | The doctest framework `Lib/doctest.py`_.             |
|                   | The CPython tests in `Lib/test`_.                    |
|                   | The test runner in `Lib/test/regrtest.py`_.          |
|                   | The test support utilities in `Lib/test/support`_.   |
+-------------------+------------------------------------------------------+
| Tkinter           | The `Lib/tkinter`_ package.                          |
+-------------------+------------------------------------------------------+
| Unicode           | Unicode, codecs, str vs bytes,                       |
|                   | `Objects/unicodeobject.c`_.                          |
+-------------------+------------------------------------------------------+
| Windows           | The Windows operating system.                        |
+-------------------+------------------------------------------------------+
| XML               | The `Lib/xml`_ package.                              |
+-------------------+------------------------------------------------------+

Versions
''''''''
The known versions of Python that the issue affects and should be fixed for.

Thus if an issue for a new feature is assigned for e.g., Python 3.8 but is not
applied before Python 3.8.0 is released, this field should be updated to say
Python 3.9 as the version and drop Python 3.8.

Priority
''''''''
What is the severity and urgency?

+------------------+--------------------------------------------------------+
| Priority         | Description                                            |
+==================+========================================================+
| low              | This is for low-impact bugs.                           |
+------------------+--------------------------------------------------------+
| normal           | The default value for most issues filed.               |
+------------------+--------------------------------------------------------+
| high             | Try to fix the issue before the next final release.    |
+------------------+--------------------------------------------------------+
| critical         | Should definitely be fixed for next final release.     |
+------------------+--------------------------------------------------------+
| deferred blocker | The issue will not hold up the next release, *n*. It   |
|                  | will be promoted to a *release blocker* for the        |
|                  | following release, *n+1*.                              |
+------------------+--------------------------------------------------------+
| release blocker  | The issue **must** be fixed before *any* release is    |
|                  | made, e.g., will block the next release even if it is  |
|                  | an alpha release.                                      |
+------------------+--------------------------------------------------------+

As a guideline, *critical* and above are usually reserved for crashes,
serious regressions or breakage of very important APIs.  Whether a bug
is a *release blocker* for the current `release schedule`_ is decided by the
release manager. Triagers may recommend this priority and should add the
release manager to the *nosy list*. If needed, consult the
`release schedule`_ and the release's associated PEP for the release
manager's name.

Keywords
''''''''
Various informational flags about the issue. Multiple values are possible.

+---------------+------------------------------------------------------------+
|    Keyword    |                        Description                         |
+===============+============================================================+
| buildbot      | A buildbot triggered the issue being reported.             |
+---------------+------------------------------------------------------------+
| easy          | Fixing the issue should not take longer than a day for     |
|               | someone new to contributing to Python to solve.            |
+---------------+------------------------------------------------------------+
| gsoc          | The issue would fit as, or is related to, a GSoC_ project. |
+---------------+------------------------------------------------------------+
| needs review  | The patch or pull request attached to the issue is in need |
|               | of a review.                                               |
+---------------+------------------------------------------------------------+
| patch         | There is a patch or pull request attached to the issue.    |
+---------------+------------------------------------------------------------+
| 3.3regression | The issue is a regression in 3.3.                          |
+---------------+------------------------------------------------------------+

Nosy List
'''''''''
A list of people who may be interested in an issue.

It is acceptable to add someone to the nosy list if you think the issue should
be brought to their attention. Use the :ref:`experts` to know who wants to be
added to the nosy list for issues targeting specific areas.

If you are logged in and have JavaScript enabled, you can use the ``[+]``
button to add yourself to the nosy list (remember to click on
"Submit Changes" afterwards).  Note that you are added to the nosy
automatically when you submit a message.

The nosy list also has an autocomplete that lets you search from the lists of
developers and :ref:`experts`.  The search is case-insensitive and
works for real names, modules, interest areas, etc., and only adds the
username(s) to the nosy once an entry is selected.

Assigned To
'''''''''''
Who is expected to take the next step in resolving the issue.

It is acceptable to assign an issue to someone if the issue cannot move
forward without their help, e.g., they need to make a technical decision to
allow the issue to move forward. Also consult the :ref:`experts` as certain
stdlib modules should always be assigned to a specific person.

Note that in order to assign an issue to someone, that person **must** have
the :ref:`Developer role <devrole>` on the issue tracker.

Dependencies
''''''''''''
The issue requires the listed issue(s) to be resolved first before it can move
forward.

Superseder
''''''''''
The issue is a duplicate of the listed issue(s).

Status
''''''

+---------------+------------------------------------------------------------+
|    Status     |                        Description                         |
+===============+============================================================+
| open          | Issue is not resolved.                                     |
+---------------+------------------------------------------------------------+
| pending       | The issue is blocked until someone (often the              |
|               | :abbr:`OP (original poster)`) provides some critical       |
|               | information; the issue will be closed after a set amount   |
|               | time if no reply comes in.                                 |
|               |                                                            |
|               | Useful when someone opens an issue that lacks enough       |
|               | information to reproduce the bug reported.  Requesting     |
|               | additional information and setting status to *pending*     |
|               | indicates that the issue should be closed if the necessary |
|               | information is not provided in a timely manner (i.e. one   |
|               | month).                                                    |
+---------------+------------------------------------------------------------+
| closed        | The issue has been resolved (somehow).                     |
+---------------+------------------------------------------------------------+

Resolution
''''''''''
Why the issue is in its current state. This is not usually used for issues
with the "open" status.

+---------------+------------------------------------------------------------+
|  Resolution   |                        Description                         |
+===============+============================================================+
| open          | Issue is not resolved.                                     |
+---------------+------------------------------------------------------------+
| duplicate     | Duplicate of another issue; should have the *Superseder*   |
|               | field filled out.                                          |
+---------------+------------------------------------------------------------+
| fixed         | A fix for the issue was committed.                         |
+---------------+------------------------------------------------------------+
| later         | Issue is to be worked on in a later release cycle.         |
+---------------+------------------------------------------------------------+
| not a bug     | For some reason the issue is invalid (e.g. the perceived   |
|               | problem is not a bug in Python).                           |
+---------------+------------------------------------------------------------+
| out of date   | The issue has already been fixed, or the problem doesn't   |
|               | exist anymore for other reasons.                           |
+---------------+------------------------------------------------------------+
| postponed     | Issue will not be worked on at the moment but in a future  |
|               | minor release version.                                     |
+---------------+------------------------------------------------------------+
| rejected      | Issue was rejected (especially for feature requests).      |
+---------------+------------------------------------------------------------+
| remind        | The issue is acting as a reminder for someone.             |
+---------------+------------------------------------------------------------+
| wont fix      | Issue will not be fixed, typically because it would cause  |
|               | a backwards-compatibility problem.                         |
+---------------+------------------------------------------------------------+
| works for me  | Bug cannot be reproduced.                                  |
+---------------+------------------------------------------------------------+

Mercurial Repository
''''''''''''''''''''
HTTP link to a Mercurial repository that contains a patch for the issue.
A :guilabel:`Create Patch` button will appear that computes a diff for the
head revision of the remote branch and attaches it to the issue.  The button
supports only CPython_ patches.

If you don't indicate a remote branch, ``default`` is used.  You can
indicate a remote branch by adding ``#BRANCH`` to the end of the URL.

Generating Special Links in a Comment
-------------------------------------
Using the following abbreviations in a comment will automatically generate
a link to relevant web pages.

+-------------------------------------------------------------+-------------------------------------------------------+
| Comment abbreviation                                        | Description                                           |
+=============================================================+=======================================================+
| ``#<number>``,                                              | Links to the tracker issue ``<number>``.              |
| ``issue<number>``, or                                       |                                                       |
| ``issue <number>``                                          |                                                       |
+-------------------------------------------------------------+-------------------------------------------------------+
| ``msg<number>``                                             | Links to the tracker message ``<number>``.            |
+-------------------------------------------------------------+-------------------------------------------------------+
| ``PR <number>``,                                            | Links to `GitHub pull requests`_.                     |
| ``PR<number>``, or                                          |                                                       |
| ``pull request <number>``                                   |                                                       |
+-------------------------------------------------------------+-------------------------------------------------------+
| a 10-, 11-, 12-, or 40-digit hex ``<number>``               | Indicates a Git or Mercurial changeset identifier and |
|                                                             | generates a link to changeset ``<number>`` on GitHub  |
|                                                             | or https://hg.python.org/. The ``git`` and ``hg``     |
|                                                             | prefixes can also be used to disambiguate, and must   |
|                                                             | precede the number without spaces.                    |
+-------------------------------------------------------------+-------------------------------------------------------+
| ``r<number>``,                                              | Indicates a legacy Subversion revision number,        |
| ``rev<number>``, or                                         | a reference to a changeset that was checked in prior  |
| ``revision <number>``                                       | to 2011-03-05 when the official Python source code    |
|                                                             | repositories were migrated from the                   |
|                                                             | :abbr:`svn (Subversion)`                              |
|                                                             | :abbr:`VCS (version control system)` to Mercurial.    |
|                                                             | The issue tracker automatically translates the legacy |
|                                                             | svn revision ``<number>`` to its corresponding        |
|                                                             | Mercurial changeset identifier.                       |
+-------------------------------------------------------------+-------------------------------------------------------+
| ``Dir/file.ext`` or                                         | Links to files in the                                 |
| ``Dir/file.ext:NNN``                                        | `Python source code repositories`_, possibly linking  |
|                                                             | to the line number specified after the ``:``.         |
|                                                             | ``3.6/Dir/file.ext`` will generate a link with ``3.6``|
|                                                             | as branch.                                            |
+-------------------------------------------------------------+-------------------------------------------------------+
| ``PEP <number>`` or                                         | Link to the :abbr:`PEP (Python Enhancement Proposal)` |
| ``PEP<number>``                                             | ``<number>``.                                         |
+-------------------------------------------------------------+-------------------------------------------------------+
| ``devguide``,                                               | Links to the Devguide, this page, and this section    |
| ``devguide/triaging``, or                                   | respectively.                                         |
| ``devguide/triaging#generating-special-links-in-a-comment`` |                                                       |
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
    - Resolution
    - Superseder
    - Assigned To
    - Nosy List
    - Priority
    - Keywords
* (Optional) Leave a brief comment about the proposed next action needed. If
  there is a long message list, a summary can be very helpful.


.. _CPython: https://github.com/python/cpython/
.. _Doc: https://github.com/python/cpython/tree/master/Doc/
.. _Grammar: https://github.com/python/cpython/tree/master/Grammar/
.. _Lib: https://github.com/python/cpython/tree/master/Lib/
.. _Lib/lib2to3: https://github.com/python/cpython/tree/master/Lib/lib2to3/
.. _Lib/ctypes: https://github.com/python/cpython/tree/master/Lib/ctypes/
.. _Lib/distutils: https://github.com/python/cpython/tree/master/Lib/distutils/
.. _Lib/doctest.py: https://github.com/python/cpython/tree/master/Lib/doctest.py
.. _Lib/idlelib: https://github.com/python/cpython/tree/master/Lib/idlelib/
.. _Lib/io.py: https://github.com/python/cpython/tree/master/Lib/io.py
.. _Lib/re.py: https://github.com/python/cpython/tree/master/Lib/re.py
.. _Lib/test: https://github.com/python/cpython/tree/master/Lib/test/
.. _Lib/test/regrtest.py: https://github.com/python/cpython/tree/master/Lib/test/regrtest.py
.. _Lib/test/support: https://github.com/python/cpython/tree/master/Lib/test/support/
.. _Lib/tkinter: https://github.com/python/cpython/tree/master/Lib/tkinter/
.. _Lib/unittest: https://github.com/python/cpython/tree/master/Lib/unittest/
.. _Lib/xml: https://github.com/python/cpython/tree/master/Lib/xml/
.. _Modules: https://github.com/python/cpython/tree/master/Modules/
.. _Modules/_io: https://github.com/python/cpython/tree/master/Modules/_io/
.. _Modules/_sre.c: https://github.com/python/cpython/tree/master/Modules/_sre.c
.. _Objects: https://github.com/python/cpython/tree/master/Objects/
.. _Objects/unicodeobject.c: https://github.com/python/cpython/tree/master/Objects/unicodeobject.c
.. _Parser: https://github.com/python/cpython/tree/master/Parser/
.. _Python: https://github.com/python/cpython/tree/master/Python/
.. _Tools: https://github.com/python/cpython/tree/master/Tools/
.. _Tools/demo: https://github.com/python/cpython/tree/master/Tools/demo/
.. _Developer's guide: https://github.com/python/devguide/
.. _GSoC: https://developers.google.com/open-source/gsoc/
.. _issue tracker: https://bugs.python.org
.. _GitHub pull requests: https://github.com/python/cpython/pulls>
.. _Python source code repositories: https://github.com/python/cpython/
.. _Reporting security issues in Python: https://www.python.org/news/security/
.. _python-ideas: https://mail.python.org/mailman/listinfo/python-ideas
.. _release schedule: https://devguide.python.org/#status-of-python-branches
.. _PSF Code of Conduct: https://www.python.org/psf/codeofconduct/
