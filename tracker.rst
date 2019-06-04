==============
Issue Tracking
==============

.. _tracker:

Using the Issue Tracker
=======================

If you think you have found a bug in Python, you can report it to the
`issue tracker`_. The `issue tracker`_ is also commonly referred to as 
`bugs.python.org` and `bpo`.  Documentation bugs can also be reported there.

You can report bugs with the issue tracker itself to the `meta tracker`_.

If you would like to file an issue about this devguide, please do so at the
`devguide repo`_.


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

To do see if the issue already exists, search the bug database using the 
search box on the top of the issue tracker page. An `advanced search`_ is also
available by clicking on "Search" in the sidebar.


Reporting an issue
------------------

If the problem you're reporting is not already in the `issue tracker`_, you
need to log in by entering your user and password in the form on the left.
If you don't already have a tracker account, select the "Register" link or,
if you use `OpenID <https://openid.net>`_, one of the OpenID provider logos in
the sidebar.

It is not possible to submit a bug report anonymously.

Once logged in, you can submit a bug by clicking on the "Create New" link
in the sidebar.

The submission form has a number of fields, and they are described in detail
in the :ref:`triaging` page.  This is a short summary:

* in the **Title** field, enter a *very* short description of the problem;
  less than ten words is good;
* in the **Type** field, select the type of your problem (usually behavior);
* if you know which **Components** and **Versions** are affected by the issue,
  you can select these too; otherwise, leave them blank;
* last but not least, you have to describe the problem in detail, including
  what you expected to happen, what did happen, and how to replicate the
  problem in the **Comment** field. Be sure to include whether any extension 
  modules were involved, and what hardware and software platform you were using
  (including version information as appropriate).


Understanding the issue's progress and status
---------------------------------------------

The triaging team will take care of setting other fields, and possibly assign
the issue to a specific developer.  You will automatically receive an update
each time an action is taken on the bug.


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
considered. Please do not reopen a closed issue.

.. _python-dev: https://mail.python.org/mailman/listinfo/python-dev


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

If an issue has a patch attached that has not been reviewed, you can help by
making sure the patch:

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
in the issue tracker or use the `advanced search`_ to search for specific 
components (e.g. "Windows" if you are a Windows developer, "Extension Modules"
if you are familiar with C, etc.). Finally you can use the "Random issue" link
in the sidebar to pick random issues until you find an issue that you like.  
You may find old issues that can be closed, either because they
are no longer valid or they have a patch that is ready to be committed, 
but no one has had the time to do so.

In the sidebar you can also find links to summaries for easy issues and
issues with a patch.


.. _devrole:

Gaining the "Developer" Role on the Issue Tracker
=================================================

When you have consistently shown the ability to properly
help triage issues without guidance, you may request that you
be given the "Developer" role on the `issue tracker`_. You can make the request
of any person who already has the Developer role. If they decide you are ready
to gain the extra privileges on the tracker they will then act as a mentor to
you until you are ready to do things entirely on your own. There is no set rule
as to how many issues you need to have helped with before or how long you have
been participating. The key requirements are that you show the desire to
help, you are able to work well with others (especially those already with the
Developer role), and that have a firm grasp of how to do things on the issue
tracker properly on your own.

Gaining the Developer role will allow you to set any value on any issue in the
tracker, releasing you from the burden of having to ask others to set values on
an issue for you in order to properly triage something. This will not only help
speed up and simplify your work in helping out, but also help lessen the
workload for everyone by gaining your help.


The Meta Tracker
================

If you find an issue with the `issue tracker`_, you can report it to the
`meta tracker`_.  The meta tracker is where you file issues against anything
you come across when working with the issue tracker itself (e.g you can't
attach a file, the layout is broken on your browser, Rietveld gave you an
error, etc.).

If you want to contribute to the tracker you can get a checkout of the source
and install a local instance where to experiment.  You can find detailed
instructions on the `Tracker Development`_ page.


.. seealso::

   | *Issues with Python and documentation*

   `The Python issue tracker <https://bugs.python.org/>`_
      Where to report issues about Python.

   `The New-bugs-announce mailing list <https://mail.python.org/mailman/listinfo/new-bugs-announce>`_
      Where all the new issues created on the tracker are reported.

   `The Python-bugs-list mailing list <https://mail.python.org/mailman/listinfo/python-bugs-list>`_
      Where all the changes to issues are reported.

   *The meta tracker and its development*

   `The meta tracker <https://github.com/python/psf-infra-meta/issues>`_
      Where to report issues about the tracker itself.

   `The Tracker development wiki page <https://wiki.python.org/moin/TrackerDevelopment>`_
      Instructions about setting up a local instance of the bug tracker.

   `The Tracker-discuss mailing list <https://mail.python.org/mailman/listinfo/tracker-discuss>`_
      Discussions about the bug tracker.


.. _issue tracker: https://bugs.python.org/
.. _meta tracker: https://github.com/python/psf-infra-meta/issues
.. _advanced search: https://bugs.python.org/issue?@template=search
.. _Tracker Development: https://wiki.python.org/moin/TrackerDevelopment
.. _devguide repo: https://github.com/python/devguide/issues
