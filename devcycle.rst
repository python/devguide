.. _devcycle:

Development Cycle
=================

The responsibilities of a core developer shift based on what kind of branch of
Python a developer is working on and what stage the branch is in.

To clarify terminology, Python uses a ``major.minor.micro`` nomenclature
for production-ready releases. So for Python 3.1.2 final, that is a *major
version* of 3, a *minor version* of 1, and a *micro version* of 2.

* new *major versions* are exceptional; they only come when strongly
  incompatible changes are deemed necessary, and are planned very long
  in advance;

* new *minor versions* are feature releases; they get released roughly
  every 18 months, from the current :ref:`in-development <indevbranch>`
  branch;

* new *micro versions* are bugfix releases; they get released roughly
  every 6 months, although they can come more often if necessary; they are
  prepared in :ref:`maintenance <maintbranch>` branches.

We also publish non-final versions which get an additional qualifier:
:ref:`alpha`, :ref:`beta`, :ref:`release candidate <rc>`.  These versions
are aimed at testing by advanced users, not production use.


Branches
''''''''

There is a branch for each *feature version*, whether released or not (e.g.
2.7, 3.5).  Development is handled separately for Python 2 and Python 3:
no merging happens between 2.x and 3.x branches.

In each of the 2.x and 3.x realms, the branch for a feature version is always a
descendant of the previous feature version: for example, the ``3.3`` branch is a
descendant of the ``3.2`` branch.

Therefore, each change should be made **first** in the oldest branch to which it
applies and forward-ported as appropriate: if a bug must be fixed in both Python
3.4 and 3.5, first fix it in ``3.4`` and then merge ``3.4`` into ``default``
(which holds the future 3.5).


.. _indevbranch:

In-development (main) branch
----------------------------

The ``default`` branch is the branch for the next feature release; it is
under active development for all kinds of changes: new features, semantic
changes, performance improvements, bug fixes.  As the name indicates, it
is the branch :ref:`checked out <checkout>` by default by Mercurial.

At some point during the life-cycle of a release, a
new :ref:`maintenance branch <maintbranch>` is created to host all bug fixing
activity for further micro versions (3.3.1, 3.3.2, etc.).

For versions 3.4 and before, this was conventionally done when the final
release was cut (for example, 3.4.0 final).

.. note::
  For the 3.5 release we're trying something new. We're creating the 3.5
  maintenance branch at the time we enter beta (3.5.0 beta 1).  This will
  allow feature development for 3.6 to occur alongside the beta and release
  candidate stabilization periods for 3.5.

.. _maintbranch:

Maintenance branches
--------------------

A branch for a previous feature release, currently being maintained for bug
fixes.  There are usually two maintenance branches at any given time: one for
Python 3.x and
one for Python 2.x.  At some point in the future, Python 2.x will be closed
for bug fixes and there will be only one maintenance branch left.

The only changes allowed to occur in a maintenance branch without debate are
bug fixes.  Also, a general rule for maintenance branches is that compatibility
must not be broken at any point between sibling minor releases (3.4.1, 3.4.2,
etc.).  For both rules, only rare exceptions are accepted and **must** be
discussed first.

Sometime after a new maintenance branch is created (after a new *minor version*
is released), the old maintenance branch on that major version will go into
:ref:`security mode <secbranch>`,
usually after one last maintenance release at the discretion of the
release manager.  For example, the 3.2 maintenance branch was put into
:ref:`security mode <secbranch>` after the 3.2.4 final maintenance release
following the release of 3.3.0.

.. _secbranch:

Security branches
-----------------

A branch less than 5 years old but no longer in maintenance mode.

The only changes made to a security branch are those fixing issues exploitable
by attackers such as crashes, privilege escalation and, optionally, other
issues such as denial of service attacks.  Any other changes are
**not** considered a security risk and thus not backported to a security branch.

Commits to security branches are to be coordinated with the release manager
for the corresponding feature version, as listed below in the Summary_.
Any release made from a security branch is source-only and done only when actual
security patches have been applied to the branch.


.. _listbranch:

Summary
-------

There are 5 open branches right now in the Mercurial repository:

- the ``default`` branch holds the future 3.5 version and descends from ``3.4``
  (RM: Larry Hastings)
- the ``3.4`` branch holds bug fixes for future 3.4.x maintenance releases
  and descends from ``3.3`` (RM: Larry Hastings)
- the ``3.3`` branch holds security fixes for future 3.3.x security releases
  and descends from ``3.2`` (RM: Georg Brandl)
- the ``3.2`` branch holds security fixes for future 3.2.x security releases
  (RM: Georg Brandl)
- the ``2.7`` branch holds bug fixes for future 2.7.x maintenance releases and
  descends from ``2.6`` (RM: Benjamin Peterson)


.. _stages:

Stages
''''''

Based on what stage the :ref:`in-development <indevbranch>` version of Python
is in, the responsibilities of a core developer change in regards to commits
to the :abbr:`VCS (version control system)`.


Pre-alpha
---------

The branch is in this stage when no official release has been done since
the latest final release.  There are no special restrictions placed on
commits, although the usual advice applies (getting patches reviewed, avoiding
breaking the buildbots).

.. _alpha:

Alpha
-----

Alpha releases typically serve as a reminder to core developers that they
need to start getting in changes that change semantics or add something to
Python as such things should not be added during a Beta_. Otherwise no new
restrictions are in place while in alpha.

.. _beta:

Beta
----

After a first beta release is published, no new features are accepted.  Only
bug fixes can now be committed.  This is when core developers should concentrate
on the task of fixing regressions and other new issues filed by users who have
downloaded the alpha and beta releases.

Being in beta can be viewed much like being in RC_ but without the extra overhead
of needing commit reviews.

Please see the note in the `In-development (main) branch`_ section above
for new information about the creation of the 3.5 maintenance branch during beta.


.. _rc:

Release Candidate (RC)
----------------------

A branch preparing for an RC release can only have bugfixes applied that have
been reviewed by other core developers.  Generally, these issues must be
severe enough (e.g. crashes) that they deserve fixing before the final release.
All other issues should be deferred to the next development cycle, since stability
is the strongest concern at this point.

You **cannot** skip the peer review during an RC, no matter how small! Even if
it is a simple copy-and-paste change, **everything** requires peer review from
a core developer.

.. note::
  For the 3.5 release we're trying something new.  At the point that we reach 3.5.0
  release candidate 1, the official release branch will no longer be hosted at
  ``hg.python.org``.  Instead, 3.5.0 rc 1 through final will be hosted
  by the 3.5 release manager on bitbucket.

  Bugfixes for 3.5 should still be checked in to the 3.5 branch.  However, if the
  core developer responsible for the bugfix feels it should be merged into 3.5.0, they
  will need to create a bitbucket "pull request" for this change.  Any bugfixes not
  merged into 3.5.0 in this way will be automatically shipped with 3.5.1.

.. _final:

Final
-----

When a final release is being cut, only the release manager (RM) can make
changes to the branch.  After the final release is published, the full
:ref:`development cycle <stages>` starts again for the next minor version.

