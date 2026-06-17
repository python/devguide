.. _quick-reference:

===============
Quick reference
===============

Here are the basic steps needed to get set up and open a pull request.

This is meant as a checklist and cheat-sheet, not a comprehensive guide.
For complete instructions please see the :ref:`setup guide <setup>`.

1. Install and set up :ref:`Git <vcsetup>` and other dependencies
   (see the :ref:`Git Setup <setup>` page for detailed information).

2. Fork `the CPython repository <https://github.com/python/cpython>`__
   to your GitHub account and :ref:`get the source code <checkout>` using::

      git clone https://github.com/<your_username>/cpython
      cd cpython

3. Build Python:

   .. tab:: Unix

      .. code-block:: shell

         ./configure --config-cache --with-pydebug && make -j $(nproc)

   .. tab:: macOS

      .. code-block:: shell

         ./configure --config-cache --with-pydebug && make -j8

   .. tab:: Windows

      .. code-block:: dosbatch

         PCbuild\build.bat -e -d

   See also :ref:`more detailed instructions <compiling>`,
   :ref:`how to install and build dependencies <build-dependencies>`,
   and the platform-specific pages for :ref:`Unix <unix-compiling>`,
   :ref:`macOS <macOS>`, and :ref:`Windows <windows-compiling>`.

4. :ref:`Run the tests <runtests>`:

   .. tab:: Unix

      .. code-block:: shell

         ./python -m test -j3

   .. tab:: macOS

      .. code-block:: shell

         ./python.exe -m test -j8

      .. note::
         :ref:`Most <mac-python.exe>` macOS systems use
         :file:`./python.exe` in order to avoid filename conflicts with
         the ``Python`` directory.

   .. tab:: Windows

      .. code-block:: dosbatch

         .\python.bat -m test -j3

5. Create a new branch where your work for the issue will go, for example::

      git checkout -b fix-issue-12345 main

   If an issue does not already exist, please `create it
   <https://github.com/python/cpython/issues>`__.  Trivial issues (for example, typos) do
   not require an issue.

6. Push the branch on your fork on GitHub and :ref:`create a pull request
   <pullrequest>`.  Include the issue number using ``gh-NNNNNN`` in the
   pull request title.  For example:

   .. code-block:: text

      gh-12345: Fix some bug in spam module

7. Add a News entry into the ``Misc/NEWS.d/`` directory as individual file. The
   news entry can be created by using `blurb-it <https://blurb-it.herokuapp.com/>`__,
   or the :pypi:`blurb` tool and its ``blurb add``
   command. Please read more about ``blurb`` in its
   `repository <https://github.com/python/blurb>`__.

.. note::

   First time contributors will need to sign the Contributor Licensing
   Agreement (CLA) as described in the :ref:`Licensing <cla>` section of
   this guide.
