.. _exploring:

Exploring CPython's Internals
=============================

This is a quick guide for people who are interested in learning more about
CPython's internals. It provides a summary of the source code structure
and contains references to resources providing a more in-depth view.


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
---------------------

For over 20 years the CPython code base has been changing and evolving.
Here's a sample of resources about the architecture of CPython aimed at
building your understanding of both the 2.x and 3.x versions of CPython:


.. csv-table:: **Current references**
   :header: "Title", "Brief", "Author", "Version"
   :widths: 50, 50, 20, 5

    "`A guide from parser to objects, observed using GDB`_", "Code walk from Parser, AST, Sym Table and Objects", Louie Lu, 3.7.a0
    "`Green Tree Snakes`_", "The missing Python AST docs", Thomas Kluyver, 3.6
    "`Yet another guided tour of CPython`_", "A guide for how CPython REPL works", Guido van Rossum, 3.5
    "`Python Asynchronous I/O Walkthrough`_", "How CPython async I/O, generator and coroutine works", Philip Guo, 3.5
    "`Coding Patterns for Python Extensions`_", "Reliable patterns of coding Python Extensions in C", Paul Ross, 3.4

.. csv-table:: **Historical references**
   :header: "Title", "Brief", "Author", "Version"
   :widths: 50, 50, 20, 5

    "`Python's Innards Series`_", "ceval, objects, pystate and miscellaneous topics", Yaniv Aknin, 3.1
    "`Eli Bendersky's Python Internals`_", "Objects, Symbol tables and miscellaneous topics", Eli Bendersky, 3.x
    "`A guide from parser to objects, observed using Eclipse`_", "Code walk from Parser, AST, Sym Table and Objects", Prashanth Raghu, 2.7.12
    "`CPython internals: A ten-hour codewalk through the Python interpreter source code`_", "Code walk from source code to generators", Philip Guo, 2.7.8


.. _A guide from parser to objects, observed using GDB: https://hackmd.io/s/ByMHBMjFe

.. _Green Tree Snakes: https://greentreesnakes.readthedocs.io/en/latest/

.. _Yet another guided tour of CPython: https://paper.dropbox.com/doc/Yet-another-guided-tour-of-CPython-XY7KgFGn88zMNivGJ4Jzv

.. _Python Asynchronous I/O Walkthrough: http://pgbovine.net/python-async-io-walkthrough.htm

.. _Coding Patterns for Python Extensions: https://pythonextensionpatterns.readthedocs.io/en/latest/

.. _Python's Innards Series: https://tech.blog.aknin.name/category/my-projects/pythons-innards/

.. _Eli Bendersky's Python Internals: http://eli.thegreenplace.net/tag/python-internals

.. _A guide from parser to objects, observed using Eclipse: https://docs.google.com/document/d/1nzNN1jeNCC_bg1LADCvtTuGKvcyMskV1w8Ad2iLlwoI/

.. _CPython internals\: A ten-hour codewalk through the Python interpreter source code: http://pgbovine.net/cpython-internals.htm
