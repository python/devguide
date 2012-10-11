.. _stdlibchanges:

Adding to the Stdlib
====================

While the stdlib contains a great amount of useful code, sometimes you want
more than is provided. This document is meant to explain how you can get either
a new addition to a pre-existing module in the stdlib or add an entirely new
module.

Changes to pre-existing code is not covered as that is considered a bugfix and
thus is treated as a bug that should be filed on the `issue tracker`_.

.. _issue tracker: http://bugs.python.org/


Adding to a pre-existing module
-------------------------------

If you have found that a function, method, or class is useful and you believe
it would be useful to the general Python community, there are some steps to go
through in order to see it added to the stdlib.

First is you should gauge the usefulness of the code. Typically this is done
by sharing the code publicly. You have a couple of options for this. One is to
post it online at the `Python Cookbook`_. Based on feedback or reviews of the
recipe you can see if others find the functionality as useful as you do.
A search of the issue tracker for previous suggestions related to the proposed
addition may turn up a rejected issue that explains why the suggestion will not
be accepted.
Another is to do a blog post about the code and see what kind of responses you
receive. Posting to python-list (see :ref:`communication` for where to find the
list and other mailing lists) to discuss your code also works. Finally, asking
on a specific :abbr:`SIG (special interest group)` from mail.python.org or
python-ideas is also acceptable. This is not a required step but it is
suggested.

If you have found general acceptance and usefulness for your code from people,
you can open an issue on the `issue tracker`_ with the code attached as a
:ref:`patch <patch>`. If possible, also submit a
:ref:`contributor agreement <contributor_agreement>`.

If a core developer decides that your code would be useful to the general
Python community, they will then commit your code. If your code is not picked
up by a core developer and committed then please do not take this personally.
Through your public sharing of your code in order to gauge community support
for it you at least can know that others will come across it who may find it
useful.

.. _Python Cookbook: http://code.activestate.com/recipes/langs/python/


Adding a new module
-------------------
It must be stated upfront that getting a new module into the stdlib is very
difficult. Adding any significant amount of code to the stdlib increases the
burden placed upon core developers. It also means that the module somewhat
becomes "sanctioned" by the core developers as a good way to do something,
typically leading to the rest of the Python community to using the new module
over other available solutions. All of this means that additions to the stdlib
are not taken lightly.


Acceptable Types of Modules
'''''''''''''''''''''''''''
Typically two types of modules get added to the stdlib. One type is a module
which implements something that is difficult to get right. A good example of
this is the :py:mod:`multiprocessing` package. Working out the various OS
issues, working through concurrency issues, etc. are all very difficult to get
right.

The second type of module is one that implements something that people
re-implement constantly. The :py:mod:`itertools` module is a good example of
this type as its constituent parts are not necessarily complex, but are used
regularly in a wide range of programs and can be a little tricky to get right.
Modules that parse widely used data formats also fall under this type of module
that the stdlib consists of.

While a new stdlib module does not need to appeal to all users of Python, it
should be something that a large portion of the community will find useful.
This makes sure that the developer burden placed upon core developers is worth
it.


Requirements
''''''''''''''
In order for a module to even be considered for inclusion into the stdlib, a
couple of requirements must be met.

The most basic is that the code must meet
:ref:`standard patch requirements <patch>`. For code that has
been developed outside the stdlib typically this means making sure the coding
style guides are followed and that the proper tests have been written.

The module needs to have been out in the community for at least a year. Because
of Python's conservative nature when it comes to backwards-compatibility, when
a module is added to the stdlib its API becomes frozen. This means that a module
should only enter the stdlib when it is mature and gone through its
"growing pains".

The module needs to be considered best-of-breed. When something is included in
the stdlib it tends to be chosen first for products over other third-party
solutions. By virtue of having been available to the public for at least a
year, a module needs to have established itself as (one of) the top choices by
the community for solving the problem the module is intended for.

The development of the module must move into Python's
infrastructure (i.e., the module is no longer directly maintained outside of
Python). This prevents a divergence between the code that is included in the
stdlib and that which is released outside the stdlib (typically done to provide
the module to older versions of Python). It also removes the burden of forcing
core developers to have to redirect bug reports or patches to an external issue
tracker and :abbr:`VCS (version control system)`.

Someone involved with the development of the
module must promise to help maintain the module in the stdlib for two years.
This not only helps out other core developers by alleviating workload from bug
reports that arrive from the first Python release containing the module, but
also helps to make sure that the overall design of the module continues to be
uniform.


Proposal Process
''''''''''''''''
If the module you want to propose adding to the stdlib meets the proper
requirements, you may propose its inclusion. To start, you should email
python-list or python-ideas to make sure the community in general would support
the inclusion of the module (see :ref:`communication`).

If the feedback from the community is positive overall, you will need to write
a :abbr:`PEP (Python enhancement proposal)` for the module's inclusion. It
should outline what the module's overall goal is, why it should be included in
the stdlib, and specify the API of the module. See the `PEP index`_ for PEPs
that have been accepted before that proposed a module for inclusion.

Once your PEP is written, send it to python-ideas for basic vetting. Be
prepared for extensive feedback and lots of discussion (not all of it
positive). This will help make the PEP be of good quality and properly
formatted.

When you have listened to, responded, and integrated as appropriate the
feedback from python-ideas into your PEP, you may send it to python-dev. You
will once again receive a large amount of feedback and discussion. A PEP
dictator will be assigned who makes the final call on whether the PEP will be
accepted or not. If the PEP dictator agrees to accept your PEP (which typically
means that the core developers end up agreeing in general to accepting
your PEP) then the module
will be added to the stdlib once the creators of the module sign
:ref:`contributor agreements <contributor_agreement>`.

.. _PEP index: http://www.python.org/dev/peps/
