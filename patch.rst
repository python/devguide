.. _patch:

Lifecycle of a Patch
====================


Creating
--------

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

Fourth, proper documentation additions/changes should be included.

Fifth, if you are not already in the ``Misc/ACKS`` file then add your name. If
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

Before creating your patch, you should make sure that the entire test suite
runs without failure because of your changes. The only time a patch will be
accepted with failing tests is because the tests fail without the patch applied
and and the patch does not make the pre-existing failures worse.

To perform a quick sanity check on your patch, you can run::

    make patchcheck

This will check and/or fix various common things people forget to do for
patches.

To create your patch, you should generate a unified diff from your checkout's
top-level directory::

    svn diff > patch.diff

To apply a patch generated this way, do::

    patch -p0 < patch.diff

To undo a patch, do::

    patch -R -p0 < patch.diff


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
reviewed it also requires a reviewer to have the spare time and motivation to
look at your patch (we cannot force anyone to review patches). If your patch has
not received any notice from reviewers (i.e., no comment made) then you may
email python-dev@python.org asking for someone to take a look at your patch.

When someone does manage to find the time to look at your patch they will most
likely make a comment about how it can be improved (don't worry, even core
developers on Python have their patches sent back to them for changes). The
status of the issue will be made "pending" and will be automatically closed in
two weeks if you do not address the issues raised. This is to prevent your
patch sitting their open forever if you happen to lose interest.


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
