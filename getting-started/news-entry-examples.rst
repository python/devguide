NEWS entry examples
===================

This page expands the guidance in :ref:`news-entry` with concrete
examples of when a ``NEWS`` entry is (and is not) required.

Examples that typically **do** need a ``NEWS`` entry
----------------------------------------------------

* a new function, method, class, or module
* a new HOWTO in the documentation
* the removal of a deprecated feature

Examples that typically **do not** need a ``NEWS`` entry
--------------------------------------------------------

* a new feature was included in Python 3.13 alpha 1, but got removed in
  3.13 beta 2, before the final release of 3.13
* a typo fix in the documentation or in a docstring
* the addition of a new test method
* the removal of a private and internal API
* code refactoring of a module with no user-visible effects

These examples follow the existing rules under :ref:`news-entry`:
documentation-only changes, test-only changes, and strictly internal
changes with no user-visible effects generally skip a ``NEWS`` entry.
