.. _coredev:

How to Become a Core Developer
==============================

What it Takes
-------------

When you have consistently contributed patches which meet quality standards
without requiring extensive rewrites prior to being committed,
you may qualify for
commit privileges and become a core developer of Python. You must also work
well with other core developers (and people in general) as you become an
ambassador for the Python project.

Typically a core developer will offer you the chance to gain commit privilege.
The person making the offer will become your mentor and watch your commits for
a while to make sure you understand the development process. If other core
developers agree that you should gain commit privileges you are then extended
an official offer.

You may request commit privileges yourself, but do not be surprised if your
request is turned down. Do not take this personally! It simply means that other
core developers think you need more time contributing patches before you are
able to commit them without supervision.

A complete list of core developer usernames can be found at
https://hg.python.org/committers.txt. :ref:`developers` lists when and why
someone received commit privileges.


Gaining Commit Privileges
-------------------------

When you have been extended an official offer to become a Python core
developer, there are several things you must do.

Mailing Lists
'''''''''''''

You are expected to subscribe to python-committers, python-dev,
python-checkins, and one of new-bugs-announce or python-bugs-list. See
:ref:`communication` for links to these mailing lists.


Issue Tracker
'''''''''''''

If you did not gain the Developer role in the `issue tracker`_ before gaining
commit privileges, please say so. This will allow issues to be assigned to you.
A tracker admin should also flip your "is committer" bit in the tracker's
account screen.

It is expected that on the issue tracker you have a username in the form of
"first_name.last_name". If your initial issue tracker username is not of this
form, please change it. This is so that it is easier to assign issues to the
right person.


SSH
'''

You need to provide an SSH-2 key to be able to commit code. You may have
multiple keys if you wish (e.g., for work and home). Using Ed25519 keys is
encouraged. Send your key as an attachment in an email to
hgaccounts@python.org along with your GitHub username so you can be added to
the "Python core" team at https://github.com/python.

Your SSH key will be set to a username in the form of "first_name.last_name".
This should match your username on the issue tracker.

You can verify your commit access by looking at
https://hg.python.org/committers.txt which lists all core developers by
username.  If you want to practice, there is a `test repository
<https://hg.python.org/test/>`_ where you can freely commit and push any
changes you like::

   hg clone ssh://hg@hg.python.org/test/ hgtest

An entry in the :ref:`developers` should also be entered for you.
Typically the person who sponsored your application to become a core developer
makes sure an entry is created for you.


.. _contributor_agreement:

Sign a Contributor Agreement
''''''''''''''''''''''''''''

Submitting a `contributor form for Python`_ licenses any code you contribute to
the Python Software Foundation. While you retain the copyright, giving the PSF
the ability to license your code means it can be put under the PSF license so
it can be legally distributed with Python.

This is a very important step! Hopefully you have already submitted a
contributor agreement if you have been submitting patches. But if you have not
done this yet, it is best to do this ASAP, probably before you even do your
first commit so as to not forget.


.. _contributor form for Python: http://www.python.org/psf/contrib/



Read/Write Checkout
'''''''''''''''''''

With your commit privileges working and your contributor form submitted, you
can now get a read/write checkout of the code. URLs for read/write checkouts
are different than those for read-only checkouts as SSH is used instead of
HTTP.

You can clone the repository (which contains all active branches) with::

   hg clone ssh://hg@hg.python.org/cpython

The default branch in that repository is the current development branch.
You can of course switch your working copy to one of the maintenance branches,
for example::

   hg update 2.7


Responsibilities
----------------

As a core developer, there are certain things that are expected of you.

First and foremost, be a good person. This might sound melodramatic, but you
are now a member of the Python project and thus represent the project and your
fellow core developers whenever you discuss Python with anyone. We have a
reputation for being a very nice group of people and we would like to keep it
that way.  Core developers responsibilities include following the `PSF Code of
Conduct`_.

Second, please be prompt in responding to questions. Many contributors to Python
are volunteers so what little free time they can dedicate to Python should be
spent being productive. If you have been asked to respond to an issue or answer
a question and you put it off it ends up stalling other people's work. It is
completely acceptable to say you are too busy, but you need to say that instead
of leaving people waiting for an answer. This also applies to anything you
do on the issue tracker.

Third, please list what areas you want to be considered an expert in the
:ref:`experts`. This allows triagers to direct issues to you which involve
an area you are an expert in. But,
as stated in the second point above, if you do not have the time to answer
questions promptly then please remove yourself as needed from the file so that
you will not be bothered in the future. Once again, we all understand how life
gets in the way, so no one will be insulted if you remove yourself from the
list.

Fourth, please consider whether or not you wish to add your name to the
:ref:`motivations` list. Core contributor participation in the list helps the
wider Python community to better appreciate the perspectives currently
represented amongst the core development team, the Python Software Foundation
to better assess the sustainability of current contributions to CPython core
development, and also serves as a referral list for organisations seeking
commercial Python support from the core development community.

