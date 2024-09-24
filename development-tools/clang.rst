.. _clang:

===========================
Dynamic analysis with Clang
===========================

.. highlight:: bash

This document describes how to use Clang to perform analysis on Python and its
libraries.

This document does not cover interpreting the findings. For a discussion of
interpreting results, see Marshall Clow's `Testing libc++ with
-fsanitize=undefined <https://cplusplusmusings.wordpress.com/tag/clang/>`_.  The
blog posting is a detailed examinations of issues uncovered by Clang in
``libc++``.

The document focuses on Clang, although most techniques should generally apply
to GCC's sanitizers as well.

The instructions were tested on Linux, but they should work on macOS as well.
Instructions for Windows are incomplete.


What is Clang?
==============

Clang is the C, C++ and Objective C front-end for the LLVM compiler.  The
front-end provides access to LLVM's optimizer and code generator. The
sanitizers - or checkers - are hooks into the code generation phase to
instrument compiled code so suspicious behavior is flagged.

What are sanitizers?
====================

Clang sanitizers are runtime checkers used to identify suspicious and undefined
behavior. The checking occurs at runtime with actual runtime parameters so false
positives are kept to a minimum.

There are a number of sanitizers available, but two that should be used on a
regular basis are the Address Sanitizer (or ASan) and the Undefined Behavior
Sanitizer (or UBSan). ASan is invoked with the compiler option
``-fsanitize=address``, and UBSan is invoked with ``-fsanitize=undefined``.  The
flags are passed through ``CFLAGS`` and ``CXXFLAGS``, and sometimes through
``CC`` and ``CXX`` (in addition to the compiler).

A complete list of sanitizers can be found at `Controlling Code Generation
<https://clang.llvm.org/docs/UsersManual.html#controlling-code-generation>`_.

.. note::

    Because sanitizers operate at runtime on real program parameters, its
    important to provide a complete set of positive and negative self tests.

Clang and its sanitizers have strengths (and weaknesses). Its just one tool in
the war chest to uncovering bugs and improving code quality. Clang should be
used to complement other methods, including Code Reviews, `Valgrind`_,
etc.

Clang/LLVM setup
================

Pre-built Clang builds are available for most platforms:

- On macOS, Clang is the default compiler.
- For mainstream Linux distros, you can install a ``clang`` package.
  In some cases, you also need to install ``llvm`` separately, otherwise
  some tools are not available.
- On Windows, the installer for Visual Studio (not Code)
  includes the "C++ clang tools for windows" feature.

You can also build ``clang`` from source; refer to
`the clang documentation <https://clang.llvm.org/>`_ for details.

The installer does not install all the components needed on occasion. For
example, you might want to run a ``scan-build`` or examine the results with
``scan-view``. If this is your case, you can build Clang from source and
copy tools from ``tools/clang/tools`` to a directory on your ``PATH``.

Another reason to build from source is to get the latest version of Clang/LLVM,
if your platform's channels don't provide it yet.
Newer versions of Clang/LLVM introduce new sanitizer checks.


Python build setup
==================

This portion of the document covers invoking Clang and LLVM with the options
required so the sanitizers analyze Python with under its test suite.

Set the compiler to Clang, in case it's not the default::

   export CC="clang"

If you want to use additional sanitizer options (found in Clang documentation),
add them to the ``CFLAGS`` variable.
For example, you may want the checked process to exit after the first failure::

   export CFLAGS="-fno-sanitize-recover"

Then, run ``./configure`` with the relevant flags:

* ASan: ``--with-address-sanitizer --without-pymalloc``
* UBsan: ``--with-undefined-behavior-sanitizer``

It is OK to specify both sanitizers.

After that, run ``make`` and ``make test`` as usual.
Note that ``make`` itself may fail with a sanitizer failure,
since the just-compiled Python runs during later stages of the build.


Build setup for enabling sanitizers for all code
------------------------------------------------

Some parts of Python (for example, ``_testembed``, ``_freeze_importlib``,
``test_cppext``) may not use the variables set by ``configure``,
and with the above settings they'll be compiled without sanitization.

As a workaround, you can pass the sanitizer options by way of the *compilers*,
``CC`` (for C) and ``CXX`` (for C++). This is used below.
Passing the options through ``LDFLAGS`` is also reported to work.

For ASan, use::

    # ASan
    export CC="clang -fsanitize=address"
    export CXX="clang++ -fsanitize=address -fno-sanitize=vptr"

And for UBSan::

    # UBSan
    export CC="clang -fsanitize=undefined"
    export CXX="clang++ -fsanitize=undefined -fno-sanitize=vptr"

It's OK to specify both sanitizers.

After this, run ``./configure``, ``make`` and ``make test`` as usual.


Analyzing the output
====================

Sanitizer failures will make the process fail and output a diagnostic,
for example:

.. code-block:: none

    Objects/longobject.c:39:42: runtime error: index -1 out of bounds
        for type 'PyLongObject [262]'
    Objects/tupleobject.c:188:13: runtime error: member access within
        misaligned address 0x2b76be018078 for type 'PyGC_Head' (aka
        'union _gc_head'), which requires 16 byte alignment
        0x2b76be018078: note: pointer points here
        00 00 00 00  40 53 5a b6 76 2b 00 00  60 52 5a b6 ...
                     ^
    ...

If you are using the address sanitizer, an additional tool is needed to
get good traces. Usually, this happens automatically through the
``llvm-symbolizer`` tool. If this tool is not installed on your ``PATH``,
you can set ``ASAN_SYMBOLIZER_PATH`` to the location of the tool,
or pipe test output through ``asan_symbolize.py`` script from the
Clang distribution. For example, from Issue 20953 during
compile (formatting added for clarity):

