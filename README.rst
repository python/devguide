The CPython Developer's Guide
=============================

.. image:: https://readthedocs.org/projects/cpython-devguide/badge/
   :target: https://devguide.python.org
   :alt: Documentation Status


This guide covers how to contribute to CPython. It is known by the
nickname of "the devguide" by the Python core developers.

The official home of this guide is https://devguide.python.org.

Compilation
-----------

For the compilation of the devguide, you need to use a version of Python which
supports the ``venv`` module, because the ``make html`` command will create a
virtual environment and will install the ``Sphinx`` package::

    make html

