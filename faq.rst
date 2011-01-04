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


How can I become a developer?
---------------------------------------------------------------------------

Contribute on a regular basis through patches and ask for commit
privileges once you have demonstrated a track record of being good
at fixing things.

(Raymond Hettinger commented on the
`School of Hard Knocks <http://mail.python.org/pipermail/python-dev/2002-September/028725.html>`_ required.)



Version Control
==================================


What do I need to use Subversion?
-------------------------------------------------------------------------------

.. _download Subversion: http://subversion.apache.org/packages.html

UNIX
'''''''''''''''''''

If you have checkin rights, you need OpenSSH_.  This is needed to verify
your identity when performing commits.

.. _OpenSSH: http://www.openssh.org/

Windows
'''''''''''''''''''

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
