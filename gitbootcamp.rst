.. _gitbootcamp:

Git Bootcamp and Cheat Sheet
============================

In this section, we'll go over some commonly used git commands that are
relevant to CPython's workflow.

.. contents::


Forking CPython GitHub Repository
---------------------------------

You'll only need to do this once.

1. Go to https://github.com/python/cpython.

2. Press ``Fork``.

3. When asked where to fork the repository, choose to fork it to your username.

4. A fork will be created at https://github.com/<username>/cpython.


Cloning The Forked CPython Repository
-------------------------------------

From your command line::

   $ git clone git@github.com:<username>/cpython.git
   $ cd cpython
   $ git remote add upstream git@github.com:python/cpython.git


Listing the Remote Repositories
-------------------------------

::

   $ git remote -v


Creating and Switching Branches
-------------------------------

.. note::
   Never commit directly to the ``master`` branch.

Create a new branch::

   $ git checkout -b some-branch master # creates a new branch off master

which is equal to::

   $ git branch some-branch master # create 'some-branch' off 'master', without checking it out
   $ git checkout some-branch # check out 'some-branch'

To find out which branch you are in now::

   $ git branch

The current branch will have an asterisk next to the branch name.  Note, this
will list all of your local branches.

To list all the branches, including the remote branches::

   $ git branch -a

To switch to a different branch::

   $ git checkout another-branch-name


Delete Local Branch
-------------------

To delete branch that you no longer need::

   $ git branch -D branch-to-delete


Staging and Committing Files
----------------------------

1. To show the current changes::

      $ git status

2. To stage the files to be included in your commit::

      $ git add /path/to/file1 path/to/file2 path/to/file3

3. To commit the files that have been staged (done in step 2)::

      $ git commit -m "This is the commit message. Prefix it with bpo-XXXX."


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

To re-apply last stashed change::

   $ git stash pop


Pushing Changes
---------------

Once your changes are ready for a review or a pull request, you'll need to push
them to the remote repository.

::

   $ git checkout some-branch
   $ git push origin some-branch


Creating a Pull Request
-----------------------

1. Go to https://github.com/python/cpython.

2. Click ``compare across forks`` link.

3. Select the base fork: ``python/cpython`` and base branch: ``master``

4. Select the head fork: ``<username>/cpython`` and base branch: the branch
   containing your changes.

5. Press ``Create Pull Request`` button.


Syncing With Upstream
---------------------

Scenario:

- You forked cpython repository some time ago.
- Time passes.
- There have been new commits made in upstream cpython repository.
- Your forked cpython repository is no longer up to date.
- You now want to update your forked cpython repository to be the same as
  upstream.

Solution::

   $ git checkout master
   $ git pull --rebase upstream master
   $ git push origin master

The `--rebase` is only needed if you have local changes to the branch.

Another scenario:

- You created ``some-branch`` some time ago.
- Time passes.
- You made some commits to ``some-branch``.
- Meanwhile, there are recent changes from upstream cpython repository.
- You want to incorporate the recent changes from upstream into ``some-branch``.

Solution::

   $ git checkout some-branch
   $ git fetch upstream
   $ git rebase upstream/master


Backporting Merged Changes
--------------------------

When a pull request has been merged to master, and it needs to be backported
into one of the maintenance branches.

First, obtain the commit sha1 from the merged pull request:

1. Go to the merged pull request page, for example::

     https://github.com/python/cpython/pull/PR-ID

2. Scroll down and find the activity that says something like::

     SomeUser merged commit <hash> into python:master ...

3. Follow the link to <hash>.

4. Copy the complete hash value.

The commit hash will be used below.

To backport the commit to 3.6::

   $ git fetch upstream
   $ git checkout -b backport-someissue-3.6 upstream/3.6
   $ git cherry-pick -x hashvalue
   $ git push origin backport-someissue-3.6

Go to https://github.com/python/cpython to create the pull request.  Select
``3.6`` as the base branch, and ``backport-someissue-3.6`` as the head branch.


Downloading Other's Patches
---------------------------

Scenario:

- A contributor made a pull request to cpython.
- Before merging it, you want to be able to test their changes locally.

Set up the following git alias::

   $ git config --global alias.pr '!sh -c "git fetch upstream pull/${1}/head:pr_${1} && git checkout pr_${1}" -'

The alias only needs to be done once.  After the alias is set up, you can get a
local copy of a pull request as follows::

   $ git pr <pr_number>

For example, to fetch and checkout pull request #777::

   $ git pr 777


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
