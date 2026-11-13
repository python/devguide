.. _fixing-issues:
.. _fixingissues:

=================================
Fixing "easy" issues (and beyond)
=================================

When you feel comfortable enough to want to help tackle issues by trying to
create a pull request to fix an issue, you can start by looking at the `"easy"
issues`_. These issues *should* be ones where it should take no longer than a
day or weekend to fix. But because the "easy" classification is typically done
at triage time it can turn out to be inaccurate, so do feel free to leave a
comment if you think the classification no longer applies.

For the truly adventurous looking for a challenge, you can look for issues that
are not considered easy and try to fix those. It must be warned, though, that
it is quite possible that a bug that has been left open has been left into that
state because of the difficulty compared to the benefit of the fix. It could
also still be open because nobody agreed on how to fix it (see
:ref:`fixing-issues-readiness`). Regardless of why the issue is open,
you can also always provide useful comments if you do attempt a fix, successful
or not.


.. _fixing-issues-readiness:

Check that the issue is ready to be worked on
=============================================

An obvious bug that nobody is working on can be fixed directly, but most
other issues have to be confirmed as worth fixing first, as they may be
duplicates, feature requests filed as bugs, already rejected features, etc.
A genuine bug is not always fixed either, since the fix may break existing
code and its impact has to be weighed. In that case, wait until a triager
or a core team member has acknowledged the issue.

If you are unsure, ask in the issue, but avoid superfluous comments, since
every comment notifies everyone following the issue. Issues are not
assigned to contributors who ask for it, but once an issue has been
acknowledged and is still relevant, you can start working on it and
mention it in the issue.

Before opening a pull request, read the whole discussion and check that the
issue still applies to the latest state of the branch you are targeting,
usually ``main``: an acknowledged issue may have been fixed since, or the
code it describes may have changed. For old issues, reporting that the
behaviour can no longer be reproduced on a supported Python version (see
:ref:`branchstatus`) is helpful on its own.

In general, avoid opening a pull request if:

* the issue has the :gh-label:`pending` label;
* the issue is old and its discussion never reached consensus;
* someone, such as the issue's author, already said they would open one;
* a pull request for the issue already exists.

In the last two cases, if there has been no activity for a while, ask the
contributor whether they still want to work on it.

Do not use automated tools to open pull requests on new issues either: a
pull request on an untriaged issue costs triagers more time than the issue
alone (see :ref:`ai-tools`).


.. _fixing-issues-no-pullrequest:

Consider whether a pull request is needed
=========================================

Before writing a pull request, check that the report describes an actual
bug (see :ref:`issue-tracker-not-a-bug`).


.. _"easy" issues: https://github.com/python/cpython/issues?q=is%3Aissue+is%3Aopen+label%3Aeasy
