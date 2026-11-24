.. _specialization:

=====================================
Specializing a bytecode instruction
=====================================

CPython 3.11 and later includes a Specializing Adaptive Interpreter (:pep:`659`).
The interpreter analyzes types and shapes of data at runtime and replaces generic,
unspecialized bytecode instructions with faster, specialized variants tailored to
specific data types or conditions (for example, lists, dictionaries, tuples, or
integers).

When an unspecialized instruction runs repeatedly, its inline cache tracks execution
frequency. Once the counter reaches zero, the interpreter attempts to *specialize*
the instruction to a faster variant. If runtime conditions change or an unexpected
type arrives, the instruction *deoptimizes* back to the base instruction.

This guide provides a step-by-step checklist for adding a new bytecode specialization
to CPython, using the specialization of ``CONTAINS_OP`` from
:github:`python/cpython pull request #116385 <python/cpython/pull/116385>` as a concrete
example.


Overview of components
======================

Specializing an instruction requires updates across several parts of the CPython codebase:

1. **Inline cache definition** in :cpy-file:`Include/internal/pycore_code.h`:
   defines the memory structure used to store the adaptive counter and any cached values.
2. **Instruction definition and DSL** in :cpy-file:`Python/bytecodes.c`:
   defines the instruction family, micro-ops (uops), specializing uop, instruction macro,
   and specialized instructions.
3. **Specialization logic** in :cpy-file:`Python/specialize.c`:
   inspects runtime objects, selects the appropriate specialized opcode, and updates
   adaptive counters and statistics.
4. **Disassembler metadata** in :cpy-file:`Lib/opcode.py`:
   describes inline cache layout so :mod:`dis` can decode instructions correctly.
5. **Bytecode magic number** in :cpy-file:`Include/internal/pycore_magic_number.h`:
   invalidates outdated ``.pyc`` files across Python builds.
6. **Code regeneration**:
   runs tools to generate C opcode headers and interpreter switch cases.


Step-by-step checklist
======================

The following steps use the ``in`` / ``not in`` operator instruction (``CONTAINS_OP``)
as a real-world example.


Step 1: Define the cache structure and function declaration
-----------------------------------------------------------

Each specializable instruction family requires an inline cache. At minimum, the
cache must include a 16-bit adaptive counter (``uint16_t counter``). If the
specialization tracks additional state (like type versions or dictionary keys),
additional fields are included in this struct.

In :cpy-file:`Include/internal/pycore_code.h`:

1. Define the cache structure and the cache entry count macro:

   .. code-block:: c

      typedef struct {
          uint16_t counter;
      } _PyContainsOpCache;

      #define INLINE_CACHE_ENTRIES_CONTAINS_OP CACHE_ENTRIES(_PyContainsOpCache)

   The ``CACHE_ENTRIES()`` macro computes the number of 2-byte code units
   (``_Py_CODEUNIT``) required for the struct.

2. Declare the specializing function:

   .. code-block:: c

      extern void _Py_Specialize_ContainsOp(PyObject *value, _Py_CODEUNIT *instr);


Step 2: Update Python/bytecodes.c
---------------------------------

In :cpy-file:`Python/bytecodes.c`, the interpreter instructions are written using
CPython's bytecode Domain Specific Language (DSL).

1. **Define the family:**
   Group the base opcode and all of its specialized variants into an instruction
   family:

   .. code-block:: c

      family(CONTAINS_OP, INLINE_CACHE_ENTRIES_CONTAINS_OP) = {
          CONTAINS_OP_LIST,
          CONTAINS_OP_SET,
          CONTAINS_OP_TUPLE,
          CONTAINS_OP_DICT,
          CONTAINS_OP_STR,
      };

2. **Convert the base instruction to a micro-op (uop):**
   Change the original instruction definition from ``inst(CONTAINS_OP, ...)``
   to an internal uop ``op(_CONTAINS_OP, ...)``:

   .. code-block:: c

      op(_CONTAINS_OP, (left, right -- b)) {
          int res = PySequence_Contains(right, left);
          DECREF_INPUTS();
          ERROR_IF(res < 0, error);
          b = (res ^ oparg) ? Py_True : Py_False;
      }

