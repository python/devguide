.. _committing:

Committing and Pushing Changes
==============================

Is the change ready for committing?
-----------------------------------

Before a change is committed, you must make sure it is ready to enter the
public source tree.  Draft commits are prohibited.  Therefore, you must
ensure your changes fulfill several mandatory criteria.

.. note::
   If you want to share your work-in-progress code on a feature or bugfix,
   either publish patches or create a public fork of the repository.


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

Apart from running the tests, there's a simple patch checklist that
``make patchcheck`` (or ``./python.exe Tools/scripts/patchcheck.py`` on
Windows) will run through:

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

Note that the automated patch check can't actually *answer* all of these
questions, and even if it could, it still wouldn't know whether or not
those answers were appropriate. Aside from the whitespace checks, it is just
a memory aid to help with remembering the various elements that can go into
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
into another in one merge commit.


Handling Others' Code
---------------------

As a core developer you will occasionally want to commit a patch created by
someone else. When doing so you will want to make sure of some things.

First, make sure the patch is in a good state. Both :ref:`patch` and
:ref:`helptriage`
explain what is to be expected of a patch. Typically patches that get cleared by
triagers are good to go except maybe lacking ``Misc/ACKS`` and ``Misc/NEWS``
entries.

Second, make sure the patch does not break backwards-compatibility without a
good reason. This means :ref:`running the entire test suite <runtests>` to
make sure everything still passes. It also means that if semantics do change
there must be a good reason for the breakage of code the change will cause
(and it **will** break someone's code). If you are unsure if the breakage
is worth it, ask on python-dev.

Third, ensure the patch is attributed correctly by adding the contributor's
name to ``Misc/ACKS`` if they aren't already there (and didn't add themselves
in their patch) and by mentioning "Patch by <x>" in the ``Misc/NEWS`` entry
and the checkin message. If the patch has been heavily modified then "Initial
patch by <x>" is an appropriate alternate wording.

If you omit correct attribution in the initial checkin, then update ``ACKS``
and ``NEWS`` in a subsequent checkin (don't worry about trying to fix the
original checkin message in that case).

Finally, especially for larger patches, check if the submitter of the
patch has a CLA in place (indicated by an asterisk following their username
in the issue tracker). If the asterisk is missing and the patch is
non-trivial, direct them to the electronic `Contributor Licensing Agreement`_
to ensure the PSF has the appropriate authorizations in place to relicense
and redistribute their code.


Contributor Licensing Agreements
--------------------------------

It's unlikely bug fixes will require a `Contributor Licensing Agreement`_
unless they touch a *lot* of code. For new features, it is preferable to
ask that the contributor submit a signed CLA to the PSF as the associated
comments, docstrings and documentation are far more likely to reach a
copyrightable standard.

These days, the CLA can be signed electronically through the form linked
above, and this process is strongly preferred to the old mechanism that
involved sending a scanned copy of the signed paper form.

As discussed on the PSF Contribution_ page, it is the CLA itself that gives
the PSF the necessary relicensing rights to redistribute contributions under
the Python license stack. This is an additional permission granted above and
beyond the normal permissions provided by the chosen open source license.

Some developers may object to the relicensing permissions granted to the PSF
by the CLA. They're entirely within their rights to refuse to sign the CLA
on that basis, but that refusal *does* mean we can't accept their patches
for inclusion.

.. _Contribution: http://www.python.org/psf/contrib/
.. _Contributor Licensing Agreement:
   http://www.python.org/psf/contrib/contrib-form/


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

   - Issue #15304: Fix warning message when `os.chdir()` fails inside
     `test.support.temp_cwd()`.  Patch by Chris Jerdonek.

(In all other ``.rst`` files, the single backticks should not be used.  They are
allowed here because NEWS is meant to be as readable as possible unprocessed.)

A nice trick to make Mercurial’s automatic file merge work more smoothly is to
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

   Issue #42: the spam module is now more spammy.
   The spam module sporadically came up short on spam. This change
   raises the amount of spam in the module by making it more spammy.
   Thanks to Monty Python for the patch.

The first line or sentence is meant to be a dense, to-the-point explanation
of what the purpose of the commit is.  If this is not enough detail for a commit,
a new paragraph(s) can be added to explain in proper depth what has happened
(detail should be good enough that a core developer reading the commit message
understands the justification for the change).  Also, if a non-core developer
contributed to the resolution, it is good practice to credit them.

