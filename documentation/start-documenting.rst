.. _start-documenting:
.. _documenting:

===============
Getting started
===============

.. raw:: html

   <script>
    document.addEventListener('DOMContentLoaded', function() {
      activateTab(getOS());
    });
    </script>

.. highlight::  rest

The Python language has a substantial body of documentation, much of it
contributed by various authors. The markup used for the Python documentation is
`reStructuredText`_, developed by the `docutils`_ project, amended by custom
directives and using a toolset named `Sphinx`_ to post-process the HTML output.

The documentation in HTML, PDF or EPUB format is generated from text files
written using the :ref:`reStructuredText format <markup>` and contained in the
:ref:`CPython Git repository <setup>`.

.. _reStructuredText: https://docutils.sourceforge.io/rst.html

.. note::

   If you're interested in contributing to Python's documentation, there's no
   need to write reStructuredText if you're not so inclined; plain text
   contributions are more than welcome as well.  Send an e-mail to
   docs@python.org or open an issue on the :ref:`tracker <reporting-bugs>`.


Introduction
============

Python's documentation has long been considered to be good for a free
programming language.  There are a number of reasons for this, the most
important being the early commitment of Python's creator, Guido van Rossum, to
providing documentation on the language and its libraries, and the continuing
involvement of the user community in providing assistance for creating and
maintaining documentation.

The involvement of the community takes many forms, from authoring to bug reports
to just plain complaining when the documentation could be more complete or
easier to use.

This section is aimed at authors and potential authors of documentation for
Python.  More specifically, it is for people contributing to the standard
documentation and developing additional documents using the same tools as the
standard documents.  This guide will be less useful for authors using the Python
documentation tools for topics other than Python, and less useful still for
authors not using the tools at all.

If your interest is in contributing to the Python documentation, but you don't
have the time or inclination to learn reStructuredText and the markup structures
documented here, there's a welcoming place for you among the Python contributors
as well.  Any time you feel that you can clarify existing documentation or
provide documentation that's missing, the existing documentation team will
gladly work with you to integrate your text, dealing with the markup for you.
Please don't let the material in this section stand between the documentation
and your desire to help out!


.. _building-doc:

Building the documentation
==========================

.. highlight:: bash

To build the documentation, follow the steps in one of the sections below.
You can view the documentation after building the HTML
by opening the file :file:`Doc/build/html/index.html` in a web browser.

Initial requirements
--------------------

Ensure your current working directory is the top level ``Doc/`` directory
inside your :ref:`CPython repository clone <checkout>`. You can switch to
it with:

.. code-block:: shell

   cd Doc

Ensure your Python version is at least 3.11. You can verify it with:

.. code-block:: shell

   python --version

.. _doc-create-venv:

Create a virtual environment
----------------------------

.. _doc-create-venv-unix:
.. _doc-create-venv-windows:

You can create a new :mod:`venv` with the required dependencies using:

.. tab:: Unix/macOS

   .. code-block:: shell

      make venv

   Building the docs with :program:`make` will automatically use this environment
   without you having to activate it.

.. tab:: Windows

   `Create a new virtual environment <venv-create_>`__ manually.
   Always be sure to `activate this environment <venv-activate_>`__
   before building the documentation.


.. _building-using-make:
.. _using-make-make-bat:
.. _doc-build-make:

Build using make / make.bat
---------------------------

.. tab:: Unix/macOS

   A Unix ``Makefile`` is provided, :cpy-file:`Doc/Makefile`.

.. tab:: Windows

   A Windows ``make.bat`` is provided, :cpy-file:`Doc/make.bat`, which
   attempts to emulate the Unix ``Makefile`` as closely as practical.

   .. important::

      The Windows ``make.bat`` batch file lacks a ``make venv`` target.
      Instead, it automatically installs any missing dependencies
      into the currently activated environment (or the base Python, if none).
      Make sure the environment you :ref:`created above <doc-create-venv-windows>`
      is `activated <venv-activate_>`__ before running ``make.bat``.

To build the docs as HTML, run:

.. tab:: Unix/macOS

   .. code-block:: shell

      make html

.. tab:: Windows

   .. code-block:: dosbatch

      .\make html

.. tip:: * Replace ``html`` with ``htmlview`` to open the docs in a web browser
           once the build completes.
         * Replace ``html`` with ``htmllive`` to rebuild the docs,
           start a local server, and automatically reload the page in your
           browser when you make changes to reST files (Unix only).

It is also possible to build only certain pages of the documentation in order
to save time during the build process. Following is an example for building two
pages:

.. tab:: Unix/macOS

   .. code-block:: shell

      make html SOURCES="tutorial/classes.rst tutorial/inputoutput.rst"

.. tab:: Windows

   See :ref:`using-sphinx-build`. When invoking ``sphinx-build``, pass the
   desired pages as the final parameter, like so:

   .. code-block:: dosbatch

      python -m sphinx -b html . build/html tutorial/classes.rst tutorial/inputoutput.rst

To check the docs for common errors with `Sphinx Lint`_
(which is run on all :ref:`pull requests <pullrequest>`), use:

.. tab:: Unix/macOS

   .. code-block:: shell

      make check

.. tab:: Windows

   .. code-block:: dosbatch

      .\make check

To list other supported :program:`make` targets, run:

.. tab:: Unix/macOS

   .. code-block:: shell

      make help

.. tab:: Windows

   .. code-block:: dosbatch

      .\make help

See :cpy-file:`Doc/README.rst` for more information.


.. _using-sphinx-build:
.. _doc-build-sphinx:

Build using Sphinx directly
---------------------------

Advanced users may want to invoke Sphinx directly,
to pass specialized options or to handle specific use cases.

Make sure the environment you :ref:`created above <doc-create-venv-windows>`
is `activated <venv-activate_>`__.
Then, install the documentation requirements, :cpy-file:`Doc/requirements.txt`.
Using pip::

   python -m pip install --upgrade -r requirements.txt

Finally, directly invoke Sphinx with::

   python -m sphinx -b html . build/html

To use a different `Sphinx builder`_,
replace ``html`` above with the desired builder ``name``.


.. _docutils: https://docutils.sourceforge.io/
.. _Sphinx: https://www.sphinx-doc.org/
.. _Sphinx builder: https://www.sphinx-doc.org/en/master/usage/builders/index.html
.. _Sphinx Lint: https://github.com/sphinx-contrib/sphinx-lint
.. _venv-activate: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment
.. _venv-create: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
