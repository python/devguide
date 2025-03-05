.. _pull-request-lifecycle:
.. _patch:
.. _pullrequest:

===========================
Lifecycle of a pull request
===========================

.. highlight:: bash

Introduction
============

CPython uses a workflow based on pull requests. What this means is
that you create a branch in Git, make your changes, push those changes
to your fork on GitHub (``origin``), and then create a pull request against
the official CPython repository (``upstream``).


.. _pullrequest-quickguide:

Quick guide
===========

`Clear communication`_ is key to contributing to any project, especially an
`Open Source`_ project like CPython.

Here is a quick overview of how you can contribute to CPython:

#. `Create an issue`_ that describes your change [*]_

#. :ref:`Create a new branch in Git <pullrequest-steps>` from the
   ``main`` branch

#. Work on changes: fix a bug or add a new feature

#. :ref:`Run tests <runtests>` and ``make patchcheck``

#. :ref:`Commit <commit-changes>` and :ref:`push <push-changes>`
   changes to your GitHub fork

#. `Create Pull Request`_ on GitHub to merge a branch from your fork

#. Make sure the :ref:`continuous integration checks on your Pull Request
   are green <keeping-ci-green>` (successful)

#. Review and address `comments on your Pull Request`_

#. When your changes are merged, you can :ref:`delete the PR branch
   <deleting_branches>`

#. Celebrate contributing to CPython! :)

.. [*] If an issue is trivial (for example, typo fixes), or if an issue already exists,
       you can skip this step.

.. note::
   In order to keep the commit history intact, please avoid squashing or amending
   history and then force-pushing to the PR. Reviewers often want to look at
   individual commits.

.. _Clear communication: https://opensource.guide/how-to-contribute/#how-to-submit-a-contribution
.. _Open Source: https://opensource.guide/
.. _create an issue: https://github.com/python/cpython/issues
.. _CPython: https://github.com/python/cpython
.. _use HTTPS: https://help.github.com/articles/which-remote-url-should-i-use/
.. _Create Pull Request: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
.. _comments on your Pull Request: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request


.. _pullrequest-steps:

Step-by-step guide
==================

You should have already :ref:`set up your system <setup>`,
:ref:`got the source code <checkout>`, and :ref:`built Python <compiling>`.

* Update data from your ``upstream`` repository::

     git fetch upstream

* Create a new branch in your local clone from the ``main`` branch
  in the upstream repository::

     git checkout -b <branch-name> upstream/main

  .. note::
     Almost all changes to Python, including bug fixes, should first be
     made against the ``main`` branch. See :ref:`here <good-prs>` for
     more details.

* Make changes to the code, and use ``git status`` and ``git diff`` to see them.

  (Learn more about :ref:`good-prs`)

* Make sure the changes are fine and don't cause any test failure::

     make patchcheck
     ./python -m test

  (Learn more about :ref:`patchcheck` and about :ref:`runtests`)

* Once you are satisfied with the changes, add the files and commit them::

     git add <filenames>
     git commit -m '<message>'

  (Learn more about :ref:`good-commits`)

* If your code isn't linted correctly, :ref:`pre-commit <install-pre-commit>`
  will block the commit with an error message, for example::

     Doc/library/stdtypes.rst:5718: No newline at end of file. (missing-final-newline)

* Once all linting errors have been fixed, you can push your work to your GitHub fork::

     git push origin <branch-name>

* Finally go on :samp:`https://github.com/{<your-username>}/cpython`: you will
  see a box with the branch you just pushed and a green button that allows
  you to create a pull request against the official CPython repository.

* When people start adding review comments, you can address them by switching
  to your branch, making more changes, committing them, and pushing them to
  automatically update your PR::

   git switch <branch-name>
   # make changes and run tests
   git add <filenames>
   git commit -m '<message>'
   git push origin <branch-name>

  * If a core developer reviewing your PR pushed one or more commits to your
    PR branch, then after checking out your branch and before editing, run::

     git pull origin <branch-name>  # pull = fetch + merge

    If you have made local changes that have not been pushed to your fork and
    there are merge conflicts, Git will warn you about this and enter conflict
    resolution mode. See :ref:`resolving-merge-conflicts` below.

