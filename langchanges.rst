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
others). For further guidance, see :ref:`suggesting-changes` in the FAQ.

Your proposed change also needs to be *Pythonic*. While Guido is the only
person who can truly classify something as Pythonic, you can read the `Zen of
Python`_ for guidance.

.. _Zen of Python: http://www.python.org/dev/peps/pep-0020/


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
python-list ahead of time you may find out it is technically not possible
(e.g., Python's parser will not support the grammar change as it is an LL(1)
parser). Expect extensive comments on the PEP, some of which will be negative.

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
