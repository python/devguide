.. _internals:

===================
CPython's internals
===================

The CPython code base is constantly changing and evolving.
Here's a sample of references about CPython's architecture aimed at
building your understanding of CPython internals and its evolution:

.. csv-table:: **Current references**
   :header: "Title", "Brief", "Author", "Version"
   :widths: 50, 50, 20, 5

    "`CPython's InternalDocs`_", "Docs on CPython internals maintained in the source tree", "", ""
    "`A guide from parser to objects, observed using GDB`_", "Code walk from Parser, AST, Sym Table and Objects", Louie Lu, 3.7.a0
    "`Green Tree Snakes`_", "The missing Python AST docs", Thomas Kluyver, 3.6
    "`Yet another guided tour of CPython`_", "A guide for how CPython REPL works", Guido van Rossum, 3.5
    "`Python Asynchronous I/O Walkthrough`_", "How CPython async I/O, generator and coroutine works", Philip Guo, 3.5
    "`Coding Patterns for Python Extensions`_", "Reliable patterns of coding Python Extensions in C", Paul Ross, 3.9+
    "`Your Guide to the CPython Source Code`_", "Your Guide to the CPython Source Code", Anthony Shaw, 3.8

.. csv-table:: **Historical references**
   :header: "Title", "Brief", "Author", "Version"
   :widths: 50, 50, 20, 5

    "`Python's Innards Series`_", "ceval, objects, pystate and miscellaneous topics", Yaniv Aknin, 3.1
    "`Eli Bendersky's Python Internals`_", "Objects, Symbol tables and miscellaneous topics", Eli Bendersky, 3.x
    "`A guide from parser to objects, observed using Eclipse`_", "Code walk from Parser, AST, Sym Table and Objects", Prashanth Raghu, 2.7.12
    "`CPython internals: A ten-hour codewalk through the Python interpreter source code`_", "Code walk from source code to generators", Philip Guo, 2.7.8

.. _CPython's InternalDocs: https://github.com/python/cpython/blob/main/InternalDocs/README.md

.. _A guide from parser to objects, observed using GDB: https://hackmd.io/s/ByMHBMjFe

.. _Green Tree Snakes: https://greentreesnakes.readthedocs.io/en/latest/

.. _Yet another guided tour of CPython: https://paper.dropbox.com/doc/Yet-another-guided-tour-of-CPython-XY7KgFGn88zMNivGJ4Jzv

.. _Python Asynchronous I/O Walkthrough: https://www.youtube.com/playlist?list=PLpEcQSRWP2IjVRlTUptdD05kG-UkJynQT

.. _Coding Patterns for Python Extensions: https://pythonextensionpatterns.readthedocs.io/en/latest/

.. _Your Guide to the CPython Source Code: https://realpython.com/cpython-source-code-guide/

.. _Python's Innards Series: https://tech.blog.aknin.name/category/my-projects/pythons-innards/

.. _Eli Bendersky's Python Internals: https://eli.thegreenplace.net/tag/python-internals

.. _A guide from parser to objects, observed using Eclipse: https://docs.google.com/document/d/1nzNN1jeNCC_bg1LADCvtTuGKvcyMskV1w8Ad2iLlwoI/

.. _CPython internals\: A ten-hour codewalk through the Python interpreter source code: https://www.youtube.com/playlist?list=PLzV58Zm8FuBL6OAv1Yu6AwXZrnsFbbR0S
