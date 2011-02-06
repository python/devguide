.. _faq:

Python Developer FAQ
~~~~~~~~~~~~~~~~~~~~

Version Control
==================================

Where can I learn about the version control system used, Mercurial (hg)?
-------------------------------------------------------------------------------

`Mercurial`_'s (also known as ``hg``) official web site is at
http://mercurial.selenic.com/.  A book on Subversion published by
`O'Reilly Media`_, `Mercurial: The Definitive Guide`_, is available
for free online.

With Mercurial installed, you can run the help tool that comes with
Mercurial to get help::

  hg help

The man page for ``hg`` provides a quick refresher on the details of
various commands, but doesn't provide any guidance on overall
workflow.

.. _Mercurial: http://mercurial.selenic.com/
.. _O'Reilly Media: http://www.oreilly.com/
.. _Mercurial\: The Definitive Guide: http://hgbook.red-bean.com/


What do I need to use Mercurial?
-------------------------------------------------------------------------------

.. _download Mercurial: http://mercurial.selenic.com/downloads/

UNIX
'''''''''''''''''''

First, you need to `download Mercurial`_.  Most UNIX-based operating systems
have binary packages available.  Most package management systems also
have native Mercurial packages available.

If you have checkin rights, you need OpenSSH_.  This is needed to verify
your identity when performing commits. As with Mercurial, binary packages
are typically available either online or through the platform's package
management system.

.. _OpenSSH: http://www.openssh.org/

Windows
'''''''''''''''''''

XXX: The following instructions need verification. They're based on
the old SVN instructions plus the info at
http://mercurial.selenic.com/wiki/AccessingSshRepositoriesFromWindows
and https://bitbucket.org/tortoisehg/stable/wiki/ssh

You have several options on Windows.  One is to `download Mercurial`_ itself
which will give you a command-line version.  Another option is to `download
TortoiseHg`_ which integrates with Windows Explorer. Note that this FAQ only
covers the command line client in detail - refer to the TortoiseHg
documentation for assistance with that tool.

If you have checkin rights, you will also need an SSH client.
`Download PuTTY and friends`_ (PuTTYgen, Pageant, and Plink) for this.  All
other questions in this FAQ will assume you are using these tools.

Once you have both Mercurial and PuTTY installed you must tell Subversion
where to find an SSH client.  Do this by editing
``%APPDATA%\Mercurial.ini`` to add the following entry (use the existing
``[ui]`` section if one is already present)::

  [ui]
  ssh="c:/path/to/putty/plink.exe" -T

Change the path to be the proper one for your system.  The ``-T``
option prevents a pseudo-terminal from being created.

You can use Pageant to prevent from having to type in your password for your
SSH 2 key constantly.  If you prefer not to have another program running,
you need to create a profile in PuTTY.

Go to Session:Saved Sessions and create a new profile named
``hg.python.org``.  In Session:Host Name, enter ``hg.python.org``.  In
SSH/Auth:Private key file select your private key.  In Connection:Auto-login
username enter ``hg``.

XXX: Does the following comment still apply to TortoiseHg?
With this set up, paths are slightly different than most other settings in that
the username is not required.  Do take notice of this when choosing to check
out a project!

.. _download TortoiseHg: http://tortoisehg.bitbucket.org/download/index.html
.. _PuTTY: http://www.chiark.greenend.org.uk/~sgtatham/putty/
.. _download PuTTY and friends: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html


How do I link my local repository to a particular remote repository?
-------------------------------------------------------------------------------

In ``.hg/hgrc`` file for the relevant local repository, add the following section::

  [paths]
  default = ssh://hg@hg.python.org/devguide

This example is for a local repository that mirrors the ``devguide`` repository
on ``hg.python.org``. The same approach works for other remote repositories.


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


How do I compare my working copy to a remote repository?
-------------------------------------------------------------------------------

First, retrieve and enable the `Rdiff extension` for Mercurial.

The following command will then show the effect of updating the working copy
to match that remote repository::

  hg diff <remote repository>``

To instead see the effects of applying the changes in the current working copy
to that remote repository, simply reverse the diff::

  hg diff --reverse <remote repository>

By executing them in a pristine working copy, these same commands work to
diff the local repository against a remote repository.

.. _Rdiff extension: http://mercurial.selenic.com/wiki/RdiffExtension


How do I update my working copy to be in sync with a remote repository?
-------------------------------------------------------------------------------