Mercurial hooks
'''''''''''''''

Special hooks have been added to the Mercurial repository to enable notifying
the issue tracker of a commit related to an issue.

A commit message can mention one or several issues in one of the following
ways::

   #12345
   issue12345
   issue 12345
   bug12345
   bug 12345

where 12345 is the number of the issue. The commit details (including its
changeset, branch and commit message) will then be posted as a message to the
issue's page in the tracker, for each mentioned issue.

If "closes" (or "closed", or "closing") is prepended, the issue is
automatically closed as "fixed".

Working with Mercurial_
=======================

As a core developer, the ability to push changes to the official Python
repositories means you have to be more careful with your workflow:

* You should not push new named branches to the main repository.  You can
  still use them in clones that you use for development of patches; you can
  also push these branches to a **separate** public repository that will be
  dedicated to maintenance of the work before the work gets integrated in the
  main repository.

* You should collapse changesets of a single feature or bugfix before pushing
  the result to the main repository.  The reason is that we don't want the
  history to be full of intermediate commits recording the private history
  of the person working on a patch.  If you are using the rebase_ extension,
  consider adding the ``--collapse`` option to ``hg rebase``.  The collapse_
  extension is another choice.

Because of these constraints, it can be practical to use other approaches
such as mq_ (Mercurial Queues), in order to maintain patches in a single
local repository and to push them seamlessly when they are ready.

It can also be useful to keep a pristine clone of the main repository around,
as it allows simple reversion of all local changes (even "committed" ones) if
your local clone gets into a state you aren't happy with.


.. _Mercurial: http://www.hg-scm.org/
.. _mq: http://mercurial.selenic.com/wiki/MqExtension
.. _rebase: http://mercurial.selenic.com/wiki/RebaseExtension
.. _collapse: http://mercurial.selenic.com/wiki/CollapseExtension


Minimal Configuration
---------------------

To use Mercurial as a committer (both of your and others' patches), you should
set up some basic options in your `configuration file`_.  Under Windows,
TortoiseHg has a graphical settings dialog for most options, meaning you
don't need to edit the file directly (it is still available in
``%USERPROFILE%\Mercurial.ini``).  Under other platforms, you must edit
``~/.hgrc``.

Here are the minimal options you need to activate:

* your *username*: this setting defines the name that will be used when you
  :ref:`commit <hg-commit>` changes.  The usual convention is to also include
  an e-mail contact address in there::

   [ui]
   username = Your Name <email@example.org>

* *extended diffing*: this setting enables an `extended diff format`_
  which is more useful than the standard unified diff format as it includes
  metadata about file copies, permission bits, and is able to represent
  binary files::

   [diff]
   git = on

Under Windows, you should also enable the `eol extension`_, which will
fix any Windows-specific line endings your text editor might insert when you
create or modify versioned files.  The public repository has a hook which
will reject all changesets having the wrong line endings, so enabling this
extension on your local computer is in your best interest.

As a core developer, it can be very helpful to set up the same commit checks
locally that the main repo enforces for incoming patch sets. This can save a
great deal of frustration with the server rejecting ``hg push`` for changes
(which can be especially time consuming if you have already merged changes
across branches).

Configuring and using the whitespace checking hook found in the `hooks
repository`_ will help check incoming patch sets. To configure a hook,
add configuration settings to ``~/.hgrc`` for the relevant repo(s) (remember
to adjust the path appropriately for the checked out location of the
`hooks repository`_). To configure a "pretxncommit" hook that will check
whitespace before the changeset is committed and can thus abort the commit
if whitespace is found, add::

   [hooks]
   pretxncommit.whitespace = python:~/path/to/checkwhitespace.py:check_whitespace_single

Another option is to configure it as a "commit" hook; if used, a warning
will still be issued but the changeset will be applied anyway::

   [hooks]
   commit = python:~/path/to/checkwhitespace.py:check_whitespace_single

.. _configuration file: http://www.selenic.com/mercurial/hgrc.5.html#files
.. _extended diff format: http://www.selenic.com/mercurial/hg.1.html#diffs
.. _eol extension: http://mercurial.selenic.com/wiki/EolExtension
.. _hooks repository: https://hg.python.org/hooks


Clones Setup
------------

There are several possible ways to set up your Mercurial clone(s).  If you are
a core developer, you often need to work on the different branches, so the best
approach is to have a separate clone/directory for each active branch.  If you
are a contributor, having a single clone might be enough.

Single Clone Approach
'''''''''''''''''''''

