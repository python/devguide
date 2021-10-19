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

* new *minor versions* are feature releases; they get released annually,
  from the current :ref:`in-development <indevbranch>` branch;

* new *micro versions* are bugfix releases; they get released roughly
  every 2 months; they are prepared in :ref:`maintenance <maintbranch>`
  branches.

We also publish non-final versions which get an additional qualifier:
:ref:`alpha`, :ref:`beta`, :ref:`release candidate <rc>`.  These versions
are aimed at testing by advanced users, not production use.

Each release of Python is tagged in the source repo with a tag of the form
``vX.Y.ZTN``, where ``X`` is the major version, ``Y`` is the
minor version, ``Z`` is the micro version, ``T`` is the release level
(``a`` for alpha releases, ``b`` for beta, ``rc`` release candidate,
and *null* for final releases), and ``N`` is the release serial number.
Some examples of release tags: ``v3.7.0a1``, ``v3.6.3``, ``v2.7.14rc1``.

Branches
''''''''

There is a branch for each *feature version*, whether released or not (e.g.
3.7, 3.8).


.. _indevbranch:

In-development (main) branch
----------------------------

The ``main`` branch is the branch for the next feature release; it is
under active development for all kinds of changes: new features, semantic
changes, performance improvements, bug fixes.

At some point during the life-cycle of a release, a
new :ref:`maintenance branch <maintbranch>` is created to host all bug fixing
activity for further micro versions in a feature version (3.8.1, 3.8.2, etc.).

For versions 3.4 and before, this was conventionally done when the final
release was cut (for example, 3.4.0 final).

Starting with the 3.5 release, we create the release maintenance branch
(e.g. 3.5) at the time we enter beta (3.5.0 beta 1).  This allows
feature development for the release 3.n+1 to occur within the main
branch alongside the beta and release candidate stabilization periods
for release 3.n.

.. _maintbranch:

Maintenance branches
--------------------

A branch for a previous feature release, currently being maintained for bug
fixes, or for the next feature release in its
:ref:`beta <beta>` or :ref:`release candidate <rc>` stages.
There is usually either one or two maintenance branches at any given time for
Python 3.x.  After the final release of a new minor version (3.x.0), releases
produced from a maintenance branch are called **bugfix** or **maintenance**
releases; the terms are used interchangeably. These releases have a
**micro version** number greater than zero.

The only changes allowed to occur in a maintenance branch without debate are
bug fixes.  Also, a general rule for maintenance branches is that compatibility
must not be broken at any point between sibling micro releases (3.5.1, 3.5.2,
etc.).  For both rules, only rare exceptions are accepted and **must** be
discussed first.

A new maintenance branch is normally created when the next feature release
cycle reaches feature freeze, i.e. at its first beta pre-release.
From that point on, changes intended for remaining pre-releases, the final
release (3.x.0), and subsequent bugfix releases are merged to
that maintenance branch.

Sometime following the final release (3.x.0), the maintenance branch for
the previous minor version will go into :ref:`security mode <secbranch>`,
usually after at least one more bugfix release at the discretion of the
release manager.  For example, the 3.4 maintenance branch was put into
:ref:`security mode <secbranch>` after the 3.4.4 bugfix release
which followed the release of 3.5.1.

.. _secbranch:

Security branches
-----------------

A branch less than 5 years old but no longer in bugfix mode is a security
branch.

The only changes made to a security branch are those fixing issues exploitable
by attackers such as crashes, privilege escalation and, optionally, other
issues such as denial of service attacks.  Any other changes are
**not** considered a security risk and thus not backported to a security branch.
You should also consider fixing hard-failing tests in open security branches
since it is important to be able to run the tests successfully before releasing.

Commits to security branches are to be coordinated with the release manager
for the corresponding feature version, as listed in the :ref:`branchstatus`.
Merging of pull requests to security branches is restricted to release managers.
Any release made from a security branch is source-only and done only when actual
security patches have been applied to the branch. These releases have a
**micro version** number greater than the last **bugfix** release.

.. _eolbranch:

End-of-life branches
--------------------

The code base for a release cycle which has reached end-of-life status
is frozen and no longer has a branch in the repo.  The final state of
the end-of-lifed branch is recorded as a tag with the same name as the
former branch, e.g. ``3.3`` or ``2.6``.

For reference, here are the Python versions that most recently reached their end-of-life:

