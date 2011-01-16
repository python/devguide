.. _languishing:

Marking Issues as "Languishing"
===============================

Sometimes an issue has no clear answer. It can be because core developers
cannot agree on the proper solution (or if a problem even exists). Other
times a solution is agreed upon but writing the code for the solution would
take too much effort for little gain, and so no one wants to do the work (or
would simply break too much pre-existing code without a different solution).

In these cases an issue will languish_ in the `issue tracker`_, and its
status should be set as such. This
serves the purpose of preventing people who are trying to :ref:`fix issues
<fixingissues>` from wasting time on issues that even core developers cannot
come up with an agreed-upon solution for.

A good way to tell if an issue is languishing is based on whether it had
an in-depth discussion that stalled several months ago. In that instance it is
typically safe to set the status of the issue to "languishing". If you are
unsure you can always leave a comment on the issue asking if others agree that
it is languishing.


.. _issue tracker: http://bugs.python.org
.. _languish: http://bugs.python.org/issue?@columns=title,id,activity,status&@sort=activity&@group=priority&@filter=status&@pagesize=50&@startwith=0&status=4&@dispname=Languishing
