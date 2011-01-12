Python Developer's Guide
========================

.. toctree::
   :hidden:

   setup
   patch
   runtests
   coverage
   docquality
   silencewarnings
   fixingissues
   triage
   devrole
   languishing
   communication
   coredev


.. todolist::


Contributing
------------

People who wish to contribute to Python **must** read the following documents
in the order provided.
You can stop where you feel comfortable and begin contributing immediately
without reading and understanding these documents all at once, but please do
not skip around within the documentation.

* :ref:`setup`
* Coding style guides
    * `PEP 7`_
    * `PEP 8`_
* :ref:`patch`
* :ref:`runtests`
* Beginner tasks to become familiar with the development process
    * :ref:`docquality`
    * :ref:`coverage`
* Advanced tasks for once you are comfortable
    * :ref:`silencewarnings`
    * Fixing issues found by the buildbots_
    * :ref:`fixingissues`
    * :ref:`triage`
* :ref:`devrole`
    * :ref:`languishing`
* :ref:`communication`
* :ref:`coredev`
    * `Committing patches <XXX>`_


Proposing changes to Python itself
----------------------------------

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
* Source code
    * `Browse online <http://svn.python.org/view/>`_
    * `Daily snapshot <http://svn.python.org/snapshots/>`_

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

.. todo::
    Could have people help make tests discoverable by unittest, but it requires
    some upfront work (e.g., how to handle ResourceDenied)

.. todo::
    Figure out where to put instructions for triagers on filling out issue
    fields properly; change pop-up explanations in tracker to point to doc
    appropriately

.. todo::
    Make sure it is explained somewhere how to apply a patch

.. todo::
    Go through http://docs.pythonsprints.com/core_development/ to make sure
    nothing is missing here



.. _buildbots: http://python.org/dev/buildbot/
.. _PEP 7: http://www.python.org/dev/peps/pep-0007
.. _PEP 8: http://www.python.org/dev/peps/pep-0008


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

