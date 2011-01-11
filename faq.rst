Content-type: text/x-rst
Title: Frequently Asked Questions for Python Developers

:Title: Frequently Asked Questions for Python Developers
:Date: $Date: 2010-09-15 07:35:08 -0700 (Wed, 15 Sep 2010) $
:Version: $Revision: 10931 $
:Web site: http://www.python.org/dev/faq/

.. contents:: :depth: 3
.. sectnum::


Version Control
==================================


What do I need to use Subversion?
-------------------------------------------------------------------------------

.. _download Subversion: http://subversion.apache.org/packages.html


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


What support is included in Python's source code for gdb?
----------------------------------------------------------

The ``Misc/gdbinit`` file contains several helpful commands that can be added
to your gdb session. You can either copy the commands into your own
``.gdbinit`` file or, if you don't have your own version of the file, simply
symlink ``~/.gdbinit`` to ``Misc/gdbinit``.



Patches
=====================================================================


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


