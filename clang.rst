**********************************
  Dynamic Analysis with Clang
**********************************

This document describes how to use Clang to perform analysis on Python and its
libraries. In addition to performing the analysis, the document will cover
downloading, building and installing the the latest Clang/LLVM combination
(which is currently 3.4).

This document does not cover interpreting the findings. For a discussion of
interpreting results, see Marshall Clow's `Testing libc++ with
-fsanitize=undefined <http://cplusplusmusings.wordpress.com/tag/clang/>`_.  The
blog posting is a detailed examinations of issues uncovered by Clang in
``libc++``.

What is Clang?
==============

Clang is the C, C++ and Objective C front-end for the LLVM compiler.  The
front-end provides access to LLVM's optimizer and code generator. The
sanitizers - or checkers - are hooks into the code generation phase to
instrument compiled code so suspicious behavior is flagged.

What are Sanitizers?
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
<http://clang.llvm.org/docs/UsersManual.html#controlling-code-generation>`_.

.. note::

    Because sanitizers operate at runtime on real program parameters, its
    important to provide a complete set of positive and negative self tests.

Clang and its sanitizers have strengths (and weaknesses). Its just one tool in
the war chest to uncovering bugs and improving code quality. Clang should be
used to compliment other methods, including Code Reviews, Valgrind, Coverity,
etc.

Clang/LLVM Setup
================

This portion of the document covers downloading, building and installing Clang
and LLVM. There are three components to download and build. They are the LLVM
compiler, the compiler front end and the compiler runtime library.

In preparation you should create a scratch directory. Also ensure you are using
Python 2 and not Python 3. Python 3 will cause the build to fail.

Download, Build and Install
---------------------------

Perform the following to download, build and install the Clang/LLVM 3.4. ::

    # Download
    wget http://llvm.org/releases/3.4/llvm-3.4.src.tar.gz
    wget http://llvm.org/releases/3.4/clang-3.4.src.tar.gz
    wget http://llvm.org/releases/3.4/compiler-rt-3.4.src.tar.gz
  
    # LLVM
    tar xvf llvm-3.4.src.tar.gz
    cd llvm-3.4/tools

    # Clang Front End
    tar xvf ../../clang-3.4.src.tar.gz
    mv clang-3.4 clang

    # Compiler RT
    cd ../projects
    tar xvf ../../compiler-rt-3.4.src.tar.gz
    mv compiler-rt-3.4/ compiler-rt

    # Build
    cd ..
    ./configure --enable-optimized --prefix=/usr/local
    make -j4
    sudo make install

.. note::

    If you receive an error ``'LibraryDependencies.inc' file not found``, then
    ensure you are utilizing Python 2 and not Python 3. If you encounter the
    error after switching to Python 2, then delete everything and start over.

After ``make install`` executes, the compilers will be installed in
``/usr/local/bin`` and the various libraries will be installed in
``/usr/local/lib/clang/3.4/lib/linux/``: ::

    $ ls /usr/local/lib/clang/3.4/lib/linux/
    libclang_rt.asan-x86_64.a   libclang_rt.profile-x86_64.a
    libclang_rt.dfsan-x86_64.a  libclang_rt.san-x86_64.a
    libclang_rt.full-x86_64.a   libclang_rt.tsan-x86_64.a
    libclang_rt.lsan-x86_64.a   libclang_rt.ubsan_cxx-x86_64.a
    libclang_rt.msan-x86_64.a   libclang_rt.ubsan-x86_64.a

On Mac OS X, the libraries are installed in
``/usr/local/lib/clang/3.3/lib/darwin/``: ::

    $ ls /usr/local/lib/clang/3.3/lib/darwin/
    libclang_rt.10.4.a                    libclang_rt.ios.a
    libclang_rt.asan_osx.a                libclang_rt.osx.a
    libclang_rt.asan_osx_dynamic.dylib    libclang_rt.profile_ios.a
    libclang_rt.cc_kext.a                 libclang_rt.profile_osx.a
    libclang_rt.cc_kext_ios5.a            libclang_rt.ubsan_osx.a
    libclang_rt.eprintf.a

.. note::

    You should never have to add the libraries to a project. Clang will handle
    it for you. If you find you cannot pass the ``-fsanitize=XXX`` flag through
    ``make``'s implicit variables (``CFLAGS``, ``CXXFLAGS``, ``CC``,
    ``CXXFLAGS``, ``LDFLAGS``) during ``configure``, then you should modify the
    makefile after configuring to ensure the flag is passed through the
    compiler.

The installer does not install all the components needed on occasion. For
example, you might want to run a ``scan-build`` or examine the results with
``scan-veiw``. You can copy the components by hand with: ::

    sudo mkdir /usr/local/bin/scan-build
    sudo cp -r llvm-3.4/tools/clang/tools/scan-build /usr/local/bin
    sudo mkdir /usr/local/bin/scan-view
    sudo cp -r llvm-3.4/tools/clang/tools/scan-view /usr/local/bin

