.. _triaging:

Triaging an Issue
=================

When you have the Developer role on the `issue tracker`_ you are able to triage
issues directly without any assistence.

Fields
------

Title
'''''
Should be properly descriptive about what the issue is about. Occasionally
people file an issue that either has too generic of a title or end up thinking
they filed about about X but in fact it turns out to be about Y and thus the
title is now wrong.

Type
''''
Self-explanatory from what is available. If something does not fit within any
specific type then simply do not set it.

Stage
'''''
What is next to advance the issue forward.

* unit test needed
    A reproducible test is needed before work can continue.
* needs patch
    The bug lacks a patch to solve the problem.
* patch review
    There is a patch, but it needs someone to do a review of it. This can be
    done by any triager as well as a core developer.
* commit review
    A triager performed a patch review and it looks good to them, but a core
    developer needs to commit the patch (and do a quick once-over to make sure
    nothing was overlooked).
* committed/rejected
    The issue is considered closed and dealt with.

Components
''''''''''
What part of Python is affected by the issue. This is a multi-select field.
Setting this properly is somewhat important as certain components lead to an
auto-assignment of the issue to the proper people.

Versions
''''''''
The known versions of Python that the issue affects and should be fixed for.
Thus if an issue for a new feature is assigned for e.g., Python 3.2 but is not
applied before Python 3.2.0 is released, this field should be updated to say
Python 3.3 as the version and drop Python 3.2.

Priority
''''''''
How important is this issue?

* Low
    Can be fixed at any time.
* normal
    Should be fixed before the final release if possible.
* high
    Make some effort to fix the issue before the next final release.
* critical
    This issue should definitely be fixed before the next final release.
* deferred blocker
    The issue will not hold up the next release, but will be promoted to a
    release blocker for the next release, e.g., won't block the next release of
    a1 but will block a2.
* release blocker
    The issue must be fixed before *any* release is made, e.g., will block the
    next release even if it is an alpha release.

Keywords
''''''''
Essentially flags about the issue. Multiple values are possible.

* after moratorium
    The issue is in regards to a language change which is not allowed during
    the `language moratorium`_.
* buildbot
    A buildbot triggered the issue being reported.
* easy
    Fixing the issue should not take longer than a day for someone new to
    contributing to Python to solve.
* gsoc
    The issue would fit as, or is related to, GSoC_.
* needs review
    The patch attached to the issue is in need of a review.
* patch
    There is a patch attached to the issue.

Nosy List
'''''''''
A list of people who may be interested in an issue. It is acceptable to add
someone to the nosy list if you think the issue should be brought to their
attention.

Assigned To
'''''''''''
Who is expected to take the next step in resolving the issue. It is acceptable
to assign an issue to someone if the issue cannot move forward without their
help, e.g., they need to make a technical decision to allow the issue to move
forward.

Dependencies
''''''''''''
The issue requires the listed issue(s) to be resolved first before it can move
forward.

Superceder
''''''''''
The issue is a duplicate of the listed issue(s).

Status
''''''
* open
    Issue is not resolved.
* languishing
    The issue has no clear solution , e.g., no agreement on a technical
    solution or if it is even a problem worth fixing.
* pending
    The issue is blocked until someone (often times the
    :abbr:`OP (original poster)`) provides some critical info; the issue is
    automatically closed after a set amount of time if no reply comes in.
    Useful for when someone reports a bug that lacks enough issue to reproduce
    and thus the issue is worthless without the needed info being provided.
* closed
    The issue has been resolved (somehow).

Resolution
''''''''''
Why the issue was closed.

* accepted
    Submitted patch was applied.
* duplicate
    Duplicate of another issue; should have the Superceder field filled out.
* fixed
    Someone contributed a fix for the issue.
* invalid
    For some reason the issue is invalid.
* later
    Issue is to be worked on at a later date.
* out of date
    The issue has already been fixed.
* postponed
    Issue will not be worked on at the moment.
* rejected
    Issue was rejected.
* remind
    The issue is acting as a reminder for someone.
* wont fix
    Issue will not be fixed, typically because it would cause a
    backwards-compatibility problem.
* works for me
    Bug cannot be reproduced.


Generating Special Links in a Comment
-------------------------------------
Comments can automatically generate a link to various things if formatted
properly.

* ``#<number>``, ``issue<number>``, ``issue <number>`` links to the
  tracker issue ``<number>``.
* ``msg<number>`` links to the tracker message ``<number>``.
* ``r<number>``, ``rev<number>``, ``revision <number>`` links to the VCS
  revision ``<number>``.


Reporting Issues About the Tracker
----------------------------------
The `meta tracker`_ is the tracker about the issue tracker. It is where you
file issues against anything you come across when working with the issue
tracker itself.


.. _GSoC: http://code.google.com/soc/
.. _issue tracker: http://bugs.python.org
.. _language moratorium: http://www.python.org/dev/peps/pep-3003/
.. _meta tracker: http://psf.upfronthosting.co.za/roundup/meta/
