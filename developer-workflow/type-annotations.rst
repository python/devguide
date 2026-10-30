.. _type-annotations:

=================
Type annotations
=================

CPython does not generally add type annotations to modules in the standard
library's ``Lib`` directory. Static type checkers use the stubs maintained in
`typeshed <https://github.com/python/typeshed>`__ for standard-library APIs.
Keeping those stubs separate lets typing tools update their descriptions
independently of Python's release cycle.

There are exceptions. Some standard-library modules and CPython development
tools already contain annotations. When adding or changing annotated code,
make sure the annotations are checked by the project's type-checking tools;
unchecked annotations can become misleading or invalid. Do not add annotations
to a standard-library module solely to provide type information to users.

This guidance describes the current practice, rather than a rule that every
existing annotation must be removed. The practice and rationale are discussed
in `Static type annotations in CPython
<https://discuss.python.org/t/static-type-annotations-in-cpython/65068>`__.

CPython's user-facing documentation is maintained separately from the Python
source code. When a type is useful to readers, include a clear, readable type
description in the documentation following the usual :ref:`documentation
guidelines <documenting>`; do not copy complex checker-oriented annotations
without considering whether they help the reader.
