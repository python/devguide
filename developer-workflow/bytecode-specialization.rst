.. _bytecode-specialization:

================================
Adding a Bytecode Specialization
================================

CPython uses an adaptive, specializing interpreter (PEP 659) to optimize bytecode execution dynamically at runtime. When generic opcodes (such as ``CONTAINS_OP`` or ``BINARY_OP``) execute frequently with predictable operand types, CPython morphs them into specialized fast-path micro-ops (uops) to bypass generic type dispatch.

This guide describes the step-by-step process of introducing a new bytecode specialization in CPython.

.. note::

   This guide uses the specialization of ``CONTAINS_OP`` (from `CPython PR #116385 <https://github.com/python/cpython/pull/116385>`_) as a reference example.


Overview of Steps
-----------------

Adding a new bytecode specialization involves coordinated changes across several files in the CPython source tree:

1. :ref:`spec-step-bytecodes`
2. :ref:`spec-step-uop`
3. :ref:`spec-step-macro`
4. :ref:`spec-step-cache-struct`
5. :ref:`spec-step-specialize-fn`
6. :ref:`spec-step-stats`
7. :ref:`spec-step-opcode-py`
8. :ref:`spec-step-magic-num`
9. :ref:`spec-step-regen`


.. _spec-step-bytecodes:

1. Modify the Opcode Definition in ``Python/bytecodes.c``
---------------------------------------------------------

In ``Python/bytecodes.c``, locate the existing generic instruction. Change its definition from a top-level instruction (``inst``) to a micro-op (``op``) and prefix its name with an underscore.

For example, convert ``CONTAINS_OP`` into ``_CONTAINS_OP``:

.. code-block:: c

    op(_CONTAINS_OP, (left, right -- res)) {
        // Implementation of generic operation
        int res_val = PySequence_Contains(right, left);
        if (res_val < 0) goto error;
        res = res_val ? Py_True : Py_False;
    }


.. _spec-step-uop:

2. Add the Specializing Micro-Op (uop)
--------------------------------------

Add a new uop definition in ``Python/bytecodes.c`` that triggers the specialization check when the execution counter reaches zero.

.. code-block:: c

    op(_SPECIALIZE_CONTAINS_OP, (left, right -- left, right)) {
        _PySpecializer_Requestation(this_instr, _SPECIALIZE_CONTAINS_OP);
    }


.. _spec-step-macro:

3. Define the Macro Instruction
-------------------------------

Combine the specializing uop and the original uop into a macro instruction using ``macro`` syntax in ``Python/bytecodes.c``:

.. code-block:: c

    macro(CONTAINS_OP) = _SPECIALIZE_CONTAINS_OP + _CONTAINS_OP;


.. _spec-step-cache-struct:

4. Define the Cache Structure in ``Include/internal/pycore_code.h``
-------------------------------------------------------------------

Define a C struct for the instruction's inline cache in ``Include/internal/pycore_code.h``. Every cache entry must include at least a 16-bit specialization counter (``counter``), plus any specialized metadata or version pointers needed.

.. code-block:: c

    typedef struct {
        _PySpecializationCacheTop counter;
        // Additional cache fields if needed (e.g., version or type pointers)
    } _PyContainsOpCache;


.. _spec-step-specialize-fn:

5. Write the Specializing Function in ``Python/specialize.c``
-------------------------------------------------------------

Implement the specializing logic in ``Python/specialize.c``. This function inspects the runtime operand types, checks whether they qualify for a fast path, updates the cache, and rewrites the opcode if appropriate.

.. code-block:: c

    void
    _Py_Specialize_ContainsOp(PyObject *left, PyObject *right, _Py_CODEUNIT *instr)
    {
        _PyContainsOpCache *cache = (_PyContainsOpCache *)instr;
        if (PySet_CheckExact(right)) {
            // Specialize for set containment
            instr->op.code = _BINARY_OP_CONTAINS_SET;
        }
        else {
            // Fallback / UNSTATISFIED
            STAT_INC(CONTAINS_OP, failure);
        }
    }


.. _spec-step-stats:

6. Update Operation Statistics in ``Python/specialize.c``
---------------------------------------------------------

Track specialization hits, misses, and execution counts by calling ``add_stat_dict()`` or incrementing statistic counters in ``Python/specialize.c``:

.. code-block:: c

    STAT_INC(CONTAINS_OP, hit);


.. _spec-step-opcode-py:

7. Add Cache Layout in ``Lib/opcode.py``
----------------------------------------

Update ``Lib/opcode.py`` to inform Python's ``dis`` (disassembler) module about the size and structure of the new instruction's inline cache entries:

.. code-block:: python

    _specialized_opcodes["CONTAINS_OP"] = {
        "counter": 1,
    }


.. _spec-step-magic-num:

8. Bump the Magic Number in ``Include/internal/pycore_magic_number.h``
----------------------------------------------------------------------

Because adding or altering inline cache structures changes the bytecode format, increment ``MAGIC_NUMBER`` in ``Include/internal/pycore_magic_number.h``. This ensures older ``.pyc`` files are invalidated and recompiled.


.. _spec-step-regen:

9. Regenerate Code Files
------------------------

Run the code generators to update auto-generated files (like ``opcode_targets.h``, ``executor_cases.c``, etc.):

On Linux / macOS:

.. code-block:: bash

    make regen-all

On Windows:

.. code-block:: bash

    build.bat --regen


See Also
--------

* `PEP 659 -- Specializing Adaptive Interpreter <https://peps.python.org/pep-0659/>`_
* `CPython PR #116385 <https://github.com/python/cpython/pull/116385>`_
* :ref:`dev-workflow`