+------------------+--------------+----------------+----------------+----------------------------------+
| Branch           | Schedule     | First release  | End-of-life    | Release manager                  |
+==================+==============+================+================+==================================+
| 3.5              | :pep:`478`   | 2015-09-13     | 2020-09-30     | Larry Hastings                   |
+------------------+--------------+----------------+----------------+----------------------------------+
| 3.4              | :pep:`429`   | 2014-03-16     | 2019-03-18     | Larry Hastings                   |
+------------------+--------------+----------------+----------------+----------------------------------+
| 3.3              | :pep:`398`   | 2012-09-29     | 2017-09-29     | Georg Brandl, Ned Deily (3.3.7+) |
+------------------+--------------+----------------+----------------+----------------------------------+
| 3.2              | :pep:`392`   | 2011-02-20     | 2016-02-20     | Georg Brandl                     |
+------------------+--------------+----------------+----------------+----------------------------------+
| 3.1              | :pep:`375`   | 2009-06-27     | 2012-04-09     | Benjamin Peterson                |
+------------------+--------------+----------------+----------------+----------------------------------+
| 3.0              | :pep:`361`   | 2008-12-03     | 2009-06-27     | Barry Warsaw                     |
+------------------+--------------+----------------+----------------+----------------------------------+
| 2.7              | :pep:`373`   | 2010-07-03     | 2020-01-01     | Benjamin Peterson                |
+------------------+--------------+----------------+----------------+----------------------------------+
| 2.6              | :pep:`361`   | 2008-10-01     | 2013-10-29     | Barry Warsaw                     |
+------------------+--------------+----------------+----------------+----------------------------------+

The latest release for each Python version can be found on the `download page
<https://www.python.org/downloads/>`_.

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
bug fixes and improvements to documentation and tests can now be committed.
This is when core developers should concentrate on the task of fixing
regressions and other new issues filed by users who have downloaded the alpha
and beta releases.

Being in beta can be viewed much like being in RC_ but without the extra
overhead of needing commit reviews.

Please see the note in the `In-development (main) branch`_ section above for
new information about the creation of the 3.5 maintenance branch during beta.


.. _rc:

Release Candidate (RC)
----------------------

A branch preparing for an RC release can only have bugfixes applied that have
been reviewed by other core developers.  Generally, these issues must be
severe enough (e.g. crashes) that they deserve fixing before the final release.
All other issues should be deferred to the next development cycle, since
stability is the strongest concern at this point.

While the goal is to have no code changes between a RC and a final release,
there may be a need for final documentation or test fixes. Any such proposed
changes should be discussed first with the release manager.

You **cannot** skip the peer review during an RC, no matter how small! Even if
it is a simple copy-and-paste change, **everything** requires peer review from
a core developer.

.. _final:

Final
-----

When a final release is being cut, only the release manager (RM) can make
changes to the branch.  After the final release is published, the full
:ref:`development cycle <stages>` starts again for the next minor version.


Repository Administration
'''''''''''''''''''''''''

The source code is currently hosted on `GitHub
<https://github.com/python/cpython>`_ in the `Python organization <https://github.com/python/>`_.

Organization Repository Policy
------------------------------

Within the `Python organization <https://github.com/python/>`_, repositories are expected to fall within these general categories:

1. The reference implementation of Python and related repositories (i.e. `CPython <https://github.com/python/cpython>`_)
2. Reference implementations of PEPs (e.g. `mypy <https://github.com/python/mypy>`_)
3. Tooling and support around CPython and the language (e.g. `python.org repository <https://github.com/python/pythondotorg>`_)
4. PSF-related repositories (e.g. the `Code of Conduct <https://github.com/python/pycon-code-of-conduct>`_)
5. PSF Infrastructure repositories (e.g. the `PSF Infrastructure Salt configurations <https://github.com/python/psf-salt>`_)

For any repository which does not explicitly and clearly fall under one of these categories, permission should be sought
from the `Python steering council <https://github.com/python/steering-council>`_.

Organization Owner Policy
-------------------------

The GitHub Organization Owner role allows for full management of all aspects of
the Python organization. Allowing for visibility and management of all aspects
at all levels including organization membership, team membership, access
control, and merge privileges on all repositories. For full details of the
permission levels see `GitHub's documentation on Organization permission
levels
<https://help.github.com/articles/permission-levels-for-an-organization/#permission-levels-for-an-organization>`_.
This role is paramount to the security of the Python Language, Community, and
Infrastructure.

The Executive Director of the Python Software Foundation delegates authority on
GitHub Organization Owner Status to Ee Durbin - Python Software
Foundation Director of Infrastructure. Common reasons for this role are:
Infrastructure Staff Membership, Python Software Foundation General Counsel,
and Python Software Foundation Staff as fallback.

