.. _patch:

Lifecycle of a Patch
====================


Creating
--------

Tool Usage
''''''''''

.. _mq-workflow:

Mercurial allows for various workflows according to each person's or
project's preference.  We present here a very simple solution based on mq_
(*Mercurial Queues*). You are welcome to use any approach you like (including
a svn-like approach of simply using ``hg diff`` to create a patch based on
uncommitted changes in your working copy).  Usage of mq_ is merely a
suggestion; it's a balance between being able to do everything needed
while allowing for more powerful usage if desired in the future.

First make sure that the extension has been turned on in your ``.hgrc`` or
``Mercurial.ini`` file::

   [extensions]
   mq =

You can verify this is working properly by running ``hg help mq``.

Before you start modifying things in your working copy, type::

   hg qnew mywork

where ``mywork`` is a descriptive name for what you are going to work on.
This will create a patch in your patch queue. Whenever you have reached a point
that you want to save what you have done, run::

   hg qrefresh

This will update the patch to contain all of the changes you have made up to
this point. If you have added or removed any file, use ``hg add`` or ``hg
remove``, respectively, before running ``hg qrefresh``.

Later on, we will explain :ref:`how to generate a patch <patch-generation>`.

If you want to delete your changes irrevocably (either because they were
committed, or they ended up uninteresting), use::

   hg qpop mywork
   hg qdelete mywork

.. seealso::
   For more advanced usage of mq, read the `mq chapter
   <http://hgbook.red-bean.com/read/managing-change-with-mercurial-queues.html>`_
   of `Mercurial: The Definitive Guide <http://hgbook.red-bean.com/>`_.

   Also, regardless of your workflow, refer to the :ref:`FAQ <faq>` for
   :ref:`more information on using Mercurial <hg-local-workflow>`.

.. _issue tracker: http://bugs.python.org
.. _mq: http://mercurial.selenic.com/wiki/MqExtension


Preparation
'''''''''''

When creating a patch for submission, there are several things that you should
do to help ensure that your patch is accepted.

First, make sure to follow Python's style guidelines. For Python code you
should follow :PEP:`8`, and for C code you should follow :PEP:`7`. If you have
one or two discrepancies those can be fixed by the core developer who commits
your patch. But if you have systematic deviations from the style guides your
patch will be put on hold until you fix the formatting issues.

Second, be aware of backwards-compatibility considerations. While the core
developer who eventually handles your patch will make the final call on whether
something is acceptable, having you think about backwards-compatibility early
will help prevent having your patch rejected on these grounds. Basically just
put yourself in the shoes of someone whose code will be broken by a change to
pre-existing semantics. It is guaranteed that any change made **will** break
someone's code, so you need to have a good reason to make a change as you will
be forcing someone somewhere to update their code (this obviously does not apply
to new semantics).

Third, make sure you have proper tests to verify your patch works as expected.
Patches will not be accepted without the proper tests!

Fourth, make sure the entire test suite :ref:`runs <runtests>` **without
failure** because of your changes.  It is not sufficient to only run whichever
test seems impacted by your changes, because there might be interferences
unknown to you between your changes and some other part of the interpreter.

Fifth, proper :ref:`documentation <documenting>`
additions/changes should be included.

Sixth, if you are not already in the ``Misc/ACKS`` file then add your name. If
you have taken the time to diagnose a problem, invent a solution, code it up,
and submit a patch you deserve to be recognized as having contributed to
Python. This also means you need to fill out a `contributor form`_ which
allows the `Python Software Foundation`_ to license your code for use with
Python (you retain the copyright).


.. _contributor form: http://www.python.org/psf/contrib/
.. _Python Software Foundation: http://www.python.org/psf/


.. _patch-generation:

