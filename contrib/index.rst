.. _c_root:

==================================
Python Contributor's Guide (draft)
==================================

.. raw:: html

    <script>
    document.addEventListener('DOMContentLoaded', function() {
      activateTab(getOS());
    });
    </script>


.. important::

   |draft|

   |purpose|


[Open question: how to divide content between this Introduction and the
:ref:`introduction <c_intro>`?]

This guide is a comprehensive resource for :ref:`contributing <contributing>`
to Python_ -- for both new and experienced contributors. It is :ref:`maintained
<devguide>` by the same community that maintains Python.  We welcome your
contributions to Python!

We encourage everyone to contribute to Python. This guide should have
everything you need to get started and be productive.  If you still have
questions after reviewing the material in this guide, the `Core Python
Mentorship`_ group is available to help you through the process.

There are a number of ways to contribute including code, documentation, and
triaging issues.  We've organized this guide to provide specifics based on the
type of activity you'll be engaged in.


Using this guide
================

We recommend reading this guide as needed. You can stop where you feel
comfortable and begin contributing immediately without reading and
understanding everything.  If you do choose to skip around this guide, be aware
that it is written assuming preceding sections have been read so you may need
to backtrack to fill in missing concepts and terminology.

No matter what kind of contribution you'll be making, you should start with
these common sections:

* :ref:`c_intro`
* :ref:`c_project`
* :ref:`c_gettingstarted`

Then choose a path based on your type of activity:

*[The original table on the devguide home had a fourth column for Core
Developers. That made the table wider and more confusing. I don't think core
team members need a quick intro path since they will have been through the
devguide before.]*

*[I haven't adjusted the links in the table yet other than to add a link to the
major section at the top of each column.]*

.. list-table::
   :widths: 10 10 10
   :header-rows: 1

   * - :ref:`Triaging <c_triage>`
     - :ref:`Documentation <c_docs>`
     - :ref:`Code <c_code>`
   * -
       * :ref:`tracker`
       * :ref:`triaging`
       * :ref:`helptriage`
       * :ref:`experts`
       * :ref:`labels`
       * :ref:`gh-faq`
       * :ref:`triage-team`
     -
       * :ref:`docquality`
       * :ref:`documenting`
       * :ref:`style-guide`
       * :ref:`rst-primer`
       * :ref:`translating`
       * :ref:`devguide`
     -
       * :ref:`setup`
       * :ref:`help`
       * :ref:`pullrequest`
       * :ref:`runtests`
       * :ref:`fixingissues`
       * :ref:`communication`
       * :ref:`gitbootcamp`
       * :ref:`devcycle`


.. toctree::
   :maxdepth: 3

   contrib-plan
   intro/index
   project/index
   get-started/index
   triage/index
   code/index
   doc/index
   core-team/index
   user-success
   security


.. _Python: https://www.python.org/
.. _Core Python Mentorship: https://www.python.org/dev/core-mentorship/