And finally, enjoy yourself! Contributing to open source software should be fun
(overall). If you find yourself no longer enjoying the work then either take a
break or figure out what you need to do to make it enjoyable again.


.. _PSF Code of Conduct: https://www.python.org/psf/codeofconduct/


.. _version-core-devs:

Version control for core developers
-----------------------------------

.. _hg-commit:

How do I commit a change to a file?
'''''''''''''''''''''''''''''''''''

To commit any changes to a file (which includes adding a new file or deleting
an existing one), you use the command::

 hg commit [PATH]

``PATH`` is optional: if it is omitted, all changes in your working copy
will be committed to the local repository.  When you commit, be sure that all
changes are desired by :ref:`reviewing them first <hg-status>`;
also, when making commits that you intend to push to public repositories,
you should **not** commit together unrelated changes.

To abort a commit that you are in the middle of, leave the message
empty (i.e., close the text editor without adding any text for the
message).  Mercurial will then abort the commit operation so that you can
try again later.

Once a change is committed to your local repository, it is still only visible
by you.  This means you are free to experiment with as many local commits
you feel like.

.. note::
   If you do not like the default text editor Mercurial uses for
   entering commit messages, you may specify a different editor,
   either by changing the ``EDITOR`` environment variable or by setting
   a Mercurial-specific editor in your global ``.hgrc`` with the ``editor``
   option in the ``[ui]`` section.


.. _hg-merge-conflicts:

How do I solve merge conflicts?
'''''''''''''''''''''''''''''''

The easiest way is to install KDiff3 --- Mercurial will open it automatically
in case of conflicts, and you can then use it to solve the conflicts and
save the resulting file(s).  KDiff3 will also take care of marking the
conflicts as resolved.

If you don't use a merge tool, you can use ``hg resolve --list`` to list the
conflicting files, resolve the conflicts manually, and the use
``hg resolve --mark <file path>`` to mark these conflicts as resolved.
You can also use ``hg resolve -am`` to mark all the conflicts as resolved.

.. note::
   Mercurial will use KDiff3 automatically if it's installed and it can find
   it --- you don't need to change any settings.  KDiff3 is also already
   included in the installer of TortoiseHg.  For more information, see
   https://www.mercurial-scm.org/wiki/KDiff3.


.. _hg-null-merge:

How do I make a null merge?
'''''''''''''''''''''''''''

If you committed something (e.g. on 3.5) that shouldn't be ported on newer
branches (e.g. on default), you have to do a *null merge*::

   cd 3.x
   hg merge 3.5
   hg revert -ar default
   hg resolve -am  # needed only if the merge created conflicts
   hg ci -m '#12345: null merge with 3.5.'

Before committing, ``hg status`` should list all the merged files as ``M``,
but ``hg diff`` should produce no output.  This will record the merge without
actually changing the content of the files.


.. _hg-heads-merge:

I got "abort: push creates new remote heads!" while pushing, what do I do?
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

If you see this message while pushing, it means that you committed something
on a clone that was not up to date, thus creating a new head.
This usually happens for two reasons:

1. You forgot to run ``hg pull`` and/or ``hg up`` before committing;
2. Someone else pushed on the main repo just before you, causing a push race;

First of all you should pull the new changesets using ``hg pull``.  Then you can
use ``hg heads`` to see which branches have multiple heads.

If only one branch has multiple heads, you can do::

   cd default
   hg heads .
   hg up csid-of-the-other-head
   hg merge
   hg ci -m 'Merge heads.'

``hg heads .``  will show you the two heads of the current branch: the one you
pulled and the one you created with your commit (you can also specify a branch
with ``hg heads <branch>``).  While not strictly necessary, it is highly
recommended to switch to the other head before merging.  This way you will be
merging only your changeset with the rest, and in case of conflicts it will be
a lot easier.

If more than one branch has multiple heads, you have to repeat these steps for
each branch.  Since this creates new changesets, you will also have to
:ref:`merge them between branches <branch-merge>`.  For example, if both ``3.5``
and ``default`` have multiple heads, you should first merge heads in ``3.5``,
then merge heads in ``default``, and finally merge ``3.5`` with ``default``
using ``hg merge 3.5`` as usual.

In order to avoid this, you should *always remember to pull and update before
committing*.


How do I undo the changes made in a recent commit?
''''''''''''''''''''''''''''''''''''''''''''''''''

First, this should not happen if you take the habit of :ref:`reviewing changes
<hg-status>` before committing them.

In any case, run::

 hg backout <revision number>

This will modify your working copy so that all changes in ``<revision number>``
(including added or deleted files) are undone.  You then need to :ref:`commit
<hg-commit>` these changes so that the backout gets permanently recorded.

.. note::
   These instructions are for Mercurial 1.7 and higher.  ``hg backout`` has
   a slightly different behaviour in versions before 1.7.
