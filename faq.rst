Content-type: text/x-rst
Title: Frequently Asked Questions for Python Developers

:Title: Frequently Asked Questions for Python Developers
:Date: $Date: 2010-09-15 07:35:08 -0700 (Wed, 15 Sep 2010) $
:Version: $Revision: 10931 $
:Web site: http://www.python.org/dev/faq/

.. contents:: :depth: 3
.. sectnum::

General Information
=====================================================================

Where do I start?
-----------------

The `dev page`_ links to various documents to help get you
started.

.. _dev page: /dev/


How can I become a developer?
---------------------------------------------------------------------------

Contribute on a regular basis through patches and ask for commit
privileges once you have demonstrated a track record of being good
at fixing things.

(Raymond Hettinger commented on the
`School of Hard Knocks <http://mail.python.org/pipermail/python-dev/2002-September/028725.html>`_ required.)



Version Control
==================================

Where can I learn about the version control system used, Subversion (svn)?
-------------------------------------------------------------------------------

`Subversion`_'s (also known as ``svn``) official web site is at
http://subversion.apache.org/ .  A book on Subversion published by
`O'Reilly Media`_, `Version Control with Subversion`_, is available
for free online.

With Subversion installed, you can run the help tool that comes with
Subversion to get help::

  svn help

The man page for ``svn`` is rather scant and not very helpful.

.. _Subversion: http://subversion.apache.org/
.. _O'Reilly Media: http://www.oreilly.com/
.. _Version Control with Subversion: http://svnbook.red-bean.com/


What do I need to use Subversion?
-------------------------------------------------------------------------------

.. _download Subversion: http://subversion.apache.org/packages.html

UNIX
'''''''''''''''''''

First, you need to `download Subversion`_.  Most UNIX-based operating systems
have binary packages available.  Also, most packaging systems also
have Subversion available.

If you have checkin rights, you need OpenSSH_.  This is needed to verify
your identity when performing commits.

.. _OpenSSH: http://www.openssh.org/

Windows
'''''''''''''''''''

You have several options on Windows.  One is to `download Subversion`_ itself
which will give you a command-line version.  Another option is to `download
TortoiseSVN`_ which integrates with Windows Explorer.

If you have checkin rights, you will also need an SSH client.
`Download PuTTY and friends`_ (PuTTYgen, Pageant, and Plink) for this.  All
other questions in this FAQ will assume you are using these tools.

Once you have both Subversion and PuTTY installed you must tell Subversion
where to find an SSH client.  Do this by editing
``%APPDATA%\Subversion\config`` to have the following
section::

  [tunnels]
  ssh="c:/path/to/putty/plink.exe" -T

Change the path to be the proper one for your system.  The ``-T``
option prevents a pseudo-terminal from being created.

You can use Pageant to prevent from having to type in your password for your
SSH 2 key constantly.  If you prefer not to have another program running,
you need to create a profile in PuTTY.

Go to Session:Saved Sessions and create a new profile named
``svn.python.org``.  In Session:Host Name, enter ``svn.python.org``.  In
SSH/Auth:Private key file select your private key.  In Connection:Auto-login
username enter ``pythondev``.

With this set up, paths are slightly different than most other settings in that
the username is not required.  Do take notice of this when choosing to check
out a project!

.. _download TortoiseSVN: http://tortoisesvn.net/downloads
.. _PuTTY: http://www.chiark.greenend.org.uk/~sgtatham/putty/
.. _download PuTTY and friends: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html


How do I get a checkout of the repository (read-only or read-write)?
-------------------------------------------------------------------------------

Regardless of whether you are checking out a read-only or read-write version of
the repository, the basic command is the same::

  svn checkout <URL> [PATH]

``<URL>`` is the specified location of the project within the repository that
you would like to check out (those paths are discussed later).  The optional
``[PATH]`` argument specifies the local directory to put the checkout into.  If
left out then the tail part of ``<URL>`` is used for the directory name.

For a read-only checkout, the format of ``<URL>`` is::

 http://svn.python.org/projects/<path>

