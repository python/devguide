.. _committing:

Committing Patches
==================

Commit Messages
---------------

Every commit has a commit message to document why a change was made and to
communicate that reason to other core developers. Python core developers have
developed a standard way of formatting commit messages that everyone is
expected to follow.

Our usual convention mimicks that used in the ``Misc/NEWS`` file.  Actually,
it is common to simply paste the NEWS entry into the commit message.  Here
is an example::

   Issue #42: the spam module is now more spammy.
   The spam module sporadically came up short on spam. This change
   raises the amount of spam in the module by making it more spammy.
   Thanks to Monty Python for the patch.

The first line or sentence is meant to be a dense, to-the-point explanation
of what the purpose of the commit is.  If this is not enough detail for a commit,
a new paragraph(s) can be added to explain in proper depth what has happened
(detail should be good enough that a core developer reading the commit message
understands the justification for the change).  Also, if a non-core developer
contributed to the resolution, it is good practice to credit them.


Common Hg Workflows
-------------------

While non-committers can use named branches without issue, as a committer
you should limit your use to only those branches to be used to collaborate
between other committers. This is because named branches do persist in the
revision history.

Instead, for personal development that does not need to be shared prior to
uploading a patch, other approaches should be considered. Two common ones are
feature clones and :abbr:`mq (Mercurial Queues)`.

Feature clones assumes you prefer to work with various directories containing
separate clones. You can then create other local clones for each feature you
wish to work on. From there you can push changes back through your local clones
until they finally get pushed to the remote repository.

With mq_, you work within a single clone, managing your changes with a queue of
patches. This allows you to easily group related changes while still having
them all applied at once.


.. _mq: http://mercurial.selenic.com/wiki/MqExtension


Handling Other's Code
---------------------

As a core developer you will occasionally want to commit a patch created by
someone else. When doing so you will want to make sure of some things.

First, make sure the patch is in a good state. Both :ref:`patch` and
:ref:`helptriage`
explain what is to be expected of a patch. Typically patches that get cleared by
triagers are good to go except maybe lacking ``Misc/ACKS`` and ``Misc/NEWS``
entries.

Second, make sure the patch does not break backwards-compatibility without a
good reason. This means :ref:`running the test suite <runtests>` to make sure
everything still passes. It also means that if semantics do change there must
be a good reason for the breakage of code the change will cause (and it
**will** break someone's code). If you are unsure if the breakage is worth it,
ask on python-dev.


Forward-Porting
---------------

If the patch is a bugfix and it does not break
backwards-compatibility *at all*, then it should be applied to the oldest
branch applicable and forward-ported until it reaches the in-development branch
of Python. A forward-port instead of a back-port is preferred as it allows the
:abbr:`DAG (directed acyclic graph)` used by hg to work with the movement of
the patch through the codebase instead of against it.


Porting Within a Major Version
''''''''''''''''''''''''''''''
Assume that Python 3.2 is the current in-development version of Python and that
you have a patch that should also be applied to Python 3.1. To properly port
the patch to both versions of Python, you should first apply the patch to
Python 3.1::

   hg update release-31maint
   patch -p1 < patch.diff
   hg commit

With the patch now committed (notice that pushing to hg.python.org is not
needed yet), you want to merge the patch up into Python 3.2. Assuming you are
doing all of your work in a single clone::

   hg update py3k
   hg merge release-31maint
   # Fix any conflicts; probably Misc/NEWS at least
   hg commit
   hg push

This will get the patch working in Python 3.2 and push **both** the Python 3.1
and Python 3.2 updates to hg.python.org. If someone has forgotten to merge
their changes from previous patches applied to Python 3.1 then they too will be
merged (hopefully this will not be the case).

If you want to do the equivalent of blocking a patch in Python 3.2 that was
applied to Python 3.1, simply pull/merge the change but revert the changes
before committing::

   # After pull/merge
   hg revert -a
   hg commit
   hg push

This will cause hg's DAG to note that the changes were merged while not
committing any change in the actual code.

Porting Between Major Versions
''''''''''''''''''''''''''''''
To move a patch between, e.g., Python 3.2 and 2.7, use the `transplant
extension`_. Assuming you committed in Python 2.7 first, to pull changeset
#12345 into Python 3.2, do::

   hg transplant -s <URL to 2.7 repo> -m 12345
   # XXX any other steps required, or is it the quivalent of merged and committed?
   hg push


.. _transplant extension: http://mercurial.selenic.com/wiki/TransplantExtension
