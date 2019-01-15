.. _grammar:

Changing CPython's Grammar
==========================

Abstract
--------

There's more to changing Python's grammar than editing
:file:`Grammar/Grammar` and :file:`Python/compile.c`.  This document aims to be a
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

* :file:`Grammar/Grammar`: OK, you'd probably worked this one out :)

* :file:`Grammar/Tokens` is a place for adding new token types.  After
  changing it, run '``make regen-token``' to regenerate :file:`Include/token.h`,
  :file:`Parser/token.c`, :file:`Lib/token.py` and
  :file:`Doc/library/token-list.inc`.

* :file:`Parser/Python.asdl` may need changes to match the Grammar.  Then run '``make
  regen-ast``' to regenerate :file:`Include/Python-ast.h` and :file:`Python/Python-ast.c`.

* :file:`Python/ast.c` will need changes to create the AST objects involved with the
  Grammar change.

* :file:`Parser/pgen` needs to be rerun to regenerate :file:`Include/graminit.h` and
  :file:`Python/graminit.c`. ('``make regen-grammar``' should handle this for you.)

* :file:`Python/symtable.c`: This handles the symbol collection pass
  that happens immediately before the compilation pass.

* :file:`Python/compile.c`: You will need to create or modify the
  ``compiler_*`` functions to generate opcodes for your productions.

* You may need to regenerate :file:`Lib/symbol.py`
  and/or :file:`Lib/keyword.py`.

* The :mod:`parser` module.  Add some of your new syntax to ``test_parser``,
  bang on :file:`Modules/parsermodule.c` until it passes.

* Add some usage of your new syntax to ``test_grammar.py``.

* If you've gone so far as to change the token structure of
  Python, then the :file:`Lib/tokenizer.py` library module will need to be changed.

* Certain changes may require tweaks to the library module :mod:`pyclbr`.

* :file:`Lib/lib2to3/Grammar.txt` may need changes to match the Grammar.

* Documentation must be written!

* After everything has been checked in, you're likely to see a new
  change to :file:`Python/Python-ast.c`.  This is because this
  (generated) file contains the git version of the source from
  which it was generated.  There's no way to avoid this; you just
  have to submit this file separately.
