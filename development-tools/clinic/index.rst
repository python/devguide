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


.. _clinic-tutorial:

Tutorial
========

The best way to get a sense of how Argument Clinic works is to
convert a function to work with it.  Here, then, are the bare
minimum steps you'd need to follow to convert a function to
work with Argument Clinic.  Note that for code you plan to
check in to CPython, you really should take the conversion farther,
using some of the :ref:`advanced concepts <clinic-howtos>`
you'll see later on in the document,
like :ref:`clinic-howto-return-converters`
and :ref:`clinic-howto-self-converter`.
But we'll keep it simple for this walkthrough so you can learn.

First, make sure you're working with a freshly updated checkout
of the CPython trunk.

Next, find a Python builtin that calls either :c:func:`PyArg_ParseTuple`
or :c:func:`PyArg_ParseTupleAndKeywords`, and hasn't been converted
to work with Argument Clinic yet.
For this tutorial, we'll be using
:py:meth:`_pickle.Pickler.dump <pickle.Pickler.dump>`.

If the call to the :c:func:`!PyArg_Parse*` function uses any of the
following format units...:

.. code-block:: none

   O&
   O!
   es
   es#
   et
   et#

... or if it has multiple calls to :c:func:`PyArg_ParseTuple`,
you should choose a different function.
(See :ref:`clinic-howto-advanced-converters` for those scenarios.)

Also, if the function has multiple calls to :c:func:`!PyArg_ParseTuple`
or :c:func:`PyArg_ParseTupleAndKeywords` where it supports different
types for the same argument, or if the function uses something besides
:c:func:`!PyArg_Parse*` functions to parse its arguments, it probably
isn't suitable for conversion to Argument Clinic.  Argument Clinic
doesn't support generic functions or polymorphic parameters.

Next, add the following boilerplate above the function,
creating our input block::

    /*[clinic input]
    [clinic start generated code]*/

Cut the docstring and paste it in between the ``[clinic]`` lines,
removing all the junk that makes it a properly quoted C string.
When you're done you should have just the text, based at the left
margin, with no line wider than 80 characters.
Argument Clinic will preserve indents inside the docstring.

If the old docstring had a first line that looked like a function
signature, throw that line away; The docstring doesn't need it anymore ---
when you use :py:func:`help` on your builtin in the future,
the first line will be built automatically based on the function's signature.

Example docstring summary line::

   /*[clinic input]
   Write a pickled representation of obj to the open file.
   [clinic start generated code]*/

If your docstring doesn't have a "summary" line, Argument Clinic will
complain, so let's make sure it has one.  The "summary" line should
be a paragraph consisting of a single 80-column line
at the beginning of the docstring.
(See :pep:`257` regarding docstring conventions.)

Our example docstring consists solely of a summary line, so the sample
code doesn't have to change for this step.

Now, above the docstring, enter the name of the function, followed
by a blank line.  This should be the Python name of the function,
and should be the full dotted path to the function ---
it should start with the name of the module,
include any sub-modules, and if the function is a method on
a class it should include the class name too.

In our example, :mod:`!_pickle` is the module, :py:class:`!Pickler` is the class,
and :py:meth:`!dump` is the method, so the name becomes
:py:meth:`!_pickle.Pickler.dump`::

   /*[clinic input]
   _pickle.Pickler.dump

   Write a pickled representation of obj to the open file.
   [clinic start generated code]*/

If this is the first time that module or class has been used with Argument
Clinic in this C file,
you must declare the module and/or class.  Proper Argument Clinic hygiene
prefers declaring these in a separate block somewhere near the
top of the C file, in the same way that include files and statics go at
the top.
In our sample code we'll just show the two blocks next to each other.

The name of the class and module should be the same as the one
seen by Python.  Check the name defined in the :c:type:`PyModuleDef`
or :c:type:`PyTypeObject` as appropriate.

When you declare a class, you must also specify two aspects of its type
in C: the type declaration you'd use for a pointer to an instance of
this class, and a pointer to the :c:type:`!PyTypeObject` for this class::

   /*[clinic input]
   module _pickle
   class _pickle.Pickler "PicklerObject *" "&Pickler_Type"
   [clinic start generated code]*/

   /*[clinic input]
   _pickle.Pickler.dump

   Write a pickled representation of obj to the open file.
   [clinic start generated code]*/

Declare each of the parameters to the function.  Each parameter
should get its own line.  All the parameter lines should be
indented from the function name and the docstring.
The general form of these parameter lines is as follows:

