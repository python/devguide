.. _lang-changes:
.. _langchanges:

Changing the Python language
============================
On occasion people come up with an idea on how to change or improve Python as a
programming language. This document is meant to explain exactly what changes
have a reasonable chance of being considered and what the process is to propose
changes to the language.


What qualifies
--------------
First and foremost, it must be understood that changes to the Python
programming language are difficult to make. When the language changes,
**every** Python programmer already in existence and all Python programmers to
come will end up eventually learning about the change you want to propose.
Books will need updating, code will be changed, and a new way to do things will
need to be learned. Changes to the Python programming language are never taken
lightly.

Because of the seriousness that language changes carry, any change must be
beneficial to a large proportion of Python users. If the change only benefits a
small percentage of Python developers then the change will not be made. A good
way to see if your idea would work for a large portion of the Python community
is to ask in the `Ideas Discourse category`_. You can also
go through Python's stdlib and find examples of code which would benefit from
your proposed change (which helps communicate the usefulness of your change to
others). For further guidance, see :ref:`suggesting-changes`.

Your proposed change also needs to be *Pythonic*. While only the Steering
Council can truly classify something as Pythonic, you can read the
:pep:`Zen of Python <20>` for guidance.


.. index::
   single: PEP process

.. _suggesting-changes:

Suggesting new features and language changes
--------------------------------------------

The `Ideas Discourse category`_
is specifically intended for discussion of new features and language changes.
Please don't be disappointed if your idea isn't met with universal approval:
as the :pep:`long list of Withdrawn and Rejected PEPs
<0#abandoned-withdrawn-and-rejected-peps>`
in the :pep:`PEP Index <0>` attests,
and as befits a reasonably mature programming language,
getting significant changes into Python isn't a simple task.

If the idea is reasonable, someone will suggest posting it as a feature
request on the `issue tracker`_, or, for larger changes,
writing it up as PEP following the :ref:`lang-changes-pep-process`.

Sometimes core developers will differ in opinion,
or merely be collectively unconvinced.
When there isn't an obvious victor, then the `Status Quo Wins a Stalemate`_.

For some examples on language changes that were accepted,
see `Justifying Python Language Changes`_.


.. index:: PEP process

.. _lang-changes-pep-process:

PEP process
-----------

Once you are certain you have a language change proposal
which will appeal to the general Python community,
you can begin the :abbr:`PEP (Python enhancement proposal)` process
to officially propose the change.
See :pep:`1` for information on PEPs and the PEP process,
and the :pep:`PEP Index <0>` for examples.

If the PEP is accepted, then your proposed language change will be introduced
in the next release of Python.
Otherwise, your PEP will be recorded as rejected along with an explanation,
to inform others who may propose a similar language change in the future.


.. _issue tracker: https://github.com/python/cpython/issues
.. _Ideas Discourse category: https://discuss.python.org/c/ideas/6
.. _Status Quo Wins a Stalemate: https://www.curiousefficiency.org/posts/2011/02/status-quo-wins-stalemate.html
.. _Justifying Python Language Changes: https://www.curiousefficiency.org/posts/2011/02/justifying-python-language-changes.html
