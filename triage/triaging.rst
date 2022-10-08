.. _triaging:

=================
Triaging an Issue
=================

This section of the devguide documents the :ref:`issue tracker <tracker>` for
users and developers.


Checklist for Triaging
======================

* Check that the title is reasonably concise, while including enough specifics
  so that those scanning the list of issues can quickly identify its topic.
* For pull requests, ensure that the corresponding issue is added before
  the title (``gh-NNNNN: ...``).
* Read the initial message and the comments.
* Set all the relevant :ref:`labels <gh-labels>`.
* Where appropriate, set the :guilabel:`Assignees`,
  :guilabel`Reviewers`, and :guilabel:`Project` fields.
* You might also leave a brief comment about the proposed next action needed.
  If there is a long message list, a summary can be very helpful.
* If instead the issue is invalid (can't reproduce, duplicate, etc.),
  you can close it as "not planned".

Note: some of these fields can only be set/edited by core developers.


.. _helptriage:

Helping Triage Issues
=====================

Once you know your way around how Python's source files are
structured and you are comfortable with the workflow, a great way to
contribute is to help triage issues. Do realize, though, that experience
working on Python is needed in order to effectively help triage.

Around the clock, new issues are being opened on the :ref:`issue tracker
<tracker>` and existing issues are being updated. Every issue needs to be
triaged to make sure everything runs smoothly.

Classifying Reports
-------------------

For bugs, an issue needs to:

* clearly explain the bug so it can be reproduced
* include all relevant platform details
* state what version(s) of Python are affected by the bug.

These are things you can help with once you have experience developing for
Python:

* Try reproducing the bug: if it is not explained clearly
  enough for you to reproduce it, then there is a good chance a core developer
  won't be able to either.
* See if the issue happens on a different Python version: it is always helpful
  to know if a bug not only affects the in-development version of Python, but
  whether it also affects other versions in maintenance mode.
* Write a unit test: if the bug lacks a unit test that should end up in
  Python's test suite, having that written can be very helpful.

This is all helpful as it allows members of the :ref:`triage team <triage-team>`
to properly classify an issue so it can be handled by the right core developers
in a timely fashion.

Reviewing Pull Requests
-----------------------

If an issue has a linked pull request that has not been reviewed,
you can help by making sure the pull request:

* is a good solution to the problem it is trying to solve
* follows the style guides
* includes proper tests
* includes proper documentation changes
* includes a :ref:`NEWS entry <news-entry>` (if needed)
* includes the author in ``Misc/ACKS``, either already or the patch adds them
* doesn't have conflicts with the ``main`` branch

Doing all of this allows core developers and :ref:`triagers <triage-team>`
to more quickly look for subtle issues that only people with extensive
experience working on Python's code base will notice.

See also :ref:`committing`.

Finding an Issue You Can Help With
----------------------------------

If you want to help with triaging, you might also want to search for issues
in modules which you have a working knowledge.  Search for the name of a
module in the issue tracker, filter by label, or use the `advanced search`_
to find these issues.

.. _advanced search: https://github.com/search/advanced
