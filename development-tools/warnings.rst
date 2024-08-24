.. warnings:

Tools for tracking compiler warnings
====================================

.. highlight:: bash

The compiler warning tracking tooling is intended to alert developers about new
compiler warnings introduced by their contributions. The tooling consists of
a Python script which is ran by the following GitHub workflows:

* Ubuntu/build and test (:cpy-file:`.github/workflows/reusable-ubuntu.yml`)
* macOS/build and test (:cpy-file:`.github/workflows/reusable-macos.yml`)

You can check the documentation for the :cpy-file:`Tools/build/check_warnings.py` tool
by running::

   python Tools/build/check_warnings.py --help

The script can be run locally by providing the compiler output file
(where the output is saved) and the compiler output type
(either ``json`` or ``clang``) to see a list of unique warnings::

   python Tools/build/check_warnings.py --compiler-output-file-path=compiler_output.txt --compiler-output-type=json

.. note:: The ``-fdiagnostics-format=json`` flag is required when compiling with GCC
          for the script to properly parse the compiler output.

.. _warning-check-failure:

What to do if a warning check fails GitHub CI
---------------------------------------------

The :cpy-file:`Tools/build/check_warnings.py` tool will fail if the compiler generates
more or less warnings than expected for a given source file as defined in the
platform-specific warning ignore file. The warning ignore file is either
:cpy-file:`Tools/build/.warningignore_ubuntu` or
:cpy-file:`Tools/build/.warningignore_macos` depending on the platform.

If a warning check fails with:

* Unexpected warnings
    * Attempt to refactor the code to avoid the warning.
    * If it is not possible to avoid the warning document in the PR why it is
      reasonable to ignore and add the warning to the platform-specific
      warning ignore file. If the file exists in the warning ignore file
      increment the count by the number of newly introduced warnings.
* Unexpected improvements (less warnings)
    * Document in the PR that the change reduces the number of compiler
      warnings. Decrement the count in the platform-specific warning
      ignore file or remove the file if the count is now zero.
