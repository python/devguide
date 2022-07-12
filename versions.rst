.. _versions:
.. _branchstatus:

=========================
Status of Python Versions
=========================

The main branch is currently the future Python 3.12, and is the only
branch that accepts new features.  The latest release for each Python
version can be found on the `download page <https://www.python.org/downloads/>`_.


Supported Versions
==================

Dates shown in *italic* are scheduled and can be adjusted.

====== ========== ======== ============= ============ =====================
Branch Schedule   Status   First release End-of-life  Release manager
====== ========== ======== ============= ============ =====================
main   TBA        features *2023-10-03*  *2028-10*    Thomas Wouters
3.11   :pep:`664` bugfix   *2022-10-03*  *2027-10*    Pablo Galindo Salgado
3.10   :pep:`619` bugfix   2021-10-04    *2026-10*    Pablo Galindo Salgado
3.9    :pep:`596` security 2020-10-05    *2025-10*    Łukasz Langa
3.8    :pep:`569` security 2019-10-14    *2024-10*    Łukasz Langa
3.7    :pep:`537` security 2018-06-27    *2023-06-27* Ned Deily
====== ========== ======== ============= ============ =====================


Unsupported versions
====================

====== ========== =========== ============= =========== ================================
Branch Schedule   Status      First release End-of-life  Release manager
====== ========== =========== ============= =========== ================================
3.6    :pep:`494` end-of-life 2016-12-23    2021-12-23  Ned Deily
3.5    :pep:`478` end-of-life 2015-09-13    2020-09-30  Larry Hastings
3.4    :pep:`429` end-of-life 2014-03-16    2019-03-18  Larry Hastings
3.3    :pep:`398` end-of-life 2012-09-29    2017-09-29  Georg Brandl, Ned Deily (3.3.7+)
3.2    :pep:`392` end-of-life 2011-02-20    2016-02-20  Georg Brandl
3.1    :pep:`375` end-of-life 2009-06-27    2012-04-09  Benjamin Peterson
3.0    :pep:`361` end-of-life 2008-12-03    2009-06-27  Barry Warsaw
2.7    :pep:`373` end-of-life 2010-07-03    2020-01-01  Benjamin Peterson
2.6    :pep:`361` end-of-life 2008-10-01    2013-10-29  Barry Warsaw
====== ========== =========== ============= =========== ================================


Status key
==========

:features: new features, bugfixes, and security fixes are accepted.
:prerelease: feature fixes, bugfixes, and security fixes are accepted for the
    upcoming feature release.
:bugfix: bugfixes and security fixes are accepted, new binaries are still
    released. (Also called **maintenance** mode or **stable** release)
:security: only security fixes are accepted and no more binaries are released,
    but new source-only versions can be released
:end-of-life: release cycle is frozen; no further changes can be pushed to it.

See also the :ref:`devcycle` page for more information about branches.

By default, the end-of-life is scheduled 5 years after the first release,
but can be adjusted by the release manager of each branch.  All Python 2
versions have reached end-of-life.
