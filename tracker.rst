==============
Issue Tracking
==============

.. _tracker:

Using the Issue Tracker
=======================

If you think you found a bug in Python, you can report it to the
`issue tracker`_.  Documentation bugs can also be reported there.
Issues about the tracker should be reported to the `meta tracker`_.


Checking if a bug already exists
--------------------------------

The first step in filing a report is to determine whether the problem has
already been reported.  The advantage in doing so, aside from saving the
developers time, is that you learn what has been done to fix it; it may be that
the problem has already been fixed for the next release, or additional
information is needed (in which case you are welcome to provide it if you can!).

To do this, search the bug database using the search box on the top of the page.
An `advanced search`_ is also available by clicking on "Search" in
the sidebar.


Reporting an issue
------------------

If the problem you're reporting is not already in the `issue tracker`_, you
need to log in by entering your user and password in the form on the left.
If you don't already have a tracker account, select the "Register" link or,
if you use OpenID, one of the OpenID provider logos in the sidebar.

It is not possible to submit a bug report anonymously.

Being now logged in, you can submit a bug by clicking on the "Create New" link
in the sidebar.

The submission form has a number of fields, and they are described in detail
in the :ref:`triaging` page.  This is a short summary:

* in the **Title** field, enter a *very* short description of the problem;
  less than ten words is good;
* in the **Type** field, select the type of your problem (usually behavior);
* if you know which **Components** and **Versions** are affected by the issue,
  you can select these too;
* if you have JavaScript enabled, you can use the **Nosy List** field to search
  developers that can help with the issue by entering the name of the affected
  module, operating system, or interest area.
* last but not least, you have to describe the problem in detail, including
  what you expected to happen and what did happen, in the **Comment** field.
  Be sure to include whether any extension modules were involved, and what
  hardware and software platform you were using (including version information
  as appropriate).

The triaging team will take care of setting other fields, and possibly assign
the issue to a specific developer.  You will automatically receive an update
each time an action is taken on the bug.


.. _helptriage:

Helping Triage Issues
=====================

Once you know your way around how Python's source files are
structured and you are comfortable working with patches, a great way to
participate is to help triage issues. Do realize, though, that experience
working on Python is needed in order to effectively help triage.

Around the clock, new issues are being opened on the `issue tracker`_ and
existing issues are being updated. Every
issue needs to be triaged to make sure various things are in proper order. Even
without special privileges you can help with this process.


Classifying Reports
-------------------

For bugs, an issue needs to:

* clearly explain the bug so it can be reproduced
* include all relevant platform details
* state what version(s) of Python are affected by the bug.

These are things you can help with once you have experience developing for
Python. For instance, if a bug is not clearly explained enough for you to
reproduce it then there is a good chance a core developer won't be able to
either. And it is always helpful to know if a bug not only affects the
in-development version of Python, but whether it also affects other versions in
maintenance mode. And if the bug lacks a unit test that should end up in
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

If you want to help triaging issues, you might also want to search for issues
that you are knowledgeable about.  An easy way to do it, is to search for
the name of a module you are familiar with.  You can also use the
`advanced search`_ and search for specific components (e.g. "Windows" if you
are a Windows developer, "Extension Modules" if you are familiar with C, etc.).
Finally you can use the "Random issue" link in the sidebar to pick random
issues until you find an issue that you like.  Is not so uncommon to find old
issues that can be closed, either because they are no longer valid, or
because they have a patch that is ready to be committed, but no one had
time to do it yet.

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

   `The Python issue tracker <http://bugs.python.org/>`_
      Where to report issues about Python.

   `The New-bugs-announce mailing list <http://mail.python.org/mailman/listinfo/new-bugs-announce>`_
      Where all the new issues created on the tracker are reported.

   `The Python-bugs-list mailing list <http://mail.python.org/mailman/listinfo/python-bugs-list>`_
      Where all the changes to issues are reported.

   `The meta tracker <http://psf.upfronthosting.co.za/roundup/meta/>`_
      Where to report issues about the tracker itself.

   `The Tracker development wiki page <http://wiki.python.org/moin/TrackerDevelopment>`_
      Instructions about setting up a local instance of the bug tracker.

   `The Tracker-discuss mailing list <http://mail.python.org/mailman/listinfo/tracker-discuss>`_
      Discussions about the bug tracker.


.. _issue tracker: http://bugs.python.org/
.. _meta tracker: http://psf.upfronthosting.co.za/roundup/meta/
.. _advanced search: http://bugs.python.org/issue?@template=search
.. _Tracker Development: http://wiki.python.org/moin/TrackerDevelopment
