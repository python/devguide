Python Developer's Guide
========================

.. toctree::
   :hidden:

   setup
   patch


.. todolist::


Contributing
------------

This list is in an overall suggested order for people wanting to contribute to
the Python programming language and/or the CPython interpreter. People should
follow the top-level bullet points in order, while sub-level bullet points can
be done in any order.

* :ref:`setup`
* Coding style guides
    * `PEP 7`_
    * `PEP 8`_
* :ref:`patch`
* :ref:`runtests`
* Projects to get familiar with the development process
    * `Help increase test coverage <XXX>`_
    * `Make all unit tests discoverable by unittest <XXX>`_
    * `Fix all warnings raised when running the test suite w/ -uall <XXX>`_
    * `Fixing documentation bugs <XXX>`_
* Projects for once you are comfortable
    * `Helping triage issues <XXX>`_
    * `Fixing issues considered "easy" <XXX>`_ (and beyond)
    * Watching the buildbots_
* `Gaining 'Developer' privileges for the issue tracker <XXX>`_
    * `Triaging issues <XXX>`_
    * `Reviewing patches <XXX>`_
* `Following Python's development <XXX>`_
* `Gaining commit privileges <XXX>`_
    * `Committing patches <XXX>`_


Making changes to Python itself
-------------------------------

* `Changing something already in the stdlib <XXX>`_
* Adding to the stdblib
    * `Adding to a pre-existing module <XXX>`_
    * `Adding a new module <XXX>`_
* `Changing the language <XXX>`_


.. _resources:

Resources
---------

* `Issue tracker <http://bugs.python.org/>`_
    * `Meta tracker <http://psf.upfronthosting.co.za/roundup/meta>`_ (issue
      tracker for the issue tracker)
* Buildbots_

.. todo::
    move various files out of Misc to here (e.g., README.valgrind,
    Porting, SpecialBuilds.txt, maintainers.rst, etc.)

.. todo::
    Write a README.gdb for Misc to cover both gdbinit and python-gdb.py

.. todo::
    Move various informational PEPs out of the PEP index and over here
    (.e.g, grammar and compiler guides)


.. _buildbots: http://python.org/dev/buildbot/
.. _PEP 7: http://www.python.org/dev/peps/pep-0007
.. _PEP 8: http://www.python.org/dev/peps/pep-0008


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