.. code-block:: none

    name_of_parameter: converter

If the parameter has a default value, add that after the
converter:

.. code-block:: none

    name_of_parameter: converter = default_value

Argument Clinic's support for "default values" is quite sophisticated;
see :ref:`clinic-howto-default-values` for more information.

Next, add a blank line below the parameters.

What's a "converter"?
It establishes both the type of the variable used in C,
and the method to convert the Python value into a C value at runtime.
For now you're going to use what's called a "legacy converter" ---
a convenience syntax intended to make porting old code into Argument
Clinic easier.

For each parameter, copy the "format unit" for that
parameter from the :c:func:`PyArg_Parse` format argument and
specify *that* as its converter, as a quoted string.
The "format unit" is the formal name for the one-to-three
character substring of the *format* parameter that tells
the argument parsing function what the type of the variable
is and how to convert it.
For more on format units please see :ref:`arg-parsing`.

For multicharacter format units like ``z#``,
use the entire two-or-three character string.

Sample::

   /*[clinic input]
   module _pickle
   class _pickle.Pickler "PicklerObject *" "&Pickler_Type"
   [clinic start generated code]*/

   /*[clinic input]
   _pickle.Pickler.dump

       obj: 'O'

   Write a pickled representation of obj to the open file.
   [clinic start generated code]*/

If your function has ``|`` in the format string,
meaning some parameters have default values, you can ignore it.
Argument Clinic infers which parameters are optional
based on whether or not they have default values.

If your function has ``$`` in the format string,
meaning it takes keyword-only arguments,
specify ``*`` on a line by itself before the first keyword-only argument,
indented the same as the parameter lines.

:py:meth:`!_pickle.Pickler.dump` has neither, so our sample is unchanged.

Next, if the existing C function calls :c:func:`PyArg_ParseTuple`
(as opposed to :c:func:`PyArg_ParseTupleAndKeywords`), then all its
arguments are positional-only.

To mark parameters as positional-only in Argument Clinic,
add a ``/`` on a line by itself after the last positional-only parameter,
indented the same as the parameter lines.

Sample::

   /*[clinic input]
   module _pickle
   class _pickle.Pickler "PicklerObject *" "&Pickler_Type"
   [clinic start generated code]*/

   /*[clinic input]
   _pickle.Pickler.dump

       obj: 'O'
       /

   Write a pickled representation of obj to the open file.
   [clinic start generated code]*/

It can be helpful to write a per-parameter docstring for each parameter.
Since per-parameter docstrings are optional,
you can skip this step if you prefer.

Nevertheless, here's how to add a per-parameter docstring.
The first line of the per-parameter docstring
must be indented further than the parameter definition.
The left margin of this first line establishes
the left margin for the whole per-parameter docstring;
all the text you write will be outdented by this amount.
You can write as much text as you like, across multiple lines if you wish.

Sample::

   /*[clinic input]
   module _pickle
   class _pickle.Pickler "PicklerObject *" "&Pickler_Type"
   [clinic start generated code]*/

   /*[clinic input]
   _pickle.Pickler.dump

       obj: 'O'
           The object to be pickled.
       /

   Write a pickled representation of obj to the open file.
   [clinic start generated code]*/

Save and close the file, then run ``Tools/clinic/clinic.py`` on it.
With luck everything worked---your block now has output,
and a :file:`.c.h` file has been generated!
Reload the file in your text editor to see the generated code::

   /*[clinic input]
   _pickle.Pickler.dump

       obj: 'O'
           The object to be pickled.
       /

   Write a pickled representation of obj to the open file.
   [clinic start generated code]*/

   static PyObject *
   _pickle_Pickler_dump(PicklerObject *self, PyObject *obj)
   /*[clinic end generated code: output=87ecad1261e02ac7 input=552eb1c0f52260d9]*/

Obviously, if Argument Clinic didn't produce any output,
it's because it found an error in your input.
Keep fixing your errors and retrying until Argument Clinic processes your file
without complaint.

For readability, most of the glue code has been generated to a :file:`.c.h`
file.  You'll need to include that in your original :file:`.c` file,
typically right after the clinic module block::

   #include "clinic/_pickle.c.h"

Double-check that the argument-parsing code Argument Clinic generated
looks basically the same as the existing code.

First, ensure both places use the same argument-parsing function.
The existing code must call either
:c:func:`PyArg_ParseTuple` or :c:func:`PyArg_ParseTupleAndKeywords`;
ensure that the code generated by Argument Clinic calls the
*exact* same function.

