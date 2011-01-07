Python Developer's Guide
========================

.. toctree::
   :hidden:

   setup
   patch
   runtests
   coverage


.. todolist::


Contributing
------------

People who wish to contribute to Python **must** read the following documents
in their top-level order (sub-level documents can be read in any order). You
can stop where you feel comfortable and begin contributing without reading and
understanding all of these documents, but please do not skip around within the
documentation.

* :ref:`setup`
* Coding style guides
    * `PEP 7`_
    * `PEP 8`_
* :ref:`patch`
* :ref:`runtests`
* Projects to get familiar with the development process
    * :ref:`coverage`
    * `Make all unit tests discoverable by unittest <XXX>`_
    * `Fixing documentation bugs <XXX>`_
* Projects for once you are comfortable
    * `Helping triage issues <XXX>`_
    * `Fixing issues considered "easy" <XXX>`_ (and beyond)
    * `Fix all warnings raised when running the test suite w/ -uall <XXX>`_
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

.. todo::
    See if tempfile or test.support has a context manager that creates and
    deletes a temp file so as to move off of test.support.TESTFN.

.. todo::
    Create test.support.optional_import() for tests to use to import modules
    that are optional on various platforms. This would allow for moving away
    from ImportError representing a skipped test and also rip out the
    expectations stuff from regrtest and put it with the tests instead.

.. todo::
    Think about beginner task of properly making APIs private (i.e., leading
    underscore where needed) or finally documenting them;
    see http://mail.python.org/pipermail/python-dev/2010-November/105476.html

.. todo::
    Think about suggesting going through stagnant issues (rather advanced)



.. _buildbots: http://python.org/dev/buildbot/
.. _PEP 7: http://www.python.org/dev/peps/pep-0007
.. _PEP 8: http://www.python.org/dev/peps/pep-0008


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

