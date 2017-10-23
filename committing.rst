.. _committing:

Accepting Pull Requests
=======================

This page is aimed to core developers, and covers the steps required to
accept, merge, and possibly backport a pull request on the main repository.

Is the PR ready to be accepted?
-------------------------------

Before a PR is accepted, you must make sure it is ready to enter the public
source tree.  Use the following as a checklist of what to check for before
merging (details of various steps can be found later in this document):

#. Has the submitter signed the CLA?
   (delineated by a label on the pull request)
#. Did the test suite pass? (delineated by a pull request check)
#. Did code coverage increase or stay the same?
   (delineated by a comment on the pull request)
#. Are the changes acceptable?
#. Was ``configure`` regenerated (if necessary)?
#. Was ``pyconfig.h.in`` regenerated (if necessary)?
#. Was the submitter added to ``Misc/ACKS`` (as appropriate)?
#. Was an entry added under ``Misc/NEWS.d/next`` (as appropriate)?
#. Was "What's New" updated (as appropriate)?
#. Were appropriate labels added to signify necessary backporting of the
   pull request?

.. note::
   If you want to share your work-in-progress code on a feature or bugfix,
   either open a ``WIP``-prefixed PR, publish patches on the
   `issue tracker`_ or create a public fork of the repository.

.. _issue tracker: https://bugs.python.org


Does the test suite still pass?
'''''''''''''''''''''''''''''''

You must :ref:`run the whole test suite <runtests>` to ensure that it
passes before merging any code changes.

.. note::
   You really need to run the **entire** test suite.  Running a single test
   is not enough as the changes may have unforeseen effects on other tests
   or library modules.

   Running the entire test suite doesn't guarantee that the changes
   will pass the :ref:`continuous integration <buildbots>` tests, as those
   will exercise more possibilities still (such as different platforms or
   build options).  But it will at least catch non-build specific,
   non-platform specific errors, therefore minimizing the chance for
   breakage.


