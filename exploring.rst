.. _exploring:

Exploring CPython's Internals
=================================

This is a quick guide for who want to know about CPython's internals,
and provide a summary about the source code structure and references.


CPython Source Code Typical Layout
---------------------------------------

For Python modules, the typical layout is:

* ``Lib/<module>.py``
* ``Modules/_<module>module.c`` (if there's also a C accelerator module)
* ``Lib/test/test_<module>.py``
* ``Doc/library/<module>.rst``

For extension-only modules, the typical layout is:

* ``Modules/<module>module.c``
* ``Lib/test/test_<module>.py``
* ``Doc/library/<module>.rst``

For builtin types, the typical layout is:

* ``Objects/<builtin>object.c``
* ``Lib/test/test_<builtin>.py``
* ``Doc/library/stdtypes.rst``

For builtin functions, the typical layout is:

* ``Python/bltinmodule.c``
* ``Lib/test/test_<builtin>.py``
* ``Doc/library/functions.rst``

Some Exception:

* builtin type ``int`` is at ``Objects/longobject.c``
* builtin type ``str`` is at ``Objects/unicodeobject.c``

CPython Internals Tutorials
---------------------------

There are several materials about CPython internals on the Internet:

* Python 2

    * `Yet another guided tour of CPython`_ by Guido van Rossum
    * `Python's Innards Series`_ by Yaniv Aknin
    * `Internals of CPython 2.7`_ by Prashanth Raghu
    * `CPython internals: A ten-hour codewalk through the Python interpreter source code`_
      by Philip Guo

* Python 3

    * `Internals of CPython 3.7`_ by Louie Lu

.. _Yet another guided tour of CPython: https://paper.dropbox.com/doc/Yet-another-guided-tour-of-CPython-XY7KgFGn88zMNivGJ4Jzv

.. _Python's Innards Series: https://tech.blog.aknin.name/category/my-projects/pythons-innards/

.. _Internals of CPython 2.7: https://docs.google.com/document/d/1nzNN1jeNCC_bg1LADCvtTuGKvcyMskV1w8Ad2iLlwoI/

.. _CPython internals\: A ten-hour codewalk through the Python interpreter source code: http://pgbovine.net/cpython-internals.htm

.. _Internals of CPython 3.7: https://hackmd.io/s/ByMHBMjFe
