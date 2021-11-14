.. _langchanges:

Changing the Python Language
============================
On occasion people come up with an idea on how to change or improve Python as a
programming language. This document is meant to explain exactly what changes
have a reasonable chance of being considered and what the process is to propose
changes to the language.


What Qualifies
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
is to ask on :ref:`python-list or python-ideas <communication>`. You can also
go through Python's stdlib and find examples of code which would benefit from
your proposed change (which helps communicate the usefulness of your change to
others). For further guidance, see :ref:`suggesting-changes`.

Your proposed change also needs to be *Pythonic*. While only the Steering
Council can truly classify something as Pythonic, you can read the `Zen of
Python`_ for guidance.

.. _Zen of Python: https://www.python.org/dev/peps/pep-0020/


.. index:: PEP process

PEP Process
-----------
Once you are certain you have a language change proposal which will appeal to
the general Python community, you can begin the process of officially proposing
the change. This process is the Python Enhancement Proposal (PEP) process.
:PEP:`1` describes it in detail.

You will first need a PEP that you will present to python-ideas. You may be a
little hazy on the technical details as various core developers can help with
that, but do realize that if you do not present your idea to python-ideas or
python-list ahead of time you may find out it is technically not possible.
Expect extensive comments on the PEP, some of which will be negative.

Once your PEP has been modified to be of proper quality and to take into
account comments made on python-ideas, it may proceed to python-dev. There it
will be assigned a PEP dictator and another general discussion will occur. Once
again, you will need to modify your PEP to incorporate the large amount of
comments you will receive.

The PEP dictator decides if your PEP is accepted (typically based on whether
most core developers support the PEP). If that occurs then your proposed
language change will be introduced in the next release of Python. Otherwise
your PEP will be recorded as rejected along with an explanation as to why so
that others do not propose the same language change in the future.


.. index::
   single: PEP process

.. _suggesting-changes:

Suggesting new features and language changes
--------------------------------------------

The `python-ideas`_ mailing list is specifically intended for discussion of
new features and language changes. Please don't be disappointed if your
idea isn't met with universal approval: as the long list of Rejected and
Withdrawn PEPs in the `PEP Index`_ attests, and as befits a reasonably mature
programming language, getting significant changes into Python isn't a simple
task.

If the idea is reasonable, someone will suggest posting it as a feature
request on the `issue tracker`_, or, for larger changes, writing it up as
a `draft PEP`_.

Sometimes core developers will differ in opinion, or merely be collectively
unconvinced. When there isn't an obvious victor then the
`Status Quo Wins a Stalemate`_ as outlined in the linked post.

For some examples on language changes that were accepted please read
`Justifying Python Language Changes`_.

.. _python-ideas: https://mail.python.org/mailman/listinfo/python-ideas
.. _issue tracker: https://bugs.python.org
.. _PEP Index: https://www.python.org/dev/peps/
.. _draft PEP: https://www.python.org/dev/peps/pep-0001/
.. _Status Quo Wins a Stalemate: https://www.curiousefficiency.org/posts/2011/02/status-quo-wins-stalemate.html
.. _Justifying Python Language Changes: https://www.curiousefficiency.org/posts/2011/02/justifying-python-language-changes.html
