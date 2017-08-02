.. highlight:: console

.. _gitbootcamp:

Git Bootcamp and Cheat Sheet
============================

In this section, we'll go over some commonly used Git commands that are
relevant to CPython's workflow.

.. contents::


Forking CPython GitHub Repository
---------------------------------

You'll only need to do this once.

1. Go to https://github.com/python/cpython.

2. Press ``Fork`` on the top right.

3. When asked where to fork the repository, choose to fork it to your username.

4. Your fork will be created at https://github.com/<username>/cpython.


Cloning The Forked CPython Repository
-------------------------------------

You'll only need to do this once.  From your command line::

   $ git clone git@github.com:<username>/cpython.git
   $ cd cpython
   $ git remote add upstream git@github.com:python/cpython.git


Listing the Remote Repositories
-------------------------------

To list the remote repositories that are configured, along with their urls::

   $ git remote -v


Creating and Switching Branches
-------------------------------

.. note::
   Never commit directly to the ``master`` branch.

Create a new branch and switch to it::

   # creates a new branch off master and switch to it
   $ git checkout -b <branch-name> master

This is equivalent to::

   # create a new branch off 'master', without checking it out
   $ git branch <branch-name> master
   # check out the branch
   $ git checkout <branch-name>

To find the branch you are currently on::

   $ git branch

The current branch will have an asterisk next to the branch name.  Note, this
will only list all of your local branches.

To list all the branches, including the remote branches::

   $ git branch -a

To switch to a different branch::

   $ git checkout <another-branch-name>

Other releases are just branches in the repository.  For example, to work
on the 2.7 release::

   $ git checkout -b 2.7 origin/2.7


Deleting Local Branches
-----------------------

To delete a branch that you no longer need::

   $ git branch -D <branch-name>

You may specify more than one branch for deletion.


Staging and Committing Files
----------------------------

1. To show the current changes::

      $ git status

2. To stage the files to be included in your commit::

      $ git add path/to/file1 path/to/file2 path/to/file3

3. To commit the files that have been staged (done in step 2)::

      $ git commit -m "bpo-XXXX: This is the commit message."


Reverting Changes
-----------------

To revert changes to a file that has not been committed yet::

   $ git checkout path/to/file

If the change has been committed, and now you want to reset it to whatever
the origin is at::

   $ git reset --hard HEAD


Stashing Changes
----------------

To stash away changes that are not ready to be committed yet::

   $ git stash

To re-apply the last stashed change::

   $ git stash pop


Pushing Changes
---------------

Once your changes are ready for a review or a pull request, you'll need to push
them to the remote repository.

::

   $ git checkout <branch-name>
   $ git push origin <branch-name>


Creating a Pull Request
-----------------------

1. Go to https://github.com/python/cpython.

2. Press ``New pull request`` button.

3. Click ``compare across forks`` link.

4. Select the base fork: ``python/cpython`` and base branch: ``master``.

5. Select the head fork: ``<username>/cpython`` and base branch: the branch
   containing your changes.

6. Press ``Create Pull Request`` button.


Syncing With Upstream
---------------------

Scenario:

- You forked the CPython repository some time ago.
- Time passes.
- There have been new commits made in upstream CPython repository.
- Your forked CPython repository is no longer up to date.
- You now want to update your forked CPython repository to be the same as
  upstream.

Solution::

   $ git checkout master
   $ git pull --rebase upstream master
   $ git push origin master

The ``--rebase`` option is only needed if you have local changes to the
branch.

Another scenario:

- You created ``some-branch`` some time ago.
- Time passes.
- You made some commits to ``some-branch``.
- Meanwhile, there are recent changes from upstream CPython repository.
- You want to incorporate the recent changes from upstream into ``some-branch``.

Solution::

   $ git checkout some-branch
   $ git fetch upstream
   $ git rebase upstream/master
   $ git push --force origin some-branch


Backporting Merged Changes
--------------------------

