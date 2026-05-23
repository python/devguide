OSS-Fuzz for CPython
====================

CPython uses `OSS-Fuzz <https://google.github.io/oss-fuzz/>`__, Google's
continuous fuzzing service for open source projects, to find bugs and
security vulnerabilities by feeding semi-random data to various APIs.

CPython has two OSS-Fuzz projects:

* `cpython3 <https://github.com/google/oss-fuzz/tree/master/projects/cpython3>`__:
  The fuzz targets, seed corpora, and dictionaries can be found in the
  :cpy-file:`Modules/_xxtestfuzz/` directory of CPython. This project
  is maintained for existing fuzz targets; add new targets to
  ``python3-libraries``.

* `python3-libraries <https://github.com/google/oss-fuzz/tree/master/projects/python3-libraries>`__:
  The fuzz targets, seed corpora, and dictionaries can be found in the
  :github:`python/library-fuzzers` repository. Access to the repository is
  managed through the `@python/fuzzers
  <https://github.com/orgs/python/teams/fuzzers>`__ team on GitHub.

OSS-Fuzz bug reports are private when filed, so access to crash details and
reproducer test cases is limited to those listed in the ``auto_ccs`` fields of
the OSS-Fuzz project configuration files. Those listed can log into
https://oss-fuzz.com/ with their Google account to view crash details,
reproducer test cases, and project statistics.
If you need access, contact the ``@python/fuzzers`` team.
Completed issues, and issues that remain unresolved after 90 days, are publicly
visible in the `OSS-Fuzz issue tracker
<https://issues.oss-fuzz.com/issues?q=(python3-libraries%20%7C%20cpython3)>`__.

Coverage and target statistics are available in the OSS-Fuzz Introspector
project profiles for `cpython3 <https://introspector.oss-fuzz.com/project-profile?project=cpython3>`__ and
`python3-libraries <https://introspector.oss-fuzz.com/project-profile?project=python3-libraries>`__.

In addition, `CIFuzz <https://google.github.io/oss-fuzz/getting-started/continuous-integration/>`__
runs the fuzz targets on GitHub Actions for PRs to the ``main`` branch changing
relevant files.

.. seealso::

   The `libFuzzer <https://llvm.org/docs/LibFuzzer.html>`__ documentation for
   details about the fuzzing engine used by OSS-Fuzz.


Adding new targets
------------------

Add new targets to the ``python3-libraries`` project. For more
information, see the documentation in the :github:`python/library-fuzzers`
repository.

If the new target covers a standard library module, update the relevant CIFuzz
path configuration so pull requests touching that module trigger fuzzing. See
the ``LIBRARY_FUZZER_PATHS`` set in :cpy-file:`Tools/build/compute-changes.py`.
