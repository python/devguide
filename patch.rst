.. _patch:

Lifecycle of a Patch
====================


Creating
--------

Tool Usage
''''''''''

Because Python uses Mercurial as its version control system, **anyone** can make
commits locally to their repository. This means that you should make as many
commits to your code checkout as you want in order for you to work effectively.

.. _named-branch-workflow:

Also, Mercurial allows for various workflows according to each person's or
project's preference.  We present here a very simple solution based on `named
branches <http://mercurial.selenic.com/wiki/NamedBranches>`_.  Before you
start modifying things in your working copy, type::

   hg branch mywork

where ``mywork`` is a descriptive name for what you are going to work on.
Then all your local commits will be recorded on that branch, which is an
effective way of distinguishing them from other (upstream) commits.


Preparation
'''''''''''

When creating a patch for submission, there are several things that you should
do to help ensure that your patch is accepted.

First, make sure to follow Python's style guidelines. For Python code you
should follow `PEP 8`_, and for C code you should follow `PEP 7`_. If you have
one or two discrepencies those can be fixed by the core developer who commits
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

Fifth, proper `documentation <http://docs.python.org/dev/documenting/>`_
additions/changes should be included.

Sixth, if you are not already in the ``Misc/ACKS`` file then add your name. If
you have taken the time to diagnose a problem, invent a solution, code it up,
and submit a patch you deserve to be recognized as having contributed to
Python. This also means you need to fill out a `contributor form`_ which
allows the `Python Software Foundation`_ to license your code for use with
Python (you retain the copyright).


.. _contributor form: http://www.python.org/psf/contrib/
.. _PEP 7: http://www.python.org/dev/peps/pep-0007
.. _PEP 8: http://www.python.org/dev/peps/pep-0008
.. _Python Software Foundation: http://www.python.org/psf/


Generation
''''''''''

To perform a quick sanity check on your patch, you can run::

    make patchcheck

This will check and/or fix various common things people forget to do for
patches, such as adding any new files needing for the patch to work.

The following instructions assume you are using the :ref:`named branch approach
<named-branch-workflow>` suggested earlier.  To create your patch, first check
that all your local changes have been committed, then type the following::

   hg diff -r default > mywork.patch

To apply a patch generated this way, do::

    patch -p1 < mywork.patch

To undo a patch applied in your working copy, simply can revert **all** changes::

    hg revert --all

This will leave backups of the files with your changes still intact. To skip
that step, you can use the ``--no-backup`` flag.

Please refer to the :ref:`FAQ <faq>` for :ref:`more information
<hg-local-workflow>` on how to manage your local changes.

.. note:: The ``patch`` program is not available by default under Windows.
   You can find it `here <http://gnuwin32.sourceforge.net/packages/patch.htm>`_,
   courtesy of the `GnuWin32 <http://gnuwin32.sourceforge.net/>`_ project.
   Also, you may find it necessary to add the "``--binary``" option when trying
   to apply Unix-generated patches under Windows.


Submitting
----------

If this is a patch in response to a pre-existing issue on the `issue tracker`_,
attach the patch to the issue. Please provide any details about your patch that
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
than there are people capable of reviewing your patch. To get your patch
reviewed it requires a reviewer to have the spare time and motivation to
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

But if your patch is committed it will then go into Python's VCS to be released
with the next major release of Python. It may also be backported to older
versions of Python as a bugfix if the core developer doing the commit believes
it is warranted.
