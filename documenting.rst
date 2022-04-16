.. _documenting:

==================
Documenting Python
==================

.. highlight::  rest

The Python language has a substantial body of documentation, much of it
contributed by various authors. The markup used for the Python documentation is
`reStructuredText`_, developed by the `docutils`_ project, amended by custom
directives and using a toolset named `Sphinx`_ to post-process the HTML output.

This document describes the style guide for our documentation as well as the
custom reStructuredText markup introduced by Sphinx to support Python
documentation and how it should be used.

The documentation in HTML, PDF or EPUB format is generated from text files
written using the :ref:`reStructuredText format <markup>` and contained in the
:ref:`CPython Git repository <setup>`.

.. _reStructuredText: https://docutils.sourceforge.io/rst.html

.. note::

   If you're interested in contributing to Python's documentation, there's no
   need to write reStructuredText if you're not so inclined; plain text
   contributions are more than welcome as well.  Send an e-mail to
   docs@python.org or open an issue on the :ref:`tracker <reporting-bugs>`.


Introduction
============

Python's documentation has long been considered to be good for a free
programming language.  There are a number of reasons for this, the most
important being the early commitment of Python's creator, Guido van Rossum, to
providing documentation on the language and its libraries, and the continuing
involvement of the user community in providing assistance for creating and
maintaining documentation.

The involvement of the community takes many forms, from authoring to bug reports
to just plain complaining when the documentation could be more complete or
easier to use.

This document is aimed at authors and potential authors of documentation for
Python.  More specifically, it is for people contributing to the standard
documentation and developing additional documents using the same tools as the
standard documents.  This guide will be less useful for authors using the Python
documentation tools for topics other than Python, and less useful still for
authors not using the tools at all.

If your interest is in contributing to the Python documentation, but you don't
have the time or inclination to learn reStructuredText and the markup structures
documented here, there's a welcoming place for you among the Python contributors
as well.  Any time you feel that you can clarify existing documentation or
provide documentation that's missing, the existing documentation team will
gladly work with you to integrate your text, dealing with the markup for you.
Please don't let the material in this document stand between the documentation
and your desire to help out!

.. _style-guide:

Style guide
===========

Use of whitespace
-----------------

All reST files use an indentation of 3 spaces; no tabs are allowed.  The
maximum line length is 80 characters for normal text, but tables, deeply
indented code samples and long links may extend beyond that.  Code example
bodies should use normal Python 4-space indentation.

Make generous use of blank lines where applicable; they help group things
together.

A sentence-ending period may be followed by one or two spaces; while reST
ignores the second space, it is customarily put in by some users, for example
to aid Emacs' auto-fill mode.

Footnotes
---------

