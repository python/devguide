.. _committing:

Accepting pull requests
=======================

.. highlight:: none

This page is a step-by-step guide for core developers who need to assess,
merge, and possibly backport a pull request on the main repository.

Assessing a pull request
------------------------

Before you can accept a pull request, you need to make sure that it is ready
to enter the public source tree. Ask yourself the following questions:

* **Are there ongoing discussions at the issue tracker?**
   Read the linked issue. If there are ongoing discussions, then
   we need to have a resolution there before we can merge the pull request.

* **Was the pull request first made against the appropriate branch?**
   The only branch that receives new features is ``main``, the
   in-development branch. Pull requests should only target bug-fix branches
   if an issue appears in only that version and possibly older versions.

* **Are the changes acceptable?**
   If you want to share your work-in-progress code on a feature or bugfix,
   then you can open a ``WIP``-prefixed pull request, publish patches on
   the `issue tracker`_, or create a public fork of the repository.

* **Do the checks on the pull request show that the test suite passes?**
   Make sure that all of the status checks are passing.

* **Is the pull request in a good state?**
   Check :ref:`pull-request-lifecycle` and :ref:`helptriage` to review what
   is expected of a pull request.

* **Does the change break backwards-compatibility without a strong reason?**
   :ref:`Run the entire test suite <runtests>` to make sure that everything
   still passes. If there is a change to the semantics, then there needs to
   be a strong reason, because it will cause some peoples' code to break.
   If you are unsure if the breakage is worth it, then ask
   on the `Core Development Discourse category
   <https://discuss.python.org/c/core-dev/23>`__.

* **Does documentation need to be updated?**
   If the pull request introduces backwards-incompatible changes (for example,
   deprecating or removing a feature), then make sure that those changes
   are reflected in the documentation before you merge the pull request.

* **Were appropriate labels added to signify necessary backporting of the pull request?**
   If it is determined that a pull request needs to be
   backported into one or more of the maintenance branches, then a core
   developer can apply the label ``needs backport to X.Y`` to the pull
   request. Once the backport pull request has been created, remove the
   ``needs backport to X.Y`` label from the original pull request. (Only
   core developers and members of the :ref:`Python Triage Team <triage-team>`
   can apply labels to GitHub pull requests).

* **Does the pull request pass a check indicating that the submitter has signed the CLA?**
   Make sure that the contributor has signed a `Contributor
   Licensing Agreement <https://www.python.org/psf/contrib/contrib-form/>`_
   (CLA), unless their change has no possible intellectual property
   associated with it (for example, fixing a spelling mistake in documentation).
   The `CPython CLA Bot <https://github.com/apps/cpython-cla-bot/>`_
   checks whether the author has signed the CLA, and replies in the PR
   if they haven't. For further questions about the CLA
   process, write to contributors@python.org.

* **Were** ``What's New in Python`` **and** ``Misc/NEWS.d/next`` **updated?**
   If the change is particularly interesting for end users (for example, new features,
   significant improvements, or backwards-incompatible changes), then an
   entry in the ``What's New in Python`` document (in ``Doc/whatsnew/``) should
   be added as well. Changes that affect only documentation generally do not
   require a ``NEWS`` entry. (See :ref:`what-s-new-and-news-entries`.)


Working with Git_
-----------------

.. seealso::
   :ref:`gitbootcamp`

As a core developer, you have the ability to push changes to the official
Python repositories, so you need to be careful with your workflow:

* **You should not push new branches to the main repository.**  You can
  still use them in the fork that you use for your own development.
  You can also push these branches to a separate public repository
  for maintenance work before it is integrated into the main repository.

* **You should not commit directly into the** ``main`` **branch, or any of the maintenance branches.**
  You should commit against your own feature branch, and then create a
  pull request.

* **For a small change, you can make a quick edit through the GitHub web UI.**
  If you choose to use the web UI, be aware that GitHub will
  create a new branch in the main CPython repository rather than in your fork.
  Delete this newly created branch after it has been merged into the
  ``main`` branch or any of the maintenance branches. To keep the CPython
  repository tidy, remove the new branch within a few days.

Keep a fork of the main repository, since it will allow you to revert all
local changes (even committed ones) if you're not happy with your local
clone.


.. _Git: https://git-scm.com/


.. _committing-active-branches:

Seeing active branches
^^^^^^^^^^^^^^^^^^^^^^

If you use ``git branch``, then you will see a :ref:`list of branches
<branchstatus>`. The only branch that receives new features is
``main``, the in-development branch. The other branches receive only
bug fixes or security fixes. In almost all cases the fixes should first
originate on ``main`` and then be ported back to older branches.


.. _branch-merge:

Backporting changes to an older version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If it is determined that a pull request needs to be backported into one or
more of the maintenance branches, then a core developer can apply the label
``needs backport to X.Y`` to the pull request.

After the pull request has been merged, miss-islington (bot) will first try to
do the backport automatically. If miss-islington is unable to do it,
then the pull request author or the core developer who merged it should look into
backporting it themselves, using the backport generated by cherry_picker.py_
as a starting point.

You can get the commit hash from the original pull request, or you can use
``git log`` on the ``main`` branch. To display the 10 most recent commit
hashes and their first line of the commit, use the following command::

   git log -10 --oneline

.. _backport-pr-title:

You can prefix the backport pull request with the branch, and reference
the pull request number from ``main``. Here is an example::

   [3.9] gh-12345: Fix the Spam Module (GH-NNNN)

Here "gh-12345" is the GitHub *issue* number, and "GH-NNNN" is the
number of the original *pull request*.
Note that cherry_picker.py_ adds the branch prefix automatically.

Once the backport pull request has been created, remove the
``needs backport to X.Y`` label from the original pull request. (Only
core developers and members of the :ref:`Python Triage Team <triage-team>`
can apply labels to GitHub pull requests).

.. _cherry_picker.py: https://github.com/python/cherry-picker


Reverting a merged pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To revert a merged pull request, press the :guilabel:`Revert` button at the
bottom of the pull request. That will bring up the page to create a
new pull request where the commit can be reverted. It will also create
a new branch on the main CPython repository. Delete the branch once
the pull request has been merged.

Always include the reason for reverting the commit to help others
understand why it was done. The reason should be included as part of
the commit message. Here is an example::

   Revert gh-NNNN: Fix Spam Module (GH-111)

   Reverts python/cpython#111.
   Reason: This commit broke the buildbot.

.. _issue tracker: https://github.com/python/cpython/issues