.. code-block:: none

    $ make test 2>&1 | asan_symbolize.py
    ...

    /usr/local/bin/clang -fsanitize=address -Xlinker -export-dynamic
        -o python Modules/python.o libpython3.3m.a -ldl -lutil
        /usr/local/ssl/lib/libssl.a /usr/local/ssl/lib/libcrypto.a -lm
    ./python -E -S -m sysconfig --generate-posix-vars
    =================================================================
    ==24064==ERROR: AddressSanitizer: heap-buffer-overflow on address
    0x619000004020 at pc 0x4ed4b2 bp 0x7fff80fff010 sp 0x7fff80fff008
    READ of size 4 at 0x619000004020 thread T0
      #0 0x4ed4b1 in PyObject_Free Python-3.3.5/./Objects/obmalloc.c:987
      #1 0x7a2141 in code_dealloc Python-3.3.5/./Objects/codeobject.c:359
      #2 0x620c00 in PyImport_ImportFrozenModuleObject
           Python-3.3.5/./Python/import.c:1098
      #3 0x620d5c in PyImport_ImportFrozenModule
           Python-3.3.5/./Python/import.c:1114
      #4 0x63fd07 in import_init Python-3.3.5/./Python/pythonrun.c:206
      #5 0x63f636 in _Py_InitializeEx_Private
           Python-3.3.5/./Python/pythonrun.c:369
      #6 0x681d77 in Py_Main Python-3.3.5/./Modules/main.c:648
      #7 0x4e6894 in main Python-3.3.5/././Modules/python.c:62
      #8 0x2abf9a525eac in __libc_start_main
           /home/aurel32/eglibc/eglibc-2.13/csu/libc-start.c:244
      #9 0x4e664c in _start (Python-3.3.5/./python+0x4e664c)

    AddressSanitizer can not describe address in more detail (wild
    memory access suspected).
    SUMMARY: AddressSanitizer: heap-buffer-overflow
      Python-3.3.5/./Objects/obmalloc.c:987 PyObject_Free
    Shadow bytes around the buggy address:
      0x0c327fff87b0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
      0x0c327fff87c0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
      0x0c327fff87d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
      0x0c327fff87e0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
      0x0c327fff87f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
    =>0x0c327fff8800: fa fa fa fa[fa]fa fa fa fa fa fa fa fa fa fa fa
      0x0c327fff8810: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
      0x0c327fff8820: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
      0x0c327fff8830: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
      0x0c327fff8840: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
      0x0c327fff8850: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
    Shadow byte legend (one shadow byte represents 8 application bytes):
      Addressable:           00
      Partially addressable: 01 02 03 04 05 06 07
      Heap left redzone:     fa
      Heap right redzone:    fb
      Freed heap region:     fd
      Stack left redzone:    f1
      Stack mid redzone:     f2
      Stack right redzone:   f3
      Stack partial redzone: f4
      Stack after return:    f5
      Stack use after scope: f8
      Global redzone:        f9
      Global init order:     f6
      Poisoned by user:      f7
      ASan internal:         fe
    ==24064==ABORTING
    make: *** [pybuilddir.txt] Error 1

.. note::

    If ``asan_symbolize.py`` is not installed, build Clang from source, then
    look in the Clang/LLVM build directory for it and use it directly or copy
    it to a directory on ``PATH``.

Ignoring findings
-----------------

.. highlight:: none

Clang allows you to alter the behavior of sanitizer tools for certain
source-level by providing a special ignorelist file at compile-time. The
ignorelist is needed because it reports every instance of an issue, even if the
issue is reported 10's of thousands of time in un-managed library code.

You specify the ignorelist with ``-fsanitize-ignorelist=XXX``. For example::

    -fsanitize-ignorelist=my_ignorelist.txt

``my_ignorelist.txt`` would then contain entries such as the following. The entry
will ignore a bug in ``libc++``'s ``ios`` formatting functions::

    fun:_Ios_Fmtflags

As an example with Python 3.4.0, ``audioop.c`` will produce a number of
findings::

    ./Modules/audioop.c:422:11: runtime error: left shift of negative value -1
    ./Modules/audioop.c:446:19: runtime error: left shift of negative value -1
    ./Modules/audioop.c:476:19: runtime error: left shift of negative value -1
    ./Modules/audioop.c:504:16: runtime error: left shift of negative value -1
    ./Modules/audioop.c:533:22: runtime error: left shift of negative value -128
    ./Modules/audioop.c:775:19: runtime error: left shift of negative value -70
    ./Modules/audioop.c:831:19: runtime error: left shift of negative value -70
    ./Modules/audioop.c:881:19: runtime error: left shift of negative value -1
    ./Modules/audioop.c:920:22: runtime error: left shift of negative value -70
    ./Modules/audioop.c:967:23: runtime error: left shift of negative value -70
    ./Modules/audioop.c:968:23: runtime error: left shift of negative value -70
    ...

One of the function of interest is ``audioop_getsample_impl`` (flagged at line
422), and the ignorelist entry would include::

    fun:audioop_getsample_imp

Or, you could ignore the entire file with::

    src:Modules/audioop.c

Unfortunately, you won't know what to ignorelist until you run the sanitizer.

The documentation is available at `Sanitizer special case list
<https://clang.llvm.org/docs/SanitizerSpecialCaseList.html>`_.

.. _Valgrind: https://github.com/python/cpython/blob/main/Misc/README.valgrind