* If time passes and there are merge conflicts with the main branch, GitHub
  will show a warning to this end and you may be asked to address this. Merge
  the changes from the main branch while resolving the conflicts locally::

   git switch <branch-name>
   git pull upstream main  # pull = fetch + merge
   # resolve conflicts: see "Resolving Merge Conflicts" below
   git push origin <branch-name>

* After your PR has been accepted and merged, you can :ref:`delete the branch
  <deleting_branches>`::

     git branch -D <branch-name>  # delete local branch
     git push origin -d <branch-name>  # delete remote branch

.. _resolving-merge-conflicts:

Resolving merge conflicts
-------------------------

When merging changes from different branches (or variants of a branch on
different repos), the two branches may contain incompatible changes to one
or more files. These are called "merge conflicts" and need to be manually
resolved as follows:

#. Check which files have merge conflicts::

      git status

#. Edit the affected files and bring them to their intended final state.
   Make sure to remove the special "conflict markers" inserted by Git.

#. Commit the affected files::

      git add <filenames>
      git merge --continue

When running the final command, Git may open an editor for writing a commit
message. It is usually okay to leave that as-is and close the editor.

See `the merge command's documentation <https://git-scm.com/docs/git-merge>`_
for a detailed technical explanation.

.. _good-prs:

Making Good PRs
===============

When creating a pull request, following best practices ensures your contribution is **clear, maintainable, and easy to review**. A well-structured PR improves collaboration and speeds up the review process.

1. **Use a Clear and Structured PR Title**

   PR titles often become commit messages, making them **critical for maintainability and searchability**. Follow these guidelines:

    **Do:**

   - Clearly summarize the change in a concise manner.
   - Use the **imperative mood** (e.g., "Fix crash in parser" instead of "Fixed a crash in parser").
   - Be specific about what is being changed (avoid vague words like "Update" or "Fix").

   **Example of a good PR title:**

   ``gh-128002: Simplify all_tasks to use PyList_Extend instead of manual iteration``

#. **Write a detailed description**

   Your PR description should provide **clear context** for reviewers. Answer the following questions:

   - What does this PR do?
   - **Why is this change necessary?**
   - **Are there any breaking changes?**
   - **Does this PR fix any open issues?** (Reference issue numbers if applicable)

   Providing detailed descriptions makes the review process **faster and more efficient**.

3. **Make Your Change Against the Right Branch**

   Ensure your PR is based on the correct branch:

   - **New changes should target the** ``main`` **branch unless they are specific to an older version.**
   - If a change affects older versions, it will be **backported** after merging.
   - Only use **maintenance branches** when the change does not apply to ``main`` or requires a different approach.

   Refer to :ref:`branch-merge` for more details on how backporting works.

4. **Follow Python's Style Guidelines**

   - Python code should follow :PEP:`8`, and C code should follow :PEP:`7`.
   - Maintainers may **fix minor style issues**, but major deviations can **delay or block merging**.
   - PRs with **only style changes** are usually rejected unless they fix a formatting error.

   .. note::
      Fixes for typos and grammar errors in documentation and docstrings are always welcome.

5. **Consider Backward Compatibility**

   - Changes should **not break existing code** unless absolutely necessary.
   - When introducing **new arguments**, provide **default values** to maintain existing behavior.
   - If unsure, refer to :PEP:`387` or discuss the issue with experienced maintainers in :ref:`communication`.

   Think about how your change affects existing users before submitting your PR.

6. **Ensure Proper Testing**

   - Every PR should include **appropriate test cases** to validate the changes.
   - PRs without tests **will not be accepted** unless they are purely documentation changes.
   - Tests should **cover edge cases** and expected behaviors.
   - For bug fixes, add a test that **fails without the fix** and **passes after applying it**.

#. **Ensure all tests pass**

   - The entire test suite must **run without failures** before submission.
   - Run ``make test`` or refer to :ref:`runtests` to check for test failures.
   - Do not submit PRs with failing tests unless the failure is **directly related** to your change.

8. **Keep Documentation Up to Date**

   - Any change affecting functionality should include relevant **documentation updates**.
   - Follow :ref:`documenting` guidelines to ensure consistency in documentation.

   Keeping documentation updated ensures clarity for future contributors and users.

By following these best practices, you increase the likelihood of your PR being **reviewed and merged**!