Footnotes are generally discouraged, though they may be used when they are the
best way to present specific information. When a footnote reference is added at
the end of the sentence, it should follow the sentence-ending punctuation. The
reST markup should appear something like this::

    This sentence has a footnote reference. [#]_ This is the next sentence.

Footnotes should be gathered at the end of a file, or if the file is very long,
at the end of a section. The docutils will automatically create backlinks to
the footnote reference.

Footnotes may appear in the middle of sentences where appropriate.

Capitalization
--------------

.. sidebar:: Sentence case

   Sentence case is a set of capitalization rules used in English
   sentences: the first word is always capitalized and other words are
   only capitalized if there is a specific rule requiring it.

In the Python documentation, the use of sentence case in section titles is
preferable, but consistency within a unit is more important than
following this rule.  If you add a section to a chapter where most
sections are in title case, you can either convert all titles to
sentence case or use the dominant style in the new section title.

Sentences that start with a word for which specific rules require
starting it with a lower case letter should be avoided.

.. note::

   Sections that describe a library module often have titles in the
   form of "modulename --- Short description of the module."  In this
   case, the description should be capitalized as a stand-alone
   sentence.

Many special names are used in the Python documentation, including the names of
operating systems, programming languages, standards bodies, and the like. Most
of these entities are not assigned any special markup, but the preferred
spellings are given here to aid authors in maintaining the consistency of
presentation in the Python documentation.

Other terms and words deserve special mention as well; these conventions should
be used to ensure consistency throughout the documentation:

CPU
   For "central processing unit." Many style guides say this should be
   spelled out on the first use (and if you must use it, do so!). For
   the Python documentation, this abbreviation should be avoided since
   there's no reasonable way to predict which occurrence will be the
   first seen by the reader. It is better to use the word "processor"
   instead.

POSIX
   The name assigned to a particular group of standards. This is always
   uppercase.

Python
   The name of our favorite programming language is always capitalized.

reST
   For "reStructuredText," an easy to read, plaintext markup syntax
   used to produce Python documentation.  When spelled out, it is
   always one word and both forms start with a lower case 'r'.

Unicode
   The name of a character coding system. This is always written
   capitalized.

Unix
   The name of the operating system developed at AT&T Bell Labs in the early
   1970s.

Affirmative Tone
----------------

The documentation focuses on affirmatively stating what the language does and
how to use it effectively.

Except for certain security or segfault risks, the docs should avoid
wording along the lines of "feature x is dangerous" or "experts only".  These
kinds of value judgments belong in external blogs and wikis, not in the core
documentation.

Bad example (creating worry in the mind of a reader):

    Warning: failing to explicitly close a file could result in lost data or
    excessive resource consumption.  Never rely on reference counting to
    automatically close a file.

Good example (establishing confident knowledge in the effective use of the
language):

    A best practice for using files is use a try/finally pair to explicitly
    close a file after it is used.  Alternatively, using a with-statement can
    achieve the same effect.  This assures that files are flushed and file
    descriptor resources are released in a timely manner.

Economy of Expression
---------------------

More documentation is not necessarily better documentation.  Err on the side
of being succinct.

It is an unfortunate fact that making documentation longer can be an impediment
to understanding and can result in even more ways to misread or misinterpret the
text.  Long descriptions full of corner cases and caveats can create the
impression that a function is more complex or harder to use than it actually is.

Security Considerations (and Other Concerns)
--------------------------------------------

Some modules provided with Python are inherently exposed to security issues
(e.g. shell injection vulnerabilities) due to the purpose of the module
(e.g. :mod:`ssl`).  Littering the documentation of these modules with red
warning boxes for problems that are due to the task at hand, rather than
specifically to Python's support for that task, doesn't make for a good
reading experience.

Instead, these security concerns should be gathered into a dedicated
"Security Considerations" section within the module's documentation, and
cross-referenced from the documentation of affected interfaces with a note
similar to ``"Please refer to the :ref:`security-considerations` section
for important information on how to avoid common mistakes."``.

Similarly, if there is a common error that affects many interfaces in a
module (e.g. OS level pipe buffers filling up and stalling child processes),
these can be documented in a "Common Errors" section and cross-referenced
rather than repeated for every affected interface.

Code Examples
-------------

Short code examples can be a useful adjunct to understanding.  Readers can often
grasp a simple example more quickly than they can digest a formal description in
prose.

People learn faster with concrete, motivating examples that match the context of
a typical use case.  For instance, the :meth:`str.rpartition` method is better
demonstrated with an example splitting the domain from a URL than it would be
with an example of removing the last word from a line of Monty Python dialog.

The ellipsis for the :py:data:`sys.ps2` secondary interpreter prompt should only
be used sparingly, where it is necessary to clearly differentiate between input
lines and output lines.  Besides contributing visual clutter, it makes it
difficult for readers to cut-and-paste examples so they can experiment with
variations.

Code Equivalents
----------------

Giving pure Python code equivalents (or approximate equivalents) can be a useful
adjunct to a prose description.  A documenter should carefully weigh whether the
code equivalent adds value.

A good example is the code equivalent for :func:`all`.  The short 4-line code
equivalent is easily digested; it re-emphasizes the early-out behavior; and it
clarifies the handling of the corner-case where the iterable is empty.  In
addition, it serves as a model for people wanting to implement a commonly
requested alternative where :func:`all` would return the specific object
evaluating to False whenever the function terminates early.

A more questionable example is the code for :func:`itertools.groupby`.  Its code
equivalent borders on being too complex to be a quick aid to understanding.
Despite its complexity, the code equivalent was kept because it serves as a
model to alternative implementations and because the operation of the "grouper"
is more easily shown in code than in English prose.

An example of when not to use a code equivalent is for the :func:`oct` function.
The exact steps in converting a number to octal doesn't add value for a user
trying to learn what the function does.

Audience
--------

The tone of the tutorial (and all the docs) needs to be respectful of the
reader's intelligence.  Don't presume that the readers are stupid.  Lay out the
relevant information, show motivating use cases, provide glossary links, and do
your best to connect-the-dots, but don't talk down to them or waste their time.

The tutorial is meant for newcomers, many of whom will be using the tutorial to
evaluate the language as a whole.  The experience needs to be positive and not
leave the reader with worries that something bad will happen if they make a
misstep.  The tutorial serves as guide for intelligent and curious readers,
saving details for the how-to guides and other sources.

Be careful accepting requests for documentation changes from the rare but vocal
category of reader who is looking for vindication for one of their programming
errors ("I made a mistake, therefore the docs must be wrong ...").  Typically,
the documentation wasn't consulted until after the error was made.  It is
unfortunate, but typically no documentation edit would have saved the user from
making false assumptions about the language ("I was surprised by ...").


.. _rst-primer:

reStructuredText Primer
=======================

This section is a brief introduction to reStructuredText (reST) concepts and
syntax, intended to provide authors with enough information to author documents
productively.  Since reST was designed to be a simple, unobtrusive markup
language, this will not take too long.

.. seealso::

    The authoritative `reStructuredText User
    Documentation <https://docutils.sourceforge.io/rst.html>`_.


Paragraphs
----------

The paragraph is the most basic block in a reST document.  Paragraphs are simply
chunks of text separated by one or more blank lines.  As in Python, indentation
is significant in reST, so all lines of the same paragraph must be left-aligned
to the same level of indentation.


Inline markup
-------------

The standard reST inline markup is quite simple: use

* one asterisk: ``*text*`` for emphasis (italics),
* two asterisks: ``**text**`` for strong emphasis (boldface), and
* backquotes: ````text```` for code samples.

If asterisks or backquotes appear in running text and could be confused with
inline markup delimiters, they have to be escaped with a backslash.

Be aware of some restrictions of this markup:

* it may not be nested,
* content may not start or end with whitespace: ``* text*`` is wrong,
* it must be separated from surrounding text by non-word characters.  Use a
  backslash escaped space to work around that: ``thisis\ *one*\ word``.

These restrictions may be lifted in future versions of the docutils.

reST also allows for custom "interpreted text roles"', which signify that the
enclosed text should be interpreted in a specific way.  Sphinx uses this to
provide semantic markup and cross-referencing of identifiers, as described in
the appropriate section.  The general syntax is ``:rolename:`content```.


Lists and Quotes
----------------

List markup is natural: just place an asterisk at the start of a paragraph and
indent properly.  The same goes for numbered lists; they can also be
automatically numbered using a ``#`` sign::

   * This is a bulleted list.
   * It has two items, the second
     item uses two lines.

   1. This is a numbered list.
   2. It has two items too.

   #. This is a numbered list.
   #. It has two items too.


Nested lists are possible, but be aware that they must be separated from the
parent list items by blank lines::

   * this is
   * a list

     * with a nested list
     * and some subitems

   * and here the parent list continues

Definition lists are created as follows::

   term (up to a line of text)
      Definition of the term, which must be indented

      and can even consist of multiple paragraphs

   next term
      Description.


Paragraphs are quoted by just indenting them more than the surrounding
paragraphs.


Source Code
-----------

Literal code blocks are introduced by ending a paragraph with the special marker
``::``.  The literal block must be indented::

   This is a normal text paragraph. The next paragraph is a code sample::

      It is not processed in any way, except
      that the indentation is removed.

      It can span multiple lines.

   This is a normal text paragraph again.

The handling of the ``::`` marker is smart:

* If it occurs as a paragraph of its own, that paragraph is completely left
  out of the document.
* If it is preceded by whitespace, the marker is removed.
* If it is preceded by non-whitespace, the marker is replaced by a single
  colon.

That way, the second sentence in the above example's first paragraph would be
rendered as "The next paragraph is a code sample:".


Hyperlinks
----------

External links
^^^^^^^^^^^^^^

Use ```Link text <http://target>`_`` for inline web links.  If the link text
should be the web address, you don't need special markup at all, the parser
finds links and mail addresses in ordinary text.

Internal links
^^^^^^^^^^^^^^

Internal linking is done via a special reST role, see the section on specific
markup, :ref:`doc-ref-role`.


Sections
--------

Section headers are created by underlining (and optionally overlining) the
section title with a punctuation character, at least as long as the text::

   =================
   This is a heading
   =================

Normally, there are no heading levels assigned to certain characters as the
structure is determined from the succession of headings.  However, for the
Python documentation, here is a suggested convention:

* ``#`` with overline, for parts
* ``*`` with overline, for chapters
* ``=``, for sections
* ``-``, for subsections
* ``^``, for subsubsections
* ``"``, for paragraphs


Explicit Markup
---------------

"Explicit markup" is used in reST for most constructs that need special
handling, such as footnotes, specially-highlighted paragraphs, comments, and
generic directives.

An explicit markup block begins with a line starting with ``..`` followed by
whitespace and is terminated by the next paragraph at the same level of
indentation.  (There needs to be a blank line between explicit markup and normal
paragraphs.  This may all sound a bit complicated, but it is intuitive enough
when you write it.)


Directives
----------

A directive is a generic block of explicit markup.  Besides roles, it is one of
the extension mechanisms of reST, and Sphinx makes heavy use of it.

Basically, a directive consists of a name, arguments, options and content. (Keep
this terminology in mind, it is used in the next chapter describing custom
directives.)  Looking at this example,

::

   .. function:: foo(x)
                 foo(y, z)
      :bar: no

      Return a line of text input from the user.

``function`` is the directive name.  It is given two arguments here, the
remainder of the first line and the second line, as well as one option ``bar``
(as you can see, options are given in the lines immediately following the
arguments and indicated by the colons).

The directive content follows after a blank line and is indented relative to the
directive start.


Footnotes
---------

For footnotes, use ``[#]_`` to mark the footnote location, and add the footnote
body at the bottom of the document after a "Footnotes" rubric heading, like so::

   Lorem ipsum [#]_ dolor sit amet ... [#]_

   .. rubric:: Footnotes

   .. [#] Text of the first footnote.
   .. [#] Text of the second footnote.

You can also explicitly number the footnotes for better context.


Comments
--------

Every explicit markup block which isn't a valid markup construct (like the
footnotes above) is regarded as a comment.


Source encoding
---------------

Since the easiest way to include special characters like em dashes or copyright
signs in reST is to directly write them as Unicode characters, one has to
specify an encoding:

All Python documentation source files must be in UTF-8 encoding, and the HTML
documents written from them will be in that encoding as well.


Gotchas
-------

There are some problems one commonly runs into while authoring reST documents:

* **Separation of inline markup:** As said above, inline markup spans must be
  separated from the surrounding text by non-word characters, you have to use
  an escaped space to get around that.


Additional Markup Constructs
============================

Sphinx adds a lot of new directives and interpreted text roles to standard reST
markup.  This section contains the reference material for these facilities.
Documentation for "standard" reST constructs is not included here, though
they are used in the Python documentation.

.. note::

   This is just an overview of Sphinx' extended markup capabilities; full
   coverage can be found in `its own documentation
   <https://www.sphinx-doc.org/>`_.


Meta-information markup
-----------------------

.. describe:: sectionauthor

   Identifies the author of the current section.  The argument should include
   the author's name such that it can be used for presentation (though it isn't)
   and email address.  The domain name portion of the address should be lower
   case.  Example::

      .. sectionauthor:: Guido van Rossum <guido@python.org>

   Currently, this markup isn't reflected in the output in any way, but it helps
   keep track of contributions.


Module-specific markup
----------------------

The markup described in this section is used to provide information about a
module being documented.  Each module should be documented in its own file.
Normally this markup appears after the title heading of that file; a typical
file might start like this::

   :mod:`parrot` -- Dead parrot access
   ===================================

   .. module:: parrot
      :platform: Unix, Windows
      :synopsis: Analyze and reanimate dead parrots.
   .. moduleauthor:: Eric Cleese <eric@python.invalid>
   .. moduleauthor:: John Idle <john@python.invalid>

As you can see, the module-specific markup consists of two directives, the
``module`` directive and the ``moduleauthor`` directive.

.. describe:: module

   This directive marks the beginning of the description of a module, package,
   or submodule. The name should be fully qualified (i.e. including the
   package name for submodules).

   The ``platform`` option, if present, is a comma-separated list of the
   platforms on which the module is available (if it is available on all
   platforms, the option should be omitted).  The keys are short identifiers;
   examples that are in use include "IRIX", "Mac", "Windows", and "Unix".  It is
   important to use a key which has already been used when applicable.

   The ``synopsis`` option should consist of one sentence describing the
   module's purpose -- it is currently only used in the Global Module Index.

   The ``deprecated`` option can be given (with no value) to mark a module as
   deprecated; it will be designated as such in various locations then.

.. describe:: moduleauthor

   The ``moduleauthor`` directive, which can appear multiple times, names the
   authors of the module code, just like ``sectionauthor`` names the author(s)
   of a piece of documentation.  It too does not result in any output currently.

.. note::

   It is important to make the section title of a module-describing file
   meaningful since that value will be inserted in the table-of-contents trees
   in overview files.


Information units
-----------------

There are a number of directives used to describe specific features provided by
modules.  Each directive requires one or more signatures to provide basic
information about what is being described, and the content should be the
description.  The basic version makes entries in the general index; if no index
entry is desired, you can give the directive option flag ``:noindex:``.  The
following example shows all of the features of this directive type::

    .. function:: spam(eggs)
                  ham(eggs)
       :noindex:

       Spam or ham the foo.

The signatures of object methods or data attributes should not include the
class name, but be nested in a class directive.  The generated files will
reflect this nesting, and the target identifiers (for HTML output) will use
both the class and method name, to enable consistent cross-references.  If you
describe methods belonging to an abstract protocol such as context managers,
use a class directive with a (pseudo-)type name too to make the
index entries more informative.

The directives are:

.. describe:: c:function

   Describes a C function. The signature should be given as in C, e.g.::

      .. c:function:: PyObject* PyType_GenericAlloc(PyTypeObject *type, Py_ssize_t nitems)

   This is also used to describe function-like preprocessor macros.  The names
   of the arguments should be given so they may be used in the description.

   Note that you don't have to backslash-escape asterisks in the signature,
   as it is not parsed by the reST inliner.

.. describe:: c:member

   Describes a C struct member. Example signature::

      .. c:member:: PyObject* PyTypeObject.tp_bases

   The text of the description should include the range of values allowed, how
   the value should be interpreted, and whether the value can be changed.
   References to structure members in text should use the ``member`` role.

.. describe:: c:macro

   Describes a "simple" C macro.  Simple macros are macros which are used
   for code expansion, but which do not take arguments so cannot be described as
   functions.  This is not to be used for simple constant definitions.  Examples
   of its use in the Python documentation include :c:macro:`PyObject_HEAD` and
   :c:macro:`Py_BEGIN_ALLOW_THREADS`.

.. describe:: c:type

   Describes a C type. The signature should just be the type name.

.. describe:: c:var

   Describes a global C variable.  The signature should include the type, such
   as::

      .. c:var:: PyObject* PyClass_Type

.. describe:: data

   Describes global data in a module, including both variables and values used
   as "defined constants."  Class and object attributes are not documented
   using this directive.

.. describe:: exception

   Describes an exception class.  The signature can, but need not include
   parentheses with constructor arguments.

.. describe:: function

   Describes a module-level function.  The signature should include the
   parameters, enclosing optional parameters in brackets.  Default values can be
   given if it enhances clarity.  For example::

      .. function:: repeat([repeat=3[, number=1000000]])

   Object methods are not documented using this directive. Bound object methods
   placed in the module namespace as part of the public interface of the module
   are documented using this, as they are equivalent to normal functions for
   most purposes.

   The description should include information about the parameters required and
   how they are used (especially whether mutable objects passed as parameters
   are modified), side effects, and possible exceptions.  A small example may be
   provided.

.. describe:: coroutinefunction

   Describes a module-level coroutine.  The description should include similar
   information to that described for ``function``.

.. describe:: decorator

   Describes a decorator function.  The signature should *not* represent the
   signature of the actual function, but the usage as a decorator.  For example,
   given the functions

   .. code-block:: python

      def removename(func):
          func.__name__ = ''
          return func

      def setnewname(name):
          def decorator(func):
              func.__name__ = name
              return func
          return decorator

   the descriptions should look like this::

      .. decorator:: removename

         Remove name of the decorated function.

      .. decorator:: setnewname(name)

         Set name of the decorated function to *name*.

   There is no ``deco`` role to link to a decorator that is marked up with
   this directive; rather, use the ``:func:`` role.

.. describe:: class

   Describes a class.  The signature can include parentheses with parameters
   which will be shown as the constructor arguments.

.. describe:: attribute

   Describes an object data attribute.  The description should include
   information about the type of the data to be expected and whether it may be
   changed directly.  This directive should be nested in a class directive,
   like in this example::

      .. class:: Spam

         Description of the class.

         .. attribute:: ham

            Description of the attribute.

   If is also possible to document an attribute outside of a class directive,
   for example if the documentation for different attributes and methods is
   split in multiple sections.  The class name should then be included
   explicitly::

      .. attribute:: Spam.eggs

.. describe:: method

   Describes an object method.  The parameters should not include the ``self``
   parameter.  The description should include similar information to that
   described for ``function``.  This directive should be nested in a class
   directive, like in the example above.

.. describe:: coroutinemethod

   Describes an object coroutine method.  The parameters should not include the
   ``self`` parameter.  The description should include similar information to
   that described for ``function``.  This directive should be nested in a
   ``class`` directive.

.. describe:: decoratormethod

   Same as ``decorator``, but for decorators that are methods.

   Refer to a decorator method using the ``:meth:`` role.

.. describe:: staticmethod

   Describes an object static method.  The description should include similar
   information to that described for ``function``.  This directive should be
   nested in a ``class`` directive.

.. describe:: classmethod

   Describes an object class method.  The parameters should not include the
   ``cls`` parameter.  The description should include similar information to
   that described for ``function``.  This directive should be nested in a
   ``class`` directive.

.. describe:: abstractmethod

   Describes an object abstract method.  The description should include similar
   information to that described for ``function``.  This directive should be
   nested in a ``class`` directive.

.. describe:: opcode

   Describes a Python :term:`bytecode` instruction.

.. describe:: cmdoption

   Describes a Python command line option or switch.  Option argument names
   should be enclosed in angle brackets.  Example::

      .. cmdoption:: -m <module>

         Run a module as a script.

.. describe:: envvar

   Describes an environment variable that Python uses or defines.


There is also a generic version of these directives:

.. describe:: describe

   This directive produces the same formatting as the specific ones explained
   above but does not create index entries or cross-referencing targets.  It is
   used, for example, to describe the directives in this document. Example::

      .. describe:: opcode

         Describes a Python bytecode instruction.


Showing code examples
---------------------

Examples of Python source code or interactive sessions are represented using
standard reST literal blocks.  They are started by a ``::`` at the end of the
preceding paragraph and delimited by indentation.

Representing an interactive session requires including the prompts and output
along with the Python code.  No special markup is required for interactive
sessions.  After the last line of input or output presented, there should not be
an "unused" primary prompt; this is an example of what *not* to do:

.. code-block:: python

   >>> 1 + 1
   2
   >>>

Syntax highlighting is handled in a smart way:

* There is a "highlighting language" for each source file.  By default,
  this is ``'python'`` as the majority of files will have to highlight Python
  snippets.

* Within Python highlighting mode, interactive sessions are recognized
  automatically and highlighted appropriately.

* The highlighting language can be changed using the ``highlight``
  directive, used as follows::

     .. highlight:: c

  This language is used until the next ``highlight`` directive is
  encountered.

* The ``code-block`` directive can be used to specify the highlight language
  of a single code block, e.g.::

     .. code-block:: c

        #include <stdio.h>

        void main() {
            printf("Hello world!\n");
        }

* The values normally used for the highlighting language are:

  * ``python`` (the default)
  * ``c``
  * ``rest``
  * ``none`` (no highlighting)

* If highlighting with the current language fails, the block is not highlighted
  in any way.

Longer displays of verbatim text may be included by storing the example text in
an external file containing only plain text.  The file may be included using the
``literalinclude`` directive. [1]_ For example, to include the Python source
file :file:`example.py`, use::

   .. literalinclude:: example.py

The file name is relative to the current file's path.  Documentation-specific
include files should be placed in the ``Doc/includes`` subdirectory.

.. _rest-inline-markup:

Inline markup
-------------

As said before, Sphinx uses interpreted text roles to insert semantic markup in
documents.

Names of local variables, such as function/method arguments, are an exception,
they should be marked simply with ``*var*``.

For all other roles, you have to write ``:rolename:`content```.

There are some additional facilities that make cross-referencing roles more
versatile:

* You may supply an explicit title and reference target, like in reST direct
  hyperlinks: ``:role:`title <target>``` will refer to *target*, but the link
  text will be *title*.

* If you prefix the content with ``!``, no reference/hyperlink will be created.

* For the Python object roles, if you prefix the content with ``~``, the link
  text will only be the last component of the target.  For example,
  ``:meth:`~Queue.Queue.get``` will refer to ``Queue.Queue.get`` but only
  display ``get`` as the link text.

  In HTML output, the link's ``title`` attribute (that is e.g. shown as a
  tool-tip on mouse-hover) will always be the full target name.

The following roles refer to objects in modules and are possibly hyperlinked if
a matching identifier is found:

.. describe:: mod

   The name of a module; a dotted name may be used.  This should also be used
   for package names.

.. describe:: func

   The name of a Python function; dotted names may be used.  The role text
   should not include trailing parentheses to enhance readability.  The
   parentheses are stripped when searching for identifiers.

.. describe:: data

   The name of a module-level variable or constant.

.. describe:: const

   The name of a "defined" constant.  This may be a C-language ``#define``
   or a Python variable that is not intended to be changed.

.. describe:: class

   A class name; a dotted name may be used.

.. describe:: meth

   The name of a method of an object.  The role text should include the type
   name and the method name.  A dotted name may be used.

.. describe:: attr

   The name of a data attribute of an object.

.. describe:: exc

   The name of an exception. A dotted name may be used.

The name enclosed in this markup can include a module name and/or a class name.
For example, ``:func:`filter``` could refer to a function named ``filter`` in
the current module, or the built-in function of that name.  In contrast,
``:func:`foo.filter``` clearly refers to the ``filter`` function in the ``foo``
module.

Normally, names in these roles are searched first without any further
qualification, then with the current module name prepended, then with the
current module and class name (if any) prepended.  If you prefix the name with a
dot, this order is reversed.  For example, in the documentation of the
:mod:`codecs` module, ``:func:`open``` always refers to the built-in function,
while ``:func:`.open``` refers to :func:`codecs.open`.

A similar heuristic is used to determine whether the name is an attribute of
the currently documented class.

---------

The following roles create cross-references to C-language constructs if they
are defined in the API documentation:

.. describe:: c:data

   The name of a C-language variable.

.. describe:: c:func

   The name of a C-language function. Should include trailing parentheses.

.. describe:: c:macro

   The name of a "simple" C macro, as defined above.

.. describe:: c:type

   The name of a C-language type.

.. describe:: c:member

   The name of a C type member, as defined above.

---------

The following roles do not refer to objects, but can create cross-references or
internal links:

.. describe:: envvar

   An environment variable.  Index entries are generated.

.. describe:: keyword

   The name of a Python keyword.  Using this role will generate a link to the
   documentation of the keyword.  ``True``, ``False`` and ``None`` do not use
   this role, but simple code markup (````True````), given that they're
   fundamental to the language and should be known to any programmer.

.. describe:: option

   A command-line option of Python.  The leading hyphen(s) must be included.
   If a matching ``cmdoption`` directive exists, it is linked to.  For options
   of other programs or scripts, use simple ````code```` markup.

.. describe:: token

   The name of a grammar token (used in the reference manual to create links
   between production displays).

---------

The following role creates a cross-reference to the term in the glossary:

.. describe:: term

   Reference to a term in the glossary.  The glossary is created using the
   ``glossary`` directive containing a definition list with terms and
   definitions.  It does not have to be in the same file as the ``term``
   markup, in fact, by default the Python docs have one global glossary
   in the ``glossary.rst`` file.

   If you use a term that's not explained in a glossary, you'll get a warning
   during build.

---------

The following roles don't do anything special except formatting the text
in a different style:

.. describe:: command

   The name of an OS-level command, such as ``rm``.

.. describe:: dfn

   Mark the defining instance of a term in the text.  (No index entries are
   generated.)

.. describe:: file

   The name of a file or directory.  Within the contents, you can use curly
   braces to indicate a "variable" part, for example::

      ``spam`` is installed in :file:`/usr/lib/python2.{x}/site-packages` ...

   In the built documentation, the ``x`` will be displayed differently to
   indicate that it is to be replaced by the Python minor version.

.. describe:: guilabel

   Labels presented as part of an interactive user interface should be marked
   using ``guilabel``.  This includes labels from text-based interfaces such as
   those created using :mod:`curses` or other text-based libraries.  Any label
   used in the interface should be marked with this role, including button
   labels, window titles, field names, menu and menu selection names, and even
   values in selection lists.

.. describe:: kbd

   Mark a sequence of keystrokes.  What form the key sequence takes may depend
   on platform- or application-specific conventions.  When there are no relevant
   conventions, the names of modifier keys should be spelled out, to improve
   accessibility for new users and non-native speakers.  For example, an
   *xemacs* key sequence may be marked like ``:kbd:`C-x C-f```, but without
   reference to a specific application or platform, the same sequence should be
   marked as ``:kbd:`Control-x Control-f```.

.. describe:: mailheader

   The name of an RFC 822-style mail header.  This markup does not imply that
   the header is being used in an email message, but can be used to refer to any
   header of the same "style."  This is also used for headers defined by the
   various MIME specifications.  The header name should be entered in the same
   way it would normally be found in practice, with the camel-casing conventions
   being preferred where there is more than one common usage. For example:
   ``:mailheader:`Content-Type```.

.. describe:: makevar

   The name of a :command:`make` variable.

.. describe:: manpage

   A reference to a Unix manual page including the section,
   e.g. ``:manpage:`ls(1)```.

.. describe:: menuselection

   Menu selections should be marked using the ``menuselection`` role.  This is
   used to mark a complete sequence of menu selections, including selecting
   submenus and choosing a specific operation, or any subsequence of such a
   sequence.  The names of individual selections should be separated by
   ``-->``.

   For example, to mark the selection "Start > Programs", use this markup::

      :menuselection:`Start --> Programs`

   When including a selection that includes some trailing indicator, such as the
   ellipsis some operating systems use to indicate that the command opens a
   dialog, the indicator should be omitted from the selection name.

.. describe:: mimetype

   The name of a MIME type, or a component of a MIME type (the major or minor
   portion, taken alone).

.. describe:: newsgroup

   The name of a Usenet newsgroup.

.. describe:: program

   The name of an executable program.  This may differ from the file name for
   the executable for some platforms.  In particular, the ``.exe`` (or other)
   extension should be omitted for Windows programs.

.. describe:: regexp

   A regular expression. Quotes should not be included.

.. describe:: samp

   A piece of literal text, such as code.  Within the contents, you can use
   curly braces to indicate a "variable" part, as in ``:file:``.

   If you don't need the "variable part" indication, use the standard
   ````code```` instead.


The following roles generate external links:

.. describe:: pep

   A reference to a Python Enhancement Proposal.  This generates appropriate
   index entries. The text "PEP *number*\ " is generated; in the HTML output,
   this text is a hyperlink to an online copy of the specified PEP. Such
   hyperlinks should not be a substitute for properly documenting the
   language in the manuals.

.. describe:: rfc

   A reference to an Internet Request for Comments.  This generates appropriate
   index entries. The text "RFC *number*\ " is generated; in the HTML output,
   this text is a hyperlink to an online copy of the specified RFC.


Note that there are no special roles for including hyperlinks as you can use
the standard reST markup for that purpose.


.. _doc-ref-role:

Cross-linking markup
--------------------

To support cross-referencing to arbitrary sections in the documentation, the
standard reST labels are "abused" a bit: Every label must precede a section
title; and every label name must be unique throughout the entire documentation
source.

You can then reference to these sections using the ``:ref:`label-name``` role.

Example::

   .. _my-reference-label:

   Section to cross-reference
   --------------------------

   This is the text of the section.

   It refers to the section itself, see :ref:`my-reference-label`.

The ``:ref:`` invocation is replaced with the section title.

Alternatively, you can reference any label (not just section titles)
if you provide the link text ``:ref:`link text <reference-label>```.

Paragraph-level markup
----------------------

These directives create short paragraphs and can be used inside information
units as well as normal text:

.. describe:: note

   An especially important bit of information about an API that a user should be
   aware of when using whatever bit of API the note pertains to.  The content of
   the directive should be written in complete sentences and include all
   appropriate punctuation.

   Example::

      .. note::

         This function is not suitable for sending spam e-mails.

.. describe:: warning

   An important bit of information about an API that a user should be aware of
   when using whatever bit of API the warning pertains to.  The content of the
   directive should be written in complete sentences and include all appropriate
   punctuation.  In the interest of not scaring users away from pages filled
   with warnings, this directive should only be chosen over ``note`` for
   information regarding the possibility of crashes, data loss, or security
   implications.

.. describe:: versionadded

   This directive documents the version of Python which added the described
   feature, or a part of it, to the library or C API.  When this applies to an
   entire module, it should be placed at the top of the module section before
   any prose.

   The first argument must be given and is the version in question.  The second
   argument is optional and can be used to describe the details of the feature.

   Example::

      .. versionadded:: 3.5

.. describe:: versionchanged

   Similar to ``versionadded``, but describes when and what changed in the named
   feature in some way (new parameters, changed side effects, platform support,
   etc.).  This one *must* have the second argument (explanation of the change).

   Example::

      .. versionchanged:: 3.1
         The *spam* parameter was added.

   Note that there should be no blank line between the directive head and the
   explanation; this is to make these blocks visually continuous in the markup.

.. describe:: deprecated

   Indicates the version from which the described feature is deprecated.

   There is one required argument: the version from which the feature is
   deprecated.

   Example::

      .. deprecated:: 3.8

.. describe:: deprecated-removed

   Like ``deprecated``, but it also indicates in which version the feature is
   removed.

   There are two required arguments: the version from which the feature is
   deprecated, and the version in which the feature is removed.

   Example::

      .. deprecated-removed:: 3.8 4.0

.. describe:: impl-detail

   This directive is used to mark CPython-specific information.  Use either with
   a block content or a single sentence as an argument, i.e. either ::

      .. impl-detail::

         This describes some implementation detail.

         More explanation.

   or ::

      .. impl-detail:: This shortly mentions an implementation detail.

   "\ **CPython implementation detail:**\ " is automatically prepended to the
   content.

.. describe:: seealso

   Many sections include a list of references to module documentation or
   external documents.  These lists are created using the ``seealso`` directive.

   The ``seealso`` directive is typically placed in a section just before any
   sub-sections.  For the HTML output, it is shown boxed off from the main flow
   of the text.

   The content of the ``seealso`` directive should be a reST definition list.
   Example::

      .. seealso::

         Module :mod:`zipfile`
            Documentation of the :mod:`zipfile` standard module.

         `GNU tar manual, Basic Tar Format <http://link>`_
            Documentation for tar archive files, including GNU tar extensions.

.. describe:: rubric

   This directive creates a paragraph heading that is not used to create a
   table of contents node.  It is currently used for the "Footnotes" caption.

.. describe:: centered

   This directive creates a centered boldfaced paragraph.  Use it as follows::

      .. centered::

         Paragraph contents.


Table-of-contents markup
------------------------

Since reST does not have facilities to interconnect several documents, or split
documents into multiple output files, Sphinx uses a custom directive to add
relations between the single files the documentation is made of, as well as
tables of contents.  The ``toctree`` directive is the central element.

.. describe:: toctree

   This directive inserts a "TOC tree" at the current location, using the
   individual TOCs (including "sub-TOC trees") of the files given in the
   directive body.  A numeric ``maxdepth`` option may be given to indicate the
   depth of the tree; by default, all levels are included.

   Consider this example (taken from the library reference index)::

      .. toctree::
         :maxdepth: 2

         intro
         strings
         datatypes
         numeric
         (many more files listed here)

   This accomplishes two things:

   * Tables of contents from all those files are inserted, with a maximum depth
     of two, that means one nested heading.  ``toctree`` directives in those
     files are also taken into account.
   * Sphinx knows that the relative order of the files ``intro``,
     ``strings`` and so forth, and it knows that they are children of the
     shown file, the library index.  From this information it generates "next
     chapter", "previous chapter" and "parent chapter" links.

   In the end, all files included in the build process must occur in one
   ``toctree`` directive; Sphinx will emit a warning if it finds a file that is
   not included, because that means that this file will not be reachable through
   standard navigation.

   The special file ``contents.rst`` at the root of the source directory is the
   "root" of the TOC tree hierarchy; from it the "Contents" page is generated.


Index-generating markup
-----------------------

Sphinx automatically creates index entries from all information units (like
functions, classes or attributes) like discussed before.

However, there is also an explicit directive available, to make the index more
comprehensive and enable index entries in documents where information is not
mainly contained in information units, such as the language reference.

The directive is ``index`` and contains one or more index entries.  Each entry
consists of a type and a value, separated by a colon.

For example::

   .. index::
      single: execution; context
      module: __main__
      module: sys
      triple: module; search; path

This directive contains five entries, which will be converted to entries in the
generated index which link to the exact location of the index statement (or, in
case of offline media, the corresponding page number).

The possible entry types are:

single
   Creates a single index entry.  Can be made a subentry by separating the
   subentry text with a semicolon (this notation is also used below to describe
   what entries are created).
pair
   ``pair: loop; statement`` is a shortcut that creates two index entries,
   namely ``loop; statement`` and ``statement; loop``.
triple
   Likewise, ``triple: module; search; path`` is a shortcut that creates three
   index entries, which are ``module; search path``, ``search; path, module``
   and ``path; module search``.
module, keyword, operator, object, exception, statement, builtin
   These all create two index entries.  For example, ``module: hashlib``
   creates the entries ``module; hashlib`` and ``hashlib; module``.  The
   builtin entry type is slightly different in that "built-in function" is used
   in place of "builtin" when creating the two entries.

For index directives containing only "single" entries, there is a shorthand
notation::

   .. index:: BNF, grammar, syntax, notation

This creates four index entries.


Grammar production displays
---------------------------

Special markup is available for displaying the productions of a formal grammar.
The markup is simple and does not attempt to model all aspects of BNF (or any
derived forms), but provides enough to allow context-free grammars to be
displayed in a way that causes uses of a symbol to be rendered as hyperlinks to
the definition of the symbol.  There is this directive:

.. describe:: productionlist

   This directive is used to enclose a group of productions.  Each production is
   given on a single line and consists of a name, separated by a colon from the
   following definition.  If the definition spans multiple lines, each
   continuation line must begin with a colon placed at the same column as in the
   first line.

   Blank lines are not allowed within ``productionlist`` directive arguments.

   The definition can contain token names which are marked as interpreted text
   (e.g. ``unaryneg ::= "-" `integer```) -- this generates cross-references
   to the productions of these tokens.

   Note that no further reST parsing is done in the production, so that you
   don't have to escape ``*`` or ``|`` characters.


.. XXX describe optional first parameter

The following is an example taken from the Python Reference Manual::

   .. productionlist::
      try_stmt: try1_stmt | try2_stmt
      try1_stmt: "try" ":" `suite`
               : ("except" [`expression` ["," `target`]] ":" `suite`)+
               : ["else" ":" `suite`]
               : ["finally" ":" `suite`]
      try2_stmt: "try" ":" `suite`
               : "finally" ":" `suite`


Substitutions
-------------

The documentation system provides three substitutions that are defined by
default. They are set in the build configuration file :file:`conf.py`.

.. describe:: |release|

   Replaced by the Python release the documentation refers to.  This is the full
   version string including alpha/beta/release candidate tags, e.g. ``2.5.2b3``.

.. describe:: |version|

   Replaced by the Python version the documentation refers to. This consists
   only of the major and minor version parts, e.g. ``2.5``, even for version
   2.5.1.

.. describe:: |today|

   Replaced by either today's date, or the date set in the build configuration
   file.  Normally has the format ``April 14, 2007``.


.. rubric:: Footnotes

.. [1] There is a standard ``include`` directive, but it raises errors if the
       file is not found.  This one only emits a warning.


.. _building-doc:

Building the documentation
==========================

.. highlight:: bash

The toolset used to build the docs is written in Python and is called Sphinx_.
Sphinx is maintained separately and is not included in this tree.  Also needed
are blurb_, a tool to create :file:`Misc/NEWS` on demand; and
python-docs-theme_, the Sphinx theme for the Python documentation.

To build the documentation, follow the instructions from one of the sections
below.  You can view the documentation after building the HTML by pointing
a browser at the file :file:`Doc/build/html/index.html`.

You are expected to have installed the latest stable version of
Sphinx_ and blurb_ on your system or in a virtualenv_ (which can be
created using ``make venv``), so that the Makefile can find the
``sphinx-build`` command.  You can also specify the location of
``sphinx-build`` with the ``SPHINXBUILD`` :command:`make` variable.


.. _building-using-make:

Using make / make.bat
---------------------

**On Unix**, run the following from the root of your :ref:`repository clone
<checkout>` to build the output as HTML::

   cd Doc
   make venv
   make html

or alternatively ``make -C Doc/ venv html``.

You can also use ``make help`` to see a list of targets supported by
:command:`make`.  Note that ``make check`` is automatically run when
you submit a :doc:`pull request <pullrequest>`, so you should make
sure that it runs without errors.

**On Windows**, a :file:`make.bat` batchfile tries to emulate :command:`make`
as closely as possible, but the venv target is not implemented, so you will
probably want to make sure you are working in a virtual environment before
proceeding, otherwise all dependencies will be automatically installed on your
system.

When ready, run the following from the root of your :ref:`repository clone
<checkout>` to build the output as HTML::

   cd Doc
   make html

You can also use ``make help`` to see a list of targets supported by
:file:`make.bat`.

See also :file:`Doc/README.rst` for more information.

Using sphinx-build
------------------

Sometimes we directly want to execute the sphinx-build tool instead of through
``make`` (although the latter is still the preferred way). In this case, you can
use the following command line from the ``Doc`` directory (make sure to install
Sphinx_, blurb_ and python-docs-theme_ packages from PyPI)::

   sphinx-build -b<builder> . build/<builder>

where ``<builder>`` is one of html, text, latex, or htmlhelp (for explanations
see the make targets above).

.. _translating:

Translating
===========

Python documentation translations are governed by :PEP:`545`.
They are built by `docsbuild-scripts
<https://github.com/python/docsbuild-scripts/>`__ and hosted on
docs.python.org. There are several documentation translations already
in production; others are works in progress.

+-----------------+-------------------------------+----------------------------+
| Language        | Contact                       | Links                      |
+=================+===============================+============================+
| Arabic (ar)     | `Abdur-Rahmaan Janhangeer     | `GitHub <github_ar_>`_     |
|                 | <bpo_osdotsystem_>`_          |                            |
+-----------------+-------------------------------+----------------------------+
| Bengali as      | `Kushal Das <bpo_kushal_>`_   | `GitHub <github_bn_in_>`_  |
| spoken in       |                               |                            |
| India (bn_IN)   |                               |                            |
+-----------------+-------------------------------+----------------------------+
| French (fr)     | `Julien Palard (mdk)          | `GitHub <github_fr_>`_     |
|                 | <bpo_mdk_>`_                  |                            |
+-----------------+-------------------------------+----------------------------+
| Hindi as spoken |                               | `GitHub <github_hi_in_>`_  |
| in India (hi_IN)|                               |                            |
+-----------------+-------------------------------+----------------------------+
| Hungarian (hu)  | `Tamás Bajusz (gbtami)        | `GitHub <github_hu_>`_     |
|                 | <bpo_gbtami_>`_               | `Mailing List <list_hu_>`_ |
+-----------------+-------------------------------+----------------------------+
| Indonesian (id) | `Oon Arfiandwi <bpo_oonid_>`_ | `GitHub <github_id_>`_     |
+-----------------+-------------------------------+----------------------------+
| Italian (it)    |                               | `mail <mail_it_>`_         |
+-----------------+-------------------------------+----------------------------+
| Japanese (ja)   | `Kinebuchi Tomohiko           | `GitHub <github_ja_>`_     |
|                 | (cocoatomo) <bpo_cocoatomo_>`_| `Doc <doc_ja_>`_           |
+-----------------+-------------------------------+----------------------------+
| Korean (ko)     |                               | `GitHub <github_ko_>`_     |
|                 |                               | `Doc <doc_ko_>`_           |
+-----------------+-------------------------------+----------------------------+
| Lithuanian (lt) |                               | `mail <mail_lt_>`_         |
+-----------------+-------------------------------+----------------------------+
| Persian (fa)    | `Komeil Parseh (mmdbalkhi)    | `GitHub <github_fa_>`_     |
|                 | <bpo_mmdbalkhi_>`_            |                            |
+-----------------+-------------------------------+----------------------------+
| Polish (pl)     |                               | `GitHub <github_pl_>`_     |
|                 |                               | `Translations <tx_pl_>`_   |
|                 |                               | `Doc <doc_pl_>`_           |
|                 |                               | `mail <mail_pl_>`_         |
+-----------------+-------------------------------+----------------------------+
| Portuguese (pt) | Gustavo Toffo                 |                            |
+-----------------+-------------------------------+----------------------------+
| Portuguese      | Marco Rougeth                 | `GitHub <github_pt_br_>`_  |
| as spoken       |                               | `Wiki <wiki_pt_br_>`_      |
| in Brasil       |                               | `Telegram <chat_pt_br_>`_  |
| (pt-br)         |                               | `article <article_pt_br_>`_|
+-----------------+-------------------------------+----------------------------+
| Russian (ru)    |                               | `mail <mail_ru_>`_         |
+-----------------+-------------------------------+----------------------------+
| Simplified      | `Shengjing Zhu <bpo_zhsj_>`_  | `Transifex <tx_zh_cn_>`_   |
| Chinese         |                               | `GitHub <github_zh_cn_>`_  |
| (zh-cn)         |                               | `Doc <doc_zh_cn_>`_        |
+-----------------+-------------------------------+----------------------------+
| Spanish (es)    | Raúl Cumplido                 | `GitHub <github_es_>`_     |
+-----------------+-------------------------------+----------------------------+
| Traditional     | `王威翔 Matt Wang             | `GitHub <github_zh_tw_>`_  |
| Chinese         | <bpo_mattwang44_>`_,          | `Transifex <tx_zh_tw_>`_   |
| (zh-tw)         | Josix Wang                    | `Doc <doc_zh_tw_>`_        |
+-----------------+-------------------------------+----------------------------+
| Turkish (tr)    | `Ege Akman (egeakman)         | `GitHub <github_tr_>`_     |
|                 | <email_egeakman_>`_           |                            |
+-----------------+-------------------------------+----------------------------+

.. _article_pt_br: https://rgth.co/blog/python-ptbr-cenario-atual/
.. _bpo_cocoatomo: https://github.com/cocoatomo
.. _bpo_gbtami: https://github.com/gbtami
.. _bpo_kushal: https://github.com/Kushal997-das
.. _bpo_mdk: https://github.com/JulienPalard
.. _bpo_mmdbalkhi: https://github.com/mmdbalkhi
.. _bpo_oonid: https://github.com/oonid
.. _bpo_osdotsystem: https://github.com/Abdur-rahmaanJ
.. _bpo_zhsj: https://github.com/zhsj
.. _bpo_mattwang44: https://github.com/mattwang44
.. _email_egeakman: mailto:egeakmanegeakman@hotmail.com
.. _chat_pt_br: https://t.me/pybr_i18n
.. _doc_ja: https://docs.python.org/ja/
.. _doc_ko: https://docs.python.org/ko/
.. _doc_pl: https://docs.python.org/pl/
.. _doc_zh_cn: https://docs.python.org/zh-cn/
.. _doc_zh_tw: https://docs.python.org/zh-tw/
.. _github_ar: https://github.com/Abdur-rahmaanJ/python-docs-ar
.. _github_bn_in: https://github.com/python/python-docs-bn-in
.. _github_es: https://github.com/python/python-docs-es
.. _github_fa: https://github.com/mmdbalkhi/python-docs-fa
.. _github_fr: https://github.com/python/python-docs-fr
.. _github_hi_in: https://github.com/CuriousLearner/python-docs-hi-in
.. _github_hu: https://github.com/python/python-docs-hu
.. _github_id: https://github.com/python/python-docs-id
.. _github_ja: https://github.com/python/python-docs-ja
.. _github_ko: https://github.com/python/python-docs-ko
.. _github_pl: https://github.com/python/python-docs-pl
.. _github_pt_br: https://github.com/python/python-docs-pt-br
.. _github_tr: https://github.com/python-docs-tr/python-docs-tr
.. _github_zh_cn: https://github.com/python/python-docs-zh-cn
.. _github_zh_tw: https://github.com/python/python-docs-zh-tw
.. _list_hu: https://mail.python.org/pipermail/python-hu
.. _mail_it: https://mail.python.org/pipermail/doc-sig/2019-April/004114.html
.. _mail_lt: https://mail.python.org/pipermail/doc-sig/2019-July/004138.html
.. _mail_pl: https://mail.python.org/pipermail/doc-sig/2019-April/004106.html
.. _mail_ru: https://mail.python.org/pipermail/doc-sig/2019-May/004131.html
.. _tx_pl: https://www.transifex.com/python-doc/python-newest/
.. _tx_zh_cn: https://www.transifex.com/python-doc/python-newest/
.. _tx_zh_tw: https://www.transifex.com/python-tw-doc/python-36-tw
.. _wiki_pt_br: https://python.org.br/traducao/

Starting a new translation
--------------------------

First subscribe to the `translation mailing list <translation_ml_>`_,
and introduce yourself and the translation you're starting. Translations
fall under the aegis of the `PSF Translation Workgroup <translation_wg_>`_

Then you can bootstrap your new translation by using our `cookiecutter
<https://github.com/JulienPalard/python-docs-cookiecutter>`__.

The important steps look like this:

- Create the GitHub repo (anywhere) with the right hierarchy (using the
  cookiecutter).
- Gather people to help you translate. You can't do it alone.
- You can use any tool to translate, as long as you can synchronize with git.
  Some use Transifex, and some use only GitHub. You can choose another
  way if you like; it's up to you.
- Ensure we update this page to reflect your work and progress, either via a
  PR or by asking on the `translation mailing list <translation_ml_>`_.
- When ``tutorial/``, ``bugs.py`` and ``library/functions``
  are complete, ask on the `translation mailing list <translation_ml_>`_ for your language to be added in the
  language picker on docs.python.org.


PEP 545 summary:
----------------

Here are the essential points of :PEP:`545`:

- Each translation is assigned an appropriate lowercased language tag,
  with an optional region subtag, and joined with a dash, like
  ``pt-br`` or ``fr``.

- Each translation is under CC0 and marked as such in the README (as in
  the cookiecutter).

- Translation files are hosted on
  ``https://github.com/python/python-docs-{LANGUAGE_TAG}`` (not
  mandatory to start a translation, but mandatory to land on
  ``docs.python.org``).

- Translations having completed ``tutorial/``, ``library/stdtypes``
  and ``library/functions`` are hosted on
  ``https://docs.python.org/{LANGUAGE_TAG}/{VERSION_TAG}/``.


How to get help
---------------

Discussions about translations occur on the `translation mailing list <translation_ml_>`_,
and there's a `Libera.Chat IRC <https://libera.chat/>`_ channel,
``#python-doc``.


Translation FAQ
---------------

Which version of the Python documentation should be translated?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Consensus is to work on current stable. You can then propagate your
translation from one branch to another using `pomerge
<https://pypi.org/project/pomerge/>`__.


Are there some tools to help in managing the repo?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here's what we're using:

- `pomerge <https://pypi.org/project/pomerge/>`__ to propagate translations
  from one file to others.
- `pospell <https://pypi.org/project/pospell/>`__ to check for typos in ``.po`` files.
- `powrap <https://pypi.org/project/powrap/>`__ to rewrap the ``.po`` files
  before committing. This helps keep git diffs short.
- `potodo <https://pypi.org/project/potodo/>`__ to list what needs to be translated.


How is a coordinator elected?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is no election; each translation has to sort this out.  Here are some suggestions.

-  Coordinator requests are to be public on the `translation mailing list <translation_ml_>`_.
-  If the given language has a native core dev, the core dev has their
   say on the choice.
-  Anyone who wants to become coordinator for their native language and shows
   motivation by translating and building a community will be named
   coordinator.
-  In case of concurrency between two persons, no one will sort this out
   for you.  It is up to you two to organize a local election or whatever is
   needed to sort this out.
-  If a coordinator becomes inactive or unreachable for a long
   period of time, someone else can ask for a takeover on the `translation mailing list <translation_ml_>`_.


The entry for my translation is missing/not up to date on this page
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ask on the `translation mailing list <translation_ml_>`_, or better, make a PR on the `devguide
<https://github.com/python/devguide/>`__.


I have a translation, but it's not in git. What should I do?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can ask for help on the `translation mailing list <translation_ml_>`_, and
the team will help you create an appropriate repository. You can still use tools like transifex,
if you like.


My git hierarchy does not match yours. Can I keep it?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No, inside the ``github.com/python`` organization we’ll all have the
exact same hierarchy so bots will be able to build all of our
translations. So you may have to convert from one hierarchy to another.
Ask for help on the `translation mailing list <translation_ml_>`_ if you’re
not sure on how to do it.


What hierarchy should I use in my GitHub repository?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As for every project, we have a *branch* per version.  We store ``.po``
files in the root of the repository using the ``gettext_compact=0``
style.



.. _docutils: https://docutils.sourceforge.io/
.. _python-docs-theme: https://pypi.org/project/python-docs-theme/
.. _Sphinx: https://www.sphinx-doc.org/
.. _virtualenv: https://virtualenv.pypa.io/
.. _blurb: https://pypi.org/project/blurb/
.. _translation_wg: https://wiki.python.org/psf/TranslationWG/Charter
.. _translation_ml: https://mail.python.org/mailman3/lists/translation.python.org/