.. note::

    Because the installer does not install all the components needed on
    occasion, you should not delete the scratch directory until you are sure
    things work as expected. If a library is missing, then you should search for
    it in the Clang/LLVM build directory.

Python Build Setup
==================

This portion of the document covers invoking Clang and LLVM with the options
required so the sanitizers analyze Python with under its test suite. Two
checkers are used - ASan and UBSan.

Because the sanitizers are runtime checkers, its best to have as many positive
and negative self tests as possible. You can never have enough self tests.

The general idea is to compile and link with the sanitizer flags. At link time,
Clang will include the needed runtime libraries. However, you can't use
``CFLAGS`` and ``CXXFLAGS`` to pass the options through the compiler to the
linker because the makefile rules for ``BUILDPYTHON``, ``_testembed`` and
``_freeze_importlib`` don't use the implicit variables.

As a workaround to the absence of flags to the linker, you can pass the
sanitizer options by way of the compilers - ``CC`` and ``CXX``.  Passing the
flags though the compiler is used below, but passing them through ``LDFLAGS`` is
also reported to work.

Building Python
---------------

To begin, export the variables of interest with the desired sanitizers. Its OK
to specify both sanitizers: ::

    # ASan
    export CC="/usr/local/bin/clang -fsanitize=address"
    export CXX="/usr/local/bin/clang++ -fsanitize=address -fno-sanitize=vptr"

Or: ::

    # UBSan
    export CC="/usr/local/bin/clang -fsanitize=undefined"
    export CXX="/usr/local/bin/clang++ -fsanitize=undefined -fno-sanitize=vptr"

The ``-fno-sanitize=vptr`` removes vtable checks that are part of UBSan from C++
projects due to noise. Its not needed with Python, but you will likely need it
for other C++ projects.

After exporting ``CC`` and ``CXX``, ``configure`` as normal: ::

    $ ./configure
    checking build system type... x86_64-unknown-linux-gnu
    checking host system type... x86_64-unknown-linux-gnu
    checking for --enable-universalsdk... no
    checking for --with-universal-archs... 32-bit
    checking MACHDEP... linux
    checking for --without-gcc... no
    checking for gcc... /usr/local/bin/clang -fsanitize=undefined
    checking whether the C compiler works... yes
    ...

Next is a standard ``make`` (formatting added for clarity): ::

    $ make
    /usr/local/bin/clang -fsanitize=undefined -c -Wno-unused-result
        -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I.
        -IInclude -I./Include -DPy_BUILD_CORE -o Modules/python.o
        ./Modules/python.c
    /usr/local/bin/clang -fsanitize=undefined -c -Wno-unused-result
        -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I.
        -IInclude -I./Include -DPy_BUILD_CORE -o Parser/acceler.o
        Parser/acceler.c
    ...

Finally is ``make test`` (formatting added for clarity): ::

    Objects/longobject.c:39:42: runtime error: index -1 out of bounds
        for type 'PyLongObject [262]'
    Objects/tupleobject.c:188:13: runtime error: member access within
        misaligned address 0x2b76be018078 for type 'PyGC_Head' (aka
        'union _gc_head'), which requires 16 byte alignment
        0x2b76be018078: note: pointer points here
        00 00 00 00  40 53 5a b6 76 2b 00 00  60 52 5a b6 ...
                     ^ 
    ...

If you are using the address sanitizer, its important to pipe the output through
``asan_symbolize.py`` to get a good trace. For example, from Issue 20953 during
compile (formatting added for clarity): ::

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

    ``asan_symbolize.py`` is supposed to be installed during ``make install``.
    If its not installed, then look in the Clang/LLVM build directory for it and
    copy it to ``/usr/local/bin``.

Blacklisting (Ignoring) Findings
--------------------------------

Clang allows you to alter the behavior of sanitizer tools for certain
source-level by providing a special blacklist file at compile-time. The
blacklist is needed because it reports every instance of an issue, even if the
issue is reported 10's of thousands of time in un-managed library code.

You specify the blacklist with ``-fsanitize-blacklist=XXX``. For example: ::

    -fsanitize-blacklist=my_blacklist.txt

``my_blacklist.txt`` would then contain entries such as the following. The entry
will ignore a bug in ``libc++``'s ``ios`` formatting functions: ::

    fun:_Ios_Fmtflags

As an example with Python 3.4.0, ``audioop.c`` will produce a number of
findings: ::

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
422), and the blacklist entry would include: ::

    fun:audioop_getsample_imp

Or, you could ignore the entire file with: ::

    src:Modules/audioop.c

Unfortunately, you won't know what to blacklist until you run the sanitizer.

The documentation is available at `Sanitizer special case list
<http://clang.llvm.org/docs/SanitizerSpecialCaseList.html>`_.