Generation
''''''''''

To perform a quick sanity check on your patch, you can run::

   make patchcheck

This will check and/or fix various common things people forget to do for
patches, such as adding any new files needed for the patch to work (note
that not all checks apply to non-core developers).  On Windows, use this
command::

   ./python.exe Tools/scripts/patchcheck.py

Assuming you are using the :ref:`mq approach <mq-workflow>` suggested earlier,
first check that all your local changes have been recorded (using
``hg qrefresh``), then type the following::

   hg qdiff > mywork.patch

If you are using another approach, you probably need to find out the right
invocation of ``hg diff`` for your purposes; see ``hg help diff`` and ``hg
help revisions``. Just please make sure that you
generate a **single, condensed** patch rather than a series of several changesets.

Also, please make sure your patch is whitespace normalized. ``patchcheck``
will check this for you.

Autoconf
''''''''

If a change is made to Python which relies on some POSIX system-specific
functionality (such as using a new system call), it is necessary to update the
``configure`` script to test for availability of the functionality.

Python's ``configure`` script is generated from ``configure.in`` using Autoconf.
Instead of editing ``configure``, edit ``configure.in`` and then run
``autoreconf`` to regenerate ``configure`` and a number of other files (such as
``pyconfig.h``.

When submitting a patch with changes made to ``configure.in``, it is preferred
to leave out the generated files as differences between Autoconf versions
frequently results in many spurious changes cluttering the patch. Instead,
remind any potential reviewers on the tracker to run ``autoreconf``.

Note that running ``autoreconf`` is not the same as running ``autoconf``. For
example, ``autoconf`` by itself will not regenerate ``pyconfig.h.in``.
``autoreconf`` runs ``autoconf`` and a number of other tools repeatedly as is
appropriate.

Python's ``configure.in`` script typically requires a specific version of
Autoconf.  At the moment, this reads: ``version_required(2.65)``

If the system copy of Autoconf does not match this version, you will need to
install your own copy of Autoconf:

1. Go to http://ftp.gnu.org/gnu/autoconf/ and download the version of Autoconf
   matching the one in ``configure.in``::

      wget http://ftp.gnu.org/gnu/autoconf/autoconf-2.65.tar.bz2

2. Unpack the tarball::

      tar -jxf autoconf-2.65.tar.bz2 

3. Build the specified version of Autoconf and install it to a writable location
   (e.g. within your home directory)::

      pushd autoconf-2.65.tar.bz2
      ./configure --prefix=$HOME/autoconf-2.65
      make
      make install

   This installs a copy of the appropriate version of Autoconf into
   ~/autoconf-2.65.

4. Go back to the Python source and rerun ``autoreconf``, pointing ``PATH`` at
   the newly installed copy of Autoconf::

      popd
      PATH=~/autoconf-2.65/bin:$PATH autoreconf

5. Autoconf should now have updated your local copy of ``configure`` to reflect
   your changes.

Submitting
----------

If this is a patch in response to a pre-existing issue on the `issue tracker`_,
attach the patch to the issue; use the ``Choose File`` button on the tracker
web page for the issue to upload your patch file. Please provide any details
about your patch that
would be relevant to the discussion of the issue or your patch.

If this is a patch for an unreported issue (assuming you already performed a
search on the issue tracker for a pre-existing issue), create a new issue and
attach your patch. Please fill in as much relevant detail as possible to
prevent patch reviewers from having to delay reviewing your patch because of
lack of information.


.. _issue tracker: http://bugs.python.org


Reviewing
---------

To begin with, please be patient! There are many more people submitting patches
than there are people capable of reviewing your patch. Getting your patch
reviewed requires a reviewer to have the spare time and motivation to
look at your patch (we cannot force anyone to review patches). If your patch has
not received any notice from reviewers (i.e., no comment made) after a
substantial amount of time then you may
email python-dev@python.org asking for someone to take a look at your patch.

When someone does manage to find the time to look at your patch they will most
likely make comments about how it can be improved (don't worry, even core
developers of Python have their patches sent back to them for changes).  It
is then expected that you post a new patch addressing these comments, and the
review process will thus iterate until a satisfactory solution has emerged.


Committing/Rejecting
--------------------

Once your patch has reached an acceptable state (and thus considered
"accepted"), it will either be committed or rejected. If it is rejected, please
do not take it personally! Your work is still appreciated regardless of whether
your patch is committed. Balancing what *does* and *does not* go into Python
is tricky and we simply cannot accept everyone's contributions.

But if your patch is committed it will then go into Python's
:abbr:`VCS (version control system)` to be released
with the next major release of Python. It may also be backported to older
versions of Python as a bugfix if the core developer doing the commit believes
it is warranted.
