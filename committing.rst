.. _committing:

Committing and Pushing Changes
==============================

Is the change ready for committing?
-----------------------------------

Before a change is committed, you must make sure it is ready to enter the
public source tree.  Draft commits are prohibited.  Therefore, you must
ensure your changes fulfill several mandatory criteria.

When working a pull request on GitHub, use the following as a checklist of
what to check for before merging (details of various steps can be found
later in this document):

#. Has the submitter signed the CLA?
   (delineated by a label on the pull request)
#. Did the test suite pass? (delineated by a pull request check)
#. Did code coverage increase or stay the same?
   (delineated by a comment on the pull request)
#. Are the changes acceptable?
#. Was ``configure`` regenerated (if necessary)?
#. Was ``pyconfig.h.in`` regenerated (if necessary)?
#. Was the submitter added to ``Misc/ACKS`` (as appropriate)?
#. Was ``Misc/NEWS`` updated (as appropriate)?
#. Was "What's New" updated (as appropriate)?
#. Were appropriate labels added to signify necessary backporting of the
   pull request?

.. note::
   If you want to share your work-in-progress code on a feature or bugfix,
   either open a ``WIP``-prefixed PR, publish patches on the
   `issue tracker`_ or create a public fork of the repository.
   
.. _issue tracker: https://bugs.python.org


Does the test suite still pass?
'''''''''''''''''''''''''''''''

You must :ref:`run the whole test suite <runtests>` to ensure that it
passes before pushing any code changes.

.. note::
   You really need to run the **entire** test suite.  Running a single test
   is not enough as your changes may have unforeseen effects on other tests
   or library modules.

   Running the entire test suite doesn't guarantee that your changes
   will pass the :ref:`continuous integration <buildbots>` tests, as those
   will exercise more possibilities still (such as different platforms or
   build options).  But it will at least catch non-build specific,
   non-platform specific errors, therefore minimizing the chance for
   breakage.