Copyrights
==========

Copyright notices are optional and informational, as international treaties
have abolished the requirement for them to protect copyrights.
However, they still serve an informative role.

According to the US Copyright Office, valid copyright notices include the year
of first publication of the work. For example:

   Copyright (C) 2001 Python Software Foundation.

Updating notices to add subsequent years is unnecessary and such PRs will be
closed.

See also `python/cpython#126133
<https://github.com/python/cpython/issues/126133#issuecomment-2460824052>`__.


.. _patchcheck:

``patchcheck``
==============

``patchcheck`` is a simple automated checklist for changes in progress that
guides a developer through common checks. To run ``patchcheck``:

On *Unix* (including macOS)::

   make patchcheck

On *Windows* (after any successful build):

.. code-block:: dosbatch

   .\python.bat Tools\patchcheck\patchcheck.py

The automated checklist runs through:

* Are there any whitespace problems in Python files?
  (using :cpy-file:`Tools/patchcheck/reindent.py`)
* Are there any whitespace problems in C files?
* Are there any whitespace problems in the documentation?
* Has the documentation been updated?
* Has the test suite been updated?
* Has an entry under ``Misc/NEWS.d/next`` been added?
  (using `blurb-it <https://blurb-it.herokuapp.com/>`_,
  or the :pypi:`blurb` tool)
* Has ``Misc/ACKS`` been updated?
* Has ``configure`` been regenerated, if necessary?
* Has ``pyconfig.h.in`` been regenerated, if necessary?

The automated checks don't actually *answer* all of these
questions. Aside from the whitespace checks, the tool is
a memory aid for the various elements that can go into
making a complete pull request.


.. _good-commits:

Making good commits
===================

Each feature or bugfix should be addressed by a single pull request,
and for each pull request there may be several commits.  In particular:

* Do **not** fix more than one issue in the same commit (except,
  of course, if one code change fixes all of them).
* Do **not** do cosmetic changes to unrelated code in the same
  commit as some feature/bugfix.

Commit messages should follow the following structure::

   Make the spam module more spammy

   The spam module sporadically came up short on spam. This change
   raises the amount of spam in the module by making it more spammy.

The first line or sentence is meant to be a dense, to-the-point explanation
of what the purpose of the commit is. The imperative form (used in the example
above) is strongly preferred to a descriptive form such as 'the spam module is
now more spammy'. Use ``git log --oneline`` to see existing title lines.
Furthermore, the first line should not end in a period.

If this is not enough detail for a commit, a new paragraph(s) can be added
to explain in proper depth what has happened (detail should be good enough
that a core developer reading the commit message understands the
justification for the change).

Check :ref:`the Git bootcamp <accepting-and-merging-a-pr>` for further
instructions on how the commit message should look like when merging a pull
request.

.. note::
   `How to Write a Git Commit Message <https://cbea.ms/git-commit/>`_
   is a nice article that describes how to write a good commit message.


.. _cla:

Licensing
=========

To accept your change we must have your formal approval for distributing
your work under the `PSF license`_.  Therefore, you need to sign a
`contributor agreement`_ which allows the `Python Software Foundation`_ to
license your code for use with Python (you retain the copyright).

.. note::
   You only have to sign this document once, it will then apply to all
   your further contributions to Python.

Here are the steps needed in order to sign the CLA:

1. Create a change and submit it as a pull request.

2. When ``cpython-cla-bot`` comments on your pull request that commit
   authors are required to sign a Contributor License Agreement, click
   on the button in the comment to sign it. It's enough to log in through
   GitHub. The process is automatic.

3. After signing, the comment by ``cpython-cla-bot`` will update to
   indicate that "all commit authors signed the Contributor License
   Agreement.

.. _PSF license: https://docs.python.org/dev/license.html#terms-and-conditions-for-accessing-or-otherwise-using-python
.. _contributor agreement: https://www.python.org/psf/contrib/
.. _contributor form: https://www.python.org/psf/contrib/contrib-form/
.. _Python Software Foundation: https://www.python.org/psf-landing/


Submitting
==========

Once you are satisfied with your work you will want to commit your
changes to your branch. In general you can run ``git commit -a`` and
that will commit everything. You can always run ``git status`` to see
what changes are outstanding.

