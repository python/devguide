========================
Python Developer's Guide
========================

.. raw:: html

    <script>
    document.addEventListener('DOMContentLoaded', function() {
      activateTab(getOS());
    });
    </script>

.. highlight:: bash

This guide is a comprehensive resource for :ref:`contributing <contributing>`
to Python_ -- for both new and experienced contributors. It is
:ref:`maintained <devguide>` by the same
community that maintains Python.  We welcome your contributions to Python!

.. _quick-reference:

Quick reference
---------------

Here are the basic steps needed to get set up and contribute a patch.
This is meant as a checklist, once you know the basics. For complete
instructions please see the :ref:`setup guide <setup>`.

1. Install and set up :ref:`Git <vcsetup>` and other dependencies
   (see the :ref:`Git Setup <setup>` page for detailed information).

2. Fork `the CPython repository <https://github.com/python/cpython>`_
   to your GitHub account and :ref:`get the source code <checkout>` using::

      git clone https://github.com/<your_username>/cpython
      cd cpython

3. Build Python:

   .. tab:: Unix

      .. code-block:: shell

         ./configure --with-pydebug && make -j

   .. tab:: macOS

      .. code-block:: shell

         ./configure --with-pydebug && make -j

   .. tab:: Windows

      .. code-block:: dosbatch

         PCbuild\build.bat -e -d

   See also :ref:`more detailed instructions <compiling>`,
   :ref:`how to install and build dependencies <build-dependencies>`,
   and the platform-specific pages for :ref:`Unix <unix-compiling>`,
   :ref:`macOS`, and :ref:`Windows <windows-compiling>`.

4. :ref:`Run the tests <runtests>`:

   .. tab:: Unix

      .. code-block:: shell

         ./python -m test -j3

   .. tab:: macOS

      .. code-block:: shell

         ./python.exe -m test -j3

      Note: :ref:`Most <mac-python.exe>` macOS systems use
      :file:`./python.exe` in order to avoid filename conflicts with
      the ``Python`` directory.

   .. tab:: Windows

      .. code-block:: dosbatch

         .\python.bat -m test -j3

5. Create a new branch where your work for the issue will go, e.g.::

      git checkout -b fix-issue-12345 main

   If an issue does not already exist, please `create it
   <https://github.com/python/cpython/issues>`_.  Trivial issues (e.g. typo fixes) do
   not require any issue to be created.

6. Once you fixed the issue, run the tests, and the patchcheck:

   .. tab:: Unix

      .. code-block:: shell

         make patchcheck

   .. tab:: macOS

      .. code-block:: shell

         make patchcheck

   .. tab:: Windows

      .. code-block:: dosbatch

         .\python.bat Tools\patchcheck\patchcheck.py

   If everything is ok, commit.

7. Push the branch on your fork on GitHub and :ref:`create a pull request
   <pullrequest>`.  Include the issue number using ``gh-NNNN`` in the
   pull request description.  For example:

   .. code-block:: text

      gh-12345: Fix some bug in spam module

8. Add a News entry into the ``Misc/NEWS.d`` directory as individual file. The
   news entry can be created by using `blurb-it <https://blurb-it.herokuapp.com/>`_,
   or the `blurb <https://pypi.org/project/blurb/>`_ tool and its ``blurb add``
   command. Please read more about ``blurb`` in its
   `repository <https://github.com/python/core-workflow/tree/main/blurb>`_.

.. note::

   First time contributors will need to sign the Contributor Licensing
   Agreement (CLA) as described in the :ref:`Licensing <cla>` section of
   this guide.

Quick links
-----------

Here are some links that you probably will reference frequently while
contributing to Python:

* `Issue tracker`_
* `Buildbot status`_
* :ref:`help`
* PEPs_ (Python Enhancement Proposals)
* :ref:`gitbootcamp`

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

