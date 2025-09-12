.. highlight:: c

.. _clinic:

***************
Argument Clinic
***************

:author: Larry Hastings

**Source code:** :cpy-file:`Tools/clinic/clinic.py`.

Argument Clinic is a preprocessor for CPython C files.
It was introduced in Python 3.4 with :pep:`436`,
in order to provide introspection signatures,
and to generate performant and tailor-made boilerplate code
for argument parsing in CPython builtins, module level functions, and class methods.
This document is divided in four major sections:

* :ref:`clinic-background` talks about the basic concepts and goals of Argument Clinic.
* :ref:`clinic-reference` describes the command-line interface and Argument Clinic terminology.
* :ref:`clinic-tutorial` guides you through all the steps required to adapt an existing C function to Argument Clinic.
* :ref:`clinic-howtos` details how to handle specific tasks.

.. toctree::
   :maxdepth: 2
   :hidden:

   tutorial
   howto

.. note::

  Argument Clinic is considered internal-only
  for CPython.  Its use is not supported for files outside
  CPython, and no guarantees are made regarding backwards
  compatibility for future versions.  In other words: if you
  maintain an external C extension for CPython, you're welcome
  to experiment with Argument Clinic in your own code.  But the
  version of Argument Clinic that ships with the next version
  of CPython *could* be totally incompatible and break all your code.


.. _clinic-background:

Background
==========

Basic concepts
--------------

When Argument Clinic is run on a file, either via the :ref:`clinic-cli`
or via ``make clinic``, it will scan over the input files looking for
:term:`start lines <start line>`:

.. code-block:: none

    /*[clinic input]

When it finds one, it reads everything up to the :term:`end line`:

.. code-block:: none

    [clinic start generated code]*/

Everything in between these two lines is Argument Clinic :term:`input`.
When Argument Clinic parses input, it generates :term:`output`.
The output is rewritten into the C file immediately after the input,
followed by a :term:`checksum line`.
All of these lines, including the :term:`start line` and :term:`checksum line`,
are collectively called an Argument Clinic :term:`block`:

.. code-block:: none

    /*[clinic input]
    ... clinic input goes here ...
    [clinic start generated code]*/
    ... clinic output goes here ...
    /*[clinic end generated code: ...]*/

If you run Argument Clinic on the same file a second time, Argument Clinic
will discard the old :term:`output` and write out the new output with a fresh
:term:`checksum line`.
If the :term:`input` hasn't changed, the output won't change either.

.. note::

   You should never modify the output of an Argument Clinic block,
   as any change will be lost in future Argument Clinic runs;
   Argument Clinic will detect an output checksum mismatch and regenerate the
   correct output.
   If you are not happy with the generated output,
   you should instead change the input until it produces the output you want.


.. _clinic-reference:

Reference
=========


.. _clinic-terminology:

Terminology
-----------

.. glossary::

   start line
      The line ``/*[clinic input]``.
      This line marks the beginning of Argument Clinic input.
      Note that the *start line* opens a C block comment.

   end line
      The line ``[clinic start generated code]*/``.
      The *end line* marks the *end* of Argument Clinic :term:`input`,
      but at the same time marks the *start* of Argument Clinic :term:`output`,
      thus the text *"clinic start start generated code"*
      Note that the *end line* closes the C block comment opened
      by the *start line*.

   checksum
      A hash to distinguish unique :term:`inputs <input>`
      and :term:`outputs <output>`.

   checksum line
      A line that looks like ``/*[clinic end generated code: ...]*/``.
      The three dots will be replaced by a :term:`checksum` generated from the
      :term:`input`, and a :term:`checksum` generated from the :term:`output`.
      The checksum line marks the end of Argument Clinic generated code,
      and is used by Argument Clinic to determine if it needs to regenerate
      output.

   input
      The text between the :term:`start line` and the :term:`end line`.
      Note that the start and end lines open and close a C block comment;
      the *input* is thus a part of that same C block comment.

   output
      The text between the :term:`end line` and the :term:`checksum line`.

   block
      All text from the :term:`start line` to the :term:`checksum line` inclusively.


.. _clinic-cli:

Command-line interface
----------------------

The Argument Clinic :abbr:`CLI (Command-Line Interface)` is typically used to
process a single source file, like this:

.. code-block:: shell-session

    $ python3 ./Tools/clinic/clinic.py foo.c

The CLI supports the following options:

.. program:: ./Tools/clinic/clinic.py [-h] [-f] [-o OUTPUT] [-v] \
             [--converters] [--make] [--srcdir SRCDIR] [--limited] [FILE ...]

.. option:: -h, --help

   Print CLI usage.

.. option:: -f, --force

   Force output regeneration.

.. option:: -o, --output OUTPUT

   Redirect file output to OUTPUT

.. option:: -v, --verbose

   Enable verbose mode.

.. option:: --converters

   Print a list of all supported converters and return converters.

.. option:: --make

   Walk :option:`--srcdir` to run over all relevant files.

.. option:: --srcdir SRCDIR

   The directory tree to walk in :option:`--make` mode.

.. option:: --exclude EXCLUDE

   A file to exclude in :option:`--make` mode.
   This option can be given multiple times.

.. option:: --limited

    Use the :ref:`Limited API <limited-c-api>` to parse arguments in the generated C code.
    See :ref:`clinic-howto-limited-capi`.

.. option:: FILE ...

   The list of files to process.


.. _clinic-classes:

Classes for extending Argument Clinic
-------------------------------------

.. module:: clinic

.. class:: CConverter

   The base class for all converters.
   See :ref:`clinic-howto-custom-converter` for how to subclass this class.

   .. attribute:: type

      The C type to use for this variable.
      :attr:`!type` should be a Python string specifying the type,
      for example, ``'int'``.
      If this is a pointer type, the type string should end with ``' *'``.

   .. attribute:: default

      The Python default value for this parameter, as a Python value.
      Or the magic value ``unspecified`` if there is no default.

   .. attribute:: py_default

      :attr:`!default` as it should appear in Python code,
      as a string.
      Or ``None`` if there is no default.

   .. attribute:: c_default

      :attr:`!default` as it should appear in C code,
      as a string.
      Or ``None`` if there is no default.

   .. attribute:: c_ignored_default

      The default value used to initialize the C variable when
      there is no default, but not specifying a default may
      result in an "uninitialized variable" warning.  This can
      easily happen when using option groups—although
      properly written code will never actually use this value,
      the variable does get passed in to the impl, and the
      C compiler will complain about the "use" of the
      uninitialized value.  This value should always be a
      non-empty string.

   .. attribute:: converter

      The name of the C converter function, as a string.

   .. attribute:: impl_by_reference

      A boolean value.  If true,
      Argument Clinic will add a ``&`` in front of the name of
      the variable when passing it into the impl function.

   .. attribute:: parse_by_reference

      A boolean value.  If true,
      Argument Clinic will add a ``&`` in front of the name of
      the variable when passing it into :c:func:`PyArg_ParseTuple`.
