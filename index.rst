========================
Python Developer's Guide
========================

This guide is a comprehensive resource for :ref:`contributing <contributing>`
to Python_ -- for both new and experienced contributors.  It is
:ref:`maintained <helping-with-the-developers-guide>` by the same community
that maintains Python.  We welcome your contributions to Python!


Quick Start
-----------

Here are the basic steps needed to get :ref:`set up <setup>` and contribute a
patch:

1. :ref:`Get the source code <checkout>`::

      hg clone http://hg.python.org/cpython

2. :ref:`Build Python <compiling>`.  On :ref:`UNIX <unix-compiling>`::

      ./configure --with-pydebug && make -j2

   On :ref:`Windows <windows-compiling>`, open the solution file
   :file:`PCbuild\\pcbuild.sln` in Visual Studio, select :menuselection:`Debug`,
   and :menuselection:`Build --> Build Solution`.
3. :doc:`Run the tests <runtests>`::

   ./python -m test -j3

   On :ref:`most <mac-python.exe>` Mac OS X systems, replace :file:`./python`
   with :file:`./python.exe`.  On Windows, use :file:`PCbuild\\python_d.exe` or
   check the :ref:`Windows instructions <win-python.exe>`.  With Python 2.7,
   replace ``test`` with ``test.regrtest``.
4. Make the :doc:`patch <patch>`.
5. Submit it to the `issue tracker`_.


Quick Links
-----------

Here are some links that you probably will reference frequently while
contributing to Python.

* `Issue tracker`_
* `Buildbot status`_
* :doc:`faq`
* PEPs_ (Python Enhancement Proposals)


.. _contributing:

Contributing
------------

We encourage everyone to contribute to Python and that's why we have put up this
developer's guide.  If you still have questions after reviewing the material in
this guide, then the `Python Mentors`_ group is available to help guide new
contributors through the process.  The :doc:`Developer FAQ <faq>` is another
useful source of information.

Guide for contributing to Python:

* :doc:`setup`
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
* :ref:`tracker` and :ref:`helptriage`
    * :doc:`triaging`
* :doc:`communication`
* :doc:`coredev`
    * :doc:`committing`
    * :doc:`devcycle`
    * :doc:`buildbots`

It is **recommended** that the above documents be read in the order listed.  You
can stop where you feel comfortable and begin contributing immediately without
reading and understanding these documents all at once.  If you do choose to skip
around within the documentation, be aware that it is written assuming preceding
documentation has been read so you may find it necessary to backtrack to fill in
missing concepts and terminology.


Proposing changes to Python itself
----------------------------------

Improving Python's code, documentation and tests are ongoing tasks that are
never going to be "finished", as Python operates as part of an ever-evolving
system of technology.  An even more challenging ongoing task than these
necessary maintenance activities is finding ways to make Python, in the form of
the standard library and the language definition, an even better tool in a
developer's toolkit.

While these kinds of change are much rarer than those described above, they do
happen and that process is also described as part of this guide:

* :doc:`stdlibchanges`
* :doc:`langchanges`

Also refer to :ref:`suggesting-changes` in the FAQ.


Other Interpreter Implementations
---------------------------------

This guide is specifically for contributing to the Python reference interpreter,
also known as CPython (while most of the standard library is written in Python,
the interpreter core is written in C and integrates most easily with the C and
C++ ecosystems).

There are other Python implementations, each with a different focus.  Like
CPython, they always have more things they would like to do than they have
developers to work on them.  Some major example that may be of interest are:

* PyPy_: A Python interpreter focused on high speed (JIT-compiled) operation
  on major platforms
* Jython_: A Python interpreter focused on good integration with the Java
  Virtual Machine (JVM) environment
* IronPython_: A Python interpreter focused on good integration with the
  Common Language Runtime (CLR) provided by .NET and Mono
* Stackless_: A Python interpreter focused on providing lightweight
  microthreads while remaining largely compatible with CPython specific
  extension modules


.. _resources:

Key Resources
-------------

* Coding style guides
    * :PEP:`7` (Style Guide for C Code)
    * :PEP:`8` (Style Guide for Python Code)
* `Issue tracker`_
    * `Meta tracker <http://psf.upfronthosting.co.za/roundup/meta>`_ (issue
      tracker for the issue tracker)
    * :doc:`experts`
    * `Firefox search engine plug-in`_
* `Buildbot status`_
* Source code
    * `Browse online <http://hg.python.org/cpython/file/default/>`_
    * `Snapshot of py3k <http://hg.python.org/cpython/archive/default.tar.bz2>`_
    * `Daily OS X installer <http://buildbot.python.org/daily-dmg/>`_
* PEPs_ (Python Enhancement Proposals)
* :doc:`faq`
* :doc:`developers`


Additional Resources
--------------------

* Anyone can clone the sources for this guide.  See
  :ref:`helping-with-the-developers-guide`.
* Help with ...
    * :doc:`grammar`
    * :doc:`compiler`
* Tool support
    * :doc:`emacs`
    * :doc:`gdb`
    * Various tools with configuration files as found in the `Misc directory`_
* `python.org maintenance`_

* :ref:`Search this guide <search>`


.. _contents:

Full Table of Contents
----------------------

.. toctree::
   :numbered:

   setup
   help
   patch
   runtests
   coverage
   docquality
   documenting
   silencewarnings
   fixingissues
   tracker
   triaging
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


.. _Buildbot status: http://python.org/dev/buildbot/
.. _Firefox search engine plug-in: http://www.python.org/dev/searchplugin/
.. _Misc directory: http://hg.python.org/cpython/file/default/Misc
.. _PEPs: http://www.python.org/dev/peps
.. _python.org maintenance: http://python.org/dev/pydotorg/
.. _Python: http://www.python.org/
.. _Python Mentors: http://pythonmentors.com/
.. _PyPy: http://www.pypy.org/
.. _Jython: http://www.jython.org/
.. _IronPython: http://ironpython.net/
.. _Stackless: http://www.stackless.com/
.. _Issue tracker: http://bugs.python.org/
