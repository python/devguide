Workflow for Deprecating Features in CPython
==============================================

Deprecation in CPython is a multi-step process that involves notifying users about deprecated functionality, planning its eventual removal, and providing adequate guidance for migration.
This document outlines the practical steps required for deprecating a feature, supplementing the policy guidelines defined in :pep:`387`.

Check prevalence and consider alternatives
------------------------------------------

Before proposing deprecation:

* **Assess Usage**: Use tools like GitHub search, ``grep``, or ``PyPI statistics`` to determine the extent and context of usage.
* **Consider Alternatives**: Ensure there are suitable replacements or upgrades available.

Open an issue
-------------

Start by creating a GitHub issue to propose the deprecation:

* Clearly describe the feature and why deprecation is needed.
* Encourage community feedback and suggestions.

Deprecation implementation
--------------------------

Once approved:

* **Raise a Warning**: Use :func:`warnings.warn` with :exc:`DeprecationWarning` for typical cases.
  If the feature is in its early deprecation phase:

  * Use :exc:`PendingDeprecationWarning` initially, which transitions to :exc:`DeprecationWarning` after a suitable period.

  Example:

  .. code-block:: python

     import warnings
     warnings.warn(
         "Feature X is deprecated and will be removed in Python 3.Y",
         DeprecationWarning,
         stacklevel=2
     )

* **Update Documentation**:

  * Add a deprecation note in the relevant docstrings.
  * Include details in the "Porting" section of the "What's New" documentation.
  * Update the ``pending-removal-in-{version}.rst`` file with the deprecation timeline.

Track deprecations
------------------

* **Monitor Usage**: After the release, observe community feedback. Deprecations may remain longer than the minimum period if low maintenance overhead is expected or usage is widespread.
* **Timeline Review**: Use GitHub milestones or specific deprecation tracking issues to manage timelines.

Plan removal
------------

After the deprecation period (not less than two releases):

* Open a new issue for removal.
* Follow removal steps:

  * Remove the deprecated code and warnings.
  * Update documentation, removing references to the deprecated feature.
  * Include the removal in the "What's New" for the release.

``PendingDeprecationWarning`` workflow
--------------------------------------

For gradual deprecations:

* **Use Case**: When you want to signal future deprecation but not yet alert end-users.
* **Transition Timeline**:

  * Move from :exc:`PendingDeprecationWarning` to :exc:`DeprecationWarning` after one or more releases.

* **Documentation**:

  * Mention the pending deprecation in “What’s New.”
  * No ``pending-removal-in`` entry is needed during this stage.

7. References and Templates
---------------------------
* Use ``.. deprecated::`` and ``.. removed::`` Sphinx roles for documentation.
* Add ``See Also`` links to :pep:`387` and DevGuide for policy and process details.