A pull request may need to be backported into one of the maintenance branches
after it has been accepted and merged into ``master``.  It is usually indicated
by the label ``needs backport to X.Y`` on the pull request itself.

Use the utility script `cherry_picker.py <https://github.com/python/core-workflow/tree/master/cherry_picker>`_
from the `core-workflow  <https://github.com/python/core-workflow>`_
repository to backport the commit.


.. _git_from_mercurial:

Applying a Patch from Mercurial to Git
--------------------------------------

Scenario:

- A Mercurial patch exists but there is no pull request for it.

Solution:

1. Download the patch locally.

2. Apply the patch::

       $ git apply /path/to/issueNNNN-git.patch

   If there are errors, update to a revision from when the patch was
   created and then try the ``git apply`` again::

       $ git checkout `git rev-list -n 1 --before="yyyy-mm-dd hh:mm:ss" master`
       $ git apply /path/to/issueNNNN-git.patch

   If the patch still won't apply, then a patch tool will not be able to
   apply the patch and it will need to be re-implemented manually.

3. If the apply was successful, create a new branch and switch to it.

4. Stage and commit the changes.

5. If the patch was applied to an old revision, it needs to be updated and
   merge conflicts need to be resolved::

       $ git rebase master
       $ git mergetool

6. Push the changes and open a pull request.



.. _git_pr:

Downloading Other's Patches
---------------------------

Scenario:

- A contributor made a pull request to CPython.
- Before merging it, you want to be able to test their changes locally.

On Unix and MacOS, set up the following git alias::

   $ git config --global alias.pr '!sh -c "git fetch upstream pull/${1}/head:pr_${1} && git checkout pr_${1}" -'

On Windows, reverse the single (`'`) and double (`"`) quotes::

   git config --global alias.pr "!sh -c 'git fetch upstream pull/${1}/head:pr_${1} && git checkout pr_${1}' -"

The alias only needs to be done once.  After the alias is set up, you can get a
local copy of a pull request as follows::

   $ git pr <pr_number>


Accepting and Merging A Pull Request
------------------------------------

Pull requests can be accepted and merged by a Python Core Developer.

1. At the bottom of the pull request page, click the ``Squash and merge``
   button.

2. Adjust and clean up the commit message.  Replace the reference
   to GitHub PR #XXX into GH-XXX.

   Example of good commit message::

      bpo-12345: Improve the spam module (GH-777)

      * Add method A to the spam module
      * Update the documentation of the spam module

   Example of bad commit message::

      bpo-12345: Improve the spam module (#777)

      * Improve the spam module
      * merge from master
      * adjust code based on review comment
      * rebased

3. Press the ``Confirm squash and merge`` button.


Editing a Pull Request Prior to Merging
---------------------------------------

When a pull request submitter has enabled the `Allow edits from maintainers`_
option, Python Core Developers may decide to make any remaining edits needed
prior to merging themselves, rather than asking the submitter to do them. This
can be particularly appropriate when the remaining changes are bookkeeping
items like updating ``Misc/ACKS``.

.. _Allow edits from maintainers: https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/

To edit an open pull request that targets ``master``:

1. In the pull request page, under the description, there is some information
   about the contributor's fork and branch name that will be useful later::

      <contributor> wants to merge 1 commit into python:master from <contributor>:<branch_name>

2. Fetch the pull request, using the :ref:`git pr <git_pr>` alias::

      $ git pr <pr_number>

   This will checkout the contributor's branch at ``pr_XXX``.

3. Make and commit your changes on the branch.  For example, merge in changes
   made to ``master`` since the PR was submitted (any merge commits will be
   removed by the later ``Squash and Merge`` when accepting the change)::

      $ git fetch upstream
      $ git merge upstream/master
      $ git add <filename>
      $ git commit -m "<commit message>"

4. Push the changes back to the contributor's PR branch::

      $ git push git@github.com:<contributor>/cpython <pr_XXX>:<branch_name>

5. Optionally, delete the local PR branch::

      $ git checkout master
      $ git branch -D <pr_XXX>
