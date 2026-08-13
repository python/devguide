.. _triaging:

=================
Triaging an issue
=================

Every issue on the :ref:`issue tracker <tracker>` needs to be triaged to make
sure everything runs smoothly. This section covers what that involves.


Checklist for triaging
======================

* Read the initial message and the comments.
* :ref:`Search the tracker <searching-gh-issues>` to check that the issue
  isn't a duplicate. If it is, use GitHub's :guilabel:`Close as duplicate`
  option and select the issue it duplicates.
* Check that the title is reasonably concise, while including enough specifics
  so that those scanning the list of issues can quickly identify its topic.
* For pull requests, ensure that the corresponding issue is added before
  the title (:samp:`gh-NNNNN: {Title}`).
* Set all the relevant :ref:`labels <triage-labels>`.
* Where appropriate, set the :guilabel:`Assignees`, :guilabel:`Reviewers`, and
  :guilabel:`Project` :ref:`fields <triage-fields>`, and possibly @mention
  relevant people.
* You might also leave a brief comment about the proposed next action needed.
  If there is a long message list, a summary can be very helpful.
* If the issue is clearly invalid (unrelated to CPython, spam, and
  so on), you can use GitHub's :guilabel:`Close as not planned` option
  and apply the :gh-label:`invalid` label.


.. _triage-fields:

Issue fields
============

These fields can be set in the sidebar of issues and pull requests.


.. _triage-labels:

Labels
------

Labels are the main way of categorizing issues and automating certain actions on
pull requests. Set all that apply. See :ref:`gh-labels` for more information.


Assignees
---------

This field indicates who is expected to take the next step in resolving
the issue.

It is acceptable to assign an issue to someone if the issue cannot move
forward without their help; for example, they need to make a technical decision on
how to proceed. Also consult the :ref:`experts` as certain
stdlib modules should always be assigned to a specific person.

Note that in order to assign an issue to someone, that person **must**
have at least triage permissions in the repository.


Reviewers
---------

This field is used to request a review from specific people.

In most cases there is nothing to do, as the maintainers listed in the
:cpy-file:`.github/CODEOWNERS` file are automatically requested to review
pull requests touching the files they maintain. Otherwise, consult the
:ref:`experts` to find someone with a working knowledge of the affected area
or platform.

If the person you have in mind doesn't show up in the :guilabel:`Reviewers`
dropdown (usually because they don't have the required permissions in the
repository), @mention them in a comment instead.


Project
-------

`GitHub projects <https://github.com/orgs/python/projects>`__ are used to track
work on a specific module, platform, or interest area across issues and pull
requests. Add all the relevant ones. Note that several are added automatically
when the corresponding :ref:`label <gh-labels>` is added.


.. _helptriage:

Helping triage issues
=====================

Once you know your way around how Python's source files are
structured and you are comfortable with the workflow, a great way to
contribute is to help triage issues. Do realize, though, that experience
working on Python is needed in order to effectively help triage.


Classifying reports
-------------------

For bugs, an issue needs to:

* clearly explain the bug so it can be reproduced
* include all relevant platform details
* state what versions of Python are affected by the bug.

These are things you can help with once you have experience developing for
Python:

* Try reproducing the bug: if it is not explained clearly
  enough for you to reproduce it, then there is a good chance a core team
  member won't be able to either.
* See if the issue happens on a different Python version: it is always helpful
  to know if a bug not only affects the in-development version of Python, but
  whether it also affects other versions in maintenance mode.
* Write a unit test: if the bug lacks a unit test that should end up in
  Python's test suite, having that written can be very helpful.

This is all helpful as it allows members of the :ref:`triage team <triage-team>`
to properly classify an issue so it can be handled by the right core team
members in a timely fashion.


Reviewing pull requests
-----------------------

If an issue has a linked pull request that has not been reviewed,
you can help by making sure the pull request:

* is a good solution to the problem it is trying to solve
* follows the style guides (for example, :pep:`7`, :pep:`8`, and :ref:`style-guide`)
* includes proper tests
* includes proper documentation changes
* includes a :ref:`NEWS entry <news-entry>` (if needed)
* doesn't have conflicts with the ``main`` branch
* :ref:`doesn't have failing CI checks <keeping-ci-green>`

Doing all of this allows core team members and :ref:`triagers <triage-team>`
to more quickly look for subtle issues that only people with extensive
experience working on Python's codebase will notice.

See also :ref:`committing`.


Finding an issue you can help with
----------------------------------

If you want to help with triaging, you might also want to search for issues
in modules for which you have a working knowledge.  See :ref:`searching-gh-issues`
for more information.
