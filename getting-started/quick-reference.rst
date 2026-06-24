.. _quick-reference:

===============
Quick reference
===============

.. include:: /include/activate-tab.rst

Here are the basic steps needed to get set up and open a pull request.

This is meant as a checklist and cheat-sheet, not a comprehensive guide.
For complete instructions see the :ref:`setup guide <setup>` and the
:ref:`pull request guide <pullrequest>`.


Set up Git
==========

Install and set up ``Git``.

For detailed setup information, see :ref:`"Install Git" <vcsetup>`.
There is also a more detailed :ref:`Git guide and cheat sheet <gitbootcamp>`.

Fork and clone the repo
-----------------------

Fork `the CPython repository <https://github.com/python/cpython>`__
to your GitHub account and clone the repo using::

   git clone https://github.com/<your_username>/cpython
   cd cpython

For detailed information, see :ref:`"Get the source code" <checkout>`.


Build Python
============

.. tab:: Unix

   .. code-block:: shell

      ./configure --config-cache --with-pydebug && make -j $(nproc)

.. tab:: macOS

   .. code-block:: shell

      ./configure --config-cache --with-pydebug && make -j$(sysctl -n hw.logicalcpu)

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

      ./python -m test -j0

.. tab:: macOS

   .. code-block:: shell

      ./python.exe -m test -j0

   .. note::
      :ref:`Most <mac-python.exe>` macOS systems use
      :file:`./python.exe` in order to avoid filename conflicts with
      the ``Python`` directory.

.. tab:: Windows

   .. code-block:: dosbatch

      .\python.bat -m test -j0


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
For more information on how and when to write news entries,
see :ref:`"Updating NEWS and What's New in Python" <news-entry>`.

A news entry can be created locally with the :pypi:`blurb` tool
and its ``blurb add`` command or online after a pull request has
been opened with `blurb-it <https://blurb-it.herokuapp.com/>`__.

For more information about how to create news entries, see
:ref:`"How to add a NEWS entry" <news-entry-howto>`.

Create pull requests
--------------------

Create pull requests on GitHub from your branches, on your fork, and make sure
to put the relevant issue number in ``gh-NNNNNN``` format in the pull request title.
For example:

.. code-block:: text

   gh-12345: Fix some bug in spam module

See also, GitHub's documentation on `creating pull requests`_.

For more detailed guidance, follow the :ref:`step-by-step pull request guide <pullrequest-steps>`.

.. note::

   First time contributors will need to sign the Contributor Licensing
   Agreement (CLA) as described in the :ref:`Licensing <cla>` section of
   this guide.

.. _creating pull requests: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

Work on your pull request
-------------------------

Make sure the :ref:`continuous integration checks on your pull
request are green <keeping-ci-green>` (successful).

Read and respond to reviewer comments on your pull request.

See also, GitHub's documentation on `commenting on pull requests`_.

Don't force-push
----------------

In order to keep the commit history intact, avoid squashing or amending
history and then force-pushing to the PR.
Reviewers often want to look at individual commits.

CPython uses squash merges, so PRs will end up as single commits when merged.

.. _commenting on Pull Requests: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request
