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

If the report describes an obvious bug that nobody is working on yet, you
can start working on it, but many issues first need a decision on whether
and how they should be addressed. The report might be a duplicate or a
feature request filed as a bug, and even a genuine bug is not always fixed,
since the fix may break existing code and someone has to weigh who is
affected. In that case, wait until a triager or a core team member has
acknowledged the issue.

If you are unsure, ask in the issue, but avoid superfluous comments, since
every comment notifies everyone following the issue. Issues are not
assigned to contributors who ask for it, but once an issue has been
acknowledged and is still relevant, you can start working on it and say so
in the issue.

Before opening a pull request, check that the issue still applies to the
latest state of the branch you are targeting, usually ``main``: an
acknowledged issue may have been fixed since, or the code it describes may
have changed. For old issues, checking whether the behaviour persists is
helpful on its own, for instance when the latest reproducer was run on a
Python version that has reached end of life (see :ref:`branchstatus`), and
if it can no longer be reproduced, say so in a comment.

Avoid opening a pull request if:

* a pull request for the issue is already open. If it has been inactive
  for a while, ask its author first whether they want to continue the
  work, and if they do not, you can take it over;
* someone, such as the issue's author, already said they would open one;
* the issue is old and its discussion inconclusive. Read the whole history
  first, since a new pull request rarely revives a stalled discussion and
  leaving things as they are is often the outcome;
* the issue has the :gh-label:`pending` label.

Do not use automated tools to open pull requests on new issues either: a
pull request on an untriaged issue costs triagers more time than the issue
alone (see :ref:`ai-tools`).


.. _fixing-issues-no-pullrequest:

Consider whether a pull request is needed
=========================================

When in doubt, it is still worth opening an issue, as knowing about a
problem is always useful. Before writing a pull request, however, check
whether the report falls into one of the following cases, where the
behaviour is usually expected or the change would cost more than it
brings:

* calling a function in a way that violates its documented contract. This
  is *garbage in, garbage out* (GIGO), and a wrong value or an unexpected
  exception is generally not considered a bug;
* changes that bring code churn without fixing an actual problem, for
  instance changing whitespace and other stylistic details for the sake of
  a foolish consistency. Maintainers sometimes make such changes
  themselves;
* bugs found through private APIs, unless realistic code using public APIs
  could trigger them as well;
* crashes caused by manipulating the interpreter's internals with tools
  such as :meth:`codeobject.replace` or :mod:`ctypes`.


.. _"easy" issues: https://github.com/python/cpython/issues?q=is%3Aissue+is%3Aopen+label%3Aeasy