Run::

 hg pull <remote repository>
 hg update

from the directory you wish to update.  The first command retrieves any
changes from the specified remote repository and merges them into the local
repository. The second commands updates the current directory and all its
subdirectories from the local repository.


How do I add a file or directory to the repository?
-------------------------------------------------------------------------------

Simply specify the path to the file or directory to add and run::

 svn add PATH

Subversion will skip any directories it already knows about.  But if
you want new files that exist in any directories specified in ``PATH``, specify
``--force`` and Subversion will check *all* directories for new files.

You will then need to run ``svn commit`` (as discussed in
`How do I commit a change to a file?`_) to commit the file to the repository.


How do I commit a change to a file?
-------------------------------------------------------------------------------

To have any changes to a file (which include adding a new file or deleting an
existing one), you use the command::

 svn commit [PATH]

Although ``[PATH]`` is optional, if PATH is omitted all changes
in your local copy will be committed to the repository.
**DO NOT USE THIS!!!**  You should specify the specific files
to be committed unless you are *absolutely* positive that
*all outstanding modifications* are meant to go in this commit.

To abort a commit that you are in the middle of, leave the message
empty (i.e., close the text editor without adding any text for the
message).  Subversion will confirm if you want to abort the commit.

If you do not like the default text editor Subversion uses for
entering commmit messages, you may specify a different editor
in your Subversion config file with the
``editor-cmd`` option in the ``[helpers]`` section.


How do I delete a file or directory in the repository?
-------------------------------------------------------------------------------

Specify the path to be removed with::

 svn delete PATH

Any modified files or files that are not checked in will not be deleted
in the working copy on your machine.


What files are modified locally in my working copy?
-------------------------------------------------------------------------------

Running::

 svn status [PATH]

will list any differences between your working copy and the repository.  Some
key indicators that can appear in the first column of output are:

=  ===========================
A  Scheduled to be added

D  Scheduled to be deleted

M  Modified locally

?  Not under version control
=  ===========================


How do I find out what Subversion properties are set for a file or directory?
-------------------------------------------------------------------------------

::

 svn proplist PATH


How do I revert a file I have modified back to the version in the respository?
-------------------------------------------------------------------------------

Running::

 svn revert PATH

will change ``PATH`` to match the version in the repository, throwing away any
changes you made locally.  If you run::

 svn revert -R .

from the root of your local repository it will recursively restore everything
to match up with the main server.


How do I find out who edited or what revision changed a line last?
-------------------------------------------------------------------------------

You want::

 svn blame PATH

This will output to stdout every line of the file along with what revision
number last touched that line and who committed that revision.  Since it is
printed to stdout, you probably want to pipe the output to a pager::

 svn blame PATH | less


How can I see a list of log messages for a file or specific revision?
---------------------------------------------------------------------

To see the log messages for a specific file, run::

 svn log PATH

That will list all messages that pertain to the file specified in ``PATH``.

If you want to view the log message for a specific revision, run::

 svn log --verbose -r REV

With ``REV`` substituted with the revision number.  The ``--verbose`` flag
should be used to get a listing of all files modified in that revision.


How can I edit the log message of a committed revision?
-------------------------------------------------------------------------------

Use::

 svn propedit -r <revision> --revprop svn:log

Replace ``<revision>`` with the revision number of the commit whose log message
you wish to change.


How do I get a diff between the repository and my working copy for a file?
-------------------------------------------------------------------------------

The diff between your working copy and what is in the repository can be had
with::

 svn diff PATH

This will work off the current revision in the repository.  To diff your
working copy with a specific revision, do::

 svn diff -r REV PATH

Finally, to generate a diff between two specific revisions, use::

 svn diff -r REV1:REV2 PATH

Notice the ``:`` between ``REV1`` and ``REV2``.


How do I undo the changes made in a recent committal?
-------------------------------------------------------------------------------

Assuming your bad revision is ``NEW`` and ``OLD`` is the equivalent of ``NEW
- 1``, then run::

 svn merge -r NEW:OLD PATH

This will revert *all* files back to their state in revision ``OLD``.
The reason that ``OLD`` is just ``NEW - 1`` is you do not want files to be
accidentally reverted to a state older than your changes, just to the point
prior.

Note:  PATH here refers to the top of the checked out repository,
not the full pathname to a file.  PATH can refer to a different
branch when merging from the head, but it must still be the top
and not an individual file or subdirectory.


