========================
Python Developer's Guide
========================

This guide is a comprehensive resource for :ref:`contributing <contributing>`
to Python_ -- for both new and experienced contributors.  It is
:ref:`maintained <helping-with-the-developers-guide>` by the same community
that maintains Python.  We welcome your contributions to Python!


Quick Reference
---------------

Here are the basic steps needed to get :ref:`set up <setup>` and contribute a
patch. This is meant as a checklist, once you know the basics. For complete 
instructions please see the `setup guide <setup>`.

1. Install and set up :ref:`Git <vcsetup>` and other dependencies
   (see the :ref:`Get Setup <setup>` page for detailed information).

2. Fork `the CPython repository <https://github.com/python/cpython>`_
   to your GitHub account and :ref:`get the source code <checkout>` using::

      git clone https://github.com/<your_username>/cpython

3. Build Python, on UNIX and Mac OS use::

      ./configure --with-pydebug && make -j

   and on Windows use::

      PCbuild\build.bat -e -d

   See also :ref:`more detailed instructions <compiling>`,
   :ref:`how to build dependencies <build-dependencies>`, and the
   plaform-specific pages for :ref:`UNIX <unix-compiling>`,
   :ref:`Mac OS <MacOS>`, and :ref:`Windows <windows-compiling>`.

4. :doc:`Run the tests <runtests>`::

      ./python -m test -j3

   On :ref:`most <mac-python.exe>` Mac OS X systems, replace :file:`./python`
   with :file:`./python.exe`.  On Windows, use :file:`python.bat`.  With Python
   2.7, replace ``test`` with ``test.regrtest``.

5. Create a new branch where your work for the issue will go, e.g.::

      git checkout -b fix-issue-12345 master

   If an issue does not already exist, please `create it
   <https://bugs.python.org/>`_.  Trivial issues (e.g. typo fixes) do not
   require any issue to be created.

6. Once you fixed the issue, run the tests, run ``make patchcheck``, and if
   everything is ok, commit.

7. Push the branch on your fork on GitHub and :doc:`create a pull request
   <pullrequest>`.  Include the issue number using ``bpo-NNNN`` in the
   pull request description.  For example::

      bpo-12345: Fix some bug in spam module

.. note::

   First time contributors will need to sign the Contributor Licensing
   Agreement (CLA) as described in the :ref:`Licensing <cla>` section of
   this guide.

Quick Links
-----------

Here are some links that you probably will reference frequently while
contributing to Python:

* `Issue tracker`_
* `Buildbot status`_
* :doc:`help`
* PEPs_ (Python Enhancement Proposals)
* :doc:`gitdevs`
* :doc:`gitbootcamp`

.. _branchstatus:

Status of Python branches
-------------------------

+------------------+--------------+-------------+----------------+----------------+----------------------------------------------------------------------------+
| Branch           | Schedule     | Status      | First release  | End-of-life    | Comment                                                                    |
+==================+==============+=============+================+================+============================================================================+
| default          | :pep:`537`   | features    | *2018-06-15*   | *2023-06-15*   | The default branch is currently the future version Python 3.7.             |
+------------------+--------------+-------------+----------------+----------------+----------------------------------------------------------------------------+
| 3.6              | :pep:`494`   | bugfix      | 2016-12-23     | *2021-12-23*   |                                                                            |
+------------------+--------------+-------------+----------------+----------------+----------------------------------------------------------------------------+
| 3.5              | :pep:`478`   | bugfix      | 2015-09-13     | *2020-09-13*   |                                                                            |
+------------------+--------------+-------------+----------------+----------------+----------------------------------------------------------------------------+
| 2.7              | :pep:`373`   | bugfix      | 2010-07-03     | *2020-01-01*   | The support has been extended to 2020 (1).                                 |
+------------------+--------------+-------------+----------------+----------------+----------------------------------------------------------------------------+
| 3.4              | :pep:`429`   | security    | 2014-03-16     | *2019-03-16*   | `Last binary release: Python 3.4.4                                         |
|                  |              |             |                |                | <https://www.python.org/download/releases/3.4.4/>`_                        |
+------------------+--------------+-------------+----------------+----------------+----------------------------------------------------------------------------+
| 3.3              | :pep:`398`   | security    | 2012-09-29     | *2017-09-29*   | `Last binary release: Python 3.3.5                                         |
|                  |              |             |                |                | <https://www.python.org/download/releases/3.3.5/>`_                        |
+------------------+--------------+-------------+----------------+----------------+----------------------------------------------------------------------------+
| 3.2              | :pep:`392`   | end-of-life | 2011-02-20     | 2016-02-20     | `Last binary release: Python 3.2.5                                         |
|                  |              |             |                |                | <https://www.python.org/download/releases/3.2.5/>`_                        |
+------------------+--------------+-------------+----------------+----------------+----------------------------------------------------------------------------+
| 3.1              | :pep:`375`   | end-of-life | 2009-06-27     | 2012-04-11     | `Last release: Python 3.1.5                                                |
|                  |              |             |                |                | <https://www.python.org/download/releases/3.1.5/>`_                        |
+------------------+--------------+-------------+----------------+----------------+----------------------------------------------------------------------------+
| 3.0              | :pep:`361`   | end-of-life | 2008-12-03     | 2009-01-13     | `Last release: Python 3.0.1                                                |
|                  |              |             |                |                | <https://www.python.org/download/releases/3.0.1/>`_                        |
+------------------+--------------+-------------+----------------+----------------+----------------------------------------------------------------------------+
| 2.6              | :pep:`361`   | end-of-life | 2008-10-01     | 2013-10-29     | `Last release: Python 2.6.9                                                |
|                  |              |             |                |                | <https://www.python.org/download/releases/2.6.9/>`_                        |
+------------------+--------------+-------------+----------------+----------------+----------------------------------------------------------------------------+