3. **Add the specializing uop:**
   Create a specializing micro-op that checks if the adaptive counter has expired.
   When the counter reaches zero, call your specializing function. Otherwise,
   decrement the counter and record deferred statistics:

   .. code-block:: c

      specializing op(_SPECIALIZE_CONTAINS_OP, (counter/1, left, right -- left, right)) {
          #if ENABLE_SPECIALIZATION
          if (ADAPTIVE_COUNTER_IS_ZERO(counter)) {
              next_instr = this_instr;
              _Py_Specialize_ContainsOp(right, next_instr);
              DISPATCH_SAME_OPARG();
          }
          STAT_INC(CONTAINS_OP, deferred);
          DECREMENT_ADAPTIVE_COUNTER(this_instr[1].cache);
          #endif  /* ENABLE_SPECIALIZATION */
      }

   .. note::
      The ``counter/1`` notation tells the generator that this uop consumes one
      inline cache entry from the instruction stream.

4. **Define the macro:**
   Combine the specializing uop with the unspecialized uop to define the top-level
   macro instruction:

   .. code-block:: c

      macro(CONTAINS_OP) = _SPECIALIZE_CONTAINS_OP + _CONTAINS_OP;

5. **Implement specialized instructions:**
   Write the specialized instruction cases. Each specialized instruction begins
   with ``unused/N`` (where ``N`` is the cache entry count) and one or more
   ``DEOPT_IF`` guards. If the guard succeeds, execute the optimized fast path:

   .. code-block:: c

      inst(CONTAINS_OP_LIST, (unused/1, left, right -- b)) {
          DEOPT_IF(!PyList_CheckExact(right));
          int res = _PyList_Contains(right, left);
          DECREF_INPUTS();
          ERROR_IF(res < 0, error);
          b = (res ^ oparg) ? Py_True : Py_False;
      }

      inst(CONTAINS_OP_DICT, (unused/1, left, right -- b)) {
          DEOPT_IF(!PyDict_CheckExact(right));
          int res = PyDict_Contains(right, left);
          DECREF_INPUTS();
          ERROR_IF(res < 0, error);
          b = (res ^ oparg) ? Py_True : Py_False;
      }

   (Repeat for any other specialized variants such as ``_SET``, ``_TUPLE``, or ``_STR``).


Step 3: Implement the specializing function in Python/specialize.c
------------------------------------------------------------------

In :cpy-file:`Python/specialize.c`, implement the function that selects the specialized
opcode based on runtime types:

1. **Register the stats dictionary:**
   Inside ``_Py_GetSpecializationStats()``, call ``add_stat_dict()``:

   .. code-block:: c

      err += add_stat_dict(stats, CONTAINS_OP, "contains_op");

2. **Implement the function:**

   .. code-block:: c

      void
      _Py_Specialize_ContainsOp(PyObject *value, _Py_CODEUNIT *instr)
      {
          assert(ENABLE_SPECIALIZATION);
          assert(_PyOpcode_Caches[CONTAINS_OP] == INLINE_CACHE_ENTRIES_CONTAINS_OP);
          _PyContainsOpCache *cache = (_PyContainsOpCache *)(instr + 1);

          if (PyUnicode_CheckExact(value)) {
              instr->op.code = CONTAINS_OP_STR;
              goto success;
          }
          if (PyList_CheckExact(value)) {
              instr->op.code = CONTAINS_OP_LIST;
              goto success;
          }
          if (PyTuple_CheckExact(value)) {
              instr->op.code = CONTAINS_OP_TUPLE;
              goto success;
          }
          if (PyDict_CheckExact(value)) {
              instr->op.code = CONTAINS_OP_DICT;
              goto success;
          }
          if (PySet_CheckExact(value)) {
              instr->op.code = CONTAINS_OP_SET;
              goto success;
          }

          STAT_INC(CONTAINS_OP, failure);
          instr->op.code = CONTAINS_OP;
          cache->counter = adaptive_counter_backoff(cache->counter);
          return;

      success:
          STAT_INC(CONTAINS_OP, success);
          cache->counter = adaptive_counter_cooldown();
      }

   * When a suitable type is matched, rewrite ``instr->op.code``, increment the ``success``
     stat, and reset the counter using ``adaptive_counter_cooldown()``.
   * If no specialized case applies, increment the ``failure`` stat and back off the
     counter using ``adaptive_counter_backoff()`` to avoid repeated failing attempts.