======================== =================== ======================= =======================
Contributors             Documentarians      Triagers                Core Developers
======================== =================== ======================= =======================
:ref:`setup`             :ref:`docquality`   :ref:`tracker`          :ref:`responsibilities`
:ref:`help`              :ref:`documenting`  :ref:`triaging`         :ref:`developers`
:ref:`pullrequest`       :ref:`style-guide`  :ref:`helptriage`       :ref:`committing`
:ref:`runtests`          :ref:`rst-primer`   :ref:`experts`          :ref:`devcycle`
:ref:`fixingissues`      :ref:`translating`  :ref:`labels`           :ref:`motivations`
:ref:`communication`     :ref:`devguide`     :ref:`gh-faq`           :ref:`office hour`
:ref:`gitbootcamp`                           :ref:`triage-team`      :ref:`experts`
:ref:`devcycle`
======================== =================== ======================= =======================

We **recommend** that the documents in this guide be read as needed. You
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

* :ref:`stdlibchanges`
* :ref:`langchanges`


Other interpreter implementations
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
* MicroPython_: A tiny Python interpreter with small subset of the Python
  standard library that is optimised to run on microcontrollers and in
  constrained environments.
* CircuitPython_: A fork of MicroPython designed to simplify experimenting
  and learning to code on low-cost microcontroller boards.


Key resources
-------------

* Coding style guides

  * :PEP:`7` (Style Guide for C Code)
  * :PEP:`8` (Style Guide for Python Code)

* `Issue tracker`_

  * :ref:`experts`

* `Buildbot status`_
* Source code

  * `Browse online <https://github.com/python/cpython/>`_
  * `Snapshot of the *main* branch <https://github.com/python/cpython/archive/main.zip>`_

* PEPs_ (Python Enhancement Proposals)
* :ref:`help`
* :ref:`developers`


.. _resources:

Additional resources
--------------------

* Anyone can clone the sources for this guide.  See :ref:`devguide`.
* Help with ...

  * :ref:`exploring`
  * :ref:`grammar`
  * :ref:`parser`
  * :ref:`compiler`
  * :ref:`garbage_collector`

* Tool support

  * :ref:`gdb`
  * :ref:`clang`
  * Various tools with configuration files as found in the `Misc directory`_
  * Information about editors and their configurations can be found in the
    `wiki <https://wiki.python.org/moin/PythonEditors>`_

* `python.org maintenance`_
* :ref:`Search this guide <search>`


Code of conduct
---------------
Please note that all interactions on
`Python Software Foundation <https://www.python.org/psf-landing/>`__-supported
infrastructure is `covered
<https://www.python.org/psf/records/board/minutes/2014-01-06/#management-of-the-psfs-web-properties>`__
by the `PSF Code of Conduct <https://www.python.org/psf/conduct/>`__,
which includes all infrastructure used in the development of Python itself
(e.g. mailing lists, issue trackers, GitHub, etc.).
In general this means everyone is expected to be open, considerate, and
respectful of others no matter what their position is within the project.

Status of Python branches
-------------------------

Moved to :ref:`versions`

.. _contents:

Full table of contents
----------------------

.. toctree::
   :maxdepth: 3

   getting-started/index
   developer-workflow/index
   triage/index
   documentation/index
   testing/index
   development-tools/index
   core-developers/index
   internals/index
   versions

.. _Buildbot status: https://www.python.org/dev/buildbot/
.. _Misc directory: https://github.com/python/cpython/tree/main/Misc
.. _PEPs: https://peps.python.org/
.. _python.org maintenance: https://pythondotorg.readthedocs.io/
.. _Python: https://www.python.org/
.. _Core Python Mentorship: https://www.python.org/dev/core-mentorship/
.. _PyPy: https://www.pypy.org
.. _Jython: https://www.jython.org/
.. _IronPython: https://ironpython.net/
.. _Stackless: https://github.com/stackless-dev/stackless/wiki/
.. _MicroPython: https://micropython.org/
.. _CircuitPython: https://circuitpython.org/
.. _Issue tracker: https://github.com/python/cpython/issues
