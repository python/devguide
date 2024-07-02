.. _c-api:

=======================
Changing Python's C API
=======================

The C API is divided into these tiers:

1. The internal, private API, available with ``Py_BUILD_CORE`` defined.
   Ideally declared in ``Include/internal/``. Any API named with a leading
   underscore is also considered private.
2. The Unstable C API, identified by the ``PyUnstable_`` name prefix.
   Ideally declared in :cpy-file:`Include/cpython/` along with the general public API.
3. The “general” public C API, available when :cpy-file:`Include/Python.h` is included normally.
   Ideally declared in ``Include/cpython/``.
4. The Limited C API, available with :c:macro:`Py_LIMITED_API` defined.
   Ideally declared directly under ``Include/``.

Each tier has different stability and maintenance requirements to consider
when you add or change definitions in it.

The compatibility guarantees for public C API are explained in the
user documentation, ``Doc/c-api/stable.rst`` (:ref:`python:stable`).


The internal API
================

Internal API is defined in ``Include/internal/`` and is only available
for building CPython itself, as indicated by a macro like ``Py_BUILD_CORE``.

While internal API can be changed at any time, it's still good to keep it
stable: other API or other CPython developers may depend on it.
For users, internal API is sometimes the best workaround for a thorny problem
--- though those use cases should be discussed on the
`C API Discourse category <https://discuss.python.org/c/30>`_
or an issue so we can try to find a supported way to serve them.


With PyAPI_FUNC or PyAPI_DATA
-----------------------------

Functions or structures in ``Include/internal/`` defined with
``PyAPI_FUNC`` or ``PyAPI_DATA`` are internal functions which are
exposed only for specific use cases like debuggers and profilers.
Ideally, these should be migrated to the :ref:`unstable-capi`.


With the extern keyword
-----------------------

Functions in ``Include/internal/`` defined with the ``extern`` keyword
*must not and can not* be used outside the CPython code base.  Only
built-in stdlib extensions (built with the ``Py_BUILD_CORE_BUILTIN``
macro defined) can use such functions.

When in doubt, new internal C functions should be defined in
``Include/internal`` using the ``extern`` keyword.

Private names
-------------

Any API named with a leading underscore is also considered internal.
There is currently only one main use case for using such names rather than
putting the definition in :cpy-file:`Include/internal/` (or directly in a ``.c`` file):

* Internal helpers for other public APIs, which users should not call directly.

Note that historically, underscores were used for APIs that are better served by
the :ref:`unstable-capi`:

* “provisional” APIs, included in a Python release to test real-world
  usage of new APIs;
* APIs for very specialized uses like JIT compilers.


Internal API tests
------------------

C tests for the internal C API live in ``Modules/_testinternalcapi.c``.
Functions named ``test_*`` are used as tests directly.
Python parts of the tests live in various places in ``Lib/test``.


.. _public-capi:

Public C API
============

CPython's public C API is available when ``Python.h`` is included normally
(that is, without defining macros to select the other variants).

It should be defined in ``Include/cpython/`` (unless part of the Limited API,
see below).

.. _public-api-guidelines:

Guidelines for expanding/changing the public API
------------------------------------------------

- Make sure the new API follows reference counting conventions.
  (Following them makes the API easier to reason about, and easier use
  in other Python implementations.)

  - Functions *must not* steal references
  - Functions *must not* return borrowed references
  - Functions returning references *must* return a strong reference

- Make sure the ownership rules and lifetimes of all applicable struct
  fields, arguments and return values are well defined.

- Functions returning ``PyObject *`` must return a valid pointer on success,
  and ``NULL`` with an exception raised on error.
  Most other API must return ``-1`` with an exception raised on error,
  and ``0`` on success.

- APIs with lesser and greater results must return ``0`` for the lesser result,
  and ``1`` for the greater result.
  Consider a lookup function with a three-way return:

  - ``return -1``: internal error or API misuse; exception raised
  - ``return 0``: lookup succeeded; no item was found
  - ``return 1``: lookup succeeded; item was found

Please start a public discussion if these guidelines won't work for your API.

.. note::

   By *return value*, we mean the value returned by the *C return statement*.

C API tests
-----------

Tests for the public C API live in the ``_testcapi`` module.
Functions named ``test_*`` are used as tests directly.
Tests that need Python code (or are just easier to partially write in Python)
live in ``Lib/test``, mainly in :cpy-file:`Lib/test/test_capi`.

Due to its size, the ``_testcapi`` module is defined in several source
files.
To add a new set of tests (or extract a set out of the monolithic
:cpy-file:`Modules/_testcapimodule.c`):

- Create a C file named ``Modules/_testcapi/yourfeature.c``

- The file should define a module as usual, except:

  - Instead of ``<Python.h>``, include ``"parts.h"``.
  - Instead of ``PyInit_modname``, define a ``_PyTestCapi_Init_yourfeature``
    function that *takes* the ``_testcapi`` module and adds functions/classes
    to it. (You can use ``PyModule_AddFunctions`` to add functions.)

- Add the ``_PyTestCapi_Init_*`` function to ``Modules/_testcapi/parts.h``

