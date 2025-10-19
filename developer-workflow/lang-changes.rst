.. _lang-changes:
.. _langchanges:

Changing Python
===============

On occasion people come up with an idea for changing or improving the Python
language or standard library.
This page explains how to propose changes and what to expect during the
process.


Considerations
--------------

First, understand that changes to Python
are difficult to make. When the language changes,
**every** Python programmer and all Python programmers to
come will end up eventually learning about the change you want to propose.
Books will need updating, code will be changed, and a new way to do things will
need to be learned. Changes to Python are never taken
lightly.

Backward compatibility is a significant concern. Existing Python code has to
continue to work. There are exceptions to this rule, but they are very rare
and are only allowed when the benefits of the change greatly outweigh the costs
of breaking existing code.

Because of the seriousness of changing the language, any change must be
beneficial to many Python users. If the change only helps a small percentage of
Python developers then the change will not be made. A good way to see if your
idea would work for a large portion of the Python community is to discuss it in
the `Ideas category in Discourse <ideas_>`_. You can also look in Python's standard
library to find examples of code which would benefit from your proposed change.

.. important::
   For all of these reasons, most proposed changes to Python are rejected. This
   doesn't mean you shouldn't suggest them. It can be useful to explore
   alternatives and to get feedback from the community. Just be aware that
   getting a change accepted is difficult. Don't take it personally.

.. index::
   single: PEP process

.. _suggesting-changes:

Suggesting new features and language changes
--------------------------------------------

Proposing a change involves the following steps:

- Describe your idea in detail.

- Engage in discussion about the idea.

- Rarely, the idea will advance to a formal proposal stage.


Describe your idea
^^^^^^^^^^^^^^^^^^

The `Ideas category in Discourse <ideas_>`_ is specifically intended for discussion
of new features and language changes. Make your proposal as a `new topic
<ideas_>`_ there.

Your proposal needs to be **detailed**. Describe the change you want to make,
why you want to make it, and what benefits it will bring to Python users. Be
specific. Show that you have considered the effect of the change on existing
code.

Some things you should **not** do:

- **Don't** format your idea as a Python Enhancement Proposal (*PEP*).
  It's good to use the PEP template as a guide for what information to include,
  but don't try to write a full PEP until the idea has been accepted for
  further consideration.

- **Don't** create a list of proposed changes. Each idea needs its own
  discussion. Proposing a change is significant work. You will need to spend
  time on each proposal. A tossed-off list will not be taken seriously.

When justifying your idea, these are **not good reasons** to make a change:

- "Other languages work this way." Languages are different. What works well
  in one language may not work well in Python, or Python may already have a
  way to do a similar thing.

- "It would be nice." This is too vague. Be specific about the benefits
  your change will bring, and consider the costs as well.

Some things you **should** do:

- Research whether your idea has been proposed before. There are many
  suggestions that have been made and rejected in the past. If your idea has a
  history, read the discussion to see why it was rejected. Previously rejected
  ideas are especially unlikely to get accepted. If you can address the
  concerns raised in the previous discussion, mention that in your proposal.

- Read other ideas to see how they are presented. This will help you flesh out
  your proposal.

- Read other ideas to understand the kinds of concerns that are raised and
  objections that must be answered. Your proposal will be stronger if you can
  address these concerns up front.

- Provide enough detail to fully explain your idea, and to show that you have
  considered all the implications of the change.  Strike the right balance
  between brevity and completeness.  A shorter proposal will be easier to
  discuss, so long as it includes all the necessary information.


Engage in discussion
^^^^^^^^^^^^^^^^^^^^

Once you post your proposal, people will respond. You need to continue
the discussion, answer questions, and address objections. This is an important
part of the process. Other people's perspectives will help explore the full
impact of the idea and find strengths or weaknesses you may not have
considered.

You will almost always get at least some push-back. Don't be disappointed,
and don't take it personally.
As the long list of :pep:`Withdrawn and Rejected PEPs
<0#rejected-superseded-and-withdrawn-peps>` in the :pep:`PEP Index <0>`
attests, and as befits a mature programming language, getting significant
changes into Python isn't a simple task.

Engage in good faith. The goal of the discussion is to find the best balance
between competing concerns. If your idea has merit, the discussion will help
refine it and make it stronger. If your idea has flaws, the discussion will
help identify them so you can address them or move on. Keep the discussion
productive and focused on the issues, not on personalities.

It is especially useful to discuss with core team members since
they know the language and design considerations well.
If your proposal makes it to the PEP stage,
you'll need a core team member as a sponsor.
Sometimes they will differ in opinion, or merely be unconvinced. When there
isn't a clear positive sentiment, the `Status Quo Wins a Stalemate`_.

Even if your idea is not accepted, the discussion can help you and others
understand the design of Python better, and help inform future proposals.


Formal proposal
^^^^^^^^^^^^^^^

If the idea gets positive discussion, someone will suggest posting it as a
feature request on the `issue tracker`_, or, for larger changes, writing it up
as PEP following the :ref:`lang-changes-pep-process`. Congratulations!


.. index:: PEP process

.. _lang-changes-pep-process:

PEP process
-----------

Once you have a proposal which will appeal to
the general Python community, you can begin the PEP
process to officially propose the change.
This starts with finding a sponsor from the core team.
See :pep:`1` for
information on PEPs and the PEP process, and the :pep:`PEP Index <0>` for
examples.

If the PEP is accepted, then your language change will be introduced in a
future release of Python. Otherwise, your PEP will be recorded as rejected
along with an explanation, to inform others who may propose a similar language
change in the future.


.. _issue tracker: https://github.com/python/cpython/issues
.. _ideas: https://discuss.python.org/c/ideas/6
.. _Status Quo Wins a Stalemate: https://www.curiousefficiency.org/posts/2011/02/status-quo-wins-stalemate/
