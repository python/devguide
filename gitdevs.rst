:tocdepth: 4

.. highlight:: bash
.. _gitdevs:

Mercurial for git developers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. contents::
   :local:


Overview
========

This guide is geared towards prospective contributors who are accustomed to
git-based development. The intention of this guide is to lower the initial
barrier of entry for prospective contributors in learning a new source control
tool. While there are projects that focus on automating this to allow seamless
bridges between the two systems, this guide focusses solely on native Mercurial
functionality. As with most tools, this is not the only method of achieving
git-like workflows with Mercurial. It is intended solely to provide one
potential path.

Note that this geared towards prospective contributors and the patch workflow.
Core developers will have a similar workflow, but it will differ in the later
stages (merge vs patch generation).

The workflow that will be used as the case study for this guide is as follows:

* Clone CPython
* Find/Create issue in the issue tracker (issueA)

  - Work on issue
  - Submit patch for review

* Work on another issue (issueB)

  - Work on issue
  - Commit work in progress

* Address review comments (issueA)

  - Commit work
  - Submit patch for review

* Continue feature work (issueB)
* *Rinse and repeat*


Git workflow
============

With the above workflow in mind, simplified steps using git may look like
this::

    git clone git@github.com:python/cpython.git

    # work on issueA
    git checkout -b issueA
    git commit -a

    # start working on issueB
    git checkout master
    git checkout -b issueB
    git commit -a

    # address review comments
    git checkout issueA
    git commit -a

    # optionally rebase work
    git pull --rebase

    # generate patch for submission
    git diff master..issueA > issueA.patch

    # continue working on issueB
    git checkout issueB


This flow will be used as the base for comparison against Mercurial usage that
aims to achieve a similar, if not identical, workflow.


Main differences between git and hg
===================================

This section aims to list major differences that may be unexpected by a git
developer. While there are many differences between git and Mercurial, only
those that are immediately relevant to new users coming from git are examined.


Mercurial branches are global and permanent
-------------------------------------------

This means that if you create a named branch, it is intended to be long-lived:

    Mercurial branch names may be used for whatever reasons users want.
    However, a good rule of thumb is to use branch names sparingly and for
    rather longer lived concepts like "release branches" (rel-1, rel-2, etc)
    and rather not for short lived work of single developers.

    -- http://mercurial.selenic.com/wiki/Branch#Named_branches


If you routinely create short-lived branches for development work and then
delete them after they've been merged to master, this is something to be aware
of. You *can* still only push select branches to remotes, so it's not a
functional issue as far as the public repo goes.


Workflow options using Mercurial
--------------------------------

There are a number of paths that could be taken to achieve a sane development
workflow. Some of these are:


Named branches
''''''''''''''

    Mercurial supports giving names to branches, by using the branch name
    property of the changeset (see NamedBranches_). If no branch name was set,
    Mercurial assigns the branch name "default". So the name of the default
    branch in a repository is "default" (which, for example, is not displayed
    when doing a hg log).

    Unfortunately, as Mercurial named (and default) branches are global and
    permanent, they don't lend themselves well to local development workflows.


Queues
''''''

    The patch queue extension integrates quilt functionality into Mercurial.
    Changes are maintained as patches which are committed into Mercurial.
    Commits can be removed or reordered, and the underlying patch can be
    refreshed based on changes made in the working directory. The patch
    directory can also be placed under revision control, so you can have a
    separate history of changes made to your patches.

    While the mq extension can indeed achieve similar functionality, it's quite
    a different workflow than git and may be difficult to adapt to for those
    coming from git.