When all of your changes are committed (that is, ``git status`` doesn't
list anything), you will want to push your branch to your fork::

  git push origin <branch name>

This will get your changes up to GitHub.

Now you want to
`create a pull request from your fork
<https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork>`_.
If this is a pull request in response to a pre-existing issue on the
`issue tracker`_, please make sure to reference the issue number using
``gh-NNNNN:`` prefix in the pull request title and ``#NNNNN`` in the description.

If this is a pull request for an unreported issue (assuming you already
performed a search on the issue tracker for a pre-existing issue), create a
new issue and reference it in the pull request. Please fill in as much
relevant detail as possible to prevent reviewers from having to delay
reviewing your pull request because of lack of information.

If this issue is so simple that there's no need for an issue to track
any discussion of what the pull request is trying to solve (for example, fixing a
spelling mistake), then the pull request needs to have the "skip issue" label
added to it by someone with commit access.

Your pull request may involve several commits as a result of addressing code
review comments.  Please keep the commit history in the pull request intact by
not squashing, amending, or anything that would require a force push to GitHub.
A detailed commit history allows reviewers to view the diff of one commit to
another so they can easily verify whether their comments have been addressed.
The commits will be squashed when the pull request is merged.


Converting an existing patch from b.p.o to GitHub
=================================================

When a patch exists in the `issue tracker`_ that should be converted into a
GitHub pull request, please first ask the original patch author to prepare
their own pull request. If the author does not respond after a week, it is
acceptable for another contributor to prepare the pull request based on the
existing patch. In this case, both parties should sign the :ref:`CLA <cla>`.
When creating a pull request based on another person's patch, provide
attribution to the original patch author by adding "Co-authored-by:
Author Name <email_address> ." to the pull request description and commit message.
See `the GitHub article <https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors>`_
on how to properly add the co-author info.

See also :ref:`Applying a Patch to Git <git_from_patch>`.


.. _reviewing-prs:

Reviewing
=========

To begin with, please be patient! There are many more people
submitting pull requests than there are people capable of reviewing
your pull request. Getting your pull request reviewed requires a
reviewer to have the spare time and motivation to look at your pull
request (we cannot force anyone to review pull requests and no one is
employed to look at pull requests). If your pull request has not
received any notice from reviewers (that is, no comment made) after one
month, first "ping" the issue on the `issue tracker`_ to remind the
subscribers that the pull request needs a review.
If you don't get a response within a week after pinging the issue,
you can post on the `Core Development Discourse category`_
to ask for someone to review your pull request.

When someone does manage to find the time to look at your pull request
they will most likely make comments about how it can be improved
(don't worry, even core developers of Python have their pull requests sent
back to them for changes).  It is then expected that you update your
pull request to address these comments, and the review process will
thus iterate until a satisfactory solution has emerged.

.. _how-to-review-a-pull-request:

How to review a pull request
----------------------------

One of the bottlenecks in the Python development
process is the lack of code reviews.
If you browse the bug tracker, you will see that numerous issues
have a fix, but cannot be merged into the main source code repository,
because no one has reviewed the proposed solution.
Reviewing a pull request can be just as informative as providing a
pull request and it will allow you to give constructive comments on
another developer's work. This guide provides a checklist for
submitting a code review. It is a common misconception that in order
to be useful, a code review has to be perfect. This is not the case at
all! It is helpful to just test the pull request and/or play around with the
code and leave comments in the pull request or issue tracker.

1. If you have not already done so, get a copy of the CPython repository
   by following the :ref:`setup guide <setup>`, build it and run the tests.

2. Check the bug tracker to see what steps are necessary to reproduce
   the issue and confirm that you can reproduce the issue in your version
   of the Python REPL (the interactive shell prompt), which you can launch
   by executing ./python inside the repository.

3. Checkout and apply the pull request (Please refer to the instruction
   :ref:`git_pr`)

4. If the changes affect any C file, run the build again.

5. Launch the Python REPL (the interactive shell prompt) and check if
   you can reproduce the issue. Now that the pull request has been applied,
   the issue should be fixed (in theory, but mistakes do happen! A good review
   aims to catch these before the code is merged into the Python repository).
   You should also try to see if there are any corner cases in this or related
   issues that the author of the fix may have missed.

