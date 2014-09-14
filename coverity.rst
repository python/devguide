=============
Coverity Scan
=============

.. _coverity:

Coverity Scan is a free service for static code analysis of Open Source
projects. It is based on Coverity's commercial product and is able to analyze
C, C++ and Java code.

Coverity's static code analysis doesn't run the code. Instead of that it uses
abstract interpretation to gain information about the code's control flow and
data flow. It's able to follow all possible code paths that a program may
take. For example the analyzer understands that ``malloc()`` returns a memory
that must be freed with ``free()`` later. It follows all branches and function
calls to see if all possible combinations free the memory. The analyzer is
able to detect all sorts of issues like resource leaks (memory, file
descriptors), NULL dereferencing, use after free, unchecked return values,
dead code, buffer overflows, integer overflows, uninitialized variables, and
many more.


Access to analysis reports
==========================

The results are available on the `Coverity Scan`_ website. In order to
access the results you have to create an account yourself. Then go to
*Projects using Scan* and add yourself to the Python project. New members must
be approved by an admin (see `Contact`_).

Access is restricted to Python core developers only. Other individuals may be
given access at our own discretion, too. Every now and then Coverity detects a
critical issue in Python's code -- new analyzers may even find new bugs in
mature code. We don't want to disclose issues prematurely.


Building and uploading analysis
===============================

The process is automated. A script runs ``hg pull``, ``hg update``,
``cov-build`` and uploads the latest analysis to Coverity. Since Coverity has
limited the maximum number of builds per week Python is analyzed every second
day. The build runs on a dedicated virtual machine on PSF's infrastructure at
OSU Open Source Labs. The process is maintained by Christian Heimes (see
`Contact`_). At present only the tip is analyzed with the 64bit Linux tools.


Known limitations
=================

Some aspects of Python's C code are not yet understood by Coverity.

False positives
---------------

``Py_BuildValue("N", PyObject*)``
  Coverity doesn't understand that ``N`` format char passes the object along
  without touching its reference count. On this ground the analyzer detects
  a resource leak. CID 719685

``PyLong_FromLong()`` for negative values
  Coverity claims that ``PyLong_FromLong()`` and other ``PyLong_From*()``
  functions cannot handle a negative value because the value might be used as
  an array index in ``get_small_int()``. CID 486783

``PyLong_FromLong()`` for n in [-5 ... +255]
  For integers in the range of Python's small int cache the ``PyLong_From*()``
  function can never fail and never returns NULL. CID 1058291

``PyArg_ParseTupleAndKeywords(args, kwargs, "s#", &data, &length)``
  Some functions use the format char combination such as ``s#``, ``u#`` or
  ``z#`` to get data and length of a character array. Coverity doesn't
  recognize the relation between data and length. Sometimes it detects a buffer
  overflow if data is written to a fixed size buffer although
  ``length <= sizeof(buffer)``.  CID 486613

``path_converter()`` dereferencing after null check
  The ``path_converter()`` function in ``posixmodule.c`` makes sure that
  either ``path_t.narrow`` or ``path_t.wide`` is filled unless
  ``path_t.nullable`` is explicitly enabled. CID 719648


Intentionally
-------------

``Py_VA_COPY()``
  Python is written in C89 (ANSI C), therefore it can't use C99 features such
  as ``va_copy()``. Python's own variant ``Py_VA_COPY()`` uses ``memcpy()``
  to make a copy of a ``va_list`` variable. Coverity detects two issues in
  this approach: "Passing argument "lva" of type "va_list" and sizeof(va_list)
  to function memcpy() is suspicious." CID 486405 and "Uninitialized pointer
  read" CID 486630.


Modeling
========

Modeling is explained in the *Coverity Help Center* which is available in
the help menu of `Coverity Connect`_. `coverity_model.c`_ contains a copy of
Python's modeling file for Coverity. Please keep the copy in sync with the
model file in *Analysis Settings* of `Coverity Scan`_.


Workflow
========

False positive and intentional issues
-------------------------------------

If the problem is listed under `Known limitations`_ then please set the
classification to either "False positive" or "Intentional", the action to
"Ignore", owner to your own account and add a comment why the issue
is considered false positive or intentional.

If you think it's a new false positive or intentional then please contact an
admin. The first step should be an updated to Python's `Modeling`_ file.


Positive issues
---------------

You should always create an issue unless it's really a trivial case. Please
add the full url to the ticket under *Ext. Reference* and add the CID
(Coverity ID) to both the ticket and the checkin message. It makes it much
easier to understand the relation between tickets, fixes and Coverity issues.


Contact
=======

Please include both Brett and Christian in any mail regarding Coverity. Mails
to Coverity should go through Brett or Christian, too.

Christian Heimes <christian (at) python (dot) org>
  admin, maintainer of build machine, intermediary between Python and Coverity

Brett Cannon <brett (at) python (dot) org>
  co-admin

Dakshesh Vyas <scan-admin@coverity.com>
  Technical Manager - Coverity Scan


.. seealso::

   `Coverity Scan FAQ <http://scan.coverity.com/faq/>`_


.. _Coverity Scan: http://scan.coverity.com/

.. _Coverity Connect: http://scan5.coverity.com:8080/

.. _coverity_model.c: https://hg.python.org/cpython/file/tip/Misc/coverity_model.c
