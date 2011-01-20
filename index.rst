Python Developer's Guide
========================

.. toctree::
   :hidden:

   setup
   help
   patch
   runtests
   coverage
   docquality
   silencewarnings
   fixingissues
   helptriage
   devrole
   triaging
   languishing
   communication
   coredev
   committing

   stdlibchanges
   langchanges

   experts
   grammar
   compiler


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
* :ref:`help`
* :ref:`patch`
* :ref:`runtests`
* Beginner tasks to become familiar with the development process
    * :ref:`docquality`
    * :ref:`coverage`
* Advanced tasks for once you are comfortable
    * :ref:`silencewarnings`
    * Fixing issues found by the buildbots_
    * :ref:`fixingissues`
    * :ref:`helptriage`
* :ref:`devrole`
    * :ref:`triaging`
    * :ref:`languishing`
* :ref:`communication`
* :ref:`coredev`
    * :ref:`committing`


Proposing changes to Python itself
----------------------------------

* :ref:`stdlibchanges`
* :ref:`langchanges`


.. _resources:

Resources
---------

* Core developers can checkout and edit this devguide at
  ssh://hg@hg.python.org/devguide
* `Issue tracker <http://bugs.python.org/>`_
    * `Meta tracker <http://psf.upfronthosting.co.za/roundup/meta>`_ (issue
      tracker for the issue tracker)
    * :ref:`experts`
* Buildbots_
* Source code
    * `Browse online <http://svn.python.org/view/>`_
    * `Daily snapshot <http://svn.python.org/snapshots/>`_
* Help with ...
    * :ref:`grammar`
    * :ref:`compiler`


.. _buildbots: http://python.org/dev/buildbot/
.. _PEP 7: http://www.python.org/dev/peps/pep-0007
.. _PEP 8: http://www.python.org/dev/peps/pep-0008


.. todo::
    move various files out of Misc to here (e.g., README.valgrind,
    Porting, SpecialBuilds.txt, maintainers.rst, etc.); asked python-dev on
    2011-01-17 if there were objections to my plans

.. todo::
    Think about beginner task of properly making APIs private (i.e., leading
    underscore where needed) or finally documenting them;
    see http://mail.python.org/pipermail/python-dev/2010-November/105476.html
    and http://bugs.python.org/issue10894; emailed Georg on 2011-01-18 to find
    out if 'make coverage' even works for py3k

.. todo::
    Make dev FAQ into a tools FAQ

.. todo::
    Talk to Collin et. al. about an unladen task; emailed 2011-01-17

.. todo::
    Task to make sure there are no warnings emitted during compilation

.. todo::
    Go through http://docs.pythonsprints.com/core_development/ to make sure
    nothing is missing here

.. todo::
    Create test.support.optional_import() for tests to use to import modules
    that are optional on various platforms. This would allow for moving away
    from ImportError representing a skipped test and also rip out the
    expectations stuff from regrtest and put it with the tests instead.

.. todo::
    Could have people help make tests discoverable by unittest, but it requires
    some upfront work (e.g., how to handle ResourceDenied)


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