Patch checklist
'''''''''''''''

Along with running the tests, a simple automated patch checklist, ``patchcheck``,
guides a developer through the common patch generation checks. To run
``patchcheck``:

   On *UNIX* (including Mac OS X)::

      make patchcheck

   On *Windows* (after any successful build)::

      python.bat Tools/scripts/patchcheck.py

The automated patch checklist runs through:

* Are there any whitespace problems in Python files?
  (using ``Tools/scripts/reindent.py``)
* Are there any whitespace problems in C files?
* Are there any whitespace problems in the documentation?
  (using ``Tools/scripts/reindent-rst.py``)
* Has the documentation been updated?
* Has the test suite been updated?
* Has ``Misc/NEWS`` been updated?
* Has ``Misc/ACKS`` been updated?
* Has ``configure`` been regenerated, if necessary?
* Has ``pyconfig.h.in`` been regenerated, if necessary?

The automated patch check doesn't actually *answer* all of these
questions. Aside from the whitespace checks, the tool is
a memory aid for the various elements that can go into
making a complete patch.


Commit Style
------------

Once a change patch is ready and tested, it can be committed to the repository.
We usually prefer to put a whole feature or bugfix into a single commit, but no
more.  In particular:

* Do **not** fix more than one issue in the same commit (except, of course, if
  one code change fixes all of them).
* Do **not** do cosmetic changes to unrelated code in the same commit as some
  feature/bugfix.

It is of course okay to pile up several commits to one branch and merge them
into another in one commit.


Handling Others' Code
---------------------

As a core developer you will occasionally want to commit a patch created by
someone else. When doing so you will want to make sure of some things.

First, make sure the patch is in a good state. Both :ref:`patch` and
:ref:`helptriage`
explain what is to be expected of a patch. Typically patches that get cleared by
triagers are good to go except maybe lacking ``Misc/ACKS`` and ``Misc/NEWS``
entries (which a core developer should make sure are updated appropriately).

Second, make sure the patch does not break backwards-compatibility without a
good reason. This means :ref:`running the entire test suite <runtests>` to
make sure everything still passes. It also means that if semantics do change
there must be a good reason for the breakage of code the change will cause
(and it **will** break someone's code). If you are unsure if the breakage
is worth it, ask on python-dev.

Third, ensure the patch is attributed correctly with the contributor's
name in ``Misc/ACKS`` if they aren't already there (and didn't add themselves
in their patch) and by mentioning "Patch by <x>" in the ``Misc/NEWS`` entry
and the checkin message. If the patch has been heavily modified then "Initial
patch by <x>" is an appropriate alternate wording.

If you omit correct attribution in the initial checkin, then update ``ACKS``
and ``NEWS`` in a subsequent checkin (don't worry about trying to fix the
original checkin message in that case).

Finally, make sure that the submitter of the
patch has a CLA in place (indicated by an asterisk following their username
in the `issue tracker`_ or by the "CLA Signed" label on the pull request).
If the submitter lacks a signed CLA and the patch is non-trivial, direct them
to the electronic `Contributor Licensing Agreement`_
to ensure the PSF has the appropriate authorizations in place to relicense
and redistribute their code.


Contributor Licensing Agreements
--------------------------------

Always get a `Contributor Licensing Agreement`_ (CLA) signed unless the
change has no possible intellectual property associated with it (e.g. fixing
a spelling mistake in documentation). Otherwise it is simply safer from a
legal standpoint to require the contributor to sign the CLA.

These days, the CLA can be signed electronically through the form linked
above, and this process is strongly preferred to the old mechanism that
involved sending a scanned copy of the signed paper form.

As discussed on the PSF Contribution_ page, it is the CLA itself that gives
the PSF the necessary relicensing rights to redistribute contributions under
the Python license stack. This is an additional permission granted above and
beyond the normal permissions provided by the chosen open source license.

Some developers may object to the relicensing permissions granted to the PSF
by the CLA. They're entirely within their rights to refuse to sign the CLA
on that basis, but that refusal *does* mean we **can't accept their patches**
for inclusion.

.. _Contribution: https://www.python.org/psf/contrib/
.. _Contributor Licensing Agreement:
   https://www.python.org/psf/contrib/contrib-form/


What's New and NEWS Entries
---------------------------

Almost all changes made to the code base deserve an entry in ``Misc/NEWS``.
If the change is particularly interesting for end users (e.g. new features,
significant improvements, or backwards-incompatible changes), an entry in
the ``What's New in Python`` document (in ``Doc/whatsnew/``) should be added
as well.

There are two notable exceptions to this general principle, and they
both relate to changes that *already* have a NEWS entry, and have not yet
been included in any formal release (including alpha and beta releases).
These exceptions are:

* If a change is reverted prior to release, then the corresponding entry
  is simply removed. Otherwise, a new entry must be added noting that the
  change has been reverted (e.g. when a feature is released in an alpha and
  then cut prior to the first beta).

* If a change is a fix (or other adjustment) to an earlier unreleased change
  and the original NEWS entry remains valid, then no additional entry is
  needed.

Needing a What's New entry almost always means that a change is *not*
suitable for inclusion in a maintenance release. A small number of
exceptions have been made for Python 2.7 due to the long support period -
when implemented, these changes *must* be noted in the "New Additions in
Python 2.7 Maintenance Releases" section of the Python 2.7 What's New
document.

New NEWS entries are customarily added at or near the top of their
respective sections, so that entries within a section appear in approximate
order from newest to oldest.  However, this is customary and not a
requirement.

The NEWS file is now read by Sphinx to produce the "Changelog" page; accordingly
it should be valid reStructuredText.  The "default role" (single backticks) can
be used to refer to objects in the documentation.  Example NEWS entry::

   - bpo-15304: Fix warning message when `os.chdir()` fails inside
     `test.support.temp_cwd()`.  Patch by Chris Jerdonek.

(In all other ``.rst`` files, the single backticks should not be used.  They are
allowed here because NEWS is meant to be as readable as possible unprocessed.)

A nice trick to make merging across branches work more smoothly is to
put a new entry after the first or first two entries rather than at the very
top.  This way if you commit, pull new changesets and merge, the merge will
succeed automatically.


Commit Messages
---------------

Every commit has a commit message to document why a change was made and to
communicate that reason to other core developers. Python core developers have
developed a standard way of formatting commit messages that everyone is
expected to follow.

Our usual convention mimics that used in the ``Misc/NEWS`` file.  Actually,
it is common to simply paste the NEWS entry into the commit message.  Here
is an example::

   bpo-42: the spam module is now more spammy.
   
   The spam module sporadically came up short on spam. This change
   raises the amount of spam in the module by making it more spammy.
   
   Thanks to Monty Python for the patch.

The first line or sentence is meant to be a dense, to-the-point explanation
of what the purpose of the commit is.  If this is not enough detail for a commit,
a new paragraph(s) can be added to explain in proper depth what has happened
(detail should be good enough that a core developer reading the commit message
understands the justification for the change).  Also, if a non-core developer
contributed to the resolution, it is good practice to credit them.


Reverting a Commit
------------------

To revert a merged pull request, press the ``Revert`` button at the bottom of
the pull request.  It will bring up the page to create a new pull request where
the commit can be reverted.  It also creates a new branch on the main CPython
repository.  Delete the branch once the pull request has been merged.

Always include the reason for reverting the commit to help others understand
why it was done.  The reason should be included as part of the commit message,
for example::

   Revert bpo-NNNN: Fix Spam Module (GH-111)

   Reverts python/cpython#111.
   Reason: This commit broke the buildbot.


Working with Git_
=================

.. seealso::
   :ref:`gitbootcamp`
   
As a core developer, the ability to push changes to the official Python
repositories means you have to be more careful with your workflow:

* You should not push new branches to the main repository.  You can still use
  them in your fork that you use for development of patches; you can
  also push these branches to a **separate** public repository that will be
  dedicated to maintenance of the work before the work gets integrated in the
  main repository.

* You should not commit directly into the ``master`` branch, or any of the 
  maintenance branches (``2.7``, ``3.5``, or ``3.6``).  You should commit against
  your own feature branch, and create a pull request.
  
It is recommended to keep a fork of the main repository around, as it allows simple
reversion of all local changes (even "committed" ones) if your local clone gets
into a state you aren't happy with.


.. _Git: https://git-scm.com/


Minimal Configuration
---------------------

If you use Git as a committer of patches (your own or others), you should
set up some basic options.  Here are the minimal options you need to activate:

* Your *name* and *email*: these settings defines what will be used when you
  commit changes::

   git config --global user.name "Your Name"
   git config --global user.email email@example.org

``--global`` flag sets configuration options at a global level, if instead you
want to set it at a project level use ``--local``, instead.

* *Under Windows*, you should also enable the *autocrlf* option, which will
  fix any Windows-specific line endings your text editor might insert when you
  create or modify versioned files.  The public repository has a hook which
  will reject all changesets having the wrong line endings, so enabling this
  extension on your local computer is in your best interest.
  ::

     git config --global core.autocrlf input


Remotes Setup
-------------


.. _remote-configuration:

Configuration
'''''''''''''

There are several possible ways how to set up your git repository. This section
discusses the simplest approach of having a single directory with two remotes,
one pointing to private fork, the other one being the official repository.

Assuming you have :ref:`cloned the official repository <checkout>` here is how
your current setup should look like::

   $ git remote -v    # show remotes
   origin  https://github.com/python/cpython (fetch)
   origin  https://github.com/python/cpython (push)

You can have multiple remotes defined for a single repository, the usual approach
is to have ``origin`` pointing to your :ref:`private fork <forking>`, and ``upstream``
pointing to the official repository. To do so, here are the steps needed to have
that setup::

   git remote set-url origin https://github.com/<your-username>/cpython
   git remote add upstream https://github.com/python/cpython

After that, your remotes configuration should look like this::

   $ git remote -v    # show remotes
   origin  https://github.com/<your-username>/cpython (fetch)
   origin  https://github.com/<your-username>/cpython (push)
   upstream  https://github.com/python/cpython (fetch)
   upstream  https://github.com/python/cpython (push)

At any point in time you can use SSH-based URL instead of HTTPS-based ones.


.. _committing-push-changes:

Pushing changes
'''''''''''''''

