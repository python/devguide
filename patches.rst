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
one or two discrepencies those can be fixed by the core committer who commits
your patch. But if you have systematic deviations from the style guides your
patch will be put on hold until you fix the formatting issues.

Second, be aware of backwards-compatibility considerations. While the core
committer who eventually handles your patch will make the final call on whether
something is acceptable, having you think about backwards-compatibility early
will help prevent having your patch rejected on these grounds. Basically just
put yourself in the shoes of someone whose code will be broken by a change to
pre-existing semantics. It is guaranteed that any change made **will** break
someone's code, so you need to have a good reason to make a change as you will
be forcing someone somewhere to update their code (this obviously does not apply
to new semantics).

Third, make sure you have proper tests to verify your patch works as expected.
Patches will not be accepted without the proper tests!

Fourth, if you are not already in the ``Misc/ACKS`` file then add your name. If
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

This will make sure extraneous whitespace has been removed from your patch,
etc.

To create your patch, you should generate a unified diff::

    svn diff > patch.diff


Submitting
----------

XXX


Reviewing
---------

XXX


Committing/Rejecting
--------------------

XXX