Patch checklist
'''''''''''''''

You should also :ref:`run patchcheck <patchcheck>` to perform a quick
sanity check on the changes.


Handling Others' Code
---------------------

As a core developer you will occasionally want to commit a patch created by
someone else. When doing so you will want to make sure of some things.

First, make sure the patch is in a good state. Both :ref:`patch` and
:ref:`helptriage`
explain what is to be expected of a patch. Typically patches that get cleared by
triagers are good to go except maybe lacking ``Misc/ACKS`` and ``Misc/NEWS.d``
entries (which a core developer should make sure are updated appropriately).

Second, make sure the patch does not break backwards-compatibility without a
good reason. This means :ref:`running the entire test suite <runtests>` to
make sure everything still passes. It also means that if semantics do change
there must be a good reason for the breakage of code the change will cause
(and it **will** break someone's code). If you are unsure if the breakage
is worth it, ask on python-dev.

Third, ensure the patch is attributed correctly with the contributor's
name in ``Misc/ACKS`` if they aren't already there (and didn't add themselves
in their patch) and by mentioning "Patch by <x>" in the ``Misc/NEWS.d`` entry
and the check-in message. If the patch has been heavily modified then "Initial
patch by <x>" is an appropriate alternate wording.

If you omit correct attribution in the initial check-in, then update ``ACKS``
and ``NEWS.d`` in a subsequent check-in (don't worry about trying to fix the
original check-in message in that case).

Finally, make sure that the submitter of the
patch has a CLA in place (indicated by an asterisk following their username
in the `issue tracker`_ or by the "CLA Signed" label on the pull request).
If the submitter lacks a signed CLA and the patch is non-trivial, direct them
to the electronic `Contributor Licensing Agreement`_
to ensure the PSF has the appropriate authorizations in place to relicense
and redistribute their code.


Contributor Licensing Agreements
--------------------------------

Always get a `Contributor Licensing Agreement`_ (CLA) signed unless the
change has no possible intellectual property associated with it (e.g. fixing
a spelling mistake in documentation). Otherwise it is simply safer from a
legal standpoint to require the contributor to sign the CLA.

These days, the CLA can be signed electronically through the form linked
above, and this process is strongly preferred to the old mechanism that
involved sending a scanned copy of the signed paper form.

As discussed on the PSF Contribution_ page, it is the CLA itself that gives
the PSF the necessary relicensing rights to redistribute contributions under
the Python license stack. This is an additional permission granted above and
beyond the normal permissions provided by the chosen open source license.

Some developers may object to the relicensing permissions granted to the PSF
by the CLA. They're entirely within their rights to refuse to sign the CLA
on that basis, but that refusal *does* mean we **can't accept their patches**
for inclusion.

.. _Contribution: https://www.python.org/psf/contrib/
.. _Contributor Licensing Agreement:
   https://www.python.org/psf/contrib/contrib-form/


What's New and News Entries
---------------------------

Almost all changes made to the code base deserve an entry in ``Misc/NEWS.d``.
If the change is particularly interesting for end users (e.g. new features,
significant improvements, or backwards-incompatible changes), an entry in
the ``What's New in Python`` document (in ``Doc/whatsnew/``) should be added
as well.

There are two notable exceptions to this general principle, and they
both relate to changes that *already* have a news entry, and have not yet
been included in any formal release (including alpha and beta releases).
These exceptions are:

* If a change is reverted prior to release, then the corresponding entry
  is simply removed. Otherwise, a new entry must be added noting that the
  change has been reverted (e.g. when a feature is released in an alpha and
  then cut prior to the first beta).

* If a change is a fix (or other adjustment) to an earlier unreleased change
  and the original news entry remains valid, then no additional entry is
  needed.

Needing a What's New entry almost always means that a change is *not*
suitable for inclusion in a maintenance release. A small number of
exceptions have been made for Python 2.7 due to the long support period -
when implemented, these changes *must* be noted in the "New Additions in
Python 2.7 Maintenance Releases" section of the Python 2.7 What's New
document.

News entries go into the ``Misc/NEWS.d`` directory as individual files. The
easiest way to create a news entry is to use the
`blurb <https://pypi.org/project/blurb/>`_ tool and its ``blurb add`` command.

If you are unable to use the tool you can create the news entry file manually.
The ``Misc/NEWS.d`` directory contains a sub-directory named ``next`` which
itself contains various sub-directories representing classifications for what
was affected (e.g. ``Misc/NEWS.d/next/Library`` for changes relating to the
standard library). The file name itself should be of the format
``<date>.bpo-<issue-number>.<nonce>.rst``:

* ``<date>`` is today's date in ``YYYY-MM-DD`` format, e.g. ``2017-05-27``
* ``<issue-number>`` is the issue number the change is for, e.g. ``12345``
  for ``bpo-12345``
* ``<nonce>`` is some "unique" string to guarantee the file name is
  unique across branches, e.g. ``Yl4gI2`` (typically six characters, but it can
  be any length of letters and numbers, and its uniqueness can be satisfied by
  typing random characters on your keyboard)

So a file name may be
``Misc/NEWS.d/next/Library/2017-05-27.bpo-12345.Yl4gI2.rst``.

The contents of a news file should be valid reStructuredText. The "default role"
(single backticks) in reST can be used to refer to objects in the documentation.
An 80 character column width should be used. There is no indentation or leading
marker in the file (e.g. ``-``). There is also no need to start the entry with
the issue number as it's part of the file name itself. Example news entry::

  Fix warning message when `os.chdir()` fails inside
  `test.support.temp_cwd()`.  Patch by Chris Jerdonek.

(In other ``.rst`` files the single backticks should not be used.  They are
allowed here because news entries are meant to be as readable as possible
unprocessed.)


Working with Git_
-----------------

.. seealso::
   :ref:`gitbootcamp`

As a core developer, the ability to push changes to the official Python
repositories means you have to be more careful with your workflow:

* You should not push new branches to the main repository.  You can still use
  them in your fork that you use for development of patches; you can
  also push these branches to a **separate** public repository that will be
  dedicated to maintenance of the work before the work gets integrated in the
  main repository.

  An exception to this rule: you can make a quick edit through the web UI of
  GitHub, in which case the branch you create can exist for less than 24 hours.
  This exception should not be abused and be left only for very simple changes.

* You should not commit directly into the ``master`` branch, or any of the
  maintenance branches (currently ``2.7`` or ``3.6``).
  You should commit against your own feature branch, and create a pull request.

It is recommended to keep a fork of the main repository around, as it allows
simple reversion of all local changes (even "committed" ones) if your local
clone gets into a state you aren't happy with.


.. _Git: https://git-scm.com/


.. _committing-active-branches:

Active branches
'''''''''''''''

If you do ``git branch`` you will see a :ref:`list of branches <listbranch>`.
``master`` is the in-development branch, and is the only branch that receives
new features.  The other branches only receive bug fixes or security fixes.


.. _branch-merge:

Backporting Changes to an Older Version
'''''''''''''''''''''''''''''''''''''''

When it is determined that a pull request needs to be backported into one or
more of the maintenance branches, a core developer can apply the labels
``needs backport to X.Y`` to the pull request.

After the pull request has been merged, miss-islington (bot) will first try to do the backport automatically. In case that miss-islington is unable to do it, then the pull request author or the core developer who merged it should look into backporting it themselves, using the backport generated by cherry_picker.py_ as a starting point.

The commit hash can be obtained from the original pull request, or by using
``git log`` on the ``master`` branch.
To display the 10 most recent commit hashes and their first line of the commit
message::

   git log -10 --oneline

Prefix the backport pull request with the branch, for example::

   [3.6] bpo-12345: Fix the Spam Module

Note that cherry_picker.py_ adds the branch prefix automatically.

Once the backport pull request has been created, remove the
``needs backport to X.Y`` label from the original pull request.  (Only Core
Developers can apply labels to GitHub pull requests).

.. _cherry_picker.py: https://github.com/python/core-workflow/tree/master/cherry_picker


Reverting a Merged Pull Request
'''''''''''''''''''''''''''''''

To revert a merged pull request, press the ``Revert`` button at the bottom of
the pull request.  It will bring up the page to create a new pull request where
the commit can be reverted.  It also creates a new branch on the main CPython
repository.  Delete the branch once the pull request has been merged.

Always include the reason for reverting the commit to help others understand
why it was done.  The reason should be included as part of the commit message,
for example::

   Revert bpo-NNNN: Fix Spam Module (GH-111)

   Reverts python/cpython#111.
   Reason: This commit broke the buildbot.
