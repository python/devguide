.. _faq:

Python Developer FAQ
~~~~~~~~~~~~~~~~~~~~

Version Control
==================================

Where can I learn about the version control system used, Mercurial (hg)?
-------------------------------------------------------------------------------

Mercurial_'s (also known as ``hg``) official web site is at
http://mercurial.selenic.com/.  A book on Mercurial published by
`O'Reilly Media`_, `Mercurial: The Definitive Guide`_, is available
for free online.

With Mercurial installed, you can run the help tool that comes with
Mercurial to get help::

  hg help

The `man page`_ for ``hg`` provides a quick refresher on the details of
various commands, but doesn't provide any guidance on overall
workflow.

.. _Mercurial: http://mercurial.selenic.com/
.. _O'Reilly Media: http://www.oreilly.com/
.. _Mercurial\: The Definitive Guide: http://hgbook.red-bean.com/
.. _man page: http://www.selenic.com/mercurial/hg.1.html


What do I need to use Mercurial?
-------------------------------------------------------------------------------

UNIX
'''''''''''''''''''

First, you need to `download Mercurial`_.  Most UNIX-based operating systems
have binary packages available.  Most package management systems also
have native Mercurial packages available.

If you have push rights, you need OpenSSH_.  This is needed to verify
your identity when performing commits. As with Mercurial, binary packages
are typically available either online or through the platform's package
management system.

.. _download Mercurial: http://mercurial.selenic.com/downloads/
.. _OpenSSH: http://www.openssh.org/


Windows
'''''''''''''''''''

The recommended option on Windows is to `download TortoiseHg`_ which
integrates with Windows Explorer and also bundles the command line client
(meaning you can type ``hg`` in a DOS box).  Note that most
entries in this FAQ only cover the command line client in detail - refer
to the TortoiseHg documentation for assistance with its graphical interface.

If you have push rights, you need to configure Mercurial to work with
your SSH keys.  For that, open your Mercurial configuration file
(you can do so by opening the TortoiseHg configuration dialog and then
clicking *"Edit File"*).  In the ``[ui]`` section, add the following line::

   ssh = TortoisePlink.exe -ssh -2 -C -i C:\path\to\yourkey.ppk

where ``C:\path\to\yourkey.ppk`` should be replaced with the actual path
to your SSH private key.

.. note::
   If your private key is in OpenSSH format, you must first convert it to
   PuTTY format by loading it into `PuTTYgen`_.

.. _download TortoiseHg: http://tortoisehg.bitbucket.org/download/index.html


What's a working copy? What's a repository?
-------------------------------------------

Mercurial is a "distributed" version control system.  This means that each
participant, even casual contributors, download a complete copy (called a
*clone*, since it is obtained by calling ``hg clone``) of the central
repository which can be treated as a stand-alone repository for all purposes.
That copy is called in the FAQ the *local repository*, to differentiate
with any *remote repository* you might also interact with.

But you don't modify files directly in the local repository; Mercurial doesn't
allow for it.  You modify files in what's called the *working copy* associated
with your local repository: you also run compilations and tests there.
Once you are satisfied with your changes, you can :ref:`commit them <hg-commit>`;
committing records the changes as a new *revision* in the *local repository*.

Changes in your *local repository* don't get automatically shared with the
rest of the world.  Mercurial ensures that you have to do so explicitly
(this allows you to experiment quite freely with multiple branches of
development, all on your private computer).  The main commands for doing
so are ``hg pull`` and ``hg push``.


Which branches are in my local repository?
------------------------------------------

Typing ``hg branches`` displays the open branches in your local repository::

   $ hg branches
   default                    68026:f12ef116dd10
   3.2                        68025:cef92ee1a323
   2.7                        68010:8174d00d0797
   3.1                        67955:5be8b695ea86
   2.6                        67287:5e26a860eded
   2.5                        65464:e4ecac76e499


Why are some branches marked "inactive"?
----------------------------------------

Assuming you get the following output::

   $ hg branches
   default                    68042:8ff33af017ef
   3.2                        68039:c17d7772c638 (inactive)

This means all changesets in the "3.2" branch have been merged into the
"default" branch (or any other branch, if such exists).


.. _hg-current-branch:

Which branch is currently checked out in my working copy?
---------------------------------------------------------

Use::

   $ hg branch
   default

Or to get more information::

   $ hg summary
   parent: 68026:f12ef116dd10 tip
    In FTP.close() method, make sure to also close the socket object, not only the file.
   branch: default
   commit: (clean)
   update: (current)


.. _hg-switch-branches:

How do I switch between branches inside my working copy?
--------------------------------------------------------

Simply use ``hg update`` to checkout another branch in the current directory::

   $ hg branch
   default
   $ hg update 3.2
   86 files updated, 0 files merged, 11 files removed, 0 files unresolved
   $ hg branch
   3.2

Adding the ``-v`` option to ``hg update`` will list all updated files.


I want to keep a separate working copy per development branch, is it possible?
------------------------------------------------------------------------------

Just clone your local repository and update each clone to a different branch::

   $ hg clone cpython py32
   updating to branch default
   3434 files updated, 0 files merged, 0 files removed, 0 files unresolved
   $ cd py32
   $ hg update 3.2
   86 files updated, 0 files merged, 11 files removed, 0 files unresolved

The current branch in a working copy is "sticky": if you pull in some new
changes, ``hg update`` will update to the head of the *current branch*.


How do I link my local repository to a particular remote repository?
-------------------------------------------------------------------------------

Your local repository is linked by default to the remote repository it
was *cloned* from.  If you created it from scratch, however, it is not linked
to any remote repository.  In ``.hg/hgrc`` file for the local repository, add
or modify the following section::

  [paths]
  default = ssh://hg@hg.python.org/devguide

This example is for a local repository that mirrors the ``devguide`` repository
on ``hg.python.org``. The same approach works for other remote repositories.

Anywhere that ``<remote repository>`` is used in the commands in this
FAQ, ``hg`` will use the default remote repository if you omit the parameter.


How do I create a shorthand alias for a remote repository?
-------------------------------------------------------------------------------

In your global ``.hgrc`` file add a section similar to the following::

  [paths]
  dg = ssh://hg@hg.python.org/devguide

This example creates a ``dg`` alias for the ``devguide`` repository
on ``hg.python.org``. This allows "dg" to be entered instead of the
full URL for commands taking a repository argument (e.g. ``hg pull dg`` or
``hg outgoing dg``).

Anywhere that ``<remote repository>`` is used in the commands in this
FAQ, ``hg`` should accept an alias in place of a complete remote URL.


How do I compare my local repository to a remote repository?
-------------------------------------------------------------------------------

To display the list of changes that are in your local repository, but not
in the remote, use::

 hg outgoing <remote repository>

This is the list of changes that will be sent if you call
``hg push <remote repository>``.  It does **not** include any :ref:`uncommitted
changes <hg-status>` in your working copy!

Conversely, for the list of changes that are in the remote repository but
not in the local, use::

 hg incoming <remote repository>

This is the list of changes that will be retrieved if you call
``hg pull <remote repository>``.

.. note::
   In most daily use, you will work against the default remote repository,
   and therefore simply type ``hg outgoing`` and ``hg incoming``.

   In this case, you can also get a synthetic summary using
   ``hg summary --remote``.


How do I update my local repository to be in sync with a remote repository?
-------------------------------------------------------------------------------

Run::

   hg pull <remote repository>

from the repository you wish to pull the latest changes into.  Most of the
time, that repository is a clone of the repository you want to pull from,
so you can simply type::

   hg pull

This doesn't update your working copy, though.  See below:


How do I update my working copy with the latest changes?
--------------------------------------------------------

Do::

   hg update

This will update your working copy with the latest changes on the
:ref:`current branch <hg-current-branch>`.  If you had :ref:`uncommitted
changes <hg-status>` in your working copy, they will be merged in.

If you find yourself typing often ``hg pull`` followed by ``hg update``,
be aware that you can combine them in a single command::

   hg pull -u


.. _hg-local-workflow:

How do I apply a patch?
-------------------------------------------------------------------------------

If you want to try out or review a patch generated using Mercurial, do::

   hg import --no-commit somework.patch

This will apply the changes in your working copy without committing them.
If the patch was not created by Mercurial (for example, a patch created by
Subversion and thus lacking any ``a``/``b`` directory prefixes in the patch),
add ``-p0`` to the above command.

