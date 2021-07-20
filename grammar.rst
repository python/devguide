.. _grammar:

Changing CPython's Grammar
==========================

Abstract
--------

There's more to changing Python's grammar than editing
:file:`Grammar/python.gram`.  Here's a checklist.

NOTE: These instructions are for Python 3.9 and beyond.  Earlier
versions use a different parser technology.  You probably shouldn't
try to change the grammar of earlier Python versions, but if you
really want to, use GitHub to track down the earlier version of this
file in the devguide.  (Python 3.9 itself actually supports both
parsers; the old parser can be invoked by passing ``-X oldparser``.)


Checklist
---------

Note: sometimes things mysteriously don't work.  Before giving up, try ``make clean``.

* :file:`Grammar/python.gram`: The grammar, with actions that build AST nodes.  After changing
  it, run ``make regen-pegen`` (or ``build.bat --regen`` on Windows), to
  regenerate :file:`Parser/parser.c`.
  (This runs Python's parser generator, ``Tools/peg_generator``).

* :file:`Grammar/Tokens` is a place for adding new token types.  After
  changing it, run ``make regen-token`` to regenerate :file:`Include/token.h`,
  :file:`Parser/token.c`, :file:`Lib/token.py` and
  :file:`Doc/library/token-list.inc`.  If you change both ``python.gram`` and ``Tokens``,
  run ``make regen-token`` before ``make regen-pegen``. On Windows,
  ``build.bat --regen`` will regenerate both at the same time.

* :file:`Parser/Python.asdl` may need changes to match the grammar.  Then run ``make
  regen-ast`` to regenerate :file:`Include/Python-ast.h` and :file:`Python/Python-ast.c`.

* :file:`Parser/tokenizer.c` contains the tokenization code.  This is where you would
  add a new type of comment or string literal, for example.

* :file:`Python/ast.c` will need changes to validate AST objects involved with the
  grammar change.

* :file:`Python/ast_unparse.c` will need changes to unparse AST objects involved with the
  grammar change ("unparsing" is used to turn annotations into strings per :pep:`563`).

* The :doc:`compiler` has its own page.

* ``_Unparser`` in the :file:`Lib/ast.py` file may need changes to accommodate
  any modifications in the AST nodes.

* :file:`Doc/library/ast.rst` may need to be updated to reflect changes to AST nodes.

* Add some usage of your new syntax to ``test_grammar.py``.

* Certain changes may require tweaks to the library module :mod:`pyclbr`.

* :file:`Lib/tokenize.py` needs changes to match changes to the tokenizer.

* Documentation must be written! Specifically, one or more of the pages in
  :file:`Doc/reference/` will need to be updated.
