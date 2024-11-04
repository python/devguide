Argument Clinic References
---------------------------

@getter Directive
-----------------

**Description**:
The ``@getter`` directive generates a C function that provides read-only access to an attribute, mimicking Python’s property. It is used to create an "impl" function that retrieves the value of an attribute.

**Parameters**:
- None

**Usage Example**:
The use of ``@getter`` in combination with the :ref:`@critical_section <clinic-howto-critical-sections>` directive::

   /*[clinic input]
    @critical_section
    @getter
    _io.TextIOWrapper._CHUNK_SIZE
    [clinic start generated code]*/


The generated glue code looks like this:

.. code-block:: c

   static PyObject *
   _io_TextIOWrapper__CHUNK_SIZE_get(textio *self, void *Py_UNUSED(context))
   {
      PyObject *return_value = NULL;
      Py_BEGIN_CRITICAL_SECTION(self);
      return_value = _io_TextIOWrapper__CHUNK_SIZE_get_impl(self);
      Py_END_CRITICAL_SECTION();
      return return_value
   }

**Explanation**:
   - The generated C function, ``get()``, retrieves the ``_CHUNK_SIZE value`` from the ``TextIOWrapper`` class.
   - A critical section ensures thread safety when accessing the attribute.

Refer to the ``getter`` function section in :ref:`clinic-howto-getset <clinic-howto-pygetsetdef>` for more details.

@setter Directive
-----------------

**Description**:
The ``@setter`` directive generates a C function that sets a value for an attribute, providing property-like write access. It works alongside the ``@getter`` directive to create read-write properties for Python objects in C extensions.

**Parameters**:
- value (automatically passed): The new value to be set for the attribute.

**Usage Example**:
The use of ``@setter`` in combination with the :ref:`@critical_section <clinic-howto-critical-sections>` directive::

    /*[clinic input]
    @critical_section
    @setter
    _io.TextIOWrapper._CHUNK_SIZE
    [clinic start generated code]*/

The generated glue code looks like this:

.. code-block:: c

    static int
    _io_TextIOWrapper__CHUNK_SIZE_set(textio *self, PyObject *value, void *Py_UNUSED(context))
    {
        int return_value;
        Py_BEGIN_CRITICAL_SECTION(self);
        return_value = _io_TextIOWrapper__CHUNK_SIZE_set_impl(self, value);
        Py_END_CRITICAL_SECTION();
        return return_value;
    }

**Explanation**:
   - The setter function assigns a new value to ``_CHUNK_SIZE``.
   - A ``critical section`` ensures thread safety during the update.
   - The ``value`` parameter is added implicitly by Argument Clinic and represents the new data passed by the user.

Refer to the ``setter`` function section in :ref:`clinic-howto-getset <clinic-howto-pygetsetdef>` for more details.

@critical_section Directive
----------------------------

**Description**:
   - The ``@critical_section`` directive in Argument Clinic ensures thread safety by wrapping a function call within a critical section. This section locks the first argument's associated object, preventing concurrent access during execution. It is particularly useful in GIL-free builds of CPython to avoid deadlocks across threads.

**Usage**:
   - Without additional arguments: Locks only the first argument’s object.
   - With additional arguments: Allows locking more objects by passing their C variable names as parameters.

Example Usage::

     /*[clinic input]
     @critical_section
     _io._Buffered.close
     [clinic start generated code]*/

The generated glue code looks like this:

.. code-block:: c

   static PyObject *
   _io__Buffered_close(buffered *self, PyObject *Py_UNUSED(ignored))
   {
      PyObject *return_value = NULL;

      Py_BEGIN_CRITICAL_SECTION(self);
      return_value = _io__Buffered_close_impl(self);
      Py_END_CRITICAL_SECTION();

      return return_value;
   }

Example with additional arguments::

    /*[clinic input]
    @critical_section object
    _weakref.getweakrefcount -> Py_ssize_t

    object: object
    /
    Return the number of weak references to 'object'.
    [clinic start generated code]*/

The generated glue code looks like this:

.. code-block:: c

   static PyObject *
   _weakref_getweakrefs(PyObject *module, PyObject *object)
   {
     PyObject *return_value = NULL;

     Py_BEGIN_CRITICAL_SECTION(object);
     return_value = _weakref_getweakrefs_impl(module, object);
     Py_END_CRITICAL_SECTION();

     return return_value;
   }

**Explanation**:
   - ``Critical Section Behavior``: The critical section acquires a lock on entry and releases it on exit.
   - ``GIL Impact``: In CPython builds with the GIL, these sections are no-ops, as the GIL already ensures thread safety.

