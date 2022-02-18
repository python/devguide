.. _github-labels:

Github Labels
=============

We're using labels on Github to categorize issues and pull requests.
Many labels are shared for both use cases, while some are dedicated
only to one. Below is a possibly inexhaustive list, but it should get
you going. For a full list, see `here <https://github.com/python/cpython/issues/labels>`_.

General purpose labels
----------------------

type-behavior
    Used for issues/PRs that address unintentional behavior, but do not
    pose significant security concerns. Generally, bugfixes will be attached
    to a specific issue where the unintended behavior was first reported.

type-documentation
    Used for issues/PRs that exclusively involve changes to
    the documentation. Documentation includes `*.rst` files, docstrings,
    and code comments.

type-enhancement
    Used for issues/PRs that provide additional functionality
    or capabilities beyond the existing specifications.

type-performance
    Used for issues/PRs that provide performance optimizations.

type-security
    Used for issues/PRs that involve critical security issues. Less severe
    security concerns can instead use the type-bugfix label.

type-tests
    Used for issues/PRs that exclusively involve changes to the tests.

OS-Mac / OS-Windows
    Used for issues/PRs involving changes which only have an effect upon
    a specific operating system.

spam
    Used for issues/PRs that don't include enough eggs or bacon.

Labels specific to issues
-------------------------

Priority
^^^^^^^^

release-blocker
    The highest priority of an issue. If unaddressed, will cause the
    release manager to hold releasing a new version of Python.

deferred-blocker
    A release blocker that was pushed one or more releases into the
    future. Possibly a temporary workaround was employed, or the version
    of Python the issue is affecting is still in alpha or beta stages
    of development.

Component
^^^^^^^^^

library
    Used for issues involving Python modules in the ``Lib/`` dir.

documentation
    Used for issues involving documentation in the ``Doc/`` dir.

interpreter-core
    Used for issues in interpreter core (``Objects/``, ``Python/``,
    ``Grammar/``, and ``Parser/`` dirs).

extension-modules
    Used for issues involving C modules in the ``Modules/`` dir.

tests
    Used for issues involving only Python's regression test suite, i.e.
    files in the ``Lib/test/`` dir.

Other
^^^^^

new
    Denotes that the issue hasn't been looked at by triagers or core
    developers yet.

easy
    Denotes that the issue is a good candidate for a newcomer to address.


Labels specific to PRs
----------------------

DO-NOT-MERGE
    Used on PRs to prevent miss-islington from being able
    to automatically merge the pull request. This label is appropriate when a PR
    has a non-trivial conflict with the branch it is being merged into.

expert-asyncio
    Used for PRs which involve changes to the asyncio module
    or other asynchronous frameworks that utilize it.

invalid
    Used manually for PRs that do not meet basic requirements and
    automatically added by bedevere when PR authors attempt to merge maintenace
    branches into the main branch. During events such as the October
    Hacktoberfest, this label will prevent the PR from counting toward the
    author's contributions.

needs backport to X.Y
    Used for PRs which are appropriate to backport to
    branches prior to main. Generally, backports to the maintenance branches
    are primarily bugfixes and documentation clarifications. Backports to the
    security branches are strictly reserved for PRs involving security fixes, such as
    crashes, privilege escalation, and DoS. The use of this label will cause
    miss-islington to attempt to automatically merge the PR into the branches
    specified.

skip issue
    Used for PRs which involve trivial changes, such as typo fixes,
    comment changes, and section rephrases. The majority of PRs require
    an issue to be attached to, but if there are no code changes and the
    section being modified retains the same meaning, this label might be
    appropriate.

skip news
    Similar to the skip issue label, this label is used for PRs which
    involve trivial changes, backports, or already have a relevant news entry
    in another PR. Any potentially impactful changes should have a
    corresponding news entry, but for trivial changes it's commonly at the
    discretion of the PR author if they wish to opt-out of making one.

sprint
    Used for PRs authored during an in-person sprint, such as
    at PyCon, EuroPython, or other official Python events. The label is
    used to prioritize the review of those PRs during the sprint.

stale
    Used for PRs that include changes which are no longer relevant, or when the
    author hasn't responded to feedback in a long period of time, or when the
    reviewer is unresponsive. This label helps core developers quickly identify
    PRs that are candidates for closure or require a ping to the author or
    reviewer.

awaiting review
    Used for PRs that haven't been reviewed by anyone yet.

awaiting core review
    Used when the PR is authored by a core developer or when a non-core
    developer has reviewed the PR, even if they requested changes.
    Note that reviewers could have been added manually by a triager or core
    developer, or included automatically through use of the `CODEOWNERS
    <https://github.com/python/cpython/blob/main/.github/CODEOWNERS>`_
    file.

awaiting changes
    A reviewer required changes to proceed with the PR.

awaiting change review
    The PR author made requested changes, and they are waiting for review.

awaiting merge
    The PR has been approved by a core developer and is ready to merge.

test-with-buildbots
    Used on PRs to test the latest commit with the buildbot fleet. Generally for
    PRs with large code changes requiring more testing before merging. This
    may take multiple hours to complete. Triagers can also stop a stuck build
    using the web interface.
