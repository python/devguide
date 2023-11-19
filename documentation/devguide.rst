.. _devguide:

==================================
Helping with the Developer's Guide
==================================

.. raw:: html

    <script>
    document.addEventListener('DOMContentLoaded', function() {
      activateTab(getOS());
    });
    </script>

.. highlight:: console

The Developer's Guide (what you're reading now) uses the same process as the
main Python documentation, except for some small differences.  The source
lives in a `separate repository`_ and bug reports should be submitted to the
`devguide GitHub tracker`_.

Our devguide workflow uses continuous integration and deployment so changes to
the devguide are normally published when the pull request is merged. Changes
to CPython documentation follow the workflow of a CPython release and are
published in the release.


Developer's Guide workflow
==========================

To submit a :ref:`pull request <pullrequest>`, you can fork the
`devguide repo`_ to your GitHub account and clone it using::

    $ git clone https://github.com/<your_username>/devguide

For your PR to be accepted, you will also need to sign the
:ref:`contributor agreement <cla>`.

To build the devguide, some additional dependencies are required (most
importantly, `Sphinx`_), and the standard way to install dependencies in
Python projects is to create a virtualenv, and then install dependencies from
a ``requirements.txt`` file. For your convenience, this is all *automated for
you*.

To build the devguide from the checkout directory:

.. tab:: Unix/macOS

      make html

.. tab:: Windows

   .. code-block:: dosbatch

      .\make html

You will find the generated files in ``_build/html``.

.. tip:: * Replace ``html`` with ``htmlview`` to open the docs in a web browser
           once the build completes.
         * Replace ``html`` with ``htmllive`` to rebuild the docs,
           start a local server, and automatically reload the page in your
           browser when you make changes to reST files (Unix only).

Note that ``make check`` runs automatically when you submit
a :ref:`pull request <pullrequest>`.  You may wish to run ``make check``
and ``make linkcheck`` to make sure that it runs without errors.

.. _separate repository:
.. _devguide repo: https://github.com/python/devguide
.. _devguide GitHub tracker: https://github.com/python/devguide/issues
.. _Sphinx: https://www.sphinx-doc.org/
