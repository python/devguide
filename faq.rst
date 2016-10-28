:tocdepth: 2

.. _faq:

Python Developer FAQ
~~~~~~~~~~~~~~~~~~~~

.. contents::
   :local:


Communications
==============

Where should I report specific problems?
----------------------------------------

Specific problems should be posted to the `issue tracker`_.

.. _issue tracker: https://bugs.python.org


What if I'm not sure it is a bug?
---------------------------------

The general Python help locations listed above are the best place to start
with that kind of question. If they agree it looks like a bug, then the
next step is to either post it to the `issue tracker`_ or else to ask further
on the core development mailing list, `python-dev`_.

.. _python-dev: http://mail.python.org/mailman/listinfo/python-dev


What if I disagree with an issue resolution on the tracker?
-----------------------------------------------------------

First, take some time to consider any comments made in association with the
resolution of the tracker issue. On reflection, they may seem more reasonable
than they first appeared.

If you still feel the resolution is incorrect, then raise the question on
`python-dev`_. If the consensus there supports the disputed resolution, please
take any further objections to `python-ideas`_ (or some other forum). Further
argument on `python-dev`_ after a consensus has been reached amongst the core
developers is unlikely to win any converts.

.. _python-ideas: https://mail.python.org/mailman/listinfo/python-ideas


How do I tell who is and isn't a core developer?
------------------------------------------------

You can check their name against the `full list of developers`_ with commit
rights to the main source control repository.

On the `issue tracker`_, most core developers will have the Python logo
appear next to their name.

.. _full list of developers: https://hg.python.org/committers.txt


Version Control
===============

The following FAQs are intended for both core developers and contributors.
Please realize that Git is a heavily-documented tool, so using your favorite
search engine to find an answer to your question will more than likely work.

Everyone
--------

Where can I learn about the version control system used, Git?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Git_'s official web site is at https://git-scm.com/.  A book on Git published
by Apress, `Pro Git`_, is available for free online.

With Git installed, you can run the help tool that comes with
Git to get help::

  git help

The `man page`_ for ``git`` provides a quick refresher on the various commands,
but doesn't provide any guidance on overall workflow. Each sub-command has a
more detailed manpage. You can view these by running a command such as::

    $ man git-pull

or following the links from the main `man page`_.

.. _Git: https://git-scm.com/
.. _Pro Git: https://git-scm.com/book/en/v2
.. _man page: https://www.kernel.org/pub/software/scm/git/docs/


What do I need to use Git?
''''''''''''''''''''''''''

First, you need to `download Git`_.  Most UNIX-based operating systems
have binary packages available.  Most package management systems also
have native Git packages available.

If you have push rights, you need OpenSSH_.  This is needed to verify
your identity when performing commits. As with Git, binary packages
are typically available either online or through the platform's package
management system.

.. _download Git: https://git-scm.com/downloads
.. _OpenSSH: http://www.openssh.org/


What's a working copy? What's a repository?
'''''''''''''''''''''''''''''''''''''''''''

Git is a "distributed" version control system.  This means that each
participant, even casual contributors, download a complete copy (called a
*clone*, since it is obtained by calling ``git clone``) of the central
repository which can be treated as a stand-alone repository for all purposes.
That copy is called in the FAQ the *local repository*, to differentiate
with any *remote repository* you might also interact with.

Changes in your *local repository* don't get automatically shared with the
rest of the world.  Git ensures that you have to do so explicitly
(this allows you to experiment quite freely with multiple branches of
development, all on your private computer).  The main commands for doing
so are ``git pull`` and ``git push``.


Which branches are in my local repository?
''''''''''''''''''''''''''''''''''''''''''

Typing ``git branch`` displays the open branches in your local repository::

    $ git branch
    * master
      2.7
      3.5
      3.4
      3.3
      3.2

.. _git-current-branch:

Which branch is currently checked out in my working copy?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Use::

   $ git branch
   * master

The asterisk (\*) next to the branch name denotes the current branch.

For more details about the current state of the repository, use::

    $ git status
    On branch master
    Your branch is up-to-date with 'origin/master'.
    nothing to commit, working directory clean


.. _git-switch-branches:

How do I switch between branches inside my working copy?
''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Simply use ``git checkout`` to checkout another branch in the current directory::

   $ git branch
   * master
     3.5
   $ git checkout 3.5
   Switched to branch '3.5'
   Your branch is up-to-date with 'origin/3.5'.
   $ git branch
     master
   * 3.5

Note that, due to some previously built executables being used as a part of
the build process, you may sometimes run into issues when attempting to
switch between Python 2.x and Python 3.x branches. In these cases, it is
best to run a ``make distclean`` to ensure that all previously built files
are removed.


I want to keep a separate working copy per development branch, is it possible?
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Create several clones of your local repository::

   $ git clone cpython py35
   Cloning into 'py35'...
   remote: Counting objects: 629890, done.
   remote: Total 629890 (delta 0), reused 0 (delta 0), pack-reused 629889
   Receiving objects: 100% (629890/629890), 216.81 MiB | 3.58 MiB/s, done.
   Resolving deltas: 100% (503219/503219), done.
   Checking connectivity... done.
   $ cd py35
   $ git checkout 3.5
   Switched to branch '3.5'
   Your branch is up-to-date with 'origin/3.5'.

