import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Dates et événements clés
dates = [
    datetime(250, 1, 1),        # Fondation de Paris
    datetime(52, 1, 1),         # Lutetia
    datetime(1163, 1, 1),       # Notre-Dame
    datetime(1605, 1, 1),       # Place des Vosges
    datetime(1789, 7, 14),      # Révolution française
    datetime(1853, 1, 1),       # Haussmann
    datetime(1889, 1, 1),       # Tour Eiffel
    datetime(1973, 1, 1),       # Périphérique
    datetime(2010, 1, 1),       # Grand Paris
    datetime(2025, 1, 1),       # Paris aujourd'hui
]

events = [
    "Fondation de Paris\n(tribu des Parisii)",
    "Lutetia sous Rome",
    "Construction de\nNotre-Dame",
    "Place des Vosges &\nMarais aristocratique",
    "Révolution française",
    "Modernisation Haussmann",
    "Tour Eiffel (1889)",
    "Boulevard périphérique",
    "Projet Grand Paris",
    "Paris aujourd'hui"
]

# Création de la frise chronologique
fig, ax = plt.subplots(figsize=

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
