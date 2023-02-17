The CPython Developer's Guide
=============================

|ReadTheDocs| |Discourse| |Codestyle|

.. |ReadTheDocs| image:: https://readthedocs.org/projects/cpython-devguide/badge/
   :target: https://devguide.python.org
   :alt: Documentation Status

.. |Discourse| image:: https://img.shields.io/badge/discourse-join_chat-brightgreen.svg
   :alt: Python Discourse chat
   :target: https://discuss.python.org/

.. |Codestyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style is black


This guide covers how to contribute to CPython. It is known by the
nickname of "the devguide" by the Python core developers.

The official home of this guide is https://devguide.python.org and if you want to have a structured roadmap to Python then do visit [Python Developer Roadmap](https://roadmap.sh/python).

Compilation
-----------

For the compilation of the devguide, you need to use a version of Python which
supports the ``venv`` module, because the ``make html`` command will create a
virtual environment and will install the ``Sphinx`` package::

    make html