with `<path>` representing the path to the project.  A list of projects can be
viewed at http://svn.python.org/view/ .  Any subdirectory may also
be checked out individually.

For a read-write checkout (with a caveat for Windows users using PuTTY without
Pageant), the format for ``<URL>`` is::

 svn+ssh://pythondev@svn.python.org/<path>

There are three critical differences between a read-only URL and a read-write
URL.  One is the protocol being specified as ``svn+ssh`` and not ``http``.
Next, the username ``pythondev`` is added (*note* that
Windows users using PuTTY without Pageant should leave off ``pythondev@`` if
PuTTY was set up following the instructions in this FAQ).  Lastly, note that
``projects`` was removed from the path entirely for a read-write checkout.

The repositories most people will be interested in are:

=========== ============================================================== ==========================================================================
Repository  read-only                                                      read-write
----------- -------------------------------------------------------------- --------------------------------------------------------------------------
PEPs        http://svn.python.org/projects/peps/trunk                      svn+ssh://pythondev@svn.python.org/peps/trunk
2.7         http://svn.python.org/projects/python/branches/release27-maint svn+ssh://pythondev@svn.python.org/python/branches/release27-maint
3.1         http://svn.python.org/projects/python/branches/release31-maint svn+ssh://pythondev@svn.python.org/python/branches/release31-maint
3.2         http://svn.python.org/projects/python/branches/py3k            svn+ssh://pythondev@svn.python.org/python/branches/py3k
=========== ============================================================== ==========================================================================


How do I update my working copy to be in sync with the repository?
-------------------------------------------------------------------------------

Run::

 svn update

from the directory you wish to update.  The directory and all its
subdirectories will be updated.


How do I browse the source code through a web browser?
-------------------------------------------------------------------------------

Visit http://svn.python.org/view/ to browse the Subversion repository.


Where can I find a downloadable snapshot of the source code?
-------------------------------------------------------------------------------

Visit http://svn.python.org/snapshots/ to download a tarball containing a daily
snapshot of the repository.


Who has commit privileges on the Subversion repository?
-------------------------------------------------------------------------------

See http://www.python.org/dev/committers for a list of committers.


How do I verify that my commit privileges are working?
-------------------------------------------------------------------------------

UNIX
'''''''''''''''''''

If you are listed as a committer at http://www.python.org/dev/committers , then
you should be able to execute::

  ssh pythondev@svn.python.org

and have the following printed to your terminal::

  ( success ( 2 2 ( ) ( edit-pipeline svndiff1 absent-entries
    commit-revprops depth log-revprops partial-replay ) ) )

If something else is printed, then there is a problem with your SSH 2 public
key and you should contact pydotorg@python.org .

Windows
'''''''''''''''''''

If you are using Pageant, you can verify that your SSH 2 key is set up properly
by running::

  c:\path\to\putty\plink.exe pythondev@svn.python.org

Using the proper path to your PuTTY installation, you should get a response
from the server that says::

  ( success ( 1 2 ( ANONYMOUS EXTERNAL ) ( edit-pipeline ) ) )

If there is a failure, run ``plink`` with ``-v`` to analyse the problem.

If you are using a profile in PuTTY, the best way to test is to try to log in
through Open.


What configuration settings should I use?
-------------------------------------------------------------------------------

Make sure the following settings are in your Subversion config file
(``~/.subversion/config`` under UNIX)::

 [miscellany]
 enable-auto-props = yes

 [auto-props]
 * = svn:eol-style=native
 *.c = svn:keywords=Id
 *.h = svn:keywords=Id
 *.py = svn:keywords=Id
 *.txt = svn:keywords=Author Date Id Revision

The ``[auto-props]`` line specifies the beginning of the section in the config
file.  The ``svn:eol-style`` setting tells Subversion to check out files using
the native line endings on your OS.  It will also automatically convert line
endings upon committal so that they are consistent across all platforms.  The
``svn:keywords`` settings are to automatically substitute ``$keyword$``
arguments in files that match the pattern.  ``*.txt`` has more options so as to
cover all needed keywords for PEPs_.

The ``[miscellany]`` section and its one option make Subversion apply the
various rules in the ``[auto-props]`` section automatically to all added or
imported files into the respository.