How do I update to a specific release tag?
-------------------------------------------------------------------------------

Run::

    svn list svn+ssh://pythondev@svn.python.org/python/tags

or visit::

    http://svn.python.org/view/python/tags/

to get a list of tags.  To switch your current sandbox to a specific tag,
run::

    svn switch svn+ssh://pythondev@svn.python.org/python/tags/r242

To just update to the revision corresponding to that tag without changing
the metadata for the repository, note the revision number corresponding to
the tag of interest and update to it, e.g.::

    svn update -r 39619


Why should I use ``svn switch``?
-------------------------------------------------------------------------------

If you picture each file/directory in Subversion as uniquely identified
by a 2-space coordinate system [URL, revision] (given a checkout, you can
use "svn info" to get its coordinates), then we can say that "svn up -r N"
(for some revision number N) keeps the url unchanged and changes the
revision to whatever number you specified.  In other words, you get the
state of the working copy URL at the time revision N was created.  For
instance, if you execute it with revision 39619 within the trunk working
copy, you will get the trunk at the moment 2.4.2 was released.

On the other hand, "svn switch" moves the URL: it basically "moves" your
checkout from [old_URL, revision] to [new_URL, HEAD], downloading the
minimal set of diffs to do so.  If the new_URL is a tag URL
(e.g. .../tags/r242), it means any revision is good, since nobody is going
to commit into that directory (it will stay unchanged forever).  So
[/tags/r242, HEAD] is the same as any other [/tags/r242, revision] (assuming
of course that /tags/r242 was already created at the time the revision was
created).

If you want to create a sandbox corresponding to a particular release tag,
use svn switch to switch to [/tags/some_tag, HEAD] if you don't plan on
doing modifications.  On the other hand if you want to make modifications to
a particular release branch, use svn switch to change to
[/branches/some_branch, HEAD].

(Written by Giovanni Bajo on python-dev.)


How do I create a branch?
-------------------------

The best way is to do a server-side copy by specifying the URL for the source
of the branch, and the eventual destination URL for the new branch::

    svn copy SRC_URL DEST_URL

You can then checkout your branch as normal.  You will want to prepare your
branch for future merging from the source branch so as to keep them in sync
using svnmerge.py.


How do I include an external svn repository (external definition) in the repository?
------------------------------------------------------------------------------------

Before attempting to include an external svn repository into Python's
repository, it is important to realize that you can only include directories,
not individual files.

To include a directory of an external definition (external svn repository) as a
directory you need to edit the ``svn:externals`` property on the root of the
repository you are working with using the format of::

  local_directory remote_repositories_http_address

For instance, to include Python's sandbox repository in the 'sandbox' directory
of your repository, run ``svn propedit svn:externals .`` while in the root of
your repository and enter::

  sandbox http://svn.python.org/projects/sandbox/trunk/

in your text editor.  The next time you run ``svn update`` it will pull in the
external definition.


How can I create a directory in the sandbox?
------------------------------------------------------------------------------

Assuming you have commit privileges and you do not already have a complete
checkout of the sandbox itself, the easiest way is to use svn's ``mkdir``
command::

  svn mkdir svn+ssh://pythondev@svn.python.org/sandbox/trunk/<directory>

That command will create the new directory on the server.  To gain access to
the new directory you then checkout it out (substitute ``mkdir`` in the command
above with ``checkout``).

If you already have a complete checkout of the sandbox then you can just use
``svn mkdir`` on a local directory name and check in the new directory itself.


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

This will generate a two files; your public key and your private key.  Your
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

Windows
'''''''''''''''''''

Running Pageant_ will prevent you from having to type your password constantly.
If you add a shortcut to Pageant to your Autostart group and edit the shortcut
so that the command line includes an argument to your private key then Pageant
will load the key every time you log in.


.. _Pageant: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html

Can I make check-ins from machines other than the one I generated the keys on?
------------------------------------------------------------------------------

Yes, all you need is to make sure that the machine you want to check
in code from has both the public and private keys in the standard
place that ssh will look for them (i.e. ~/.ssh on Unix machines).
Please note that although the key file ending in .pub contains your
user name and machine name in it, that information is not used by the
verification process, therefore these key files can be moved to a
different computer and used for verification.  Please guard your keys
and never share your private key with anyone.  If you lose the media
on which your keys are stored or the machine on which your keys are
stored, be sure to report this to pydotorg@python.org at the same time
that you change your keys.
