.. _sanitizers:
.. _clang:

==========
Sanitizers
==========

.. highlight:: bash

.. include:: /include/activate-tab.rst

Sanitizers are runtime checkers built into compilers such as GCC and Clang.
They instrument compiled code to report memory errors, undefined
behavior and data races as they happen. They only find bugs in code that actually
runs, so run as much of CPython as possible, for example the full test suite
or a fuzzer.

.. note::

   This page describes the ``main`` branch. Sanitizer support changes
   quickly, so the details here may not apply to older branches.


Available sanitizers
====================

``configure`` has an option for each supported sanitizer. It adds the
necessary compiler and linker flags.

.. list-table::
   :header-rows: 1

   * - Sanitizer
     - Detects
     - ``configure`` option
     - Compilers
   * - `AddressSanitizer (ASan)
       <https://clang.llvm.org/docs/AddressSanitizer.html>`__
     - Out-of-bounds accesses, use-after-free, leaks
     - :option:`python:--with-address-sanitizer`
     - GCC, Clang
   * - `HWAddressSanitizer (HWASan)
       <https://clang.llvm.org/docs/HardwareAssistedAddressSanitizerDesign.html>`__
     - Like ASan, with hardware pointer tagging
     - :option:`python:--with-hwaddress-sanitizer`
     - GCC, Clang (AArch64; experimental on x86-64)
   * - `MemorySanitizer (MSan)
       <https://clang.llvm.org/docs/MemorySanitizer.html>`__
     - Reads of uninitialized memory
     - :option:`python:--with-memory-sanitizer`
     - Clang
   * - `UndefinedBehaviorSanitizer (UBSan)
       <https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html>`__
     - Signed overflow, misaligned access, invalid shifts, null dereference
     - :option:`python:--with-undefined-behavior-sanitizer`
     - GCC, Clang
   * - `ThreadSanitizer (TSan)
       <https://clang.llvm.org/docs/ThreadSanitizer.html>`__
     - Data races
     - :option:`python:--with-thread-sanitizer`
     - GCC, Clang

UBSan can be combined with any of the others. ASan, HWASan, MSan and TSan
are mutually exclusive.

Compilers provide additional sanitizers that CPython has no ``configure``
option for. They may or may not work with CPython, and can be enabled
manually through ``CFLAGS`` and ``LDFLAGS``. See `Controlling Code Generation
<https://clang.llvm.org/docs/UsersManual.html#controlling-code-generation>`__
for Clang's full list and `Instrumentation Options
<https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html>`__ for
GCC's, which currently keeps its options compatible with Clang's.


Building and testing
====================

Pick a compiler if needed, then configure with the option you want:

.. tab:: Unix

   .. code-block:: shell

      export CC=clang CXX=clang++
      ./configure --with-pydebug --with-address-sanitizer
      make -j $(nproc)
      make test

.. tab:: macOS

   .. code-block:: shell

      export CC=clang CXX=clang++
      ./configure --with-pydebug --with-address-sanitizer
      make -j$(sysctl -n hw.logicalcpu)
      make test

``make`` itself may fail with a sanitizer report, since the just-built
interpreter runs during later stages of the build.

The sanitizer jobs in CPython's CI, configured in
:cpy-file:`.github/workflows/reusable-san.yml`, are a good reference for a
working set of options for each sanitizer. Notes:

* **MSan**: reports false positives for memory initialized by libraries not
  built with MSan. Build dependencies with MSan or disable the extension
  modules that use them in :file:`Modules/Setup.local`, as CI does.
  Additionally, avoid ``--with-pydebug``, since the debug
  allocator hooks hide uninitialized reads. You can use ``--with-assertions``
  instead.
* **TSan**: most useful on the :ref:`free-threaded build
  <python:freethreading-python-howto>`. A full test run is slow, so use the
  curated lists in :cpy-file:`Lib/test/libregrtest/tsan.py`::

     ./python -m test --tsan
     ./python -m test --tsan-parallel --parallel-threads=4

* **HWASan**: on x86-64 the aliasing mode is unsafe for programs that
  ``fork()``, including much of the test suite.

Each sanitizer reads runtime options from ``ASAN_OPTIONS``,
``HWASAN_OPTIONS``, ``MSAN_OPTIONS``, ``UBSAN_OPTIONS`` or ``TSAN_OPTIONS``.
CI uses ``detect_leaks=0`` (the test suite is not leak-clean),
``allocator_may_return_null=1`` (for out-of-memory tests), ``handle_segv=0``
(leave crashes to :mod:`python:faulthandler`), ``halt_on_error=1`` for UBSan
and ``log_path=`` to collect reports from subprocesses.

``./python -m test`` prints the active sanitizers and these variables in its
header, which helps reproduce CI failures locally.


Suppressing findings
====================

CPython keeps the runtime suppression files used by CI in the repository:

* :cpy-file:`Tools/ubsan/suppressions.txt`
* :cpy-file:`Tools/tsan/suppressions.txt`
* :cpy-file:`Tools/tsan/suppressions_free_threading.txt`

Load one with the ``suppressions=`` option::

   export UBSAN_OPTIONS="suppressions=$PWD/Tools/ubsan/suppressions.txt"

When adding a suppression, include a comment referencing a GitHub issue
that describes how to reproduce the problem and includes the sanitizer
output, so the suppression can be removed once the issue is fixed.
The file formats are described in the `UBSan
<https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html#runtime-suppressions>`__
and `TSan
<https://github.com/google/sanitizers/wiki/ThreadSanitizerSuppressions>`__
documentation.


Analyzing the output
====================

A report names the failed check and the source location, and ASan, MSan and
TSan add a stack trace:

.. code-block:: none

   ==24064==ERROR: AddressSanitizer: heap-buffer-overflow on address
   0x619000004020 at pc 0x4ed4b2 bp 0x7fff80fff010 sp 0x7fff80fff008
   READ of size 4 at 0x619000004020 thread T0
     #0 0x4ed4b1 in PyObject_Free Objects/obmalloc.c:987
     #1 0x7a2141 in code_dealloc Objects/codeobject.c:359
     ...

Traces are symbolized automatically via ``llvm-symbolizer`` (Clang) or
``addr2line`` (GCC). If the tool is not on your ``PATH``, set
``ASAN_SYMBOLIZER_PATH`` (or the equivalent for other sanitizers) to its
location. In the CPython CI, reports are printed at the end of the job log and
attached as ``san_log.*`` artifacts.
