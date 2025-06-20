.. _versions:
.. _branchstatus:

=========================
Status of Python versions
=========================

The ``main`` branch is currently the future Python |mainversion|, and is the only
branch that accepts new features.  The latest release for each Python
version can be found on the `download page <https://www.python.org/downloads/>`_.


.. raw:: html
   :file: include/release-cycle.svg

(See :ref:`below <full-chart>` for a chart with older versions.
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


.. _full-chart:

Full chart
==========

.. raw:: html
   :file: include/release-cycle-all.svg


Status key
==========

Python releases go through five phases, as described in :pep:`602`.  Release
managers can adjust specific dates as needed.

:feature: Before the first beta, the next full release can accept new features,
   bug fixes, and security fixes.

:prerelease: After the first beta, no new features can go in, but feature fixes
   (including significant changes to new features), bug fixes, and security fixes
   are accepted for the upcoming feature release.

:bugfix: Once a version has been fully released, bug fixes and security fixes are
   accepted. New binaries are built and released roughly every two months. This
   phase is also called **maintenance** mode or **stable** release.

:security: After two years (18 months for versions before 3.13), only security
   fixes are accepted and no more binaries are released.  New source-only versions
   can be released as needed.

:end-of-life: Five years after a release, support ends. The release cycle is
   frozen; no further changes are allowed.

See also the :ref:`devcycle` page for more information about branches and backporting.
