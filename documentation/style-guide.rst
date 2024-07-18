.. _style-guide:

===========
Style guide
===========

.. highlight:: rest

This page describes the linguistic style guide for our documentation.
For markup details in reST files, see :ref:`markup`.


Footnotes
=========

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
==============

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
starting it with a lowercase letter should be avoided.

.. note::

   Sections that describe a library module often have titles in the
   form of "modulename --- Short description of the module."  In this
   case, the description should be capitalized as a stand-alone
   sentence.

Many special names are used in the Python documentation, including the names of
operating systems, programming languages, standards bodies, and the like. Most
of these entities are not assigned any special markup, but the preferred
spellings are given in :ref:`specific words` to aid authors in maintaining the
consistency of presentation in the Python documentation.

.. _specific words:

Specific words
==============

Some terms and words deserve special mention. These conventions should
be used to ensure consistency throughout the documentation:

C API
  Python's `API <https://docs.python.org/3/c-api/>`_ used by C programmers
  to write extension modules. All caps and unhyphenated.

CPU
   Central processing unit. No need to spell out.

POSIX
   The name assigned to a particular group of standards. This is always
   uppercase.

Python
   The name of our favorite programming language is always capitalized.

reST
   For "reStructuredText," an easy to read, plaintext markup syntax
   used to produce Python documentation.  When spelled out, it is
   always one word and both forms start with a lowercase 'r'.

time zone
   When referring to a Python term like a module, class, or argument spell it
   as one word with appropriate markup (for example, ``:mod:`timezone```).
   When talking about the real-world concept spell it as two words with no
   markup.

Unicode
   The name of a character coding system. This is always written
   capitalized.

Unix
   The name of the operating system developed at AT&T Bell Labs in the early
   1970s.


Use simple language
===================

Avoid esoteric phrasing where possible.  Our audience is world-wide and may not
be native English speakers.

Don't use Latin abbreviations like "e.g." or "i.e." where English words will do,
such as "for example" or "that is."


.. index:: diataxis
.. _diataxis:

Diátaxis
========

Python's documentation strives to follow the `Diátaxis <https://diataxis.fr/>`_
framework. This means adapting the writing style according to the nature of
the documentation that is being written. The framework splits
documentation into four distinct types: tutorials, how-to guides, reference, and
explanation.

* :ref:`python:tutorial-index` should
  be explicit and avoid making assumptions about the
  reader's knowledge. The goal of a tutorial is to get the user writing
  Python code as quickly as possible with clear logical steps. Explanations
  and abstract concepts should be avoided. Please consult the Diátaxis guide on
  :ref:`diataxis:tutorials` for more detail.

* `Python how-to guides <https://docs.python.org/3/howto/index.html>`_ are
  designed to guide a user through a problem-field.
  Both tutorials and how-to guides are instructional rather than explanatory
  and should provide logical steps on how to complete a task. However,
  how-to guides make more assumptions about the user's knoweldge and
  focus on the user finding the best way to solve their own
  particular problem.

* :ref:`python:reference-index` should
  be factual and succinct. The purpose of reference documentation is
  to describe rather than to explain. Accuracy and consistency are key as
  this type of documentation should be seen as an authoritative source.
  :ref:`Code-examples` can be a useful way of achieving these
  objectives.

* Python explanations provide
  a deeper level of understanding and are naturally more discursive. They aim
  to deepen the reader's understanding and answer 'why' questions. They should
  provide context, make connections between topics, and discuss alternative
  opinions. There is no section dedicated to explanations but these can be
  found throughout Python's documentation, for example the
  :ref:`python:unicode-howto`.

Please consult the `Diátaxis <https://diataxis.fr/>`_ guide for more
detail.

Links
=====

Links are a powerful tool for helping people navigate documentation and find
more information, but links can be over-used.  Links should be used only if
they help the reader.

Generally, a link should be provided for the first use of a term in a unit,
such as a section or paragraph. This is not a hard and fast rule.  Sometimes
the second mention is more appropriate for a link.  Some units are long enough
to have a few repeated links.  Use judgement to decide when a link will help
the reader.

Do not use a link when the link would point to the current unit.  It's natural
to use the name of a function in the documentation for the function, but a link
on that function name that simply reloads the section the user is already
reading is useless and distracting.

Do not use links in section headers.  They distract from the title of the
section.  The term will be mentioned in the paragraph text and can be linked
from there.

Sphinx provides ways to automatically add links to references, and a way to
suppress the link.  Using roles like ``:func:`map``` will link to the
documentation for ``map``.  You can suppress the link while keeping the
semantic presentation of the function name by adding an exclamation point
prefix: ``:func:`!map```.  See :ref:`roles` for more details.

Affirmative tone
================

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

Economy of expression
=====================

More documentation is not necessarily better documentation.  Err on the side
of being succinct.

It is an unfortunate fact that making documentation longer can be an impediment
to understanding and can result in even more ways to misread or misinterpret the
text.  Long descriptions full of corner cases and caveats can create the
impression that a function is more complex or harder to use than it actually is.

Security considerations (and other concerns)
============================================

Some modules provided with Python are inherently exposed to security issues
(for example, shell injection vulnerabilities) due to the purpose of the module
(for example, :mod:`ssl`).  Littering the documentation of these modules with red
warning boxes for problems that are due to the task at hand, rather than
specifically to Python's support for that task, doesn't make for a good
reading experience.

Instead, these security concerns should be gathered into a dedicated
"Security Considerations" section within the module's documentation, and
cross-referenced from the documentation of affected interfaces with a note
similar to :samp:`"Please refer to the :ref:\`{security-considerations}\`
section for important information on how to avoid common mistakes."`.

Similarly, if there is a common error that affects many interfaces in a
module (for example, OS level pipe buffers filling up and stalling child processes),
these can be documented in a "Common Errors" section and cross-referenced
rather than repeated for every affected interface.

.. _code-examples:

Code examples
=============

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

Code equivalents
================

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
========

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

Function signatures
===================

These are the evolving guidelines for how to include function signatures in the
reference guide.  As outlined in :ref:`diataxis`, reference material should
prioritize precision and completeness.

- If a function accepts positional-only or keyword-only arguments, include the
  slash and the star in the signature as appropriate::

   .. function:: some_function(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

  Although the syntax is terse, it is precise about the allowable ways to call
  the function and is taken from Python itself.
