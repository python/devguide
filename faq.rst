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
=========== ============================================================== ==========================================================================



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


