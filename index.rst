========================
Python Developer's Guide
========================

.. highlight:: bash

This guide is a comprehensive resource for :ref:`contributing <contributing>`
to Python_ -- for both new and experienced contributors. It is
:ref:`maintained <helping-with-the-developers-guide>` by the same
community that maintains Python.  We welcome your contributions to Python!

.. _quick-reference:

Quick Reference
---------------

Here are the basic steps needed to get :ref:`set up <setup>` and contribute a
patch. This is meant as a checklist, once you know the basics. For complete
instructions please see the :ref:`setup guide <setup>`.

1. Install and set up :ref:`Git <vcsetup>` and other dependencies
   (see the :ref:`Git Setup <setup>` page for detailed information).

2. Fork `the CPython repository <https://github.com/python/cpython>`_
   to your GitHub account and :ref:`get the source code <checkout>` using::

      git clone https://github.com/<your_username>/cpython
      cd cpython

3. Build Python, on UNIX and Mac OS use::

      ./configure --with-pydebug && make -j

   and on Windows use:

   .. code-block:: dosbatch

      PCbuild\build.bat -e -d

   See also :ref:`more detailed instructions <compiling>`,
   :ref:`how to install and build dependencies <build-dependencies>`,
   and the platform-specific pages for :ref:`UNIX <unix-compiling>`,
   :ref:`Mac OS <MacOS>`, and :ref:`Windows <windows-compiling>`.

4. :doc:`Run the tests <runtests>`::

      ./python -m test -j3

   On :ref:`most <mac-python.exe>` Mac OS X systems, replace :file:`./python`
   with :file:`./python.exe`.  On Windows, use :file:`python.bat`.

5. Create a new branch where your work for the issue will go, e.g.::

      git checkout -b fix-issue-12345 main

   If an issue does not already exist, please `create it
   <https://bugs.python.org/>`_.  Trivial issues (e.g. typo fixes) do not
   require any issue to be created.

6. Once you fixed the issue, run the tests, run ``make patchcheck``, and if
   everything is ok, commit.

7. Push the branch on your fork on GitHub and :doc:`create a pull request
   <pullrequest>`.  Include the issue number using ``bpo-NNNN`` in the
   pull request description.  For example::

      bpo-12345: Fix some bug in spam module

8. Add a News entry into the ``Misc/NEWS.d`` directory as individual file. The
   news entry can be created by using `blurb-it <https://blurb-it.herokuapp.com/>`_,
   or the `blurb <https://pypi.org/project/blurb/>`_ tool and its ``blurb add``
   command. Please read more about ``blurb`` in :ref:`documentation <documenting>`.

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
* :doc:`gitbootcamp`

.. _branchstatus:

Status of Python branches
-------------------------

+------------------+--------------+-------------+----------------+----------------+-----------------------+
| Branch           | Schedule     | Status      | First release  | End-of-life    | Release manager       |
+==================+==============+=============+================+================+=======================+
| main             | :pep:`664`   | features    | *2022-10-03*   | *2027-10*      | Pablo Galindo Salgado |
+------------------+--------------+-------------+----------------+----------------+-----------------------+
| 3.10             | :pep:`619`   | bugfix      | 2021-10-04     | *2026-10*      | Pablo Galindo Salgado |
+------------------+--------------+-------------+----------------+----------------+-----------------------+
| 3.9              | :pep:`596`   | bugfix      | 2020-10-05     | *2025-10*      | Łukasz Langa          |
+------------------+--------------+-------------+----------------+----------------+-----------------------+
| 3.8              | :pep:`569`   | security    | 2019-10-14     | *2024-10*      | Łukasz Langa          |
+------------------+--------------+-------------+----------------+----------------+-----------------------+
| 3.7              | :pep:`537`   | security    | 2018-06-27     | *2023-06-27*   | Ned Deily             |
+------------------+--------------+-------------+----------------+----------------+-----------------------+
| 3.6              | :pep:`494`   | security    | 2016-12-23     | *2021-12-23*   | Ned Deily             |
+------------------+--------------+-------------+----------------+----------------+-----------------------+

.. Remember to update the end-of-life table in devcycle.rst.

Dates in *italic* are scheduled and can be adjusted.

The main branch is currently the future Python 3.11, and is the only
branch that accepts new features.  The latest release for each Python
version can be found on the `download page <https://www.python.org/downloads/>`_.

Status:

:features: new features, bugfixes, and security fixes are accepted.
:prerelease: feature fixes, bugfixes, and security fixes are accepted for the
    upcoming feature release.
:bugfix: bugfixes and security fixes are accepted, new binaries are still
    released. (Also called **maintenance** mode or **stable** release)
