.. _documenting:

=================
 Getting Started
=================

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

The toolset used to build the docs is written in Python and is called Sphinx_.
Sphinx is maintained separately and is not included in this tree.  Also needed
are blurb_, a tool to create :file:`Misc/NEWS` on demand; and
python-docs-theme_, the Sphinx theme for the Python documentation.

To build the documentation, follow the instructions from one of the sections
below.  You can view the documentation after building the HTML by pointing
a browser at the file :file:`Doc/build/html/index.html`.

You are expected to have installed the latest stable version of
Sphinx_ and blurb_ on your system or in a virtualenv_ (which can be
created using ``make venv``), so that the Makefile can find the
``sphinx-build`` command.  You can also specify the location of
``sphinx-build`` with the ``SPHINXBUILD`` :command:`make` variable.


.. _building-using-make:

Using make / make.bat
---------------------

**On Unix**, run the following from the root of your :ref:`repository clone
<checkout>` to build the output as HTML::

   cd Doc
   make venv
   make html

or alternatively ``make -C Doc/ venv html``.  ``htmlview`` can be used
instead of ``html`` to conveniently open the docs in a browser once the
build completes.

You can also use ``make help`` to see a list of targets supported by
:command:`make`.  Note that ``make check`` is automatically run when
you submit a :ref:`pull request <pullrequest>`, so you should make
sure that it runs without errors.

**On Windows**, a :file:`make.bat` batchfile tries to emulate :command:`make`
as closely as possible, but the venv target is not implemented, so you will
probably want to make sure you are working in a virtual environment before
proceeding, otherwise all dependencies will be automatically installed on your
system.

When ready, run the following from the root of your :ref:`repository clone
<checkout>` to build the output as HTML::

   cd Doc
   make html

You can also use ``make help`` to see a list of targets supported by
:file:`make.bat`.

See also :file:`Doc/README.rst` for more information.

Using sphinx-build
------------------

Sometimes we directly want to execute the sphinx-build tool instead of through
``make`` (although the latter is still the preferred way). In this case, you can
use the following command line from the ``Doc`` directory (make sure to install
Sphinx_, blurb_ and python-docs-theme_ packages from PyPI)::

   sphinx-build -b<builder> . build/<builder>

where ``<builder>`` is one of html, text, latex, or htmlhelp (for explanations
see the make targets above).


.. _docutils: https://docutils.sourceforge.io/
.. _python-docs-theme: https://pypi.org/project/python-docs-theme/
.. _Sphinx: https://www.sphinx-doc.org/
.. _virtualenv: https://virtualenv.pypa.io/
.. _blurb: https://pypi.org/project/blurb/


Style Guide
===========

Moved to :doc:`style-guide`


Translating
===========

Moved to :doc:`translating`
