.. _committing:

Committing and Pushing Changes
==============================

.. TODO: include a checklist of items to be included in a commit?
   e.g updated Misc/NEWS entry, tests, doc

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
  metadata about file copies and permission bits::

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


Handling Other's Code
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


Forward-Porting
---------------

If the patch is a bugfix and it does not break
backwards-compatibility *at all*, then it should be applied to the oldest
branch applicable and forward-ported until it reaches the in-development branch
of Python (for example, first in ``3.1``, then in ``3.2`` and finally in
``default``). A forward-port instead of a back-port is preferred as it allows
the :abbr:`DAG (directed acyclic graph)` used by hg to work with the movement of
the patch through the codebase instead of against it.

.. warning::
   Even when porting an already committed patch, you should **still** check the
   test suite runs successfully before committing the patch to another branch.
   Subtle differences between two branches sometimes make a patch bogus if
   ported straightly.


Porting Within a Major Version
''''''''''''''''''''''''''''''

Assume that Python 3.3 is the current in-development version of Python and that
you have a patch that should also be applied to Python 3.2. To properly port
the patch to both versions of Python, you should first apply the patch to
Python 3.2::

   hg update 3.2
   hg import --no-commit patch.diff
   # Compile; run the test suite
   hg commit

With the patch now committed, you want to merge the patch up into Python 3.3.
This should be done *before* pushing your changes to hg.python.org, so that
the branches are in sync on the public repository.  Assuming you are doing
all of your work in a single clone, do::

   hg update default
   hg merge 3.2
   # Fix any conflicts; compile; run the test suite
   hg commit

.. note::
   *If the patch shouldn't be ported* from Python 3.2 to Python 3.3, you must
   also make it explicit: merge the changes but revert them before committing::

      hg update default
      hg merge 3.2
      hg revert -a
      hg commit

   This is necessary so that the merge gets recorded; otherwise, somebody
   else will have to make a decision about your patch when they try to merge.

When you have finished your porting work (you can port several patches one
after another in your local repository), you can push **all** outstanding
changesets to hg.python.org::

   hg push

This will push changes in both the Python 3.2 and Python 3.3 branches to
hg.python.org.


Porting Between Major Versions
''''''''''''''''''''''''''''''

Let's say you have committed your changes as changeset ``a7df1a869e4a``
in the 3.2 branch and now want to port it to 2.7.  This is simple.  First
update your working copy to the 2.7 branch, then import the patch::

   hg update 2.7
   hg export a7df1a869e4a | hg import --no-commit -
   # Compile; run the test suite
   hg commit

You can also use the `transplant extension`_::

   hg update 2.7
   hg transplant a7df1a869e4a
   # Compile; run the test suite


.. warning::
   transplant always commits automatically. This breaks the
   "run the test suite before committing" rule. We could advocate using
   "hg qimport -r tip -P" afterwards but that would add another level of
   complexity.


Using several working copies
''''''''''''''''''''''''''''

If you often work on bug fixes, you may want to avoid switching branches
in your local repository.  The reason is that rebuilding takes time
when many files are updated.  Instead, it is desirable to use a separate
working copy for each maintenance branch.

There are various ways to achieve this, but here is a possible scenario:

* First do a clone of the public repository, whose working copy be updated
  to the ``default`` branch::

   $ hg clone ssh://hg@hg.python.org/cpython default

* Then clone it to create another local repository which is then used to
  checkout branch 3.2::

   $ hg clone default 3.2
   $ cd 3.2
   $ hg update 3.2

* If you also need the 3.1 branch, you can similarly clone it, either from
  the ``3.2`` or the ``default`` repository.

* You can also clone a 2.7-dedicated repository from the ``default`` branch::

   $ hg clone default 2.7
   $ cd 2.7
   $ hg update 2.7

Given this arrangement of local repositories, pushing from the ``3.1``
repository will update the ``3.2`` repository, where you can then merge your
3.1 changes into the 3.2 branch.  In turn, pushing changes from the ``3.2``
repository will update the ``default`` repository.  Finally, once you have
merged (and tested!) your ``3.2`` changes into the ``default`` branch, pushing
from the ``default`` repository will publish your changes in the public
repository.

If you want, you can later :ref:`change the flow of changes <hg-paths>` implied
by the cloning of repositories.


Differences with ``svnmerge``
'''''''''''''''''''''''''''''

If you are coming from Subversion, you might be surprised by Mercurial
:ref:`merges <hg-merge>`.
Despite its name, ``svnmerge`` is different from ``hg merge``: while ``svnmerge``
allows to cherrypick individual revisions, ``hg merge`` can only merge whole
lines of development in the repository's :abbr:`DAG (directed acyclic graph)`.
Therefore, ``hg merge`` might force you to review outstanding changesets by
someone else that haven't been merged yet.


.. _transplant extension: http://mercurial.selenic.com/wiki/TransplantExtension

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


.. _named branch: http://mercurial.selenic.com/wiki/NamedBranches


Uploading a patch for review
''''''''''''''''''''''''''''

In this scheme, your work will probably consist of many commits (some of
them merges).  If you want to upload a patch for review somewhere, you need
a single agregate patch.  This is where having a dedicated named branch
``mywork`` gets handy.

First ensure that you have pulled *and merged* all changes from the main
repository, as explained above.  Then, assuming your :ref:`currently checked
out branch <hg-current-branch>` is still ``mywork``, simply do::

   $ hg diff -r default > mywork.patch

This will write to ``mywork.patch`` all the changes between ``default`` and
``mywork``.
