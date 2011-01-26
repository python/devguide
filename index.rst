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
   developers
   committing
   devcycle

   stdlibchanges
   langchanges

   experts
   emacs
   gdb
   grammar
   compiler
   faq


Contributing
------------

We encourage everyone to contribute to Python and that's why we have put up
this developer's guide.  You **should** read the following documents in
the order provided.  You can stop where you feel comfortable and begin
contributing immediately without reading and understanding these documents all
at once, but please do not skip around within the documentation as everything
is written assuming preceding documentation has been read.

* :ref:`setup`
* Coding style guides
    * `PEP 7`_ (Style Guide for C Code)
    * `PEP 8`_ (Style Guide for Python Code)
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
    * :ref:`developers`
    * :ref:`committing`
    * :ref:`devcycle`


Proposing changes to Python itself
----------------------------------

* :ref:`stdlibchanges`
* :ref:`langchanges`


.. _resources:

Resources
---------

* Anyone can checkout this guide from http://hg.python.org/devguide/.
  Core developers should use ssh://hg@hg.python.org/devguide instead, so
  that they can push back their edits to the server.
* `Issue tracker <http://bugs.python.org/>`_
    * `Meta tracker <http://psf.upfronthosting.co.za/roundup/meta>`_ (issue
      tracker for the issue tracker)
    * :ref:`experts`
    * `Firefox search engine plug-in`_
* Buildbots_
* Source code
    * `Browse online <http://svn.python.org/view/>`_
    * `Daily snapshot <http://svn.python.org/snapshots/>`_
    * `Daily OS X installer <http://python.org/dev/daily-dmg/>`_
* Tool support
    * :ref:`emacs`
    * :ref:`gdb`
    * Various tools with configuration files as found in the `Misc directory`_
* Help with ...
    * :ref:`grammar`
    * :ref:`compiler`
* :ref:`faq`
* PEPs_ (Python Enhancement Proposals)
* `python.org maintenance`_


.. _buildbots: http://python.org/dev/buildbot/
.. _Firefox search engine plug-in: http://www.python.org/dev/searchplugin/
.. _Misc directory: http://svn.python.org/view/python/branches/py3k/Misc/
.. _PEPs: http://www.python.org/dev/peps
.. _PEP 7: http://www.python.org/dev/peps/pep-0007
.. _PEP 8: http://www.python.org/dev/peps/pep-0008
.. _python.org maintenance: http://python.org/dev/pydotorg/


Indices and tables
==================

.. XXX commented until non-empty
   * :ref:`genindex`
   * :ref:`modindex`

* :ref:`search`

