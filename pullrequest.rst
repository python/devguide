.. _patch:

Lifecycle of a Pull Request
===========================


Creating
--------

Tool Usage
''''''''''

.. _workflow:

Mercurial allows for various workflows according to each person's or
project's preference.  It is out of this guide's scope to present them all,
so we will stick to a basic workflow where you work on a patch in your
working copy without ever making any local commits.

If you use this workflow, and your work adds or removes files to the
source tree, you will have to temporarily ``hg add`` or ``hg remove`` them,
respectively, before generating a patch.

To generate a patch, just invoke ``hg diff`` which will print out a
patch of the working copy's changes against the current revision::

   hg diff > mywork.patch

If you want to undo your changes, you can revert them from the working copy::

   hg revert -a

You can later re-apply the changes if you want to continue working on the
patch::

   hg import --no-commit mywork.patch


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
something is acceptable, thinking about backwards-compatibility early
will help prevent having your patch rejected on these grounds. Put yourself in
the shoes of someone whose code will be broken by the change(s) introduced by
the patch. It is quite likely that any change made will break
someone's code, so you need to have a good reason to make a change as you will
be forcing someone to update their code. (This obviously does not apply to new
classes or functions; new arguments should be optional and have default values
which maintain the existing behavior.) If in doubt, have a look at
:PEP:`387` or :ref:`discuss <communication>` the issue with experienced
developers.

Third, make sure you have proper tests to verify your patch works as expected.
Patches will not be accepted without the proper tests!

Fourth, make sure the entire test suite :ref:`runs <runtests>` **without
failure** because of your changes.  It is not sufficient to only run whichever
test seems impacted by your changes, because there might be interferences
unknown to you between your changes and some other part of the interpreter.

Fifth, proper :ref:`documentation <documenting>`
additions/changes should be included.


.. _patch-generation:

Generation
''''''''''

To perform a quick sanity check on your patch, you can run::

   make patchcheck

This will check and/or fix various common things people forget to do for
patches, such as adding any new files needed for the patch to work (note
that not all checks apply to non-core developers).  On Windows, use this
command (after any successful build of Python)::

   python.bat Tools/scripts/patchcheck.py

Assuming you are using the :ref:`basic approach <workflow>` suggested earlier,
just type the following::

   hg diff > mywork.patch

If you are using another approach, you probably need to find out the right
invocation of ``hg diff`` for your purposes; see ``hg help diff`` and ``hg
help revisions``. Just please make sure that you generate a
**single, condensed** patch rather than a series of several changesets.


Licensing
---------

For non-trivial changes, we must have your formal approval for distributing
your work under the `PSF license`_.  Therefore, you need to fill out a
`contributor form`_ which allows the `Python Software Foundation`_ to
license your code for use with Python (you retain the copyright).

.. note::
   You only have to sign this document once, it will then apply to all
   your further contributions to Python.


.. _PSF license: http://docs.python.org/dev/license.html#terms-and-conditions-for-accessing-or-otherwise-using-python
.. _contributor form: http://www.python.org/psf/contrib/
.. _Python Software Foundation: http://www.python.org/psf/


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
not received any notice from reviewers (i.e., no comment made) after one
month, first "ping" the issue on the `issue tracker`_ to remind the nosy list
that the patch needs a review.  If you don't get a response within a few days
after pinging the issue, then you can try emailing python-dev@python.org asking
for someone to review your patch.

When someone does manage to find the time to look at your patch they will most
likely make comments about how it can be improved (don't worry, even core
developers of Python have their patches sent back to them for changes).  It
is then expected that you post a new patch addressing these comments, and the
review process will thus iterate until a satisfactory solution has emerged.

How to Review a Patch
'''''''''''''''''''''

One of the bottlenecks in the Python development
process is the lack of patch reviews.
If you browse the bug tracker, you will see that numerous issues
have a patch, but cannot be commited to the main source code repository,
because no one has reviewed the proposed patch.
Reviewing a patch can be just as informative as providing a patch and it will allow
you to give constructive comments on another developer's work.
This guide provides a checklist for submitting a patch review.
It is a common misconception that in order to be useful, a patch review has to
be perfect. This is not the case at all! It is helpful to just test the patch and/or
play around with the code and leave comments in the bug tracker.

1. If you have not already done so, get a copy of the CPython repository
   by following the :ref:`setup guide <setup>`, build it and run the tests.

2. Check the bug tracker to see what steps are necessary to reproduce
   the issue and confirm that you can reproduce the issue in your version
   of the Python REPL (the interactive shell prompt), which you can launch
   by executing ./python inside the repository.

3. Apply the patch you saved from the bug tracker. If you are not sure how
   to apply a patch, please check the :ref:`Lifecycle of a Patch <patch>` documentation.

4. If the patch affects any C file, run the build again.

5. Launch the Python REPL (the interactive shell prompt) and check if
   you can reproduce the issue. Now that the patch has been applied, the issue
   should be fixed (in theory, but mistakes do happen! A good review aims to
   catch these before the code is committed to the Python repository). You should
   also try to see if there are any corner cases in this or related issue that the author
   of the patch may have missed.

6. If you have time, run the entire test suite. If you are pressed for time,
   run the tests for the module(s) where changes were applied.
   However, please be aware that if you are recommending a patch as 'commit-ready',
   you should always make sure the entire test suite passes.


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


Crediting
---------

Non-trivial contributions are credited in the ``Misc/ACKS`` file (and, most
often, in a contribution's ``Misc/NEWS`` entry as well).  This is something
the core developer will do when committing your patch, you don't have to
propose the addition by yourself.
