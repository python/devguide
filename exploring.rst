.. _exploring:

Exploring CPython's Internals
=============================

This is a quick guide for who want to know about CPython's internals,
and provide a summary about the source code structure and references.


CPython Source Code Layout
--------------------------

This guide gives an overview of CPython's code structure.
It serves as a summary of file locations for modules and builtins.

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

Some Exceptions:

* builtin type ``int`` is at ``Objects/longobject.c``
* builtin type ``str`` is at ``Objects/unicodeobject.c``

Additional References
---------------------------

For over 20 years the CPython code base has been changing and evolving.
Here's a sample of resources about the architecture of CPython aimed at
building your understanding of both the 2.x and 3.x versions of CPython:


===================================================================================== ================== =========
               Title                                                                        Author        Version
===================================================================================== ================== =========
`Internals of CPython 3.7`_ (using gdb)                                               Louie Lu            3.7.a0

`Yet another guided tour of CPython`_                                                 Guido van Rossum    3.5

`Python's Innards Series`_                                                            Yaniv Aknin         3.1

`Internals of CPython 2.7`_ (using Eclipse)                                           Prashanth Raghu     2.7.12

`CPython internals: A ten-hour codewalk through the Python interpreter source code`_  Philip Guo          2.7.8

===================================================================================== ================== =========


.. _Yet another guided tour of CPython: https://paper.dropbox.com/doc/Yet-another-guided-tour-of-CPython-XY7KgFGn88zMNivGJ4Jzv

.. _Python's Innards Series: https://tech.blog.aknin.name/category/my-projects/pythons-innards/

.. _Internals of CPython 2.7: https://docs.google.com/document/d/1nzNN1jeNCC_bg1LADCvtTuGKvcyMskV1w8Ad2iLlwoI/

.. _CPython internals\: A ten-hour codewalk through the Python interpreter source code: http://pgbovine.net/cpython-internals.htm

.. _Internals of CPython 3.7: https://hackmd.io/s/ByMHBMjFe
