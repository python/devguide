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

Different branches are used at a time to represent different *minor versions*
in which development is made.  All development should be done **first** in the
:ref:`in-development <indevbranch>` branch, and selectively backported
to other branches when necessary.


.. _indevbranch:

In-development (main) branch
----------------------------

The branch for the next minor version; it is under active development for
all kinds of changes: new features, semantic changes, performance improvements,
bug fixes.  It can be :ref:`checked out <checkout>` from
http://svn.python.org/projects/python/branches/py3k.

Once a :ref:`final` release is made from the in-development branch (say, 3.2), a
new :ref:`maintenance branch <maintbranch>` (e.g. ``release32-maint``)
is created to host all bug fixing activity for further micro versions
(3.2.1, 3.2.2, etc.).


.. _maintbranch:

Maintenance branches
--------------------

A branch currently being maintained for bug fixes.  There are currently
two of them in activity: one for Python 3.x and one for Python 2.x.  At
some point in the future, Python 2.x will be closed for bug fixes and there
will be only one maintenance branch left.

The only changes allowed to occur in a maintenance branch without debate are
bug fixes.  Also, a general rule for maintenance branches is that compatibility
must not be broken at any point between sibling minor releases (3.1.1, 3.1.2,
etc.).  For both rules, only rare exceptions are accepted and **must** be
discussed first.

When a new maintenance branch is created (after a new *minor version* is
released), the old maintenance branch on that major version (e.g. 3.1.x
after 3.2 gets released) goes into :ref:`security mode <secbranch>`.


.. _secbranch:

Security branches
-----------------

A branch less than 5 years old but no longer in maintenance mode.

The only changes made to a security branch are those fixing issues exploitable
by attackers such as crashes, privilege escalation and, optionally, other
issues such as denial of service attacks.  Other behavioral issues are
**not** considered a security risk and thus not backported to a security branch.
Any release made from a security branch is source-only and done only when
actual security patches have been applied to the branch.


.. _stages:

Stages
''''''

Based on what stage the :ref:`in-development <indevbranch>` version of Python
is in, the responsibilities of a core developer change in regards to commits
to the VCS.


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

.. _final:

Final
-----

When a final release is being cut, only the release manager (RM) can make
changes to the branch.  After the final release is published, the full
:ref:`development cycle <stages>` starts again for the next minor version.