.. _PEPs: http://www.python.org/dev/peps/


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
branch for future merging from the source branch so as to keep them in sync.
To find out how to do that, read `How do I merge between branches?`_.


What tools do I need to merge between branches?
-----------------------------------------------

You need `svnmerge.py
<http://svn.apache.org/repos/asf/subversion/trunk/contrib/client-side/svnmerge/svnmerge.py>`__.


How do I prepare a new branch for merging?
------------------------------------------

You need to initialize a new branch by having ``svnmerge.py`` discover the
revision number that the branch was created with.  Do this with the command::

    svnmerge.py init

Then check in the change to the root of the branch.  This is a one-time
operation (i.e. only when the branch is originally created, not when each
developer creates a local checkout for the branch).


How do I merge between branches?
--------------------------------

In the current situation for Python there are four branches under development,
meaning that there are three branches to merge into. Assuming a change is
committed into ``trunk`` as revision 0001, you merge into the 2.x maintenance
by doing::

    # In the 2.x maintenance branch checkout.
    svnmerge.py merge -r 0001
    svn commit -F svnmerge-commit-message.txt  # r0002

To pull into py3k::

    # In a py3k checkout.
    svnmerge.py merge -r 0001
    svn commit -F svnmerge-commit-message.txt  # r0003

The 3.x maintenance branch is a special case as you must pull from the py3k
branch revision, *not* trunk::

    # In a 3.x maintenance checkout.
    svnmerge.py merge -r 0003  # Notice the rev is the one from py3k!
    svn resolved .
    svn commit -F svnmerge-commit-message.txt


How do I block a specific revision from being merged into a branch?
-------------------------------------------------------------------

With the revision number that you want to block handy and ``svnmerge.py``, go
to your checkout of the branch where you want to block the revision and run::

    svnmerge.py block -r <revision #>

This will modify the repository's top directory (which should be your current
directory) and create ``svnmerge-commit-message.txt`` which contains a
generated log message.

If the command says "no available revisions to block", then it means someone
already merged the revision.

To check in the new metadata, run::

    svn ci -F svnmerge-commit-message.txt


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


Compilation
=====================================================================

How do I create a debug build of Python?
-----------------------------------------

A debug build, sometimes called a "pydebug" build, has extra checks and bits of
information to help with developing Python.

