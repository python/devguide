.. _helptriage:

Helping Triage Issues
=====================

Once you know your way around how Python's source files are
structured and you are comfortable working with patches, a great way to
participate is to help triage issues. Do realize, though, that experience
working on Python is needed in order to effectively help triage.

Around the clock, new issues are being opened on the `issue tracker`_ and
existing issues are being updated. Every
issue needs to be triaged to make sure various things are in proper order. Even
without special privileges you can help with this process.


Bugs
----

For bugs, an issue needs to:

* clearly explain the bug so it can be reproduced
* include all relevant platform details
* state what version(s) of Python are affected by the bug.

These are things you can help with once you have experience developing for
Python. For instance, if a bug is not clearly explained enough for you to
reproduce it then there is a good chance a core developer won't be able to
either. And it is always helpful to know if a bug not only affects the
in-development version of Python, but whether it also affects other versions in
maintenance mode. And if the bug lacks a unit test that should end up in
Python's test suite, having that written can be very helpful.

This is all helpful as it allows triagers (i.e.,
:ref:`people with the Developer role on the issue tracker <devrole>`) to
properly classify an issue so it can be handled by the right core developers in
a timely fashion.


Patches
-------

If an issue has a patch attached that has not been reviewed, you can help by
making sure the patch:

* follows the style guides
* applies cleanly to an up-to-date checkout
* is a good solution to the problem it is trying to solve
* includes proper tests
* includes proper documentation changes
* submitter is listed in ``Misc/ACKS``, either already or the patch adds them

Doing all of this allows core developers and :ref:`triagers <devrole>` to more
quickly look for subtle issues that only people with extensive experience
working on Python's code base will notice.

There is a complete list of `open issues with patches`_ as well as a list of
`issues needing a review`_, although make sure
that someone has not already done the checklist above as it is possible the
issue is still open for reasons other than needing help being triaged.


.. _issue tracker: http://bugs.python.org
.. _issues needing a review: http://bugs.python.org/issue?status=1&@sort=-activity&@columns=id,activity,title,creator,status&@dispname=Show%20Needing%20Review&@startwith=0&@group=priority&@filter=&keywords=8&@action=search&@pagesize=50
.. _open issues with patches: http://bugs.python.org/issue?status=1&@sort=-activity&@columns=id,activity,title,creator,status&@dispname=Issues%20with%20patch&@startwith=0&@group=priority&@filter=&keywords=2&@action=search&@pagesize=50
