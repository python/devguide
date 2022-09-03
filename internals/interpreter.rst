.. _interpreter:

=====================================
The CPython 3.11 Bytecode Interpreter
=====================================

.. highlight:: none

Preface
=======

The CPython 3.11 bytecode interpreter (a.k.a. virtual machine) has a number of improvements over 3.10.
We describe the inner workings of the 3.11 interpreter here, with an emphasis on understanding not just the code but its design.
While the interpreter is forever evolving, and the 3.12 design will undoubtedly be different again, understanding the 3.11 design will help you understand future improvements to the interpreter.

Introduction
============

The bytecode interpreter's job is to execute Python code.
Its main input is a code object, although this is not a direct argument to the interpreter.
The interpreter is structured as a (potentially recursive) function taking a thread state (``tstate``) and a stack frame (``frame``).
The function also takes an integer ``throwflag``, which is used by the implementation of ``generator.throw()``.
It returns a new reference to a Python object (``PyObject *``) or an error indicator, ``NULL``.
Since :pep:`523` this function is configurable by setting ``interp->eval_frame``; we describe only the default function, ``_PyEval_EvalFrameDefault()``.
(This function's signature has evolved and no longer matches what PEP 523 specifies; the thread state argument is added and the stack frame argument is no longer an object.)

The interpreter finds the code object by looking in the stack frame (``frame->f_code``).
Various other items needed by the interpreter (e.g. globals and builtins) are also accessed via the stack frame.
The thread state stores exception information and a variety of other information, such as the recursion depth.
The thread state is also used to access per-interpreter state (``tstate->interp``) and per-runtime (i.e., truly global) state (``tstate->interp->runtime``).

Note the slightly confusing terminology here.
"Interpreter" refers to the bytecode interpreter, a recursive function.
"Interpreter state" refers to state shared by threads, each of which may be running its own bytecode interpreter.
A single process may even host multiple interpreters, each with their own interpreter state, but sharing runtime state.
The topic of multiple interpreters is covered by several PEPs, notably :pep:`684`, :pep:`630`, and :pep:`554` (and more coming).
The current document focuses on the bytecode interpreter.

Code objects
============

The interpreter uses as its starting point a code object (```frame->f_code``).
Code objects contain many fields used by the interpreter, as well as some for use by debuggers and other tools.
In 3.11, the final field of a code object is an array of indeterminate length containing the bytecode, ``code->co_code_adaptive``.
(In previous versions the code object was a ``bytes`` object, ``code->co_code``; it was changed to save an allocation and to allow it to be mutated.)

Code objects are typically produced by the bytecode :ref:``compiler``, although often they are written to disk by one process and read back in by another.
The disk version of a code object is serialized using the `marshal protocol <https://docs.python.org/dev/library/marshal.html>`_.
Some code objects are pre-loaded into the interpreter using ``Tools/scripts/deepfreeze.py``, which writes ``Python/deepfreeze/deepfreeze.c``.

Code objects are nominally immutable.
Some fields (including ``co_code_adaptive``) are mutable, but mutable fields are not included when code objects are hashed or compared.

Instruction decoding
====================

The first task of the interpreter is to decode the bytecode instructions.
Bytecode is stored as an array of 16-bit code units (``_Py_CODEUNIT``).
Each code unit contains an 8-bit ``opcode`` and an 8-bit argument (``oparg``), both unsigned.
In order to make the bytecode format independent of the machine architecture when stored on disk, ``opcode`` is always the first byte and ``oparg`` is always the second byte.
Macros are used to extract the ``opcode`` and ``oparg`` from a code unit (``_Py_OPCODE(word)`` and ``_Py_OPARG(word)``).
Some instructions (e.g. ``NOP`` or ``POP_TOP``) have no argument -- in this case we ignore ``oparg``.

A simple instruction decoding loop would look like this::

    _Py_CODEUNIT *first_instr = code->co_code_adaptive;
    _Py_CODEUNIT *next_instr = first_instr;
    while (1) {
        _Py_CODEUNIT word = *next_instr;
        unsigned char opcode = _Py_OPCODE(word);
        unsigned char oparg = _Py_OPARG(word);
        next_instr++;

        switch (opcode) {
        case NOP:
            break;
    
        // ... A case for each known opcode ...
    
        default:
            PyErr_SetString(PyExc_SystemError, "unknown opcode");
            return NULL;
        }
    }

This format supports 256 different opcodes, which is sufficient.
However, it also limits ``oparg`` to 8-bit values, which is not.
To overcome this, the ``EXTENDED_ARG`` opcode allows us to prefix any instruction with one or more additional data bytes.
For example, this sequence of code units::

    EXTENDED_ARG  1
    EXTENDED_ARG  0
    LOAD_CONST    0

would set ``opcode`` to ``LOAD_CONST`` and ``oparg`` to ``65536`` (i.e., ``2**16``).
The compiler should limit itself to at most three ``EXTENDED_ARG`` prefixes, to allow the resulting ``oparg`` to fit in 32 bits, but the interpreter does not check this.
A series of code units starting with ``EXTENDED_ARG`` is called a complete instruction, to distinguish it from code unit, which is always two bytes.

If we allow ourselves the use of ``goto``, the decoding loop (still far from realistic) could look like this::

    _Py_CODEUNIT *first_instr = code->co_code_adaptive;
    _Py_CODEUNIT *next_instr = first_instr;
    while (1) {
        _Py_CODEUNIT word = *next_instr;
        unsigned char opcode = _Py_OPCODE(word);
        unsigned int oparg = _Py_OPARG(word);
        next_instr++;

    dispatch_opcode:
        switch (opcode) {
        case NOP:
            break;

        // ... A case for each known opcode ...

        case EXTENDED_ARG:
            word = *next_instr;
            opcode = _Py_OPCODE(word);
            oparg *= 256;
            oparg += _Py_OPARG(word);
            next_instr++;
            goto dispatch_opcode;

        default:
            PyErr_SetString(PyExc_SystemError, "unknown opcode");
            return NULL;
        }
    }

Jumps
=====

Note that in the switch statement, ``next_instr`` (the "instruction offset") already points to the next instruction.
Thus, jump instructions can be implemented by manipulating ``next_instr``:

- An absolute jump (``JUMP_ABSOLUTE``) sets ``next_instr = first_instr + oparg``.
- A relative jump forward (``JUMP_FORWARD``) sets ``next_instr += oparg``.
- A relative jump backward sets ``next_instr -= oparg``.

A relative jump whose ``oparg`` is zero is a no-op.

Inline cache entries
====================

Some (usually specialized) instructions have an associated "inline cache".
The inline cache consists of one or more two-byte entries included in the bytecode array.
The size of the inline cache for a particular instruction is fixed by its ``opcode`` alone.
Cache entries are reserved by the compiler and initialized with zeros.
If an instruction has an inline cache, the layout of its cache can be described by a ``struct`` definition and the address of the cache is given by casting ``next_instr`` to a pointer to the cache ``struct``.
The size of such a ``struct`` must be independent of the machine architecture and word size.
Even though inline cache entries are represented by code units, they do not have to conform to the ``opcode``/``oparg`` format.

The instruction implementation is responsible for advancing ``next_instr`` past the inline cache.
For example, if an instruction's inline cache is four bytes (two code units) in size, the code for the instruction must contain ``next_instr += 2;``.
This is equivalent to a relative forward jump by that many code units.

Serializing non-zero cache entries would present a problem because the serialization (``marshal``) format must be independent of the machine byte order.

More information about the use of inline caches can be found in :pep:`659` (search for "ancillary data").

The evaluation stack
====================

Apart from unconditional jumps, almost all instructions read or write some data in the form of object references (``PyObject *``).
The CPython bytecode interpreter is a stack machine, meaning that it operates by pushing data onto and popping it off the stack.
For example, the "add" instruction (which used to be called ``BINARY_ADD`` but is now ``BINARY_OP 0``) pops two objects off the stack and pushes the result back onto the stack.
An interesting property of the CPython bytecode interpreter is that the stack size required to evaluate a given function is known in advance.
The stack size is computed by the bytecode compiler and is stored in ``code->co_stacksize``.
The interpreter uses this information to allocate stack.

The stack grows up in memory; the operation ``PUSH(x)`` is equivalent to ``*stack_pointer++ = x``, whereas ``x = POP()`` means ``x = *--stack_pointer``.
There is no overflow or underflow check (except when compiled in debug mode) -- it would be too expensive, so we really trust the compiler.

At any point during execution, the stack level is knowable based on the instruction pointer alone, and some properties of each item on the stack are also known.
In particular, only a few instructions may push a ``NULL`` onto the stack, and the positions that may be ``NULL`` are known.
A few other instructions (``GET_ITER``, ``FOR_ITER``) push or pop an object that is known to be an interator.

Do not confuse the evaluation stack with the call stack, which is used to implement calling and returning from functions.

Error handling
==============

When an instruction like encounters an error, an exception is raised.
At this point a traceback entry is added to the exception (by ``PyTraceBack_Here()``) and cleanup is performed.
In the simplest case (absent any ``try`` blocks) this results in the remaining objects being popped off the evaluation stack and their reference count (if not ``NULL``) decremented.
Then the interpreter function (``_PyEval_EvalFrameDefault()``) returns ``NULL``.

However, if an exception is raised in a ``try`` block, the interpreter must jump to the corresponding ``except`` or ``finally`` block.
In 3.10 and before there was a separate "block stack" which was used to keep track of nesting ``try`` blocks.
In 3.11 this mechanism has been replaced by a statically generated table, `code->co_exceptiontable``.
The advantage of this approach is that entering and leaving a ``try`` block normally does not execute any code, making execution faster.
But of course the table needs to be generated by the compiler, and decoded (by ``get_exception_handler``) when an exception happens.

Exception table format
----------------------

The table is conceptually a list of records, each containing four variable-length integer fields (in a unique format, see below):

- start: start of `try` block, in code units from the start of the bytecode
- length: size of the `try` block, in code units
- target: start of the first instruction of the `except` or `finally` block, in code units from the start of the bytecode
- depth_and_lasti: the low bit gives the "lasti" flag, the remaining bits give the stack depth

The stack depth is used to clean up evaluation stack entries above this depth.
The "lasti" flag indicates whether, after stack cleanup, the instruction offset of the raising instruction should be pushed.
For more information on the design, see the file ``Objects/exception_handling_notes.txt``.

Each varint is encoded as one or more bytes.
The high bit (bit 7) is reserved for random access -- it is set for the first varint of a record.
The second bit (bit 6) indicates whether this is the last byte or not -- it is set for all but the last bytes of a varint.
The low 6 bits (bits 0-5) are used for the integer value, in big-endian order.

To find the table entry (if any) for a given instruction offset, we can use bisection without decoding the whole table.
We bisect the raw bytes, at each probe finding the start of the record by scanning back for a byte with the high bit set, and then decode the first varint.
See ``get_exception_handler()`` for the exact code (like all bisection algorithms, the code is a bit subtle).

The locations table
-------------------

Whenever an exception is raised, we add a traceback entry to the exception.
The ``tb_lineno`` field of a traceback entry must be set to the line number of the instruction that raised it.
This field is computed from the locations table, ``co_linetable`` (this name is an understatement), using ``PyCode_Addr2Line()``.
This table has an entry for every instruction rather than for every ``try`` block, so a compact format is very important.

The full design of the 3.11 locations table is written up in ``Objects/locations.md``.
While there are rumors that this file is slightly out of date, it is still the best reference we have.
Don't be confused by ``lnotab_notes.txt``, which describes the 3.10 format.
For backwards compatibility this format is still supported by the ``co_lnotab`` property.

The 3.11 location table format is different because it stores not just the starting line number for each instruction, but also the end line number, *and* the start and end column numbers.
Note that traceback objects don't store all this information -- they store the start line number, for backward compatibility, and the "last instruction" value.
The rest can be computed from the last instruction (``tb_lasti``) with the help of the locations table.
For Python code, a convenient method exists, ``co_positions()``, which returns an iterator of *(line, endline, column, endcolumn)* tuples, one per instruction.
There is also ``co_lines()`` which returns an interator of *(start, end, line)* tuples, where *start* and *end* are bytecode offsets.
The latter is described by :pep:`626`.
It is more compact, but doesn't return end line numbers or column offsets.
For C code, you have to call ``PyCode_Addr2Location()``.

Fortunately, the locations table is only consulted by exception handling (to set ``tb_lineno``) and by tracing (to pass the line number to the tracing function).
In order to reduce the overhead during tracing, the mapping from instruction offset to linenumber is cached in the ``_co_linearray`` field.

XXX exception chaining
----------------------

Python-to-Python calls
======================

The ``_PyEval_EvalFrameDefault()`` function is recursive, because sometimes the interpreter calls some C function that calls back into the interpreter.
In 3.10 and before this was the case even when a Python function called another Python function:
The ``CALL`` instruction would call the ``tp_call`` dispatch function of the callee, which would extract the code object, create a new frame for the call stack, and then call back into the interpreter.
This approach is very general but consumes several C stack frames for each nested Python call, thereby increasing the risk of an (unrecoverable) C stack overflow.

In 3.11 the ``CALL`` instruction special-cases function objects to "inline" the call.
When a call gets inlined, a new frame gets pushed onto the call stack and the interpreter "jumps" to the start of the callee's bytecode.
When the callee executes a ``RETURN_VALUE`` instruction, the frame is popped off the call stack and the interpreter returns to the caller.
There is a flag in the frame (``frame->is_entry``) that indicates whether the frame was inlined.
If ``RETURN_VALUE`` returns to a caller where this flag is set, it performs the usual cleanup and return from ``_PyEval_EvalFrameDefault()``.

A similar check is performed when an unhandled exception occurs.

The call stack
==============

XXX Also frame layout and use, locals "plus"

All sorts of variables
======================

The bytecode compiler determines for each variable name in which scope it is defined and generates instructions accordingly.
For example, loading a local variable onto the stack is done using ``LOAD_FAST``, while loading a global is done using ``LOAD_GLOBAL``.
The key types of variables are:
- fast locals: used in functions
- (slow or regular) locals: used in classes and at the top level
- globals and builtins: the compiler does not distinguish between globals and builtins (though the specializing interpreter does)
- cells -- used for nonlocal references

XXX More

XXX Getting variable names

XXX More
========

- co_consts, co_names, co_varnames, and their ilk
- How calls work (how args are transferred, return, exceptions)
- Generators, async functions, async generators, and ``yield from`` (next, send, throw, close; and await; and how this code breaks the interpreter abstraction)
- Eval breaker (interrupts, GIL)
- Tracing
- Setting the current lineno (debugger-induced jumps)
- Specialization, inline caches etc.