UNIX
'''''''''''''''''''''''

The basic steps for building Python for development is to configure it and
then compile it.

Configuration is typically::

  ./configure --prefix=/dev/null --with-pydebug

More flags are available to ``configure``, but this is the minimum you should
do. This will give you a debug version of Python along with a safety measure
to prevent you from accidentally installing your development version over
your system install. If you are developing on OS X for Python 2.x and will not
be working with the OS X-specific modules from the standard library, then
consider using the ``--without-toolbox-glue`` flag to faster compilation time.

Once ``configure`` is done, you can then compile Python.::

    make -s

This will build Python with only warnings and errors being printed to
stderr. If you are using a multi-core machine you can use the ``-j`` flag
along with the number of cores your machine has
(e.g. with two cores, you would want ``make -s -j2``)
to compile multiple files at a time.

Once Python is done building you will then have a working build of Python
that can be run in-place; ``./python`` on most machines, ``./python.exe``
on OS X.

Windows
'''''''''''''''''''''''''

For VC 9, the ``PCbuild`` directory contains the build
files. For older versions of VC, see the ``PC`` directory. For a free
compiler for Windows, go to http://www.microsoft.com/express/ .

To build from the GUI, load the project files and press F7. Make sure to
choose the Debug build. If you want to build from the command line, run the
``build_env.bat`` file to get a terminal with proper environment variables.
From that terminal, run::

    build.bat -c Debug

Once built you will want to set Python as a startup project. F5 will
launch the interpreter as well as double-clicking the binary.


Editors and Tools
=====================================================================

What support is included in Python's source code for Vim?
---------------------------------------------------------

Within the ``Misc/Vim`` directory you will find two files to help you when
editing Python code. One is ``python.vim``, which is a generated syntax
highlight file for Python code. This file is updated much more frequently as it
contains syntax highlighting for keywords as they are added to the source tree.
See the top of the file to find out how to use the file.

The other file for Vim is a vimrc file that supports PEP 7 and 8 coding
standards. All settings are specific to Python and C code and thus will not
affect other settings. There are also some settings which are helpful but
turned off by default at the end of the file if one cares to use non-essential
settings. Once again, see the top of the file to learn how to take advantage of
the file.


What support is included in Python's source code for gdb?
----------------------------------------------------------

The ``Misc/gdbinit`` file contains several helpful commands that can be added
to your gdb session. You can either copy the commands into your own
``.gdbinit`` file or, if you don't have your own version of the file, simply
symlink ``~/.gdbinit`` to ``Misc/gdbinit``.


Can I run Valgrind against Python?
----------------------------------

Because of how Python uses memory, Valgrind requires setting some suppression
rules to cut down on the false positives (which still occur, suggesting one
typically should know how Python uses memory before running Valgrind against
Python). See ``Misc/README.valgrind`` for more details.


Patches
=====================================================================

How to make a patch?
-------------------------


If you are using subversion (anonymous or developer) you can use
subversion to make the patches for you. Just edit your local copy and
enter the following command::

  svn diff | tee ~/name_of_the_patch.diff

Else you can use the diff util which comes with most operating systems (a
Windows version is available as part of the cygwin tools).


How do I apply a patch?
-------------------------

For the general case, to apply a patch go to the directory that the patch was
created from (usually /dist/src/) and run::

  patch -p0 < name_of_the_patch.diff

The ``-p`` option specifies the number of directory separators ("/" in the
case of UNIX) to remove from the paths of the files in the patch.  ``-p0``
leaves the paths alone.


How do I undo an applied patch?
-------------------------------

Undoing a patch differs from applying one by only a command-line option::

  patch -R -p0 < name_of_the_patch.diff

Another option is to have 'patch' create backups of all files by using the
``-b`` command-line option.  See the man page for 'patch' on the details of
use.


How to submit a patch?
---------------------------

Please consult the patch submission guidelines at
http://www.python.org/patches/ .


How to test a patch?
------------------------------

Firstly, you'll need to get a checkout of the source tree you wish to
test the patch against and then build python from this source tree.

Once you've done that, you can use Python's extensive regression test
suite to check that the patch hasn't broken anything.

In general, for thorough testing, use::

  python -m test.regrtest -uall

For typical testing use::

  python -m test.regrtest

For running specific test modules::

  python -m test.regrtest test_mod1 test_mod2

NB: Enabling the relevant test resources via ``-uall`` or something more
specific is especially important when working on things like the
networking code or the audio support - many of the relevant tests are
skipped by default.

For more thorough documentation,
read the documentation for the ``test`` package at
http://docs.python.org/library/test.html.

If you suspect the patch may impact other operating systems, test as
many as you have easy access to.  You can get help on alternate
platforms by contacting the people listed on
http://www.python.org/moin/PythonTesters, who have
volunteered to support a particular operating system.


How to change the status of a patch?
-----------------------------------------


To change the status of a patch or assign it to somebody else you have to
have the Developer role in the bug tracker. Contact one of the project
administrators if the following does not work for you.

Click on the patch itself. In the screen that comes up, there is a drop-box
for "Assigned To:" and a drop-box for "Status:" where you can select a new
responsible developer or a new status respectively. After selecting the
appropriate victim and status, hit the "Submit Changes" button at the bottom
of the page.

Note: If you are sure that you have the right permissions and a drop-box
does not appear, check that you are actually logged in to Roundup!


Bugs
=====================================================================

Where can I submit/view bugs for Python?
---------------------------------------------


The Python project uses Roundup for bug tracking. Go to
http://bugs.python.org/ for all bug management needs. You will need to
create a Roundup account for yourself before submitting the first bug
report; anonymous reports have been disabled since it was too
difficult to get in contact with submitters. If you previously
had used SourceForge to report Python bugs, you can use Roundup's
"Lost your login?" link to obtain your Roundup password.
