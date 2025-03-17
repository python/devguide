.. _versions:
.. _branchstatus:

=========================
Status of Python versions
=========================

The ``main`` branch is currently the future Python 3.14, and is the only
branch that accepts new features.  The latest release for each Python
version can be found on the `download page <https://www.python.org/downloads/>`_.


.. raw:: html
   :file: include/release-cycle.svg

(See :ref:`below <versions-chart-all>` for a chart with older versions.
Another useful visualization is `endoflife.date/python <https://endoflife.date/python>`_.)


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


.. _versions-chart-all:

Full chart
==========

.. raw:: html
   :file: include/release-cycle-all.svg


Status key
==========

Python releases go through five phases:

:feature: Before the first beta, the next full release can accept new features,
   bug fixes, and security fixes.

:prerelease: After the first beta, no new features can go in, but feature fixes
   (including significant changes to new features), bug fixes, and security fixes
   are accepted for the upcoming feature release.

:bugfix: Once a version has been fully released, bug fixes and security fixes are
   accepted. New binaries are built and released. (Also called **maintenance**
   mode or **stable** release.)

:security: After a few years, only security fixes are accepted and no more
   binaries are released.  New source-only versions can be released as needed.

:end-of-life: Five years after a release, support ends. The release cycle is
   frozen; no further changes can be pushed to it.

See also the :ref:`devcycle` page for more information about branches and backporting.

By default, the end-of-life is scheduled 5 years after the first release,
but can be adjusted by the release manager of each branch.  All Python 2
versions have reached end-of-life.
