.. _gdb:

gdb Support
===========

If you experience low-level problems such as crashes or deadlocks
(e.g. when tinkering with parts of CPython which are written in C),
it can be convenient to use a low-level debugger such as gdb in
order to diagnose and fix the issue.  By default, however, gdb (or any
of its front-ends) doesn't know about high-level information specific to the
CPython interpreter, such as which Python function is currently executing,
or what type or value has a given Python object represented by a standard
``PyObject *`` pointer.  We hereafter present two ways to overcome this
limitation.

gdb 7 and later
---------------

In gdb 7, support for `extending gdb with Python
<http://sourceware.org/gdb/current/onlinedocs/gdb/Python.html#Python>`_ was
added. When CPython is built you will notice a ``python-gdb.py`` file in the
root directory of your checkout. Read the module docstring for details on how
to use the file to enhance gdb for easier debugging of a CPython process.

.. note: This is only available for Python 2.7, 3.2 and higher.

gdb 6 and earlier
-----------------

The file at ``Misc/gdbinit`` contains a gdb configuration file which provides
extra commands when working with a CPython process. To register these commands
permanently, either copy the commands to your personal gdb configuration file
or symlink ``~/.gdbinit`` to ``Misc/gdbinit``.  To use these commands from
a single gdb session without registering them, type ``source Misc/gdbinit``
from your gdb session.