You can also use the ``patch`` program, but be aware that it does not
understand the `extended diff format`_ used by Mercurial.

If you want to work on the patch using mq_ (Mercurial Queues), type instead::

   hg qimport somework.patch

This will create a patch in your queue with a name that matches the filename.
You can use the ``-n`` argument to specify a different name.  To have the
patch applied to the working copy, type::

   hg qpush

Finally, to delete the patch, first un-apply it if necessary using ``hg qpop``,
then do::

   hg qdelete somework.patch

.. _extended diff format: http://www.selenic.com/mercurial/hg.1.html#diffs
.. _mq: http://mercurial.selenic.com/wiki/MqExtension


How do I add a file or directory to the repository?
-------------------------------------------------------------------------------

Simply specify the path to the file or directory to add and run::

 hg add PATH

If ``PATH`` is a directory, Mercurial will recursively add any files in that
directory and its descendents.

If you want Mercurial to figure out by itself which files should be added
and/or removed, just run::

 hg addremove

**Be careful** though, as it might add some files that are not desired in
the repository (such as build products, cache files, or other data).

You will then need to run ``hg commit`` (as discussed below) to commit
the file(s) to your local repository.


.. _hg-commit:

How do I commit a change to a file?
-------------------------------------------------------------------------------

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
   entering commmit messages, you may specify a different editor,
   either by changing the ``EDITOR`` environment variable or by setting
   a Mercurial-specific editor in your global ``.hgrc`` with the ``editor``
   option in the ``[ui]`` section.


How do I delete a file or directory in the repository?
-------------------------------------------------------------------------------

Specify the path to be removed with::

 hg remove PATH

This will remove the file or the directory from your working copy; you will
have to :ref:`commit your changes <hg-commit>` for the removal to be recorded
in your local repository.


.. _hg-status:

What files are modified in my working copy?
-------------------------------------------------------------------------------

Running::

 hg status

will list any pending changes in the working copy.  These changes will get
commited to the local repository if you issue an ``hg commit`` without
specifying any path.

Some
key indicators that can appear in the first column of output are:

   =  ===========================
   A  Scheduled to be added
   R  Scheduled to be removed
   M  Modified locally
   ?  Not under version control
   =  ===========================

If you want a line-by-line listing of the differences, use::

 hg diff


How do I revert a file I have modified back to the version in the repository?
-------------------------------------------------------------------------------

Running::

 hg revert PATH

will revert ``PATH`` to its version in the repository, throwing away any
changes you made locally.  If you run::

 hg revert -a

from the root of your working copy it will recursively restore everything
to match up with the repository.


How do I find out which revisions need merging?
-----------------------------------------------

In unambiguous cases, Mercurial will find out for you if you simply try::

   hg merge

If that fails and Mercurial asks for explicit revisions, running::

   hg heads

will give you the list of branch heads in your local repository.  If you are
working only in a particular named branch, for example ``default``, do::

   hg heads default

to display the heads on that branch.


How do I list the files in conflict after a merge?
--------------------------------------------------

Use::

   hg resolve --list

(abbreviated ``hg resolve -l``)


How I mark a file resolved after I have resolved merge conflicts?
-----------------------------------------------------------------

Type::

   hg resolve --mark <file path>

(abbreviated ``hg resolve -m <file path>``)

If you are sure you have resolved all conflicts, use ``hg resolve -am``.


How do I find out who edited or what revision changed a line last?
-------------------------------------------------------------------------------

You want::

 hg annotate PATH

This will output to stdout every line of the file along with which revision
last modified that line.  When you have the revision number, it is then
easy to :ref:`display it in detail <hg-log-rev>`.


.. _hg-log:

How can I see a list of log messages for a file or specific revision?
---------------------------------------------------------------------

To see the history of changes for a specific file, run::

 hg log -v [PATH]

That will list all messages of revisions which modified the file specified
in ``PATH``.  If ``PATH`` is omitted, all revisions are listed.

If you want to display line-by-line differences for each revision as well,
add the ``-p`` option::

 hg log -vp [PATH]

.. _hg-log-rev:

If you want to view the differences for a specific revision, run::

 hg log -vp -r <revision number>


How can I see the changeset graph in my repository?
---------------------------------------------------

In Mercurial repositories, changesets don't form a simple list, but rather
a graph: every changeset has one or two parents (it's called a merge changeset
in the latter case), and can have any number of children.

The graphlog_ extension is very useful for examining the structure of the
changeset graph.  It is bundled with Mercurial.

Graphical tools, such as TortoiseHG, will display the changeset graph
by default.

.. _graphlog: http://mercurial.selenic.com/wiki/GraphlogExtension


How do I undo the changes made in a recent commit?
-------------------------------------------------------------------------------

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


How do I update to a specific release tag?
-------------------------------------------------------------------------------

Run::

   hg tags

to get a list of tags.  To update your working copy to a specific tag, use::

   hg update <tag>


How come feature XYZ isn't available in Mercurial?
--------------------------------------------------

Mercurial comes with many bundled extensions which can be explicitly enabled.
You can get a list of them by typing ``hg help extensions``.  Some of these
extensions, such as ``color``, can prettify output; others, such as ``fetch``
or ``transplant``, add new Mercurial commands.

There are also many `configuration options`_ to tweak various aspects of the
command line and other Mercurial behaviour; typing `man hgrc`_ displays
their documentation inside your terminal.

In the end, please refer to the Mercurial `wiki`_, especially the pages about
`extensions`_ (including third-party ones) and the `tips and tricks`_.


.. _man hgrc: http://www.selenic.com/mercurial/hgrc.5.html
.. _wiki: http://mercurial.selenic.com/wiki/
.. _extensions: http://mercurial.selenic.com/wiki/UsingExtensions
.. _tips and tricks: http://mercurial.selenic.com/wiki/TipsAndTricks
.. _configuration options: http://www.selenic.com/mercurial/hgrc.5.html


SSH
=======

How do I generate an SSH 2 public key?
-------------------------------------------------------------------------------

All generated SSH keys should be sent to pydotorg for adding to the list of
keys.

UNIX
'''''''''''''''''''

Run::

  ssh-keygen -t rsa

This will generate two files; your public key and your private key.  Your
public key is the file ending in ``.pub``.

Windows
'''''''''''''''''''

Use PuTTYgen_ to generate your public key.  Choose the "SSH2 DSA" radio button,
have it create an OpenSSH formatted key, choose a password, and save the private
key to a file.  Copy the section with the public key (using Alt-P) to a file;
that file now has your public key.

.. _PuTTYgen: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html


Is there a way to prevent from having to enter my password for my SSH 2 public key constantly?
------------------------------------------------------------------------------------------------

UNIX
'''''''''''''''''''

Use ``ssh-agent`` and ``ssh-add`` to register your private key with SSH for
your current session.  The simplest solution, though, is to use KeyChain_,
which is a shell script that will handle ``ssh-agent`` and ``ssh-add`` for you
once per login instead of per session.

.. _KeyChain: http://www.gentoo.org/proj/en/keychain/


.. _pageant:

Windows
'''''''''''''''''''

The Pageant program is bundled with TortoiseHg.  You can find it in its
installation directory (usually ``C:\Program Files (x86)\TortoiseHg\``);
you can also `download it separately
<http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`_.

Running Pageant will prevent you from having to type your password constantly.
If you add a shortcut to Pageant to your Autostart group and edit the shortcut
so that the command line includes an argument to your private key then Pageant
will load the key every time you log in.


Can I make commits from machines other than the one I generated the keys on?
------------------------------------------------------------------------------

You can :ref:`make commits <hg-commit>` from any machine, since they will be
recorded in your *local repository*.

However, to push these changes to the remote server, you will need proper
credentials.  All you need is to make sure that the machine you want to
push changes from has both the public and private keys in the standard
place that ssh will look for them (i.e. ~/.ssh on Unix machines).
Please note that although the key file ending in .pub contains your
user name and machine name in it, that information is not used by the
verification process, therefore these key files can be moved to a
different computer and used for verification.  Please guard your keys
and never share your private key with anyone.  If you lose the media
on which your keys are stored or the machine on which your keys are
stored, be sure to report this to pydotorg@python.org at the same time
that you change your keys.