Second, the format string passed in to :c:func:`!PyArg_ParseTuple` or
:c:func:`!PyArg_ParseTupleAndKeywords` should be *exactly* the same
as the hand-written one in the existing function,
up to the colon or semi-colon.

Argument Clinic always generates its format strings
with a ``:`` followed by the name of the function.
If the existing code's format string ends with ``;``,
to provide usage help, this change is harmless --- don't worry about it.

Third, for parameters whose format units require two arguments,
like a length variable, an encoding string, or a pointer
to a conversion function, ensure that the second argument is
*exactly* the same between the two invocations.

Fourth, inside the output portion of the block,
you'll find a preprocessor macro defining the appropriate static
:c:type:`PyMethodDef` structure for this builtin::

   #define __PICKLE_PICKLER_DUMP_METHODDEF    \
   {"dump", (PyCFunction)__pickle_Pickler_dump, METH_O, __pickle_Pickler_dump__doc__},

This static structure should be *exactly* the same as the existing static
:c:type:`!PyMethodDef` structure for this builtin.

If any of these items differ in *any way*,
adjust your Argument Clinic function specification and rerun
``Tools/clinic/clinic.py`` until they *are* the same.

Notice that the last line of its output is the declaration
of your "impl" function.  This is where the builtin's implementation goes.
Delete the existing prototype of the function you're modifying, but leave
the opening curly brace.  Now delete its argument parsing code and the
declarations of all the variables it dumps the arguments into.
Notice how the Python arguments are now arguments to this impl function;
if the implementation used different names for these variables, fix it.

Let's reiterate, just because it's kind of weird.
Your code should now look like this::

   static return_type
   your_function_impl(...)
   /*[clinic end generated code: input=..., output=...]*/
   {
   ...

Argument Clinic generated the checksum line and the function prototype just
above it.  You should write the opening and closing curly braces for the
function, and the implementation inside.

Sample::

   /*[clinic input]
   module _pickle
   class _pickle.Pickler "PicklerObject *" "&Pickler_Type"
   [clinic start generated code]*/
   /*[clinic end generated code: checksum=da39a3ee5e6b4b0d3255bfef95601890afd80709]*/

   /*[clinic input]
   _pickle.Pickler.dump

       obj: 'O'
           The object to be pickled.
       /

   Write a pickled representation of obj to the open file.
   [clinic start generated code]*/

   PyDoc_STRVAR(__pickle_Pickler_dump__doc__,
   "Write a pickled representation of obj to the open file.\n"
   "\n"
   ...
   static PyObject *
   _pickle_Pickler_dump_impl(PicklerObject *self, PyObject *obj)
   /*[clinic end generated code: checksum=3bd30745bf206a48f8b576a1da3d90f55a0a4187]*/
   {
       /* Check whether the Pickler was initialized correctly (issue3664).
          Developers often forget to call __init__() in their subclasses, which
          would trigger a segfault without this check. */
       if (self->write == NULL) {
           PyErr_Format(PicklingError,
                        "Pickler.__init__() was not called by %s.__init__()",
                        Py_TYPE(self)->tp_name);
           return NULL;
       }

       if (_Pickler_ClearBuffer(self) < 0) {
           return NULL;
       }

       ...

Remember the macro with the :c:type:`PyMethodDef` structure for this function?
Find the existing :c:type:`!PyMethodDef` structure for this
function and replace it with a reference to the macro.  If the builtin
is at module scope, this will probably be very near the end of the file;
if the builtin is a class method, this will probably be below but relatively
near to the implementation.

Note that the body of the macro contains a trailing comma; when you
replace the existing static :c:type:`!PyMethodDef` structure with the macro,
*don't* add a comma to the end.

Sample::

   static struct PyMethodDef Pickler_methods[] = {
       __PICKLE_PICKLER_DUMP_METHODDEF
       __PICKLE_PICKLER_CLEAR_MEMO_METHODDEF
       {NULL, NULL}                /* sentinel */
   };

Argument Clinic may generate new instances of ``_Py_ID``. For example::

   &_Py_ID(new_unique_py_id)

If it does, you'll have to run ``make regen-global-objects``
to regenerate the list of precompiled identifiers at this point.

Finally, compile, then run the relevant portions of the regression-test suite.
This change should not introduce any new compile-time warnings or errors,
and there should be no externally visible change to Python's behavior,
except for one difference: :py:func:`inspect.signature` run on your function
should now provide a valid signature!

Congratulations, you've ported your first function to work with Argument Clinic!