You have two remotes configured (see previous section for setup). Publishing
your changes to any of them is as simple as specifying the name of the remote
upon your push. Assuming I am working on a local branch ``bug1234`` and I want to
push it to my private branch I do::

   git push origin bug1234

Option ``-u|--set-upstream`` creates a remote-tracking branch that tracks what
have been pushed to ``origin``::

   git push -u origin bug1234

That allows to avoid rebasing beyond already pushed commits.
``git status --branch`` and ``git branch --verbose`` remind that the branch(es)
have not pushed commits.


Synchronizing remotes
'''''''''''''''''''''

To synchronize your fork, from the official repository you need to execute following
commands::

   git fetch upstream         # fetch remote changes
   git checkout master        # checkout your current master branch
   git merge upstream/master  # merge remote changes into your local master branch
   git push origin master     # publish changes to your private fork

The above steps can be executed against any branch you wish to, just replace master
with an appropriate branch name.


.. _committing-active-branches:

Active branches
---------------

If you do ``git branch`` you will see a :ref:`list of branches <listbranch>`.
``master`` is the in-development branch, and is the only branch that receives
new features.  The other branches only receive bug fixes or security fixes.


.. _branch-merge:

Backporting Changes to an Older Version
---------------------------------------

When it is determined that a pull request needs to be backported into one or more of 
the maintenance branches, a core developer can apply the labels ``needs backport to X.Y``
to the pull request.

After the pull request has been merged, it can be backported using cherry_picker.py_.

The commit hash can be obtained from the original pull request, or by using `git log`
on the ``master`` branch.  To display the 10 most recent commit hashes and their first
line of the commit message::

   git log -10 --oneline
   
Prefix the backport pull request with the branch, for example::

   [3.6] bpo-12345: Fix the Spam Module
   
Note that cherry_picker.py_ adds the branch prefix automatically.
   
Once the backport pull request has been created, remove the
``needs backport to X.Y`` label from the original pull request.  (Only Core
Developers can apply labels to GitHub pull requests).

.. _cherry_picker.py: https://github.com/python/core-workflow/tree/master/cherry_picker


.. _forking:

Forking repository
------------------

Forking a repository on GitHub is as simple as clicking Fork button in the right
upper corner at https://github.com/python/cpython.


Maintaining a repository
------------------------

The Git object database and other files/directories under ``.git`` require
periodic maintenance and cleanup. For example, commit editing leaves
unreferenced objects (dangling objects, in git terminology) and these
objects should be pruned to avoid collecting cruft in the DB. The
command ``git gc`` is used for maintenance. Git automatically runs
``git gc --auto`` as a part of some commands to do quick maintenance.
Users are recommended to run ``git gc --aggressive`` from time to
time; ``git help gc`` recommends to run it  every few hundred
changesets; for CPython it should be something like once a week
(GitHub itself runs the command weekly, so new checkouts do not need to
perform this step).

``git gc --aggressive`` not only removes dangling objects, it also
repacks object database into indexed and better optimized pack(s); it
also packs symbolic references (branches and tags).

From time to time run ``git fsck --strict`` to verify integrity of
the database. ``git fsck`` may produce a list of dangling objects;
that's not an error, just a reminder to perform regular maintenance.
