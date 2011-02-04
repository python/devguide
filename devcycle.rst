.. _devcycle:

Development Cycle
=================

The responsibilities of a core developer shift based on what kind of branch of
Python a developer is working on and what stage the branch is in.

To clarify terminology, Python uses a ``major.minor.micro.releaselevel``
nomenclature for versions. So for Python 3.1.2 final, that is a major version
of 3, a minor version of 1, a micro version of 2, and a release level (or
stage) of "final".


Branches
''''''''

Python has branches at the granularity of minor versions. Micro and
release-level versions are represented using tags in the VCS.


.. _indevbranch:

In-Development
--------------

The current branch under active development.  It can be :ref:`checked out
<checkout>` from http://svn.python.org/projects/python/branches/py3k.

The in-development branch is where new functionality and semantic changes
occur. Currently this branch is known as the "py3k" branch. The next minor
release of Python will come from this branch (major releases are once a decade
and so have no specific rules on how they are started). All changes land in this
branch and then trickle down to other branches.

Once a Final_ release is made from the in-development branch, a branch is made
to represent the minor version of Python and it goes into maintenance mode.
Typically a minor version of Python is under development for about 18 months.


Maintenance
-----------

The branch currently being maintained for bug fixes.

The branch under maintenance is the last minor version of Python to be released
as Final_. This means if the latest release of Python was 3.1.2, then the
branch representing Python 3.1 is in maintenance mode.

The only changes allowed to occur in a maintenance branch without debate are bug
fixes.
Semantic changes **must** be carefully considered as code out in the world will
have already been developed that will rely on the released semantics. Changes
related to semantics should be discussed on python-dev before being made.

A branch stays in maintenance mode as long as a new minor release has not been
made. For example, this means that Python 2.6 stayed in maintenance mode until
Python 2.7.0 was released, at which point 2.7 went into maintenance mode and
2.6 went into Security_ mode. As new minor releases occur on a (roughly) 18
month schedule, a branch stays in maintenance mode for the same amount of time.

A micro release of a maintenance branch is made about every six months.
Typically when a new minor release is made one more release of the new-old
version of Python is made.


Security
--------
A branch less than five years old but no longer in maintenance mode.

The only changes made to a branch that is being maintained for security
purposes are somewhat obviously those related to security, e.g., privilege
escalation, and issues that lead to crashes. Other behavioral issues are
**not** considered a
security risk and thus not backported to a branch being maintained for
security. Any release made from a branch under security maintenance is
source-only and done only when actual security patches have been applied to the
branch.


Stages
''''''

Based on what stage the in-development version of Python is in, the
responsibilities of a core developer change in regards to commits to the VCS.


Pre-alpha
---------
This is the stage a branch is in from the last final release until the first
alpha (a1). There are no special restrictions placed on commits beyond those
imposed by the type of branch being worked on (e.g., in-development vs.
maintenance).


Alpha
-----
Alphas typically serve as a reminder to core developers that they need to start
getting in changes that change semantics or add something to Python as such
things should not be added during a Beta_. Otherwise no new restrictions are in
place while in alpha.


Beta
----
A branch in beta means that no new additions to Python are accepted. Bugfixes
and the like are still fine. Being in beta can be viewed much like being in RC_
but without the extra overhead of needing commit reviews.


.. _RC:

Release Candidate (RC)
----------------------
A branch preparing for an RC release can only have bugfixes applied that have
been reviewed by other core developers. That reviewer should make a post to the
issue related to the change and be mentioned in the commit message.

You **cannot** skip the peer review during an RC, no matter how small! Even if
it is a simple copy-and-paste change, **everything** requires peer review from
a core developer.


Final
-----
When a final release is being cut, only the release manager (RM) can make
changes to the branch.
