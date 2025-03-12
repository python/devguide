.. _versions:
.. _branchstatus:

=========================
Status of Python versions
=========================

The ``main`` branch is currently the future Python 3.14, and is the only
branch that accepts new features.  The latest release for each Python
version can be found on the `download page <https://www.python.org/downloads/>`_.


Python release cycle
====================

.. raw:: html
   :file: include/release-cycle.svg

Another useful visualization is `endoflife.date/python <https://endoflife.date/python>`_.

Supported versions
==================

Dates shown in *italic* are scheduled and can be adjusted.

.. csv-table::
   :header-rows: 1
   :width: 100%
   :file: include/branches.csv

.. Remember to update main branch in the paragraph above too


Unsupported versions
====================

.. csv-table::
   :header-rows: 1
   :width: 100%
   :file: include/end-of-life.csv


Status key
==========

:feature: new features, bugfixes, and security fixes are accepted.
:prerelease: feature fixes, bugfixes, and security fixes are accepted for the
    upcoming feature release.
:bugfix: bugfixes and security fixes are accepted, new binaries are still
    released. (Also called **maintenance** mode or **stable** release)
:security: only security fixes are accepted and no more binaries are released,
    but new source-only versions can be released
:end-of-life: release cycle is frozen; no further changes can be pushed to it.

See also the :ref:`devcycle` page for more information about branches and backporting.

By default, the end-of-life is scheduled 5 years after the first release,
but can be adjusted by the release manager of each branch.  All Python 2
versions have reached end-of-life.