(1) The exact date of Python 2.7 end-of-life has not been decided yet. It will
be decided by Python 2.7 release manager, Benjamin Peterson, who will update
the :pep:`373`. Read also the `[Python-Dev] Exact date of Python 2 EOL?
<https://mail.python.org/pipermail/python-dev/2017-March/147655.html>`_ thread
on python-dev (March 2017).

Status:

:features: new features are only added to the default branch, this branch
    accepts any kind of change.
:bugfix: bugfixes and security fixes are accepted, new binaries are still
    released.
:security: only security fixes are accepted and no more binaries are released,
    but new source-only versions can be released
:end-of-life: branch no longer maintained; no more changes can be pushed to
    this branch.

Dates in *italic* are scheduled and can be adjusted.

By default, the end-of-life is scheduled 5 years after the first release.  It
can be adjusted by the release manager of each branch. Versions older than 2.7
have reached end-of-life.

See also :ref:`Security branches <secbranch>`.


.. _contributing:

Contributing
------------

We encourage everyone to contribute to Python and that's why we have put up this
developer's guide.  If you still have questions after reviewing the material in
this guide, then the `Python Mentors`_ group is available to help guide new
contributors through the process.

A number of individuals from the Python community have contributed to a series
of excellent guides at `Open Source Guides <https://opensource.guide/>`_.

Core developers and contributors alike will find the following guides useful:

* `How to Contribute to Open Source <https://opensource.guide/how-to-contribute/>`_
* `Building Welcoming Communities <https://opensource.guide/building-community/>`_

Guide for contributing to Python:

* :doc:`setup`
* :doc:`help`
* :doc:`pullrequest`
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
    * :doc:`experts`
* :doc:`communication`
* :doc:`coredev`
    * :doc:`committing`
    * :doc:`devcycle`
    * :doc:`buildbots`
    * :doc:`coverity`
* :doc:`gitdevs`
* :doc:`gitbootcamp`

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
    * `Browse online <https://github.com/python/cpython/>`_
    * `Snapshot of the *master* branch <https://github.com/python/cpython/archive/master.zip>`_
    * `Daily OS X installer <http://buildbot.python.org/daily-dmg/>`_
* PEPs_ (Python Enhancement Proposals)
* :doc:`help`
* :doc:`developers`


.. _resources:

Additional Resources
--------------------

* Anyone can clone the sources for this guide.  See
  :ref:`helping-with-the-developers-guide`.
* Help with ...
    * :doc:`exploring`
    * :doc:`grammar`
    * :doc:`compiler`
* Tool support
    * :doc:`gdb`
    * :doc:`clang`
    * Various tools with configuration files as found in the `Misc directory`_
    * Information about editors and their configurations can be found in the
      `wiki <https://wiki.python.org/moin/PythonEditors>`_
* `python.org maintenance`_

* :ref:`Search this guide <search>`


Code of Conduct
---------------
Please note that all interactions on
`Python Software Foundation <https://www.python.org/psf-landing/>`__-supported infrastructure is
`covered <https://www.python.org/psf/records/board/minutes/2014-01-06/#management-of-the-psfs-web-properties>`__
by the `PSF Code of Conduct <https://www.python.org/psf/codeofconduct/>`__, which includes all
infrastructure used in the development of Python itself (e.g. mailing lists, issue trackers, GitHub, etc.).
In general this means everyone is expected to be open, considerate, and respectful of others no matter what
their position is within the project.

.. _contents:

Full Table of Contents
----------------------

.. toctree::
   :numbered:

   setup
   help
   pullrequest
   runtests
   coverage
   docquality
   documenting
   silencewarnings
   fixingissues
   tracker
   triaging
   communication
   porting
   coredev
   developers
   committing
   devcycle
   buildbots
   stdlibchanges
   langchanges
   experts
   gdb
   exploring
   grammar
   compiler
   coverity
   clang
   buildslave
   gitdevs
   motivations
   gitbootcamp


.. _Buildbot status: https://www.python.org/dev/buildbot/
.. _Firefox search engine plug-in: https://www.python.org/dev/searchplugin/
.. _Misc directory: https://github.com/python/cpython/tree/master/Misc
.. _PEPs: https://www.python.org/dev/peps/
.. _python.org maintenance: https://pythondotorg.readthedocs.io/
.. _Python: https://www.python.org/
.. _Python Mentors: http://pythonmentors.com/
.. _PyPy: http://www.pypy.org/
.. _Jython: http://www.jython.org/
.. _IronPython: http://ironpython.net/
.. _Stackless: http://www.stackless.com/
.. _Issue tracker: https://bugs.python.org/
