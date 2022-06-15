.. _triaging:

===================
 Triaging an Issue
===================

This section of the devguide documents the :ref:`issue tracker <tracker>` for
users and developers.

Contributors with the Triager role on the issue tracker can triage issues
directly without any assistance.


Checklist for Triaging
======================

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


.. _helptriage:

Helping Triage Issues
=====================

Once you know your way around how Python's source files are
structured and you are comfortable working with patches, a great way to
contribute is to help triage issues. Do realize, though, that experience
working on Python is needed in order to effectively help triage.

Around the clock, new issues are being opened on the :ref:`issue tracker
<tracker>` and existing issues are being updated. Every issue needs to be
triaged to make sure various things are in proper order. Even without special
privileges you can help with this process.

Classifying Reports
-------------------

For bugs, an issue needs to:

* clearly explain the bug so it can be reproduced
* include all relevant platform details
* state what version(s) of Python are affected by the bug.

These are things you can help with once you have experience developing for
Python:

* try reproducing the bug: For instance, if a bug is not clearly explained
  enough for you to reproduce it then there is a good chance a core developer
  won't be able to either.
* see if the issue happens on a different Python version: It is always helpful
  to know if a bug not only affects the in-development version of Python, but
  whether it also affects other versions in maintenance mode.
* write a unit test: If the bug lacks a unit test that should end up in
  Python's test suite, having that written can be very helpful.

This is all helpful as it allows triagers (i.e.,
:ref:`people with the Developer role on the issue tracker <triagers>`) to
properly classify an issue so it can be handled by the right core developers in
a timely fashion.

Reviewing Patches
-----------------

If an issue has a pull request attached that has not been reviewed, you can help
by making sure the patch:

* follows the style guides
* applies cleanly to an up-to-date clone
* is a good solution to the problem it is trying to solve
* includes proper tests
* includes proper documentation changes
* submitter is listed in ``Misc/ACKS``, either already or the patch adds them

Doing all of this allows core developers and :ref:`triagers` to more
quickly look for subtle issues that only people with extensive experience
working on Python's code base will notice.

Finding an Issue You Can Help With
----------------------------------

If you want to help triage issues, you might also want to search for issues
in modules which you have a working knowledge.  Search for the name of a module
in the issue tracker or use the `advanced search`_ query builder to search for
specific kinds of issues (e.g. the "Windows" label if you are a Windows
developer, "Extension Modules" if you are familiar with C, etc.).

.. _advanced search: https://github.com/search/advanced
