.. _triaging:

Triaging an Issue
=================

When you have the Developer role on the `issue tracker`_ you are able to triage
issues directly without any assistance.

Fields
------

Title
'''''
Should be properly descriptive of what the issue is about. Occasionally
people file an issue that either has too generic of a title or end up thinking
they filed about X but in fact it turns out to be about Y and thus the
title is now wrong.

Type
''''
Describes the type of issue.  If something does not fit within any
specific type then simply do not set it.

behavior
    Wrong or unexpected behavior, result, or exception.  This includes most of
    the bugs.
crash
    Hard crashes of the Python interpreter -- possibly with a core
    dump or a Windows error box.
compile error
    Errors reported by the compiler while compiling Python.
resource usage
    Situations where too many resources (e.g. memory) are used.
security
    Issues that might have security implications.  If you think the issue
    should not be made public, please report it to security@python.org instead.
performance
    Situations where too much time is necessary to complete the task.
enhancement
    Issues that propose the addition of new functionality, such as new
    functions, classes, modules, or even new arguments for existing functions.
    Also used for improvements in the documentation and test suite and for
    other refactorings.

Stage
'''''
What is needed next to advance the issue.  The *stage* needn't be set until
it is clear that the issue warrants fixing.

test needed
    The bug reporter should post a script or instructions to let a triager or
    developer reproduce the issue.
needs patch
    The issue lacks a patch to solve the problem (i.e. fixing the bug, or
    adding the requested improvement).
patch review
    There is a patch, but it needs reviewing or is in the process of being
    reviewed. This can be done by any triager as well as a core developer.
commit review
    A triager performed a patch review and it looks good to them, but a core
    developer needs to commit the patch (and do a quick once-over to make sure
    nothing was overlooked).
resolved
    The issue is considered closed and dealt with.

Components
''''''''''
What part of Python is affected by the issue. This is a multi-select field.
Be aware that what component is chosen may cause the issue to be auto-assigned,
i.e. the issue tracker may automatically fill in the `Assigned To`_ field
after you press ``Submit changes``.

The following component(s) should be selected if the issue applies to:

2to3 (2.x to 3.0 conversion tool)
    The 2to3 conversion tool in `Lib/lib2to3`_.
Build
    The build process.
ctypes
    The ctypes package in `Lib/ctypes`_.
Demos and Tools
    The files in Tools_ and `Tools/demo`_.
Distutils
    The distutils package in `Lib/distutils`_.
