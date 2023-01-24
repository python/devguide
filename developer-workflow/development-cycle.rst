.. _development-cycle:
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

The :ref:`versions` page contains list of active and end-of-life branches.

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

Within the `GitHub Python organization <https://github.com/python/>`_,
repositories are expected to relate to the Python language, the CPython
reference implementation, their documentation and their development workflow.
This includes, for example:

* The reference implementation of Python and related repositories (i.e. `CPython <https://github.com/python/cpython>`_)
* Tooling and support around CPython development (e.g. `pyperformance <https://github.com/python/pyperformance>`_, `Bedevere <https://github.com/python/bedevere>`_)
* Helpers and backports for Python/CPython features (e.g. `typing_extensions <https://github.com/python/typing_extensions>`_, `typeshed <https://github.com/python/typeshed>`_, `tzdata <https://github.com/python/tzdata>`_, `pythoncapi-compat <https://github.com/python/pythoncapi-compat>`_)
* Organization-related repositories (e.g. the `Code of Conduct <https://github.com/python/pycon-code-of-conduct>`_, `.github <https://github.com/python/.github>`_)
* Documentation and websites for all the above (e.g. `python.org repository <https://github.com/python/pythondotorg>`_, `PEPs <https://github.com/python/peps>`_, `Devguide <https://github.com/python/devguide>`_, docs translations)
* Infrastructure for all the above (e.g. `docsbuild-scripts <https://github.com/python/docsbuild-scripts>`_, `buildmaster-config <https://github.com/python/buildmaster-config>`_)
* Discussions and notes around official development-related processes and events (e.g. `steering-council <https://github.com/python/steering-council>`_, `core-sprint <https://github.com/python/core-sprint>`_)

Before adding a new repository to the organization, open a discussion to seek consensus
in the `Committers Discourse category <https://discuss.python.org/c/committers/5>`_.
Once people are satisfied with that, ask the `Python steering council <https://github.com/python/steering-council>`_
to grant permission.

Note that several repositories remain in the organization for historic reasons,
and would probably not be appropriate to add today.

Generally, new repositories should start their life under personal GitHub
accounts or other GitHub orgs. It is relatively easy to move a repository to
the organization once it is mature. For example, this would now apply to
experimental features like `asyncio <https://github.com/python/asyncio>`_,
`exceptiongroups <https://github.com/python/exceptiongroups>`_, or
`typed_ast <https://github.com/python/typed_ast>`_, and drafts of new guides
and other documentation (e.g. `redistributor-guide <https://github.com/python/redistributor-guide>`_).

General-use tools and libraries (e.g. `mypy <https://github.com/python/mypy>`_
or `black <https://github.com/psf/black>`_) should also be developed outside
the python organization, unless core devs (as represented by the SC)
specifically want to “bless” one implementation (as with e.g.
`typeshed <https://github.com/python/typeshed>`_,
`tzdata <https://github.com/python/tzdata>`_, or
`pythoncapi-compat <https://github.com/python/pythoncapi-compat>`_).


Organization Owner Policy
-------------------------

The GitHub Organization Owner role allows for full management of all aspects of
the Python organization. Allowing for visibility and management of all aspects
at all levels including organization membership, team membership, access
control, and merge privileges on all repositories. For full details of the
permission levels see `GitHub's documentation on Organization permission
levels
<https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#permissions-for-organization-roles>`_.
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

.. _current owners:

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
| Ee Durbin            | PSF Director of Infrastructure | ewdurbin        |
+----------------------+--------------------------------+-----------------+
| Van Lindberg         | PSF General Counsel            | VanL            |
+----------------------+--------------------------------+-----------------+
| Łukasz Langa         | CPython Developer in Residence | ambv            |
+----------------------+--------------------------------+-----------------+

Certain actions (blocking spam accounts, inviting new users, adjusting
organization-level settings) can only `be performed`_ by owners of the Python
organization on GitHub. The ``@python/organization-owners`` team can be
mentioned to request assistance from an organization owner.

.. _be performed: https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#permissions-for-organization-roles

Repository Administrator Role Policy
------------------------------------

The Administrator role on the repository allows for managing all aspects
including collaborators, access control, integrations, webhooks, and branch
protection. For full details of the permission levels see `GitHub's
documentation on repository permission levels
<https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#permissions-for-organization-roles>`_.
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
| Larry Hastings    | Retired Release Manager (for Python 3.4 and 3.5)         | larryhastings   |
+-------------------+----------------------------------------------------------+-----------------+
| Berker Peksag     | Maintainer of bpo-linkify and cpython-emailer-webhook    | berkerpeksag    |
+-------------------+----------------------------------------------------------+-----------------+
| Brett Cannon      |                                                          | brettcannon     |
+-------------------+----------------------------------------------------------+-----------------+
| Ezio Melotti      | Maintainer of bugs.python.org GitHub webhook integration | ezio-melotti    |
+-------------------+----------------------------------------------------------+-----------------+
| Mariatta Wijaya   | Maintainer of bedevere, blurb_it and miss-islington      | Mariatta        |
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
