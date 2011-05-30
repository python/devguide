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
   buildbots

   stdlibchanges
   langchanges

   experts
   emacs
   gdb
   grammar
   compiler
   faq


Quick Links
-----------

Here are some links that you may find you reference frequently while
contributing to Python.

* `Issue tracker <http://bugs.python.org/>`_
* `Buildbot status`_
* :doc:`faq`
* PEPs_ (Python Enhancement Proposals)


Contributing
------------

We encourage everyone to contribute to Python and that's why we have put up
this developer's guide.  You **should** read the following documents in
the order provided.  You can stop where you feel comfortable and begin
contributing immediately without reading and understanding these documents all
at once, but please do not skip around within the documentation as everything
is written assuming preceding documentation has been read.

You can, *however*, read the :doc:`FAQ <faq>` at any point!

* :doc:`setup`
* Coding style guides
    * `PEP 7`_ (Style Guide for C Code)
    * `PEP 8`_ (Style Guide for Python Code)
* :doc:`help`
* :doc:`patch`
* :doc:`runtests`
* Beginner tasks to become familiar with the development process
    * :doc:`docquality`
    * :doc:`coverage`
* Advanced tasks for once you are comfortable
    * :doc:`silencewarnings`
    * Fixing issues found by the :doc:`buildbots <buildbots>`
    * :doc:`fixingissues`
    * :doc:`helptriage`
* :doc:`devrole`
    * :doc:`triaging`
    * :doc:`languishing`
* :doc:`communication`
* :doc:`coredev`
    * :doc:`committing`
    * :doc:`devcycle`
    * :doc:`buildbots`


Proposing changes to Python itself
----------------------------------

* :doc:`stdlibchanges`
* :doc:`langchanges`


.. _resources:


Resources
---------

* Anyone can checkout this guide from http://hg.python.org/devguide/.
  Core developers should use ssh://hg@hg.python.org/devguide instead, so
  that they can push back their edits to the server.
* `Issue tracker <http://bugs.python.org/>`_
    * `Meta tracker <http://psf.upfronthosting.co.za/roundup/meta>`_ (issue
      tracker for the issue tracker)
    * :doc:`experts`
    * `Firefox search engine plug-in`_
* `Buildbot status`_
* Source code
    * `Browse online <http://hg.python.org/cpython/>`_
    * `Snapshot of py3k <http://hg.python.org/cpython/archive/tip.tar.bz2>`_
    * `Daily OS X installer <http://www.python.org/dev/daily-dmg/>`_
* Tool support
    * :doc:`emacs`
    * :doc:`gdb`
    * Various tools with configuration files as found in the `Misc directory`_
* Help with ...
    * :doc:`grammar`
    * :doc:`compiler`
* :doc:`faq`
* PEPs_ (Python Enhancement Proposals)
* `python.org maintenance`_
* :doc:`developers`


.. _Buildbot status: http://python.org/dev/buildbot/
.. _Firefox search engine plug-in: http://www.python.org/dev/searchplugin/
.. _Misc directory: http://hg.python.org/cpython/file/tip/Misc
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

