.. _stdlib:
.. _stdlibchanges:

Adding to the stdlib
====================

While the stdlib contains a great amount of useful code, sometimes you want
more than is provided. This document is meant to explain how you can get either
a new addition to a pre-existing module in the stdlib or add an entirely new
module.

Changes to pre-existing code is not covered as that is considered a bugfix and
thus is treated as a bug that should be filed on the `issue tracker`_.


Adding to a pre-existing module
-------------------------------

If you have found that a function, method, or class is useful and you believe
it would be useful to the general Python community, there are some steps to go
through in order to see it added to the stdlib.

First, you should gauge the usefulness of the code,
which is typically done by sharing the code publicly.
This is not a required step, but it is suggested.
You have a several options for this:

* Search the `issue tracker`_ for discussion related to the proposed addition.
  This may turn up an issue that explains why the suggestion wasn't accepted.
* Open a new thread in the `Ideas Discourse category`_
  to gather feedback directly from the Python core developers and community.
* Write a blog post about the code, which may also help gather useful feedback.
* Post it to the `Python Cookbook`_.
  Based on feedback and reviews of the recipe,
  you can see if others find the functionality as useful as you do.

If you have found general acceptance and usefulness for your code from people,
you can open an issue on the `issue tracker`_ with the code attached as a
:ref:`pull request <patch>`. If possible, also submit a
:ref:`contributor agreement <contributor_agreement>`.

If a core developer decides that your code would be useful to the general
Python community, they will then commit your code. If your code is not picked
up by a core developer and committed then please do not take this personally.
Through your public sharing of your code in order to gauge community support
for it you at least can know that others will come across it who may find it
useful.

.. _Ideas Discourse category: https://discuss.python.org/c/ideas/6
.. _Python Cookbook: https://code.activestate.com/recipes/langs/python/


Adding a new module
-------------------

It must be stated upfront that getting a new module into the stdlib is very
difficult. Adding any significant amount of code to the stdlib increases the
burden placed upon core developers. It also means that the module somewhat
becomes "sanctioned" by the core developers as a good way to do something,
typically leading to the rest of the Python community to using the new module
over other available solutions. All of this means that additions to the stdlib
are not taken lightly.


Acceptable types of modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^

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


Proposal process
^^^^^^^^^^^^^^^^

If the module you want to propose adding to the stdlib meets the requirements,
you may propose its inclusion
by following the :abbr:`PEP (Python Enhancement Proposal)` process.
See :pep:`1` for details,
and the :pep:`PEP index <0>` for previously-accepted PEPs
that have proposed a module for inclusion.

If the PEP is accepted, then the module will be added to the stdlib
once the authors of the module sign
:ref:`contributor agreements <contributor_agreement>`.

.. _issue tracker: https://github.com/python/cpython/issues

Adding a new environment variable
---------------------------------

Names of environment variables should be uppercase and, from Python 3.13
onwards, use underscores for readability and accessibility.

For example, use ``PYTHON_CPU_COUNT`` instead of ``PYTHONCPUCOUNT``.

See also:

* :ref:`python:using-on-envvars`
* `"Change environment variable style" Discourse discussion
  <https://discuss.python.org/t/change-environment-variable-style/35180>`__
