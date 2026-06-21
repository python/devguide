.. _quick-reference:

===============
Quick reference
===============

Here are the basic steps needed to get set up and open a pull request.

This is meant as a checklist and cheat-sheet, not a comprehensive guide.
For complete instructions please see the :ref:`setup guide <setup>` and the
:ref:`pull request guide <pullrequest>`.


Setup Git
=========

Install and set up ``Git``.

For detailed setup information, see :ref:`"Install Git" <vcsetup>`.
There is also a more detailed :ref:`Git guide and cheat sheet <gitbootcamp>`.

Fork and clone the repo
-----------------------

Fork `the CPython repository <https://github.com/python/cpython>`__
to your GitHub account and :ref:`get the source code <checkout>` using::

   git clone https://github.com/<your_username>/cpython
   cd cpython

We recommend also setting up ``pre-commit``::

   pre-commit install

For detailed information, see :ref:`"Get the source code" <checkout>` and
:ref:`"Install pre-commit as a Git hook" <install-pre-commit>`.


Build Python
============

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


Run the tests
=============

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


See also :ref:`how to write and run tests <run-write-tests>`.


.. _pullrequest-quickguide:

Create issues and pull requests
===============================

Create issues for nontrivial changes
------------------------------------

For most changes, `create an issue <https://github.com/python/cpython/issues>`__
before submitting a pull request.
Trivial changes like typo fixes do not need issues.

Create work branches
--------------------

Work on a feature or fix in a new branch in Git from the ``main`` branch::

   git checkout -b fix-issue-12345 main

Make changes, then :ref:`commit <commit-changes>` and
:ref:`push to your fork <push-changes>`.

Document your changes
---------------------

Many changes deserve a NEWS entry which documents what changed.

Add a News entry into the ``Misc/NEWS.d/`` directory as individual file.
The news entry can be created by using
`blurb-it <https://blurb-it.herokuapp.com/>`__,
or the :pypi:`blurb` tool and its ``blurb add`` command.

.. tip::

   You can read more about ``blurb`` in its
   `repository <https://github.com/python/blurb>`__.

For more information on writing news entries,
see :ref:`"Updating NEWS and What's New in Python" <news-entry>`.

Create pull requests
--------------------

Create pull bequests on GitHub from your branches, on your fork, and make sure
to put the relevant issue number in ``gh-NNNNNN``` format in the pull request title.
For example:

.. code-block:: text

   gh-12345: Fix some bug in spam module

See also, GitHub's documentation on `creating Pull Requests`_.

For more detailed guidance, follow the :ref:`step-by-step pull request guide <pullrequest-steps>`.

.. note::

   First time contributors will need to sign the Contributor Licensing
   Agreement (CLA) as described in the :ref:`Licensing <cla>` section of
   this guide.

.. _creating Pull Requests: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

Work on your pull request
-------------------------

Make sure the
:ref:`continuous integration checks on your Pull Request are green <keeping-ci-green>` (successful).

Read and respond to reviewer comments on your pull request.

See also, GitHub's documentation on `commenting on Pull Requests`_.

.. note::

   In order to keep the commit history intact, please avoid squashing or amending
   history and then force-pushing to the PR.
   Reviewers often want to look at individual commits.

   CPython uses squash merges, so PRs will end up as single commits when merged.

.. _commenting on Pull Requests: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request