.. _git-paths:

How do I link my local repository to a particular remote repository?
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Your local repository is linked by default to the remote repository it
was *cloned* from. If you would like to link to a different remote, first add
the remote::

    $ git remote add myremote <remote url>

Then set it as the upstream::

    $ git branch --set-upstream-to myremote/<branch name>


How do I compare my local repository to a remote repository?
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

To display the list of changes that are in your local repository, but not
in the remote, use::

    $ git log origin/master..

This is the list of changes that will be sent if you call
``git push``.  It does **not** include any uncommitted
changes in your working copy (use ``git status`` to find out what is
not staged for committal)!

Conversely, for the list of changes that are in the remote repository but
not in the local, use::

    $ git log ..origin/master

This is the list of changes that will be retrieved if you call
``git pull``.

Note that these commands will not query the latest state of the remote
repository, but instead the state the repository was in the last time you ran a
command such as ``git fetch`` or ``git pull``. To update the state of remote
branches, run::

    $ git remote update


How do I update my local repository to be in sync with a remote repository?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Run::

    $ git pull --ff-only <remote> <branch name>

For example::

    $ git pull --ff-only origin master

from the repository you wish to pull the latest changes into.  Most of the
time, that repository is a clone of the repository you want to pull from,
so you can simply type::

   $ git pull --ff-only


How do I apply a patch?
'''''''''''''''''''''''

If you want to try out or review a patch generated using Mercurial, do::

   patch -p1 < somework.patch

This will apply the changes in your working copy without committing them.
If the patch was not created by Mercurial (for example, a patch created by
Subversion and thus lacking any ``a``/``b`` directory prefixes in the patch),
replace ``-p1`` with ``-p0``.

If the patch contains renames, deletions or copies, and you intend committing
it after your review, you might prefer using::

   git apply somework.patch


General
=======


How do I regenerate configure?
------------------------------

If a change is made to Python which relies on some POSIX system-specific
functionality (such as using a new system call), it is necessary to update the
``configure`` script to test for availability of the functionality.

Python's ``configure`` script is generated from ``configure.ac`` using Autoconf.
Instead of editing ``configure``, edit ``configure.ac`` and then run
``autoreconf`` to regenerate ``configure`` and a number of other files (such as
``pyconfig.h``.

When submitting a patch with changes made to ``configure.ac``, it is preferred
to leave out the generated files as differences between Autoconf versions
frequently results in many spurious changes cluttering the patch. Instead,
remind any potential reviewers on the tracker to run ``autoreconf``.

Note that running ``autoreconf`` is not the same as running ``autoconf``. For
example, ``autoconf`` by itself will not regenerate ``pyconfig.h.in``.
``autoreconf`` runs ``autoconf`` and a number of other tools repeatedly as is
appropriate.

Python's ``configure.ac`` script typically requires a specific version of
Autoconf.  At the moment, this reads: ``version_required(2.65)``

If the system copy of Autoconf does not match this version, you will need to
install your own copy of Autoconf.


How do I port Python to a new platform?
---------------------------------------

The first step is to familiarize yourself with the development toolchain on
the platform in question, notably the C compiler. Make sure you can compile and
run a hello-world program using the target compiler.

Next, learn how to compile and run the Python interpreter on a platform to
which it has already been ported; preferably Unix, but Windows will
do, too. The build process for Python, in particular the ``Makefile`` in the
source distribution, will give you a hint on which files to compile
for Python.  Not all source files are relevant: some are platform
specific, others are only used in emergencies (e.g. ``getopt.c``).

It is not recommended to start porting Python without at least medium-level
understanding of your target platform; i.e. how it is generally used, how to
write platform specific apps, etc. Also, some Python knowledge is required, or
you will be unable to verify that your port is working correctly.

You will need a ``pyconfig.h`` file tailored for your platform.  You can
start with ``pyconfig.h.in``, read the comments, and turn on definitions that
apply to your platform.  Also, you will need a ``config.c`` file, which lists
the built-in modules you support.  Again, starting with
``Modules/config.c.in`` is recommended.

Finally, you will run into some things that are not supported on your
target platform.  Forget about the ``posix`` module in the beginning. You can
simply comment it out of the ``config.c`` file.

Keep working on it until you get a ``>>>`` prompt.  You may have to disable the
importing of ``site.py`` by passing the ``-S`` option. When you have a prompt,
bang on it until it executes very simple Python statements.

At some point you will want to use the ``os`` module; this is the time to start
thinking about what to do with the ``posix`` module.  It is okay to simply
comment out functions in the ``posix`` module that cause problems; the
remaining ones will be quite useful.

Before you are done, it is highly recommended to run the Python regression test
suite, as described in :ref:`runtests`.
