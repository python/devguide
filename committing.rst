.. _committing:

Committing and Pushing Changes
==============================

Once a change patch is ready and tested, it can be committed to the repository.
We usually prefer to put a whole feature or bugfix into a single commit, but no
more.  In particular:

* Do **not** fix more than one issue in the same commit (except, of course, if
  one code change fixes all of them).
* Do **not** do cosmetic changes to unrelated code in the same commit as some
  feature/bugfix.

It is of course okay to pile up several commits to one branch and merge them
into another in one merge commit.


Patch Checklist
---------------

Here's the simple patch checklist that ``make patchcheck`` (or ``./python.exe
Tools/scripts/patchcheck.py`` on Windows) will run through
on a system that uses the makefile to build Python:

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
* Has the test suite been run?
* Are there any reference leaks?

Note that the automated patch check can't actually *answer* all of these
questions, and even if it could, it still wouldn't know whether or not
those answers were appropriate. Aside from the whitespace checks, it is just
a memory aid to help with remembering the various elements that can go into
making a complete patch.


NEWS Entries
------------

Almost all changes made to the code base deserve an entry in ``Misc/NEWS``.
The ``What's New in Python`` document is the place for more subjective
judgments of the "importance" of changes. There are two notable exceptions
to this general principle, and they both relate to changes that *already*
have a NEWS entry, and have not yet been included in any formal release
(including alpha and beta releases). These exceptions are:

* If a change is reverted prior to release, then the corresponding entry
  is simply removed. Otherwise, a new entry must be added noting that the
  change has been reverted (e.g. when a feature is released in an alpha and
  then cut prior to the first beta).

* If a change is a fix (or other adjustment) to an earlier unreleased change
  and the original NEWS entry remains valid, then no additional entry is
  needed.

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
-----------------------

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


.. _configuration file: http://www.selenic.com/mercurial/hgrc.5.html#files
.. _extended diff format: http://www.selenic.com/mercurial/hg.1.html#diffs
.. _eol extension: http://mercurial.selenic.com/wiki/EolExtension


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
good reason. This means :ref:`running the test suite <runtests>` to make sure
everything still passes. It also means that if semantics do change there must
be a good reason for the breakage of code the change will cause (and it
**will** break someone's code). If you are unsure if the breakage is worth it,
ask on python-dev.

Third, ensure the patch is attributed correctly by adding the contributor's
name to ``Misc/ACKS`` if they aren't already there (and didn't add themselves
in their patch) and by mentioning "Patch by <x>" in the ``Misc/NEWS`` entry
and the checkin message. If the patch has been heavily modified then "Initial
patch by <x>" is an appropriate alternate wording.

If you omit correct attribution in the initial checkin, then update ``ACKS``
and ``NEWS`` in a subsequent checkin (don't worry about trying to fix the
original checkin message in that case).


Contributor Licensing Agreements
--------------------------------

It's unlikely bug fixes will require a `Contributor Licensing Agreement`_
unless they touch a *lot* of code. For new features, it is preferable to
ask that the contributor submit a signed CLA to the PSF as the associated
comments, docstrings and documentation are far more likely to reach a
copyrightable standard.