This approach has the advantage of being simpler because it requires a single
clone/directory, but, on the other hand, it requires you to recompile Python
every time you need to switch branch.  For this reason, this approach is not
suggested to core developers, but it's usually suitable for contributors.

See :ref:`checkout` to find information about cloning and switching branches.

.. _multiple-clones:

Multiple Clones Approach
''''''''''''''''''''''''

This approach requires you to keep a separate clone/directory for each active
branch, but, on the other hand, it doesn't require you to switch branches and
recompile Python, so it saves times while merging and testing a patch on the
different branches.  For this reason, this approach is suggested to core
developers.

The easiest way to do this is by using the `share extension`_, that can be
enabled by adding the following lines to your ``~/.hgrc``::

   [extensions]
   share =

Once you have :ref:`cloned the hg.python.org/cpython repository <checkout>`
you can create the other shared clones using::

   $ hg share cpython 2.7  # create a new shared clone
   $ cd 2.7                # enter the directory
   $ hg up 2.7             # switch to the 2.7 branch

You can then repeat the same operation for the other active branches.
This will create different clones/directories that share the same history.
This means that once you commit or pull new changesets in one of the clones,
they will be immediately available in all the other clones (note however that
while you only need to use ``hg pull`` once, you still need to use ``hg up``
in each clone to update its working copy).

If you don't want to specify ssh://hg@hg.python.org/cpython every time you pull
or push, you should add to the ``.hg/hgrc`` files of the clones::

   [paths]
   default = ssh://hg@hg.python.org/cpython

In order to apply a patch, commit, and merge it on all the branches, you can do
as follow::

   $ cd 2.7
   $ hg pull
   $ hg up
   $ hg import --no-c http://bugs.python.org/url/to/the/patch.diff
   $ # review, run tests, run `make patchcheck`
   $ hg ci -m '#12345: fix some issue.'
   $ # switch to 3.4 and port the changeset using `hg graft`
   $ cd ../3.4
   $ hg up
   $ hg graft 2.7
   $ # switch to 3.x, merge, commit, and push everything
   $ cd ../3.x
   $ hg up
   $ hg merge 3.4
   $ hg ci -m '#12345: merge with 3.4.'
   $ hg push

Unless noted otherwise, the rest of the page will assume you are using the
multiple clone approach, and explain in more detail these basic steps.

For more advanced explanations about :ref:`null merges <hg-null-merge>`,
:ref:`heads merges <hg-heads-merge>`, :ref:`merge conflicts
<hg-merge-conflicts>`, etc., see the :ref:`FAQs for core developers
<core-devs-faqs>`.

.. _share extension: http://mercurial.selenic.com/wiki/ShareExtension


Active branches
---------------

If you do ``hg branches`` you will see a :ref:`list of branches <listbranch>`.
``default`` is the in-development branch, and is the only branch that receives
new features.  The other branches only receive bug fixes or security fixes.
Depending on what you are committing (feature, bug fix, or security fix), you
should commit to the oldest branch applicable, and then forward-port until the
in-development branch.


Merging order
-------------

There are two separate lines of development: one for Python 2 (the ``2.x``
branches) and one for Python 3 (the ``3.x`` branches and ``default``).
You should *never* merge between the two major versions (2.x and 3.x) ---
only between minor versions (e.g. 3.x->3.y).  The merge always happens from
the oldest applicable branch to the newest branch within the same major
Python version.


.. _branch-merge:

Merging between different branches (within the same major version)
------------------------------------------------------------------

Assume that Python 3.5 is the current in-development version of Python and that
you have a patch that should also be applied to Python 3.4.  To properly port
the patch to both versions of Python, you should first apply the patch to
Python 3.4::

   cd 3.4
   hg import --no-commit patch.diff
   # Compile; run the test suite
   hg ci -m '#12345: fix some issue.'

Then you can switch to the ``3.5`` clone, merge, run the tests and commit::

   cd ../3.5
   hg merge 3.4
   # Fix any conflicts (e.g. ``hg revert -r default Misc/NEWS``); compile; run the test suite
   hg ci -m '#12345: merge with 3.4.'

If you are not using the share extension, you will need to use
``hg pull ../3.4`` before being able to merge.

.. note::
   Even when porting an already committed patch, you should *still* check the
   test suite runs successfully before committing the patch to another branch.
   Subtle differences between two branches sometimes make a patch bogus if
   ported without any modifications.


