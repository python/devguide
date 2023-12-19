.. _grammar:

==========================
Changing CPython's grammar
==========================

Abstract
========

There's more to changing Python's grammar than editing
:cpy-file:`Grammar/python.gram`.  Here's a checklist.

.. note::
    These instructions are for Python 3.9 and beyond.  Earlier
    versions use a different parser technology.  You probably shouldn't
    try to change the grammar of earlier Python versions, but if you
    really want to, use GitHub to track down the earlier version of this
    file in the devguide.

For more information on how to use the new parser, check the
:ref:`section on how to use CPython's parser <parser>`.

Checklist
=========

Note: sometimes things mysteriously don't work.  Before giving up, try ``make clean``.

* :cpy-file:`Grammar/python.gram`: The grammar, with actions that build AST nodes.
  After changing it, run ``make regen-pegen`` (or ``build.bat --regen`` on Windows),
  to regenerate :cpy-file:`Parser/parser.c`.
  (This runs Python's parser generator, :cpy-file:`Tools/peg_generator`).

* :cpy-file:`Grammar/Tokens` is a place for adding new token types.  After
  changing it, run ``make regen-token`` to regenerate
  :cpy-file:`Include/internal/pycore_token.h`, :cpy-file:`Parser/token.c`,
  :cpy-file:`Lib/token.py` and :cpy-file:`Doc/library/token-list.inc`.
  If you change both ``python.gram`` and ``Tokens``,
  run ``make regen-token`` before ``make regen-pegen``.
  On Windows, ``build.bat --regen`` will regenerate both at the same time.

* :cpy-file:`Parser/Python.asdl` may need changes to match the grammar.
  Then run ``make regen-ast`` to regenerate
  :cpy-file:`Include/internal/pycore_ast.h` and :cpy-file:`Python/Python-ast.c`.

* :cpy-file:`Parser/lexer/` contains the tokenization code.
  This is where you would add a new type of comment or string literal, for example.

* :cpy-file:`Python/ast.c` will need changes to validate AST objects
  involved with the grammar change.

* :cpy-file:`Python/ast_unparse.c` will need changes to unparse AST
  involved with the grammar change ("unparsing" is used to turn annotations
  into strings per :pep:`563`).

* The :ref:`compiler` has its own page.

* ``_Unparser`` in the :cpy-file:`Lib/ast.py` file may need changes
  to accommodate any modifications in the AST nodes.

* :cpy-file:`Doc/library/ast.rst` may need to be updated to reflect changes
  to AST nodes.

* Add some usage of your new syntax to ``test_grammar.py``.

* Certain changes may require tweaks to the library module :mod:`pyclbr`.

* :cpy-file:`Lib/tokenize.py` needs changes to match changes to the tokenizer.

* Documentation must be written! Specifically, one or more of the pages in
  :cpy-file:`Doc/reference/` will need to be updated.
