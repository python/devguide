.. warnings:

=================================
Compiler Warning Tracking Tooling
=================================

The compiler warning tracking tooling is intended to alert developers to new
compiler warnings introduced by their contributions. The tooling consists of
python script which is ran by a few GitHub Actions worksflows. Currently these
GitHub Actions jobs run the warning checking tooling:

- Ubuntu/Build and Test
- macOS/Build and Test

The help text for the `Tools/build/check_warnings.py` is as follows:
::

    usage: check_warnings.py [-h]
           -c COMPILER_OUTPUT_FILE_PATH
           [-i WARNING_IGNORE_FILE_PATH] [-x] [-X] -t {json,clang}

    options:
        -h, --help            show this help message and exit
        -c COMPILER_OUTPUT_FILE_PATH, --compiler-output-file-path COMPILER_OUTPUT_FILE_PATH
                                                    Path to the compiler output file
        -i WARNING_IGNORE_FILE_PATH, --warning-ignore-file-path WARNING_IGNORE_FILE_PATH
                                                    Path to the warning ignore file
        -x, --fail-on-regression
                                                    Flag to fail if new warnings are found
        -X, --fail-on-improvement
                                                    Flag to fail if files that were expected to have warnings have no warnings
        -t {json,clang}, --compiler-output-type {json,clang}
                                                    Type of compiler output file (json or clang)

The script can be run locally by providing the compiler output and the
compiler output type to see a list of unique warnings.

::

        $ python Tools/build/check_warnings.py -c <compiler_output_file> -t <compiler_output_type>

..

    Note: `-fdiagnostics-format=json` flag is required when compiling with GCC
           for the script to properly parse the compiler output.

.. _warning-check-failure:

What To Do If Warning Check Fails GitHub CI
-------------------------------------------

The warning check tooling will fail if the compiler generates more or less
warnings than expected for a given source file as defined in the platform
specific warning ignore file. The warning ignore file is either
`Tools/build/.warningignore_ubuntu` or `Tools/build/.warningignore_macos`
depending on the platform.

If warning check fails with:

1. Unexpected Warnings
    a. Attempt to refactor the code to avoid the warning.
    b. If it is not possible to avoid the warning document in the PR why it is
       reasonable to ignore and add the warning to the platform specific
       warning ignore file. If the file exists in the warning ignore file
       increment the count by the number of new introduced warnings.
2. Unexpected Imrpovements (Less Warnings)
    a. Document in the PR that the change reduces the number of compiler
       warnings. Decrement the count in the platform specific warning
       ignore file or remove the file if the count is now zero.