Porting changesets between the two major Python versions (2.x and 3.x)
----------------------------------------------------------------------

Assume you just committed something on ``2.7``, and want to port it to ``3.4``.
You can use ``hg graft`` as follow::

   cd ../3.4
   hg graft 2.7

This will port the latest changeset committed in the 2.7 clone to the 3.4 clone.
``hg graft`` always commits automatically, except in case of conflicts, when
you have to resolve them and run ``hg graft --continue`` afterwards.
Instead of the branch name you can also specify a changeset id, and you can
also graft changesets from 3.x to 2.7.

On older version of Mercurial where ``hg graft`` is not available, you can use::

    cd ../3.4
    hg export 2.7 | hg import -

The result will be the same, but in case of conflict this will create ``.rej``
files rather than using Mercurial merge capabilities.

A third option is to apply manually the patch on ``3.4``.  This is convenient
when there are too many differences with ``2.7`` or when there is already a
specific patch for ``3.4``.

.. warning::
   Never use ``hg merge`` to port changes between 2.x and 3.x (or vice versa).


Long-term development of features
---------------------------------

If you want to work on a feature long-term (perhaps you're implementing a
PEP), you will probably want to publish your work in a dedicated repository.
The following instructions will help you do so on `hg.python.org
<https://hg.python.org>`_'s infrastructure without requiring a lot of upload
bandwidth.

Go to the main repository's Web page (https://hg.python.org/cpython/); there
you find a button labelled "server-side clone", which you can click on to
display a Web form.  Enter the relative path of the repository you want to
create on the server, for example ``features/mywork``; and press the button.
A new repository gets created on the server with all the changesets of the
original repository (it will seem very fast; this is normal).

You can now do a local clone of this repository on your disk::

   $ hg clone ssh://hg@hg.python.org/features/mywork
   $ cd mywork

.. commented out: old instructions (without server-side cloning)

   First create a public (empty) repository on hg.python.org::

      $ hg init ssh://hg@hg.python.org/features/mywork

   And do a local clone of that repository on your disk::

      $ hg clone ssh://hg@hg.python.org/features/mywork
      $ cd mywork

   There, pull all the contents from the main repository, either from a local
   clone::

      $ hg pull ../cpython
      $ hg update

   or directly from the network (which is of course slower)::

      $ hg pull http://hg.python.org/cpython
      $ hg update

It is recommended that you create a new `named branch`_ for your work, so as
to easily track changes.  That named branch will exist in your feature
repository, but not in the main repository::

   $ hg branch mywork
   $ hg commit -m "Creating branch mywork"
   $ hg push --new-branch

You can now work on your feature, commit changes as you will, and push them
when desired::

   $ hg push

When you push them, they will land in the public repository at
``ssh://hg@hg.python.org/features/mywork`` (or
``https://hg.python.org/features/mywork`` for the read-only URL).  Other
people can clone the public repository and work on the code too.

When you want to synchronize with CPython's upstream changes, you can pull
from the main repository, either from its remote URL::

   $ hg pull https://hg.python.org/cpython

or from a local clone that you may have on your disk (which is of course
faster)::

   $ hg pull ../cpython

and merge all new changes from branch ``default`` to branch ``mywork``::

   $ hg branch
   mywork
   $ hg merge default

Rather than using a clone on ``python.org`` (which isn't particularly useful
for collaboration with folks that don't already have CPython commit rights),
Bitbucket_ also maintain an `up to date clone`_ of the main ``cpython``
repository that can be used as the basis for a new clone or patch queue.

.. _named branch: http://mercurial.selenic.com/wiki/NamedBranches
.. _Bitbucket: http://www.bitbucket.org
.. _up to date clone: https://bitbucket.org/mirror/cpython/overview


Uploading a patch for review
''''''''''''''''''''''''''''

In this scheme, your work will probably consist of many commits (some of
them merges).  If you want to upload a patch for review somewhere, you need
a single aggregate patch.  This is where having a dedicated named branch
``mywork`` gets handy.

First ensure that you have pulled *and merged* all changes from the main
repository, as explained above.  Then, assuming your :ref:`currently checked
out branch <hg-current-branch>` is still ``mywork``, simply do::

   $ hg diff -r default > mywork.patch

This will write to ``mywork.patch`` all the changes between ``default`` and
``mywork``.