6. If you have time, run the entire test suite. If you are pressed for time,
   run the tests for the module(s) where changes were applied.
   However, please be aware that if you are recommending a pull request as
   'merge-ready', you should always make sure the entire test suite passes.

Leaving a pull request review on GitHub
---------------------------------------

When you review a pull request, you should provide additional details and context
of your review process.

Instead of simply "approving" the pull request, leave comments.  For example:

#. If you tested the PR, report the result and the system and version tested on,
   such as 'Windows 10', 'Ubuntu 16.4', or 'Mac High Sierra'.

#. If you request changes, try to suggest how.

#. Comment on what is "good" about the pull request, not just the "bad". Doing
   so will make it easier for the PR author to find the good in your comments.

#. Look at any failures in CI on the current PR. See :ref:`"Keeping CI green"
   <keeping-ci-green>` below for simple things you can do to help move the PR forward.

Dismissing review from another core developer
---------------------------------------------

A core developer can dismiss another core developer's review if they confirmed
that the requested changes have been made.  When a core developer has assigned
the PR to themselves, then it is a sign that they are actively looking after
the PR, and their review should not be dismissed.

.. _keeping-ci-green:

Keeping continuous integration green
====================================

Our change management workflows generally won't allow merging PRs with
failures. Therefore, if you see a CI failure on a PR, have a look
what it is about.

Usually the failure will be directly related to the changes in the current
PR. If you happen to have any insight into the failure, let the author know
in a review comment. CI runs sometimes generate thousands of lines of output.
Even something as simple as finding the traceback and putting it in the
comment will be helpful to the PR author.

If the failure doesn't look related to the change you're looking at, check
if it's not present on the `Release Status`_ Buildbot dashboard as well.
If so, that means the failure was introduced in a prior change. Using Buildbot's
UI you can find which PR introduced the issue and comment that it
affects other PRs.

If you still don't see where the failure originates from, check for
a "This branch is out-of-date with the base branch" sign next to the
list of executed checks. Clicking "Update branch" next to this message
will merge in the latest changes from the base branch into the PR.

If this still doesn't help with the failure on the PR, you can try
to re-run that particular failed check. Go to the red GitHub Action job,
click on the :guilabel:`Re-run jobs` button on the top right, and select
:guilabel:`Re-run failed jobs`. The button will only be present when all other
jobs finished running.

Re-running failed jobs shouldn't be your first instinct but it is occasionally
helpful because distributed systems can have intermittent failures, and
some of our unit tests are sensitive to overloaded virtual machines.
If you identify such flaky behavior, look for an issue in the `issue tracker`_
that describes this particular flakiness. Create a new issue if you can't
find one.

:guilabel:`Update branch` button
================================

You can click on the :guilabel:`Update branch` button to merge the latest
changes from the base branch (usually ``main``) into the PR.
This is useful to :ref:`keep the CI green <keeping-ci-green>` for old PRs,
or to check if a CI failure has been fixed in the base branch.

If the PR is very old, it may be useful to update the branch before merging to
ensure that the PR does not fail any CI checks that were added or changed since
CI last ran.

Do not click :guilabel:`Update branch` without a good reason because it notifies
everyone watching the PR that there are new changes, when there are not,
and it uses up limited CI resources.

Committing/rejecting
====================

Once your pull request has reached an acceptable state (and thus considered
"accepted"), it will either be merged or rejected. If it is rejected, please
do not take it personally! Your work is still appreciated regardless of whether
your pull request is merged. Balancing what *does* and *does not* go into
Python is tricky and we simply cannot accept everyone's contributions.

But if your pull request is merged it will then go into Python's
:abbr:`VCS (version control system)` to be released
with the next feature release of Python. It may also be backported to older
versions of Python as a bugfix if the core developer doing the merge believes
it is warranted.


Crediting
=========

Non-trivial contributions are credited in the ``Misc/ACKS`` file (and, most
often, in a contribution's news entry as well).  You may be
asked to make these edits on the behalf of the core developer who
accepts your pull request.

.. _issue tracker: https://github.com/python/cpython/issues
.. _Core Development Discourse category: https://discuss.python.org/c/core-dev/23
.. _Release Status: https://buildbot.python.org/all/#/release_status