Step 4: Expose internal fast-path C helpers if needed
-----------------------------------------------------

If your specialized operations need direct access to type-internal functions without
generic slot lookups, declare internal helpers in :cpy-file:`Include/internal/` and
define them in the corresponding object file.

For example, in PR #116385:

* Declared ``PyAPI_FUNC(int) _PyList_Contains(PyObject *aa, PyObject *el);`` in
  :cpy-file:`Include/internal/pycore_list.h`.
* Exported the definition in :cpy-file:`Objects/listobject.c`.
* Similar internal helpers were declared for sets (:cpy-file:`Include/internal/pycore_setobject.h`)
  and tuples (:cpy-file:`Include/internal/pycore_tuple.h`).


Step 5: Add cache layout in Lib/opcode.py
-----------------------------------------

In :cpy-file:`Lib/opcode.py`, add your instruction's cache format to ``_inline_cache_entries``:

.. code-block:: python

   _inline_cache_entries = {
       ...
       "CONTAINS_OP": {
           "counter": 1,
       },
       ...
   }

This enables the :mod:`dis` module to recognize the cache entry words following the opcode,
allowing disassembly output to format and display cache entries properly.


Step 6: Bump the bytecode magic number
--------------------------------------

Because adding inline cache entries alters the bytecode layout, compiled ``.pyc`` files
generated by earlier builds are incompatible.

Bump the value of ``MAGIC_NUMBER`` in :cpy-file:`Include/internal/pycore_magic_number.h`
(and note the change in comments).


Step 7: Regenerate code files
-----------------------------

Regenerate the opcode metadata and generated interpreter files:

* On Linux/macOS:

  .. code-block:: shell

     make regen-all

* On Windows:

  .. code-block:: bat

     build.bat --regen

This regenerates the following files:

* :cpy-file:`Include/opcode_ids.h`
* :cpy-file:`Include/internal/pycore_opcode_metadata.h`
* :cpy-file:`Include/internal/pycore_uop_ids.h`
* :cpy-file:`Include/internal/pycore_uop_metadata.h`
* :cpy-file:`Python/generated_cases.c.h`
* :cpy-file:`Python/executor_cases.c.h`
* :cpy-file:`Python/optimizer_cases.c.h`
* :cpy-file:`Python/opcode_targets.h`
* :cpy-file:`Lib/_opcode_metadata.py`


Step 8: Testing and benchmarking
--------------------------------

1. **Run the test suite:**

   .. code-block:: shell

      ./python -m test test_dis test_opcodes

2. **Verify disassembly:**
   Ensure :mod:`dis` correctly shows the cache entries:

   .. code-block:: shell

      ./python -m dis -c "x in [1, 2, 3]"

3. **Check specialization statistics:**
   Build Python with specialization statistics enabled (``--enable-pystats``)
   and inspect stats using ``python -X pystats`` to ensure that hits and successes
   are properly recorded.

4. **Benchmark:**
   Run relevant benchmarks using `pyperformance <https://pyperformance.readthedocs.io/>`__
   to verify that the specialization produces measurable speedups and that deoptimization
   penalties remain low.


See also
========

* :pep:`659` -- Specializing Adaptive Interpreter
* :cpy-file:`InternalDocs/interpreter.md`
* :github:`python/cpython PR #116385 <python/cpython/pull/116385>`: Specialization of ``CONTAINS_OP``