Documentation
    The documentation in Doc_ (used to build the HTML doc at
    https://docs.python.org/).
email
    The email package and related modules.
Extension Modules
    C modules in Modules_.
IDLE
    The `Lib/idlelib`_ package.
Installation
    The installation process.
Interpreter Core
    The interpreter core, the built-in objects in `Objects`_, the `Python`_,
    `Grammar`_ and `Parser`_ dirs.
IO
    The I/O system, `Lib/io.py`_ and `Modules/_io`_.
Library (Lib)
    Python modules in Lib_.
Macintosh
    The Mac OS X operating system.
Regular Expressions
    The `Lib/re.py`_ and `Modules/_sre.c`_ modules.
Tests
    The unittest and doctest frameworks in `Lib/unittest`_ and
    `Lib/doctest.py`_.

    The CPython tests in `Lib/test`_, the test runner in `Lib/test/regrtest.py`_
    and the `Lib/test/support`_ package.
Tkinter
    The `Lib/tkinter`_ package.
Unicode
    Unicode, codecs, str vs bytes, `Objects/unicodeobject.c`_.
Windows
    The Windows operating system.
XML
    The `Lib/xml`_ package.

Versions
''''''''
The known versions of Python that the issue affects and should be fixed for.
Thus if an issue for a new feature is assigned for e.g., Python 3.7 but is not
applied before Python 3.7.0 is released, this field should be updated to say
Python 3.8 as the version and drop Python 3.7.

Priority
''''''''
How important is this issue?

low
    This is for low-impact bugs, or feature requests of little utility.
normal
    The default value for most issues, which deserve fixing but without
    any urgency to do so.
high
    Make some effort to fix the issue before the next final release.
critical
    This issue should definitely be fixed before the next final release.
deferred blocker
    The issue will not hold up the next release, but will be promoted to a
    release blocker for the following release, e.g., won't block the next
    release of a1 but will block a2.
release blocker
    The issue must be fixed before *any* release is made, e.g., will block the
    next release even if it is an alpha release.

As a guideline, *critical* and above are usually reserved for crashes,
serious regressions or breakage of very important APIs.  Whether a bug
is a *release blocker* is a decision better left to the release manager so,
in any doubt, add him or her to the *nosy list*.

Keywords
''''''''
Various flags about the issue. Multiple values are possible.

buildbot
    A buildbot triggered the issue being reported.
easy
    Fixing the issue should not take longer than a day for someone new to
    contributing to Python to solve.
gsoc
    The issue would fit as, or is related to, a GSoC_ project.
needs review
    The patch attached to the issue is in need of a review.
patch
    There is a patch attached to the issue.
3.3regression
    The issue is a regression in 3.3.

Nosy List
'''''''''
A list of people who may be interested in an issue. It is acceptable to add
someone to the nosy list if you think the issue should be brought to their
attention. Use the :ref:`experts` to know who wants to be added to the nosy
list for issues targeting specific areas.


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
Who is expected to take the next step in resolving the issue. It is acceptable
to assign an issue to someone if the issue cannot move forward without their
help, e.g., they need to make a technical decision to allow the issue to move
forward. Also consult the :ref:`experts` as certain stdlib modules should
always be assigned to a specific person.

Dependencies
''''''''''''
The issue requires the listed issue(s) to be resolved first before it can move
forward.

Superseder
''''''''''
The issue is a duplicate of the listed issue(s).

Status
''''''
open
    Issue is not resolved.
languishing
    The issue has no clear solution , e.g., no agreement on a technical
    solution or if it is even a problem worth fixing.
pending
    The issue is blocked until someone (often the
    :abbr:`OP (original poster)`) provides some critical information;
    the issue will be closed after a set amount of time if no reply comes in.
    Useful when someone opens an issue that lacks enough information to
    reproduce the bug reported.  Requesting additional information and setting
    status to *pending* indicates that the issue should be closed if the
    necessary information is never provided.
closed
    The issue has been resolved (somehow).

Resolution
''''''''''
Why the issue is in its current state (not usually used for "open").

duplicate
    Duplicate of another issue; should have the Superseder field filled out.
fixed
    A fix for the issue was committed.
later
    Issue is to be worked on at a later date.
not a bug
    For some reason the issue is invalid (e.g. the perceived problem is not
    a bug in Python).
out of date
    The issue has already been fixed, or the problem doesn't exist anymore
    for other reasons.
postponed
    Issue will not be worked on at the moment.
rejected
    Issue was rejected (especially for feature requests).
remind
    The issue is acting as a reminder for someone.
wont fix
    Issue will not be fixed, typically because it would cause a
    backwards-compatibility problem.
works for me
    Bug cannot be reproduced.

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
Comments can automatically generate a link to various web pages if formatted
properly.

* ``#<number>``, ``issue<number>``, or ``issue <number>`` links to the
  tracker issue ``<number>``.
* ``msg<number>`` links to the tracker message ``<number>``.
* ``PR <number>``, ``PR<number>``, and ``pull request <number>`` can be used
  to link to `GitHub pull requests <https://github.com/python/cpython/pulls>`_.
* a 10-, 11-, 12-, or 40-digit hex ``<number>`` is assumed to be a Git or
  Mercurial changeset identifier and generates a link to changeset ``<number>``
  on GitHub or https://hg.python.org/.  The ``git`` and ``hg`` prefixes can
  also be used to disambiguate, and must precede the number without spaces.
* ``r<number>``, ``rev<number>``, or ``revision <number>`` is assumed to be
  a legacy Subversion revision number, a reference to a changeset that was
  checked in prior to 2011-03-05 when the official Python source code
  repositories were migrated from the :abbr:`svn (Subversion)`
  :abbr:`VCS (version control system)` to Mercurial.
  The issue tracker automatically translates the legacy svn revision
  ``<number>`` to its corresponding Mercurial changeset identifier.
* ``Dir/file.ext`` and ``Dir/file.ext:NNN`` generate links to files in the
  `Python source code repositories <https://github.com/python/cpython/>`_,
  possibly linking to the line number specified after the ``:``.
  ``3.6/Dir/file.ext`` will generate a link with ``3.6`` as branch.
* ``PEP <number>`` and ``PEP<number>`` link to the
  :abbr:`PEP (Python Enhancement Proposal)` ``<number>``.
* ``devguide`` (lowercase), ``devguide/triaging``, and
  ``devguide/triaging#generating-special-links-in-a-comment`` generate links to
  the Devguide, this page, and this section respectively.


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
