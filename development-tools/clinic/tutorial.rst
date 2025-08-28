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