Bookmarks
'''''''''

    Bookmarks can be used as an alternative to NamedBranches_ for tracking
    multiple lines of development. Systems like Mercurial, CVS, and Subversion
    store their branch information as a permanent part of each commit. This
    is useful for future auditing of long-lived branches, as it's always
    possible to identify which branch a commit was introduced on. Git, by
    contrast, has "branches" that are not stored in history, which is useful
    for working with numerous short-lived feature branches, but makes future
    auditing impossible. Mercurial's bookmark feature is analogous to Git's
    branching scheme, but can also be used in conjunction with Mercurial's
    traditional named branches.

    Bookmarks are the feature that emulate git workflows most closely and will
    therefore be used throughout the remainder of this guide.


An introduction to Mercurial bookmarks
--------------------------------------

While the functionality may seem entirely analogous to git branches
at first, there are fundamental differences to be aware of:


Bookmarks are not git branches
''''''''''''''''''''''''''''''

Bookmarks are *not* lightweight Git branches. Bookmarks are simply named
references to commits that are automatically updated when new commits are made.
This, coupled with the creation of new branch heads when committing from a
previous commit provides a workflow similar to git branching, but the fact that
a new branch is *not* created is an important detail to be aware of. This will
be demonstrated in the `Mercurial workflow`_ section.


Bookmarks are local
'''''''''''''''''''

Mercurial bookmarks are intended for local
development and can be deleted with ease, whereas branches cannot.
Note that deleting a bookmark does not mean that the releated changesets
are also deleted. You must use the `strip extension`_ to do that. Bookmarks can
be published to a remote repo to be shared, but must explicitly be pushed (see
http://mercurial.selenic.com/wiki/Bookmarks#Working_with_remote_repositories
for details).

.. _`strip extension`: http://mercurial.selenic.com/wiki/StripExtension



Mercurial workflow
==================

The following details hg usage with the above git workflow in mind. The
changeset graphs are displayed using :code:`hg log -G -l [num_commits]`,
which can be tremendously useful when first starting to use hg in order
to help you understand through visuals what it is that hg does with the
branches.


Cloning
-------

Pulling the latest CPython code and looking at the current commits::

    hg clone https://hg.python.org/cpython

    @    changeset:   93654:bd97eab25c70
    |\   tag:         tip
    | |  parent:      93652:70163e18da87
    | |  parent:      93653:21257f916668
    | |  user:        Ned Deily <nad@example.com>
    | |  date:        Fri Nov 28 15:22:15 2014 -0800
    | |  summary:     Issue #16113: Also remove test_case_sha3_224_huge
    | |
    | o  changeset:   93653:21257f916668
    | |  branch:      3.4
    | |  parent:      93647:737355f61ba2
    | |  user:        Ned Deily <nad@example.com>
    | |  date:        Fri Nov 28 15:21:12 2014 -0800
    | |  summary:     Issue #16113: Also remove test_case_sha3_224_huge
    | |
    o |  changeset:   93652:70163e18da87
    | |  user:        Raymond Hettinger <python@rcn.com>
    | |  date:        Fri Nov 28 14:52:14 2014 -0800
    | |  summary:     Minor code cleanup.

*Note that in the above graph, `@` represents your current changeset*


Working on issueA
-----------------

Assuming you've found a bug logged against default tip (master head in git-speak),
create a bookmark, which automatically activates it::

    hg bookmark issueA

Now, the history graph should look like this::

    @    changeset:   93654:bd97eab25c70
    |\   bookmark:    issueA
    | |  tag:         tip
    | |  parent:      93652:70163e18da87
    | |  parent:      93653:21257f916668
    | |  user:        Ned Deily <nad@example.com>
    | |  date:        Fri Nov 28 15:22:15 2014 -0800
    | |  summary:     Issue #16113: Also remove test_case_sha3_224_huge
    | |
    | o  changeset:   93653:21257f916668
    | |  branch:      3.4
    | |  parent:      93647:737355f61ba2
    | |  user:        Ned Deily <nad@example.com>
    | |  date:        Fri Nov 28 15:21:12 2014 -0800
    | |  summary:     Issue #16113: Also remove test_case_sha3_224_huge
    | |
    o |  changeset:   93652:70163e18da87
    | |  user:        Raymond Hettinger <python@rcn.com>
    | |  date:        Fri Nov 28 14:52:14 2014 -0800
    | |  summary:     Minor code cleanup.

Notice that the only difference between this and the previous one is that
changeset 91935 now also has the bookmark "issueA". Bookmarks are advanced
automatically with each subsequent commit.

Once work has been completed on issueA, commit and prepare a patch for
submission to the issue tracker. Note that Mercurial doesn't have git's concept
of staging, so all changes will be committed::

    hg commit -m 'fix for issueA'

    @  changeset:   93655:a542bc2066d1
    |  bookmark:    issueA
    |  tag:         tip
    |  user:        Demian Brecht <demianbrecht@example.com>
    |  date:        Thu Dec 04 17:33:42 2014 -0800
    |  summary:     issueA
    |
    o    changeset:   93654:bd97eab25c70
    |\   parent:      93652:70163e18da87
    | |  parent:      93653:21257f916668
    | |  user:        Ned Deily <nad@example.com>
    | |  date:        Fri Nov 28 15:22:15 2014 -0800
    | |  summary:     Issue #16113: Also remove test_case_sha3_224_huge
    | |
    o |  changeset:   93653:21257f916668
    | |  branch:      3.4
    | |  parent:      93647:737355f61ba2
    | |  user:        Ned Deily <nad@example.com>
    | |  date:        Fri Nov 28 15:21:12 2014 -0800
    | |  summary:     Issue #16113: Also remove test_case_sha3_224_huge

Notice that the new commit's parent was the previous default tip and the
bookmark has automatically been advanced to the new tip. A patch for submission
to the issue tracker can now be prepared with::

    hg diff -c 93655 > issueA.patch

The above will diff revision 93655 against its parent. This will work
regardless of the commit that you happen to currently updated to.


Working on issueB
-----------------

Now that the patch has been submitted and it's pending review, work on another
issue can be started. Because of how bookmarks work (and as can be seen in the
previous history graph), the named branch "default" is advanced (remember that
bookmarks are not git branches). A new named branch (such as in git) has not
been created. This means that in order to update the working copy back to the
latest public commit, you must know which commit to revert back to before
creating a new bookmark::

    hg update 93654
    hg bookmark issueB

    o  changeset:   93655:a542bc2066d1
    |  bookmark:    issueA
    |  tag:         tip
    |  user:        Demian Brecht <demianbrecht@example.com>
    |  date:        Thu Dec 04 17:33:42 2014 -0800
    |  summary:     issueA
    |
    @    changeset:   93654:bd97eab25c70
    |\   bookmark:    issueB
    | |  parent:      93652:70163e18da87
    | |  parent:      93653:21257f916668
    | |  user:        Ned Deily <nad@example.com>
    | |  date:        Fri Nov 28 15:22:15 2014 -0800
    | |  summary:     Issue #16113: Also remove test_case_sha3_224_huge
    | |
    o |  changeset:   93653:21257f916668
    | |  branch:      3.4
    | |  parent:      93647:737355f61ba2
    | |  user:        Ned Deily <nad@example.com>
    | |  date:        Fri Nov 28 15:21:12 2014 -0800
    | |  summary:     Issue #16113: Also remove test_case_sha3_224_huge


Addressing issueA review comments
---------------------------------

While working on my new feature, I've received reviews of my bug fix and want to
finish that up before continuing on this much longer feature task. First step is
to commit my current feature work:
While working on issueB, a review has been completed for issueA. The following
demonstrates one method of store current state of issueB, and update back to
issueA::

    hg commit -m 'issueB WIP'
    created new head

In the above, hg will confirm that a divergent path has been created. This is
intentional and to be expected::

    hg update issueA

Reviewing the history graph, a new head can now be seen::

    o  changeset:   93656:6c166f6c1970
    |  bookmark:    issueB
    |  tag:         tip
    |  parent:      93654:bd97eab25c70
    |  user:        Demian Brecht <demianbrecht@example.com>
    |  date:        Thu Dec 04 17:36:36 2014 -0800
    |  summary:     issueB WIP
    |
    | @  changeset:   93655:a542bc2066d1
    |/   bookmark:    issueA
    |    user:        Demian Brecht <demianbrecht@example.com>
    |    date:        Thu Dec 04 17:33:42 2014 -0800
    |    summary:     issueA
    |
    o    changeset:   93654:bd97eab25c70
    |\   parent:      93652:70163e18da87
    | |  parent:      93653:21257f916668
    | |  user:        Ned Deily <nad@example.com>
    | |  date:        Fri Nov 28 15:22:15 2014 -0800
    | |  summary:     Issue #16113: Also remove test_case_sha3_224_huge

Once review comments have been addressed, commit again and prepare an updated
patch. In this case, using :code:`hg commit --amend` will amend the previous
commit with the most recent changes::

    hg commit --amend
    hg diff -c issueA > issueA.patch

    @  changeset:   93656:bba24fde02f0
    |  bookmark:    issueA
    |  tag:         tip
    |  parent:      93654:bd97eab25c70
    |  user:        Demian Brecht <demianbrecht@example.com>
    |  date:        Thu Dec 04 17:33:42 2014 -0800
    |  summary:     issueA
    |
    | o  changeset:   93655:6c166f6c1970
    |/   bookmark:    issueB
    |    user:        Demian Brecht <demianbrecht@example.com>
    |    date:        Thu Dec 04 17:36:36 2014 -0800
    |    summary:     issueB WIP
    |
    o    changeset:   93654:bd97eab25c70
    |\   parent:      93652:70163e18da87
    | |  parent:      93653:21257f916668
    | |  user:        Ned Deily <nad@example.com>
    | |  date:        Fri Nov 28 15:22:15 2014 -0800
    | |  summary:     Issue #16113: Also remove test_case_sha3_224_huge


Continue work on issueB
-----------------------

Work can now be continued on issueB::

    hg update issueB

    o  changeset:   93656:bba24fde02f0
    |  bookmark:    issueA
    |  tag:         tip
    |  parent:      93654:bd97eab25c70
    |  user:        Demian Brecht <demianbrecht@example.com>
    |  date:        Thu Dec 04 17:33:42 2014 -0800
    |  summary:     issueA
    |
    | @  changeset:   93655:6c166f6c1970
    |/   bookmark:    issueB
    |    user:        Demian Brecht <demianbrecht@example.com>
    |    date:        Thu Dec 04 17:36:36 2014 -0800
    |    summary:     issueB WIP
    |
    o    changeset:   93654:bd97eab25c70
    |\   parent:      93652:70163e18da87
    | |  parent:      93653:21257f916668
    | |  user:        Ned Deily <nad@example.com>
    | |  date:        Fri Nov 28 15:22:15 2014 -0800
    | |  summary:     Issue #16113: Also remove test_case_sha3_224_huge


Rebasing your work
==================

Rebasing was not previously included as it's an optional step.

As patches sometimes take time to have merged, there can be times when you'll
need to re-apply commits against the latest version in the public repo. Using
git, you might do this::

   git pull --rebase

The Mercurial equivalent is::

   hg pull --rebase

As this alters history (which Mercurial largely avoids in practice), the rebase
extension will need to be enabled. To enable the rebase extension, it must be
added to your .hgrc file::

   [extensions]
   rebase =


Workflow comparison
===================

Comparing against the git workflow above (skipping optional steps), the hg
equivalent in its entirety looks like this::

    # git clone git@github.com:python/cpython.git
    hg clone https://hg.python.org/cpython

    # work on issueA
    # git checkout -b issueA
    # git commit -a
    hg bookmark issueA
    hg commit

    # start work on issueB
    # git checkout master
    hg update [revision_number]

    # git checkout -b issueB
    # git commit -a
    hg bookmark issueB
    hg commit

    # address review comments
    # git checkout issueA
    # git commit -a
    hg update issueA
    hg commit --amend

    # create patch
    # git diff master..issueA > issueA.patch
    hg diff -c issueA > issueA.patch

    # continue working on issueB
    # git checkout issueB
    hg update issueB


.. _NamedBranches: http://mercurial.selenic.com/wiki/NamedBranches
