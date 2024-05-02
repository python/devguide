.. _gdb:

===========
GDB support
===========

.. highlight:: none

Page moved
==========

Information on debugging CPython using GDB is now in the main Python
documentation, since it is relevant for C extension modules as well.
Please read it first: :ref:`python:gdb`


CPython tips
============

This document includes a few additional tips that are useful specifically for
debugging CPython internals.


Breaking at labels
------------------

You will most often set breakpoints at the start of functions, but
this approach is less helpful when debugging the runtime virtual
machine, since the main interpreter loop function,
``_PyEval_EvalFrameDefault``, is well over 4,000 lines long as of Python 3.12.
Fortunately, among the `many ways to set breakpoints
<https://sourceware.org/gdb/current/onlinedocs/gdb.html/Location-Specifications.html>`_,
you can break at C labels, such as those generated for computed gotos.
If you are debugging an interpreter compiled with computed goto support
(generally true, certainly when using GCC), each instruction will be
prefaced with a label named ``TARGET_<instruction>``, e.g.,
``TARGET_LOAD_CONST``.  You can then set a breakpoint with a command
like::

   (gdb) break ceval.c:_PyEval_EvalFrameDefault:TARGET_LOAD_CONST

Add commands, save to a file, then reload in future sessions without
worrying that the starting line number of individual instructions
change over time.

Saving and loading breakpoints
------------------------------

With extended exposure to particular parts of the Python runtime, you
might find it helpful to define a routine set of breakpoints and
commands to execute when they are hit.
For convenience, save your breakpoints to a file and load them in future
sessions using the ``save breakpoints`` command::

   (gdb) save breakpoints python.brk

You can edit the file to your heart's content, then load it in a later
session::

   (gdb) source python.brk
