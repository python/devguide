.. _issue-tracker:
.. _tracker:

=============
Issue Tracker
=============


Using the Issue Tracker
=======================

If you think you have found a bug in Python, you can report it to the
`issue tracker`_. The `issue tracker`_ is now hosted on GitHub, alongside
the codebase and pull requests.  Documentation bugs can also be reported there.

If you would like to file an issue about this devguide, please do so at the
`devguide repo`_.

.. note::
    Python used to use a dedicated `Roundup`_ instance as its issue tracker.
    That old bug tracker was hosted under the domain ``bugs.python.org``
    (sometimes called ``bpo`` for short). Currently a read-only version is still
    available on that domain for historical purposes. All ``bpo`` data has been
    migrated to the current `issue tracker`_ on GitHub.

    If you're familiar with ``bpo`` and would like to learn more about GitHub
    issues, please read this page, and the :ref:`triaging` page as they
    provide good introductory material. There is also a :ref:`gh-faq`
    document to answer some of the more popular questions.

Checking if a bug already exists
--------------------------------

The first step before filing an issue report is to see whether the problem has
already been reported.  Checking if the problem is an existing issue will:

* help you see if the problem has already been resolved or has been fixed for
  the next release
* save time for you and the developers
* help you learn what needs to be done to fix it
* determine if additional information, such as how to replicate the issue,
  is needed

To see if an issue already exists, search the bug database using the search box
above the list of bugs on the issues page. A form-based `advanced search`_ query
builder is also available on GitHub to help creating the text query you need.

Reporting an issue
------------------

If the problem you're reporting is not already in the `issue tracker`_, you
can report it using the green "New issue" button on the right of the search
box above the list of bugs. If you're not already signed in to GitHub, it
will ask you to do so now.

First you need to select what kind of problem you want to report. The
available choices are:

* **Bug report**: an existing feature isn't working as expected;
* **Documentation**: there is missing, invalid, or misleading documentation;
* **Enhancement**: suggest a new feature for Python;
* **Performance**: something should work faster;
* **Security**: there is a specific kind of weakness open to exploitation
  through the points of vulnerability;
* **Tests**: something is wrong with CPython's suite of regression tests;
* **Discuss**: you'd like to learn more about Python, discuss ideas for
  possible changes to future Python versions, track core development
  discussions, or join a specific special-interest group.

Depending on your choice, a dedicated form template will appear.
In particular, you'll notice that the last button actually takes you to
the `Python Discourse`_ (``discuss.python.org``),
where many Python-related discussions take place.

The submission form has only two fields that you need to fill:

* in the **Title** field, enter a *very* short description of the problem;
  less than ten words is good;
* in the **Write** field, describe the problem in detail using hints from
  the template that was put in that field for you. Be sure to include what
  you expected to happen, what did happen, and how to replicate the
  problem. Be sure to include whether any extension modules were involved,
  and what hardware and software platform you were using (including version
  information as appropriate). In particular, *what version of Python* you
  were using.

You can tag someone, with :samp:`@{username}` in a comment,
if you think the issue should be brought to their attention.
Use the :ref:`experts` to know who wants to be tagged for specific areas.

There are a number of additional fields like **Assignees**, **Labels**,
**Projects**, and **Milestone**. Those are filled by triagers and core
developers and are covered in the :ref:`triaging` page. You don't need
to worry about those when reporting issues as a Python user.

Adding special links
--------------------

The following abbreviations can be used in a comment to generate a link:

* :samp:`GH-{NNN}`: to link to another issue or PR;
* :samp:`PEP-{NNN}`: to link to a specific PEP;
* :samp:`BPO-{NNN}`: to link to a bugs.python.org issue;

See also the `list of autolinks supported by GitHub <autolinks_>`_.

Following issues
----------------

If you want to subscribe yourself to an issue, click the :guilabel:`🔔 Subscribe`
button in the sidebar.  Similarly, if you were tagged by somebody else but
decided this issue is not for you, you might click the :guilabel:`🔕 Unsubscribe`
button in the sidebar.  Note that you are automatically subscribed to
issues you created.

Tracking dependencies and duplicates
------------------------------------

It is possible to use `checklists`_ to track dependencies or,
in case of meta-issues, to link to the other related issues.

By writing :samp:`Duplicate of #{NNN}` in a comment, you can
`mark issues and PRs as duplicates <duplicates_>`_.


Disagreement With a Resolution on the Issue Tracker
===================================================

As humans, we will have differences of opinions from time to time. First and
foremost, please be respectful that care, thought, and volunteer time went into
the resolution.

With this in mind, take some time to consider any comments made in association
with the resolution of the issue. On reflection, the resolution steps may seem
more reasonable than you initially thought.

If you still feel the resolution is incorrect, then raise a thoughtful question
on the `Core Development Discourse category`_.
Further argument and disrespectful responses
after a consensus has been reached amongst the core developers is unlikely to
win any converts.

As a reminder, issues closed by a core developer have already been carefully
considered. Please do not reopen a closed issue. An issue can be closed with
reason either as ``complete`` or ``not planned``.

.. seealso::

   `The Python issue tracker <issue tracker_>`_
      Where to report issues about Python.


.. _issue tracker: https://github.com/python/cpython/issues
.. _advanced search: https://github.com/search/advanced
.. _devguide repo: https://github.com/python/devguide/issues
.. _Roundup: https://roundup.sourceforge.io/
.. _Python Discourse: https://discuss.python.org/
.. _autolinks: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls
.. _checklists: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-task-lists
.. _duplicates: https://docs.github.com/en/issues/tracking-your-work-with-issues/marking-issues-or-pull-requests-as-a-duplicate
.. _Core Development Discourse category: https://discuss.python.org/c/core-dev/23
