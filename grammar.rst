.. _grammar:

Changing CPython's Grammar
==========================

Abstract
--------

There's more to changing Python's grammar than editing
Grammar/Grammar and Python/compile.c.  This document aims to be a
checklist of places that must also be fixed.

It is probably incomplete.  If you see omissions,  submit a bug or patch.

This document is not intended to be an instruction manual on Python
grammar hacking, for several reasons.


Rationale
---------

People are getting this wrong all the time; it took well over a
year before someone `noticed <http://bugs.python.org/issue676521>`_
that adding the floor division
operator (//) broke the parser module.


Checklist
---------

* Grammar/Grammar: OK, you'd probably worked this one out :)

* Parser/Python.asdl may need changes to match the Grammar.  Run make to
  regenerate Include/Python-ast.h and Python/Python-ast.c.

* Python/ast.c will need changes to create the AST objects involved with the
  Grammar change.

* Parser/pgen needs to be rerun to regenerate Include/graminit.h and
  Python/graminit.c. (make should handle this for you.)

* Python/symtable.c: This handles the symbol collection pass
  that happens immediately before the compilation pass.

* Python/compile.c: You will need to create or modify the
  compiler_* functions to generate opcodes for your productions.

* You may need to regenerate Lib/symbol.py and/or Lib/token.py
  and/or Lib/keyword.py.

* The parser module.  Add some of your new syntax to test_parser,
  bang on Modules/parsermodule.c until it passes.

* Add some usage of your new syntax to test_grammar.py

* If you've gone so far as to change the token structure of
  Python, then the Lib/tokenizer.py library module will need to be changed.

* Certain changes may require tweaks to the library module pyclbr.

* Documentation must be written!

* After everything has been checked in, you're likely to see a new
  change to Python/Python-ast.c.  This is because this
  (generated) file contains the hg version of the source from
  which it was generated.  There's no way to avoid this; you just
  have to submit this file separately.
