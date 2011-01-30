.. _silencewarnings:

Silence Warnings From the Test Suite
====================================

When running Python's test suite, no warnings should result when you run it
under :ref:`strenuous testing conditions <strenuous_testing>` (you can ignore
the extra flags passed to ``test`` that cause randomness and parallel execution
if you want). Unfortunately new warnings are added to Python on occasion which
take some time to eliminate (e.g., ``ResourceWarning``). Typically the easy
warnings are dealt with quickly, but the more difficult ones that require some
thought and work do not get fixed immediately.

If you decide to tackle a warning you have found, open an issue on the `issue
tracker`_ (if one has not already been opened) and say you are going to try and
tackle the issue, and then proceed to fix the issue.

.. _issue tracker: http://bugs.python.org
