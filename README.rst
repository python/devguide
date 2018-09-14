The CPython Developer's Guide
=============================

|ReadTheDocs| |Zulip| |Codestyle|

.. |ReadTheDocs| image:: https://readthedocs.org/projects/cpython-devguide/badge/
   :target: https://devguide.python.org
   :alt: Documentation Status

.. |Zulip| image:: https://img.shields.io/badge/zulip-join_chat-brightgreen.svg
   :alt: Python Zulip chat
   :target: https://python.zulipchat.com

.. |Codestyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Code style is black


This guide covers how to contribute to CPython. It is known by the
nickname of "the devguide" by the Python core developers.

The official home of this guide is https://devguide.python.org.

Compilation
-----------

For the compilation of the devguide, you need to use a version of Python which
supports the ``venv`` module, because the ``make html`` command will create a
virtual environment and will install the ``Sphinx`` package::

    make html