Inactive or unreachable members may be removed with or without notice. Members
who no longer necessitate this level of access will be removed with notice.

Multi-Factor Authentication must be enabled by the user in order to remain an
Owner of the Python Organization.

Current Owners
--------------

+----------------------+--------------------------------+-----------------+
| Name                 | Role                           | GitHub Username |
+======================+================================+=================+
| Benjamin Peterson    | Infrastructure Staff           | benjaminp       |
+----------------------+--------------------------------+-----------------+
| Noah Kantrowitz      | Infrastructure Staff           | coderanger      |
+----------------------+--------------------------------+-----------------+
| Donald Stufft        | Infrastructure Staff           | dstufft         |
+----------------------+--------------------------------+-----------------+
| Ewa Jodlowska        | PSF Executive Director         | ejodlowska      |
+----------------------+--------------------------------+-----------------+
| Ee Durbin            | PSF Director of Infrastructure | ewdurbin        |
+----------------------+--------------------------------+-----------------+
| Van Lindberg         | PSF General Counsel            | VanL            |
+----------------------+--------------------------------+-----------------+
| Ezio Melotti         | roundup -> github migration    | ezio-melotti    |
+----------------------+--------------------------------+-----------------+
| Łukasz Langa         | CPython Developr in Residence  | ambv            |
+----------------------+--------------------------------+-----------------+

Repository Administrator Role Policy
------------------------------------

The Administrator role on the repository allows for managing all aspects
including collaborators, access control, integrations, webhooks, and branch
protection. For full details of the permission levels see `GitHub's
documentation on Repository permission levels
<https://help.github.com/articles/repository-permission-levels-for-an-organization/>`_.
Common reasons for this role are: maintenance of Core Developer
Workflow tooling, Release Managers for all :ref:`in-development <indevbranch>`,
:ref:`maintenance <maintbranch>`, and :ref:`security mode <secbranch>`
releases, and additional Python Core Developers as necessary for redundancy.
Occasional temporary administrator access is acceptable as necessary for Core
Developer workflow projects.

Inactive or unreachable members may be removed with or without notice. Members
who no longer necessitate this level of access will be removed with notice.

Multi-Factor Authentication must be enabled by the user in order to remain an
Administrator of the repository.

Current Administrators
----------------------

+-------------------+----------------------------------------------------------+-----------------+
| Name              | Role                                                     | GitHub Username |
+===================+==========================================================+=================+
| Pablo Galindo     | Python 3.10 and 3.11 Release Manager,                    | pablogsal       |
|                   | Maintainer of buildbot.python.org                        |                 |
+-------------------+----------------------------------------------------------+-----------------+
| Łukasz Langa      | Python 3.8 and 3.9 Release Manager,                      | ambv            |
|                   | PSF CPython Developer in Residence 2021-2022             |                 |
+-------------------+----------------------------------------------------------+-----------------+
| Ned Deily         | Python 3.6 and 3.7 Release Manager                       | ned-deily       |
+-------------------+----------------------------------------------------------+-----------------+
| Lary Hastings     | Retired Release Manager (for Python 3.4 and 3.5)         | larryhastings   |
+-------------------+----------------------------------------------------------+-----------------+
| Berker Peksag     | Maintainer of bpo-linkify and cpython-emailer-webhook    | berkerpeksag    |
+-------------------+----------------------------------------------------------+-----------------+
| Brett Cannon      | Maintainer of bedevere and the-knights-who-say-ni        | brettcannon     |
+-------------------+----------------------------------------------------------+-----------------+
| Ezio Melotti      | Maintainer of bugs.python.org GitHub webhook integration | ezio-melotti    |
+-------------------+----------------------------------------------------------+-----------------+
| Mariatta Wijaya   | Maintainer of blurb_it and miss-islington                | Mariatta        |
+-------------------+----------------------------------------------------------+-----------------+

Repository Release Manager Role Policy
--------------------------------------

Release Managers for :ref:`in-development <indevbranch>`, :ref:`maintenance
<maintbranch>`, and :ref:`security mode <secbranch>` Python releases are
granted Administrator privileges on the repository. Once a release branch has
entered :ref:`end-of-life <eolbranch>`, the Release Manager for that branch is
removed as an Administrator and granted sole privileges (out side of repository
administrators) to merge changes to that branch.

Multi-Factor Authentication must be enabled by the user in order to retain
access as a Release Manager of the branch.
