.. _tracker:

==============
Issue Tracking
==============


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

Depending on your choice, a dedicated form template will appear. In particular,
you'll notice that the last button actually takes you to `Discourse`_ where
many Python-related discussions take place.

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

Understanding the issue's progress and status
---------------------------------------------

There is a number of additional fields like **Assignees**, **Labels**,
**Projects**, and **Milestone**. Those are filled by triagers and core
developers, this is covered in the :ref:`triaging` page. You don't need
to worry about those when reporting issues as a Python user.

You will automatically receive an update each time an action is taken on
the bug, unless you changed your GitHub notification settings.


Disagreement With a Resolution on the Issue Tracker
===================================================

As humans, we will have differences of opinions from time to time. First and
foremost, please be respectful that care, thought, and volunteer time went into
the resolution.

With this in mind, take some time to consider any comments made in association
with the resolution of the issue. On reflection, the resolution steps may seem
more reasonable than you initially thought.

If you still feel the resolution is incorrect, then raise a thoughtful question
on `python-dev`_. Further argument and disrespectful discourse on `python-dev`_
after a consensus has been reached amongst the core developers is unlikely to
win any converts.

As a reminder, issues closed by a core developer have already been carefully
considered. Please do not reopen a closed issue. An issue can be closed with
reason either as ``complete`` or ``not planned``.

.. _helptriage:

Helping Triage Issues
=====================

Once you know your way around how Python's source files are
structured and you are comfortable working with patches, a great way to
contribute is to help triage issues. Do realize, though, that experience
working on Python is needed in order to effectively help triage.

Around the clock, new issues are being opened on the `issue tracker`_ and
existing issues are being updated. Every issue needs to be triaged to make
sure various things are in proper order. Even without special privileges you
can help with this process.

Classifying Reports
-------------------

For bugs, an issue needs to:

* clearly explain the bug so it can be reproduced
* include all relevant platform details
* state what version(s) of Python are affected by the bug.

These are things you can help with once you have experience developing for
Python:

* try reproducing the bug: For instance, if a bug is not clearly explained
  enough for you to reproduce it then there is a good chance a core developer
  won't be able to either.
* see if the issue happens on a different Python version: It is always helpful
  to know if a bug not only affects the in-development version of Python, but
  whether it also affects other versions in maintenance mode.
* write a unit test: If the bug lacks a unit test that should end up in
  Python's test suite, having that written can be very helpful.

This is all helpful as it allows triagers (i.e.,
:ref:`people with the Developer role on the issue tracker <devrole>`) to
properly classify an issue so it can be handled by the right core developers in
a timely fashion.

Reviewing Patches
-----------------

If an issue has a pull request attached that has not been reviewed, you can help
by making sure the patch:

* follows the style guides
* applies cleanly to an up-to-date clone
* is a good solution to the problem it is trying to solve
* includes proper tests
* includes proper documentation changes
* submitter is listed in ``Misc/ACKS``, either already or the patch adds them

Doing all of this allows core developers and :ref:`triagers <devrole>` to more
quickly look for subtle issues that only people with extensive experience
working on Python's code base will notice.

Finding an Issue You Can Help With
----------------------------------

If you want to help triage issues, you might also want to search for issues
in modules which you have a working knowledge.  Search for the name of a module
in the issue tracker or use the `advanced search`_ query builder to search for
specific kinds of issues (e.g. the "Windows" label if you are a Windows
developer, "Extension Modules" if you are familiar with C, etc.).


.. _devrole:

Gaining the "Triager" Role on the Issue Tracker
===============================================

When you have consistently shown the ability to properly
help triage issues without guidance, you may request that you
be given the "Triager" role on the `issue tracker`_. You can make the request
to any person who already has the Triager role. If they decide you are ready
to gain the extra privileges on the tracker they will then act as a mentor to
you until you are ready to do things entirely on your own. There is no set rule
as to how many issues you need to have helped with before or how long you have
been participating. The key requirements are that you show the desire to
help, you are able to work well with others (especially those already with the
Triager role), and that have a firm grasp of how to do things on the issue
tracker properly on your own.

Gaining the Triager role will allow you to set any value on any issue in the
tracker, releasing you from the burden of having to ask others to set values on
an issue for you in order to properly triage something. This will not only help
speed up and simplify your work in helping out, but also help lessen the
workload for everyone by gaining your help.


.. seealso::

   `The Python issue tracker <https://github.com/python/cpython/issues>`_
      Where to report issues about Python.

   `The New-bugs-announce mailing list <https://mail.python.org/mailman/listinfo/new-bugs-announce>`_
      Where all the new issues created on the tracker are reported.

   `The Python-bugs-list mailing list <https://mail.python.org/mailman/listinfo/python-bugs-list>`_
      Where all the changes to issues are reported.


.. _issue tracker: https://github.com/python/cpython/issues
.. _advanced search: https://github.com/search/advanced
.. _devguide repo: https://github.com/python/devguide/issues
.. _Roundup: https://roundup.sourceforge.io/
.. _Discourse: https://discuss.python.org/
.. _python-dev: https://mail.python.org/mailman/listinfo/python-dev
