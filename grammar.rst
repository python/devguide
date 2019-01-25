.. _grammar:

Changing CPython's Grammar
==========================

Abstract
--------

There's more to changing Python's grammar than editing
:file:`Grammar/Grammar`.  This document aims to be a
checklist of places that must also be fixed.

It is probably incomplete.  If you see omissions,  submit a bug or patch.

This document is not intended to be an instruction manual on Python
grammar hacking, for several reasons.


Rationale
---------

People are getting this wrong all the time; it took well over a
year before someone `noticed <https://bugs.python.org/issue676521>`_
that adding the floor division
operator (``//``) broke the :mod:`parser` module.


Checklist
---------

Note: sometimes things mysteriously don't work.  Before giving up, try ``make clean``.

* :file:`Grammar/Grammar`: OK, you'd probably worked this one out. :-)  After changing
  it, run ``make regen-grammar``, to regenerate :file:`Include/graminit.h` and
  :file:`Python/graminit.c`.  (This runs Python's parser generator, ``Python/pgen``.

* :file:`Grammar/Tokens` is a place for adding new token types.  After
  changing it, run ``make regen-token`` to regenerate :file:`Include/token.h`,
  :file:`Parser/token.c`, :file:`Lib/token.py` and
  :file:`Doc/library/token-list.inc`.  If you change both ``Grammar`` and ``Tokens``,
  run ``make regen-tokens`` before ``make regen-grammar``.

* :file:`Parser/Python.asdl` may need changes to match the Grammar.  Then run ``make
  regen-ast`` to regenerate :file:`Include/Python-ast.h` and :file:`Python/Python-ast.c`.

* :file:`Parser/tokenizer.c` contains the tokenization code.  This is where you would
  add a new type of comment or string literal, for example.

* :file:`Python/ast.c` will need changes to create the AST objects involved with the
  Grammar change.

* The :doc:`compiler` has its own page.

* The :mod:`parser` module.  Add some of your new syntax to ``test_parser``,
  bang on :file:`Modules/parsermodule.c` until it passes.

* Add some usage of your new syntax to ``test_grammar.py``.

* Certain changes may require tweaks to the library module :mod:`pyclbr`.

* :file:`Lib/tokenize.py` needs changes to match changes to the tokenizer.

* :file:`Lib/lib2to3/Grammar.txt` may need changes to match the Grammar.

* Documentation must be written!