For Python sprints we now recommend collecting CLAs as a matter of course, as
the folks leading the sprints can then handle the task of scanning (or otherwise
digitising) the forms and passing them on to the PSF secretary. (Yes, we
realise this process is quite archaic. Yes, we're in the process of fixing
it. No, it's not fixed yet).

As discussed on the PSF Contribution_ page, it is the CLA itself that gives
the PSF the necessary relicensing rights to redistribute contributions under
the Python license stack. This is an additional permission granted above and
beyond the normal permissions provided by the chosen open source license.

.. _Contribution: http://www.python.org/psf/contrib/
.. _Contributor Licensing Agreement:
   http://www.python.org/psf/contrib/contrib-form/


Forward-Porting
---------------

If the patch is a bugfix and it does not break
backwards-compatibility *at all*, then it should be applied to the oldest
branch applicable and forward-ported until it reaches the in-development branch
of Python (for example, first in ``3.2``, then in ``3.3`` and finally in
``default``). A forward-port instead of a back-port is preferred as it allows
the :abbr:`DAG (directed acyclic graph)` used by hg to work with the movement of
the patch through the codebase instead of against it.

Note that this policy applies only within a major version - the ``2.7`` branch
is an independent thread of development, and should *never* be merged to any
of the ``3.x`` branches or ``default``. If a bug fix applies to both ``2.x``
and ``3.x``, the two additions are handled as separate commits. It doesn't
matter which is updated first, but any associated tracker issues should be
closed only after all affected versions have been modified in the main
repository.

.. warning::
   Even when porting an already committed patch, you should **still** check the
   test suite runs successfully before committing the patch to another branch.
   Subtle differences between two branches sometimes make a patch bogus if
   ported without any modifications.


Porting Within a Major Version
''''''''''''''''''''''''''''''

Assume that Python 3.4 is the current in-development version of Python and that
you have a patch that should also be applied to Python 3.3. To properly port
the patch to both versions of Python, you should first apply the patch to
Python 3.3::

   hg update 3.3
   hg import --no-commit patch.diff
   # Compile; run the test suite
   hg commit

With the patch now committed, you want to merge the patch up into Python 3.4.
This should be done *before* pushing your changes to hg.python.org, so that
the branches are in sync on the public repository.  Assuming you are doing
all of your work in a single clone, do::

   hg update default
   hg merge 3.3
   # Fix any conflicts; compile; run the test suite
   hg commit

.. index:: null merging

.. note::
   If the patch should *not* be ported from Python 3.3 to Python 3.4, you must
   also make this explicit by doing a *null merge*: merge the changes but
   revert them before committing::

      hg update default
      hg merge 3.3
      hg revert -ar default
      hg resolve -am  # needed only if the merge created conflicts
      hg commit

   This is necessary so that the merge gets recorded; otherwise, somebody
   else will have to make a decision about your patch when they try to merge.
   (Using a three-way merge tool generally makes the ``hg resolve`` step
   in the above unnecessary; also see `this bug report
   <http://bz.selenic.com/show_bug.cgi?id=2706>`__.)

When you have finished your porting work (you can port several patches one
after another in your local repository), you can push **all** outstanding
changesets to hg.python.org::

   hg push

This will push changes in both the Python 3.3 and Python 3.4 branches to
hg.python.org.


Porting Between Major Versions
''''''''''''''''''''''''''''''

Let's say you have committed your changes as changeset ``a7df1a869e4a``
in the 3.3 branch and now want to port it to 2.7.  This is simple using
the "graft" command, which uses Mercurial's merge functionality to
cherry-pick::

   hg update 2.7
   hg graft a7df1a869e4a
   # Compile; run the test suite

Graft always commits automatically, except in case of conflicts, when you
have to resolve them and run ``hg graft --continue`` afterwards.

Another method is using "export" and "import": this has the advantage that
you can run the test suite before committing, but the disadvantage that
in case of conflicts, you will only get ``.rej`` files, not inline merge
markers. ::

   hg update 2.7
   hg export a7df1a869e4a | hg import --no-commit -
   # Compile; run the test suite
   hg commit


Using several working copies
''''''''''''''''''''''''''''

If you often work on bug fixes, you may want to avoid switching branches
in your local repository.  The reason is that rebuilding takes time
when many files are updated.  Instead, it is desirable to use a separate
working copy for each maintenance branch.

There are various ways to achieve this, but here is a possible scenario:

* First do a clone of the public repository, whose working copy will be
  updated to the ``default`` branch::

   $ hg clone ssh://hg@hg.python.org/cpython py3k

* Then clone it to create another local repository which is then used to
  checkout branch 3.3::

   $ hg clone py3k py3.3
   $ cd py3.3
   $ hg update 3.3

* Then clone it to create another local repository which is then used to
  checkout branch 3.2::

   $ hg clone py3.3 py3.2
   $ cd py3.2
   $ hg update 3.2

* If you also need the 3.1 branch to work on security fixes, you can similarly
  clone it, either from the ``py3.2`` or the ``py3k`` repository. It is
  suggested, though, that you clone from ``py3.2`` as that it will force you
  to push changes back up your clone chain so that you make sure to port
  changes to all proper versions.

* You can also clone a 2.7-dedicated repository from the ``py3k`` branch::

   $ hg clone py3k py2.7
   $ cd py2.7
   $ hg update 2.7

Given this arrangement of local repositories, pushing from the ``py3.2``
repository will update the ``py3.3`` repository, where you can then merge your
3.2 changes into the 3.3 branch.  In turn, pushing changes from the ``py3.3``
repository will update the ``py3k`` repository.  Finally, once you have
merged (and tested!) your ``3.3`` changes into the ``default`` branch, pushing
from the ``py3k`` repository will publish your changes in the public
repository.

When working with this kind of arrangement, it can be useful to have a simple
script that runs the necessary commands to update all branches with upstream
changes::

  cd ~/py3k
  hg pull -u
  cd ~/py3.3
  hg pull -u
  cd ~/py3.2
  hg pull -u
  cd ~/py2.7
  hg pull -u

Only the first of those updates will touch the network - the latter two will
just transfer the changes locally between the relevant repositories.

If you want, you can later :ref:`change the flow of changes <hg-paths>` implied
by the cloning of repositories. For example, you may choose to add a separate
``sandbox`` repository for experimental code (potentially published somewhere
other than python.org) or an additional pristine repository that is
never modified locally.


Differences with ``svnmerge``
'''''''''''''''''''''''''''''

If you are coming from Subversion, you might be surprised by Mercurial
:ref:`merges <hg-merge>`.
Despite its name, ``svnmerge`` is different from ``hg merge``: while ``svnmerge``
allows to cherry-pick individual revisions, ``hg merge`` can only merge whole
lines of development in the repository's :abbr:`DAG (directed acyclic graph)`.
Therefore, ``hg merge`` might force you to review outstanding changesets by
someone else that haven't been merged yet.


.. seealso::
   `Merging work
   <http://hgbook.red-bean.com/read/a-tour-of-mercurial-merging-work.html>`_,
   in `Mercurial: The Definitive Guide <http://hgbook.red-bean.com/>`_.


Long-term development of features
---------------------------------

If you want to work on a feature long-term (perhaps you're implementing a
PEP), you will probably want to publish your work in a dedicated repository.
The following instructions will help you do so on `hg.python.org
<http://hg.python.org>`_'s infrastructure without requiring a lot of upload
bandwidth.

Go to the main repository's Web page (http://hg.python.org/cpython/); there
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
``http://hg.python.org/features/mywork`` for the read-only URL).  Other
people can clone the public repository and work on the code too.

When you want to synchronize with CPython's upstream changes, you can pull
from the main repository, either from its remote URL::

   $ hg pull http://hg.python.org/cpython

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