- Call the ``_PyTestCapi_Init_*`` from ``PyInit__testcapi`` in
  ``Modules/_testcapimodule.c``.

- Add the new C file to :cpy-file:`Modules/Setup.stdlib.in`,
  :cpy-file:`PCbuild/_testcapi.vcxproj` and
  :cpy-file:`PCbuild/_testcapi.vcxproj.filters`,
  alongside the other ``_testcapi/*.c`` entries.

Note that all ``Modules/_testcapi/*.c`` sources initialize the same module,
so be careful about name collisions.

When moving existing tests, feel free to replace ``TestError`` with
``PyExc_AssertionError`` unless actually testing custom exceptions.


.. _unstable-capi:

Unstable C API
==============

The unstable C API tier is meant for extensions that need tight integration
with the interpreter, like debuggers and JIT compilers.
Users of this tier may need to change their code with every feature release.

In many ways, this tier is like the general C API:

- it's available when ``Python.h`` is included normally,
- it should be defined  in :cpy-file:`Include/cpython/`,
- it requires tests, so we don't break it unintentionally
- it requires docs, so both we and the users,
  can agree on the expected behavior,
- it is tested and documented in the same way.

The differences are:

- Names of functions structs, macros, etc. start with the ``PyUnstable_``
  prefix. This defines what's in the unstable tier.
- The unstable API can change in feature releases, without any deprecation
  period.
- A stability note appears in the docs.
  This happens automatically, based on the name
  (via :cpy-file:`Doc/tools/extensions/c_annotations.py`).

Despite being “unstable”, there are rules to make sure third-party code can
use this API reliably:

* Changes and removals can be done in feature releases
  (:samp:`3.{x}.0`, including Alphas and Betas for :samp:`3.{x}.0`).
* Adding a new unstable API *for an existing feature* is allowed even after
  Beta feature freeze, up until the first Release Candidate.
  Consensus on the `Core Development Discourse <https://discuss.python.org/c/core-dev/23>`_
  is needed in the Beta period.
* Backwards-incompatible changes should make existing C callers fail to compile.
  For example, arguments should be added/removed, or a function should be
  renamed.
* When moving an API into or out of the Unstable tier, the old name
  should continue to be available (but deprecated) until an incompatible
  change is made. In other words, while we're allowed to break calling code,
  we shouldn't break it *unnecessarily*.


Moving an API from the public tier to Unstable
----------------------------------------------

* Expose the API under its new name, with the ``PyUnstable_`` prefix.
  The ``PyUnstable_`` prefix must be used for all symbols (functions, macros,
  variables, etc.).
* Make the old name an alias (for example, a ``static inline`` function calling the
  new function).
* Deprecate the old name, typically using :c:macro:`Py_DEPRECATED`.
* Announce the change in the "What's New".

The old name should continue to be available until an incompatible change is
made. Per Python’s backwards compatibility policy (:pep:`387`),
this deprecation needs to last at least two releases
(modulo Steering Council exceptions).

The rules are relaxed for APIs that were introduced in Python versions
before 3.12, when the official Unstable tier was added.
You can make an incompatible change (and remove the old name)
as if the function was already part of the Unstable tier
for APIs introduced before Python 3.12 that are either:

* Documented to be less stable than default.
* Named with a leading underscore.

Moving an API from the private tier to unstable
-----------------------------------------------

* Expose the API under its new name, with the ``PyUnstable_`` prefix.
* If the old name is documented, or widely used externally,
  make it an alias and deprecate it (typically with :c:macro:`Py_DEPRECATED`).
  It should continue to be available until an incompatible change is made,
  as if it was previously public.

  This applies even to underscored names. Python wasn't always strict with
  the leading underscore.
* Announce the change in What's New.

Moving an API from unstable to public
-------------------------------------

* Expose the API under its new name, without the ``PyUnstable_`` prefix.
* Make the old ``PyUnstable_*`` name be an alias (for example, a ``static inline``
  function calling the new function).
* Announce the change in What's New.

The old name should remain available until the
new public name is deprecated or removed.
There's no need to deprecate the old name (it was unstable to begin with),
but there's also no need to break working code just because some function
is now ready for a wider audience.


Limited API
===========

The Limited API is a subset of the C API designed to guarantee ABI
stability across Python 3 versions.
Defining the macro ``Py_LIMITED_API`` will limit the exposed API to
this subset.

No changes that break the Stable ABI are allowed.

The Limited API should be defined in ``Include/``, excluding the
``cpython`` and ``internal`` subdirectories.


Guidelines for changing the Limited API, and removing items from it
-------------------------------------------------------------------

While the *Stable ABI*  must not be broken, the existing Limited API can be
changed, and items can be removed from it, if:

- the Backwards Compatibility Policy (:pep:`387`) is followed, and
- the Stable ABI is not broken -- that is, extensions compiled with
  Limited API of older versions of Python continue to work on
  newer versions of Python.

This is tricky to do and requires careful thought.
Some examples:

- Functions, structs etc. accessed by macros in *any version* of the
  Limited API are part of the Stable ABI, even if they are named with
  an underscore. They must not be removed and their signature must not change.
  (Their implementation may change, though.)
- Structs members cannot be rearranged if they were part of any version of
  the Limited API.
- If the Limited API allows users to allocate a struct directly,
  its size must not change.
- Exported symbols (functions and data) must continue to be available
  as exported symbols. Specifically, a function can only be converted
  to a ``static inline`` function (or macro) if Python also continues to
  provide the actual function.
  For an example, see the ``Py_NewRef`` `macro`_ and `redefinition`_ in 3.10.

.. _macro: https://github.com/python/cpython/blob/2cd268a3a9340346dd86b66db2e9b428b3f878fc/Include/object.h#L592-L596
.. _redefinition: https://github.com/python/cpython/blob/2cd268a3a9340346dd86b66db2e9b428b3f878fc/Objects/object.c#L2303-L2313

It is possible to remove items marked as part of the Stable ABI, but only
if there was no way to use them in any past version of the Limited API.


.. _limited-api-guidelines:

Guidelines for adding to the Limited API
----------------------------------------

- Guidelines for the general :ref:`public-capi` apply.
  See :ref:`public-api-guidelines`.

- New Limited API should only be defined if ``Py_LIMITED_API`` is set
  to the version the API was added in or higher.
  (See below for the proper ``#if`` guard.)

- All parameter types, return values, struct members, etc. need to be part
  of the Limited API.

  - Functions that deal with ``FILE*`` (or other types with ABI portability
    issues) should not be added.

- Think twice when defining macros.

  - Macros should not expose implementation details
  - Functions must be exported as actual functions, not (only)
    as functions-like macros.
  - If possible, avoid macros. This makes the Limited API more usable in
    languages that don't use the C preprocessor.

- Please start a public discussion before expanding the Limited API

- The Limited API and must follow standard C, not just features of currently
  supported platforms. The exact C dialect is described in :pep:`7`.

  - Documentation examples (and more generally: the intended use of the API)
    should also follow standard C.
  - In particular, do not cast a function pointer to ``void*`` (a data pointer)
    or vice versa.

- Think about ease of use for the user.

  - In C, ease of use itself is not very important; what is useful is
    reducing boilerplate code needed to use the API. Bugs like to hide in
    boiler plates.

  - If a function will be often called with specific value for an argument,
    consider making it default (used when ``NULL`` is passed in).
  - The Limited API needs to be well documented.

- Think about future extensions

  - If it's possible that future Python versions will need to add a new
    field to your struct, make sure it can be done.
  - Make as few assumptions as possible about implementation details that
    might change in future CPython versions or differ across C API
    implementations. The most important CPython-specific implementation
    details involve:

    - The GIL
    - :ref:`Garbage collection <gc>`
    - Memory layout of PyObject, lists/tuples and other structures

If following these guidelines would hurt performance, add a fast function
(or macro) to the non-limited API and a stable equivalent to the Limited
API.

If anything is unclear, or you have a good reason to break the guidelines,
consider discussing the change at the `capi-sig`_ mailing list.

.. _capi-sig: https://mail.python.org/mailman3/lists/capi-sig.python.org/

Adding a new definition to the Limited API
------------------------------------------

- Add the declaration to a header file directly under ``Include/``, into a
  block guarded with the following:

  .. code-block:: c

    #if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03yy0000

  with the ``yy`` corresponding to the target CPython version, for example,
  ``0x030A0000`` for Python 3.10.
- Append an entry to the Stable ABI manifest, ``Misc/stable_abi.toml``
- Regenerate the autogenerated files using ``make regen-limited-abi``.
  On platforms without ``make``, run this command directly:

  .. code-block:: shell

     ./python ./Tools/build/stable_abi.py --generate-all ./Misc/stable_abi.toml

- Build Python and check the using ``make check-limited-abi``.
  On platforms without ``make``, run this command directly:

  .. code-block:: shell

    ./python ./Tools/build/stable_abi.py --all ./Misc/stable_abi.toml

- Add tests -- see below.


Limited API tests
-----------------

Since Limited API is a subset of the C API, there's no need to test the
behavior of individual functions. Rather, the tests could verify that some
task is possible using the exposed subset, or exercise a feature that was
removed from the current Limited API but still needs to be supported for
older Limited API/Stable ABI versions.

To add a test file:

- Add a C file ``Modules/_testcapi/yourfeature_limited.c``. If that file
  already exists but its ``Py_LIMITED_API`` version is too low, add a version
  postfix, for example, ``yourfeature_limited_3_12.c`` for Python 3.12+.
- ``#define Py_LIMITED_API`` to the minimum limited API version needed.
- ``#include "parts.h"`` after the ``Py_LIMITED_API`` definition
- Enclose the entire rest of the file in ``#ifdef LIMITED_API_AVAILABLE``,
  so it's skipped on incompatible builds.
- Follow the general instructions for `C API tests`_. All additions go in the
  sections guarded by ``#ifdef LIMITED_API_AVAILABLE``.

Use the ``test.support.requires_limited_api`` decorator for Python tests
in ``Lib/test``, so they're skipped on incompatible builds.
