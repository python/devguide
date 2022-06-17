.. _github-bpo-faq:
.. _gh-faq:

===========================
GitHub Issues for BPO Users
===========================

Here are some frequently asked questions about how to do things in
GitHub issues that you used to be able to do on `bpo`_.

Before you ask your own question, make sure you read :ref:`tracker`
and :ref:`triaging` (specifically including :ref:`gh-labels`) as those
pages include a lot of introductory material.

How to format my comments nicely?
=================================

There is a wonderful `beginner guide to writing and formatting on GitHub
<https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github>`_.
Highly recommended.

One pro-tip we can sell you right here is that if you want to paste
some longer log as a comment, attach a file instead (see how below).
If you still insist on pasting it in your comment, do it like this::

    <details>
    <summary>This is the summary text, click me to expand</summary>

    Here goes the long, long text.
    It will be collapsed by default!
    </details>

How to attach files to an issue?
================================

Drag them into the comment field, wait until the file uploads, and GitHub
will automatically put a link to your file in your comment text.

How to link to file paths in the repository when writing comments?
==================================================================

Use Markdown links. If you link to the default GitHub path, the file
will link to the latest current version on the given branch.

You can get a permanent link to a given revision of a given file by
`pressing "y" <https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files>`_.

How to do advanced searches?
============================

Use the `GitHub search syntax`_ or the interactive `advanced search`_ form
that generates search queries for you.

Where is the "nosy list"?
=========================

Subscribe another person to the issue by tagging them in the comment with
``@username``.

If you want to subscribe yourself to an issue, click the *🔔 Subscribe*
button in the sidebar.

Similarly, if you were tagged by somebody else but
decided this issue is not for you, you might click the *🔕 Unsubscribe*
button in the sidebar.

There is no exact equivalent of the "nosy list" feature, so to preserve
this information during the transfer, we list the previous members of
this list in the first message on the migrated issue.

How to add issue dependencies?
==============================

Add a checkbox list like this in the issue description::

    - [x] #739
    - [ ] https://github.com/octo-org/octo-repo/issues/740
    - [ ] Add delight to the experience when all tasks are complete :tada:

then those will become sub-tasks on the given issue. Moreover, GitHub will
automatically mark a task as complete if the other referenced issue is
closed. More details in the `official GitHub documentation
<https://docs.github.com/en/issues/tracking-your-work-with-issues/about-task-lists>`_.

What on Earth is a "mannequin"?
===============================

For issues migrated to GitHub from `bpo`_ where the authors or commenters
are not core developers, we opted not to link to their GitHub accounts
directly. Users not in the `python organization on GitHub
<https://github.com/orgs/python/people>`_ might not like comments to
appear under their name from an automated import.  Others never linked GitHub on
`bpo`_ in the first place so linking their account, if any, would be impossible.

In those cases a "mannequin" account is present to help follow the conversation
that happened in the issue. In case the user did share their GitHub account
name in their `bpo`_ profile, we use that. Otherwise, their classic `bpo`_
username is used instead.

Where did the "Resolution" field go?
====================================

Based on historical data we found it not being used very often.

Where did the "Low", "High", and "Critical" priorities go?
==========================================================

Based on historical data we found those not being used very often.

How to find a random issue?
===========================

This is not supported by GitHub.

Where are regression labels?
============================

We rarely updated this information and it turned out not to be
particularly useful outside of the change log.


.. _bpo: https://bugs.python.org/
.. _GitHub search syntax: https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax
.. _advanced search: https://github.com/search/advanced
