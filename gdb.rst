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

This is what a backtrace looks like (truncated) when this extension is
enabled::

   #0  0x000000000041a6b1 in PyObject_Malloc (nbytes=Cannot access memory at address 0x7fffff7fefe8
   ) at Objects/obmalloc.c:748
   #1  0x000000000041b7c0 in _PyObject_DebugMallocApi (id=111 'o', nbytes=24) at Objects/obmalloc.c:1445
   #2  0x000000000041b717 in _PyObject_DebugMalloc (nbytes=24) at Objects/obmalloc.c:1412
   #3  0x000000000044060a in _PyUnicode_New (length=11) at Objects/unicodeobject.c:346
   #4  0x00000000004466aa in PyUnicodeUCS2_DecodeUTF8Stateful (s=0x5c2b8d "__lltrace__", size=11, errors=0x0, consumed=
       0x0) at Objects/unicodeobject.c:2531
   #5  0x0000000000446647 in PyUnicodeUCS2_DecodeUTF8 (s=0x5c2b8d "__lltrace__", size=11, errors=0x0)
       at Objects/unicodeobject.c:2495
   #6  0x0000000000440d1b in PyUnicodeUCS2_FromStringAndSize (u=0x5c2b8d "__lltrace__", size=11)
       at Objects/unicodeobject.c:551
   #7  0x0000000000440d94 in PyUnicodeUCS2_FromString (u=0x5c2b8d "__lltrace__") at Objects/unicodeobject.c:569
   #8  0x0000000000584abd in PyDict_GetItemString (v=
       {'Yuck': <type at remote 0xad4730>, '__builtins__': <module at remote 0x7ffff7fd5ee8>, '__file__': 'Lib/test/crashers/nasty_eq_vs_dict.py', '__package__': None, 'y': <Yuck(i=0) at remote 0xaacd80>, 'dict': {0: 0, 1: 1, 2: 2, 3: 3}, '__cached__': None, '__name__': '__main__', 'z': <Yuck(i=0) at remote 0xaace60>, '__doc__': None}, key=
       0x5c2b8d "__lltrace__") at Objects/dictobject.c:2171

(notice how the dictionary argument to ``PyDict_GetItemString`` is displayed
as its ``repr()``, rather than an opaque ``PyObject *`` pointer)


.. note: This is only available for Python 2.7, 3.2 and higher.

gdb 6 and earlier
-----------------

The file at ``Misc/gdbinit`` contains a gdb configuration file which provides
extra commands when working with a CPython process. To register these commands
permanently, either copy the commands to your personal gdb configuration file
or symlink ``~/.gdbinit`` to ``Misc/gdbinit``.  To use these commands from
a single gdb session without registering them, type ``source Misc/gdbinit``
from your gdb session.