:security: only security fixes are accepted and no more binaries are released,
    but new source-only versions can be released
:end-of-life: release cycle is frozen; no further changes can be pushed to it.

See also the :ref:`devcycle` page for more information about branches.

By default, the end-of-life is scheduled 5 years after the first release,
but can be adjusted by the release manager of each branch.  All Python 2
versions have reached end-of-life.


.. _contributing:

Contributing
------------

We encourage everyone to contribute to Python and that's why we have put up this
developer's guide.  If you still have questions after reviewing the material in
this guide, then the `Core Python Mentorship`_ group is available to help guide new
contributors through the process.

A number of individuals from the Python community have contributed to a series
of excellent guides at `Open Source Guides <https://opensource.guide/>`_.

Core developers and contributors alike will find the following guides useful:

* `How to Contribute to Open Source <https://opensource.guide/how-to-contribute/>`_
* `Building Welcoming Communities <https://opensource.guide/building-community/>`_

Guide for contributing to Python:

+------------------------+---------------------+-----------------------+---------------------+
| New Contributors       | Documentarians      | Triagers              | Core Developers     |
+========================+=====================+=======================+=====================+
| :doc:`setup`           | :doc:`docquality`   | :doc:`tracker`        | :doc:`coredev`      |
+------------------------+---------------------+-----------------------+---------------------+
| :doc:`help`            | :doc:`documenting`  | :doc:`triaging`       | :doc:`developers`   |
+------------------------+---------------------+-----------------------+---------------------+
| :doc:`pullrequest`     | :ref:`style-guide`  | :ref:`helptriage`     | :doc:`committing`   |
+------------------------+---------------------+-----------------------+---------------------+
| :doc:`runtests`        | :ref:`rst-primer`   | :doc:`experts`        | :doc:`devcycle`     |
+------------------------+---------------------+-----------------------+---------------------+
| :doc:`fixingissues`    | :ref:`translating`  |                       | :doc:`motivations`  |
+------------------------+---------------------+-----------------------+---------------------+
| :doc:`communication`   |                     |                       | :ref:`office hour`  |
+------------------------+---------------------+-----------------------+---------------------+
| :doc:`gitbootcamp`     |                     |                       |                     |
+------------------------+---------------------+-----------------------+---------------------+

Advanced tasks and topics for once you are comfortable:

* :doc:`silencewarnings`
* Fixing issues found by the :doc:`buildbots <buildbots>`
* :doc:`coverity`
* Helping out with reviewing `open pull requests`_.
  See :ref:`how to review a Pull Request <how-to-review-a-pull-request>`.
* :doc:`fixingissues`

It is **recommended** that the above documents be read as needed. New
contributors will build understanding of the CPython workflow by reading the
sections mentioned in this table. You
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
developers to work on them.  Some major examples that may be of interest are:

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
* `Buildbot status`_
* Source code
    * `Browse online <https://github.com/python/cpython/>`_
    * `Snapshot of the *main* branch <https://github.com/python/cpython/archive/main.zip>`_
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
    * :doc:`parser`
    * :doc:`compiler`
    * :doc:`garbage_collector`
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
`Python Software Foundation <https://www.python.org/psf-landing/>`__-supported
infrastructure is `covered
<https://www.python.org/psf/records/board/minutes/2014-01-06/#management-of-the-psfs-web-properties>`__
by the `PSF Code of Conduct <https://www.python.org/psf/codeofconduct/>`__,
which includes all infrastructure used in the development of Python itself
(e.g. mailing lists, issue trackers, GitHub, etc.).
In general this means everyone is expected to be open, considerate, and
respectful of others no matter what their position is within the project.

.. _contents:

Full Table of Contents
----------------------

.. toctree::
   :maxdepth: 3

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
   parser
   compiler
   garbage_collector
   extensions
   c-api
   coverity
   clang
   buildworker
   motivations
   gitbootcamp
   appendix

.. _Buildbot status: https://www.python.org/dev/buildbot/
.. _Misc directory: https://github.com/python/cpython/tree/main/Misc
.. _PEPs: https://www.python.org/dev/peps/
.. _python.org maintenance: https://pythondotorg.readthedocs.io/
.. _Python: https://www.python.org/
.. _Core Python Mentorship: https://www.python.org/dev/core-mentorship/
.. _PyPy: http://www.pypy.org
.. _Jython: http://www.jython.org/
.. _IronPython: http://ironpython.net/
.. _Stackless: http://www.stackless.com/
.. _Issue tracker: https://bugs.python.org/
.. _open pull requests: https://github.com/python/cpython/pulls?utf8=%E2%9C%93&q=is%3Apr%20is%3Aopen%20label%3A%22awaiting%20review%22
