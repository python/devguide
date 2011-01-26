.. _committing:

Committing Patches
==================


Handling Other's Code
---------------------
As a core developer you will occasionally want to commit a patch created by
someone else. When doing so you will want to make sure of some things.

First, make sure the patch in a good state. Both :ref:`patch` and
:ref:`helptriage`
explain what is to be expected of a patch. Typically patches that get cleared by
triagers are good to go except maybe lacking ``Misc/ACKS`` and ``Misc/NEWS``
entries.

Second, make sure the patch does not break backwards-compatibility without a
good reason. This means :ref:`running the test suite <runtests>` to make sure
everything still passes. It also means that if semantics do change there must
be a good reason for the the breakage of code the change will cause (and it
**will** break someone's code). If you are unsure if the breakage is worth it,
ask on python-dev.


Backporting
-----------
If the patch is a bugfix and it does not break
backwards-compatibility *at all*, then backport it to the branch(es) in
maintenance mode. The easiest way to do this is to apply the patch in the
development branch, commit, and then use svnmerge.py_ to backport the patch.

For example, let us assume you just made commit 42 in the development branch
and you want to backport it to the ``release31-maint`` branch. You would change
your working directory to the maintenance branch and run the command::

    svnmerge.py merge -r 42

This will try to apply the patch to the current branch and generate a commit
message. You will need to revert ``Misc/NEWS`` and do a new entry (the file
changes too much between releases to ever have a merge succeed). To do a
reversion, you can either undo the changes::

    svn revert Misc/NEWS

or you can manually fix the issue and tell svn the problem is resolved::

    svn resolved Misc/NEWS

Once your checkout is ready to be committed, do::

    svn ci -F svnmerge-commit-message.txt

This will commit the backport along with using the commit message created by
``svnmerge.py`` for you.

If it turns out you do not have the time to do a backport, then at least leave
the proper issue open on the tracker with a note specifying that the change
should be backported so someone else can do it.


.. _svnmerge.py: http://svn.apache.org/repos/asf/subversion/trunk/contrib/client-side/svnmerge/svnmerge.py