Refer to the ``@critical_section`` directive in the section :ref:`@critical_section <clinic-howto-critical-sections>` for details.

@text_signature Directive
-------------------------

**Description**:
The ``@text_signiture`` directive is used to override the default generated signature in the docstring.

**Parameters**:
   - The ``@text_signiture`` directive takes on argument: ``( @text_signiture [arg1] )``

Example from :cpy-file:`Objects/codeobject.c`::


   /*[clinic input]
   @text_signature "($self, /, **changes)"
   code.replace
       *
       co_argcount: int(c_default="self->co_argcount") = unchanged
       co_posonlyargcount: int(c_default="self->co_posonlyargcount") = unchanged
       # etc ...

       Return a copy of the code object with new values for the specified fields.
   [clinic start generated output]*/

The generated docstring ends up looking like this:

.. code-block:: none

    replace($self, /, **changes)
   --

   Return a copy of the code object with new values for the specified fields.

dump Directive
---------------

**Description**:
Dumps the contents of the specified destination buffer into the output of the current block and empties it. This is useful in configuring how and where Argument Clinic outputs generated code, particularly in multi-pass processing.

**Parameters**:
   - The ``dump`` directive takes in one argument ``(dump [arg1])``
   - Where ``arg1`` corresponds to the name of the ``destination`` of the buffer to dump, valid options being ``buffer`` or ``two-pass`` destinations.

.. code-block:: none

   dump <destination>


output Directive
----------------

**Description**:
The ``output`` directive specifies where Argument Clinic should output specific fields, supporting custom and preset configurations.

**Parameters**:
   - The ``output`` directive takes in two arguments ``(output [arg1] [arg2])``
   - Where ``arg1`` is the ``field`` to output and ``arg2`` is the ``destination`` for the output.

.. code-block:: none

   output <field> <destination>

Outputs the specified ``<field>`` to ``<destination>``.

.. note::

   For all fields, use ``everything`` as the ``<field>``.

**Configuration Commands**:
   - ``output push``: Pushes the current configuration to the stack for temporary changes.
   - ``output pop``: Restores the last configuration from the stack.
   - ``preset <preset>``: Sets output configuration to a preset.

**Preset Options**:
   - ``block``: Outputs most fields immediately after input block.
   - ``file``: Outputs fields to a separate file for inclusion.
   - ``buffer``: Saves output to dump later, reducing file edits.
   - ``two-pass``: Uses two buffers to handle forward declarations and definitions separately.
   - ``partial-buffer``: Outputs smaller code chunks to ``block``, larger ones to ``buffer``.

destination Directive
---------------------

**Description**:
The ``destination`` directive allows for operations on output destinations.

**Parameters**:
   - The ``destination`` directive takes in two arguments ``(destination [arg1] [arg2])``.
   - Where ``arg1`` is the ``name`` of the output destination and ``arg2`` is the ``command`` on the output destination.

.. code-block:: none

    destination <name> <command> [...]

There two defined subcommands: ``new`` and ``clear``

The ``new`` subcommand works like this:

.. code-block:: none

    destination <name> new <type>

This creates a new destination with name ``<name>`` and type ``<type>``.

There are five destination types:

   - ``suppress``: Discards the output.
   - ``block``: Writes to the current block.
   - ``buffer``: A simple text buffer.
   - ``file``: A text file (requires a filename template).
   - ``two-pass``: A two-pass buffer.


The ``clear`` subcommand works like this:

.. code-block:: none

    destination <name> clear

This removes all the accumulated text in the specified destination.

set Directive
-------------
The ``set`` directive allows you to configure internal variables in Argument Clinic.

**Syntax**:

.. code-block:: none

   set line_prefix "string"
   set line_suffix "string"

**Description**:
   - ``line_prefix``: Specifies a string to prepend to each line of Clinic's output.
   - ``line_suffix``: Specifies a string to append to each line of Clinic's output.

**Format Strings**:

Both ``line_prefix`` and ``line_suffix`` support the following format strings:

``{block comment start}``
   Turns into the string ``/*``, the start-comment text sequence for C files.

``{block comment end}``
   Turns into the string ``*/``, the end-comment text sequence for C files.

preserve Directive
------------------

The ``preserver`` directive tells Clinic that the current contents of the output should be kept, unmodified.
This is used internally by Clinic when dumping output into ``file`` files; wrapping
it in a Clinic block lets Clinic use its existing checksum functionality to ensure
the file was not modified by hand before it gets overwritten.

.. code-block:: none

    preserve
