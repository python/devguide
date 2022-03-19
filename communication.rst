.. _communication:

Following Python's Development
==============================

Python's development is communicated through a myriad of ways, mostly through
mailing lists, but also other forms.


Standards of behaviour in these communication channels
------------------------------------------------------
We try to foster environments of mutual respect, tolerance and encouragement,
as described in the PSF's `Diversity Statement`_. Abiding by the guidelines
in this document and asking questions or posting suggestions in the
appropriate channels are an excellent way to get started on the mutual respect
part, greatly increasing the chances of receiving tolerance and encouragement
in return.

.. _Diversity Statement: https://www.python.org/psf/diversity/


.. _mailinglists:

Mailing Lists
-------------

python-dev_ is the primary mailing list for discussions about Python's
development. The list is open to the public and is subscribed to by all core
developers plus many people simply interested in following Python's
development. Discussion is focused on issues related to Python's development,
such as how to handle a specific issue, a PEP, etc.

- Ideas about new functionality should **not** start here and instead
  should be sent to python-ideas_.
- Technical support questions should also not be asked here and instead
  should go to python-list_ or python-help_.

Python-ideas_ is a mailing list open to the public to discuss ideas on changing
Python. If a new idea does not start here (or python-list_, discussed below),
it will get redirected here.

Sometimes people post new ideas to python-list_ to gather community opinion
before heading to python-ideas_. The list is also sometimes known as
comp.lang.python, the name of the newsgroup it mirrors (it is also known by
the abbreviation c.l.py).

The python-committers_ mailing list is a private mailing list for core
developers (the archives are publicly available).
If something only affects core developers (e.g., the
tree is frozen for commits, etc.), it is discussed here instead of python-dev
to keep traffic down on the latter.

python-dev_, python-committers_, and python-ideas_ all use Mailman 3, and
are hence accessible via the Mailman 3 `web gateway`_.

Python-checkins_ sends out an email for every commit to Python's various
repositories from https://github.com/python/cpython. All core developers
subscribe to this list and are known to reply to these emails to make comments
about various issues they catch in the commit. Replies get redirected to
python-dev.

There are two mailing lists related to issues on the `issue tracker`_. If you
only want an email for when a new issue is open, subscribe to
new-bugs-announce_. If you would rather receive an email for all changes made
to any issue, subscribe to python-bugs-list_.

General Python questions should go to `python-list`_ or `tutor`_
or similar resources, such as StackOverflow_ or the ``#python`` IRC channel
on Libera.Chat_.

`The core-workflow <https://github.com/python/core-workflow/issues>`_
issue tracker is the place to discuss and work on improvements to the CPython
core development workflow.

A complete list of Python mailing lists can be found at https://mail.python.org/mailman/listinfo.
Most lists are also mirrored at `GMANE <https://gmane.io/>`_ and can be read and
posted to in various ways, including via web browsers, NNTP newsreaders, and
RSS feed readers.

.. _issue tracker: https://bugs.python.org
.. _new-bugs-announce: https://mail.python.org/mailman/listinfo/new-bugs-announce
.. _python-bugs-list: https://mail.python.org/mailman/listinfo/python-bugs-list
.. _python-checkins: https://mail.python.org/mailman/listinfo/python-checkins
.. _python-committers: https://mail.python.org/mailman3/lists/python-committers.python.org/
.. _python-dev: https://mail.python.org/mailman3/lists/python-dev.python.org/
.. _python-help: https://mail.python.org/mailman/listinfo/python-help
.. _python-ideas: https://mail.python.org/mailman3/lists/python-ideas.python.org
.. _python-list: https://mail.python.org/mailman/listinfo/python-list
.. _tutor: https://mail.python.org/mailman/listinfo/tutor
.. _StackOverflow: https://stackoverflow.com/
.. _Libera.Chat: https://libera.chat/
.. _web gateway: https://mail.python.org/archives/


Discourse (discuss.python.org web forum)
----------------------------------------

We have our own `Discourse`_ forum for both developers and users. This forum
complements the `python-dev`_, `python-ideas`_, `python-help`_, and
`python-list`_ mailing lists.

Most core development discussions take place in the open forum categories for
`PEPs`_ and `Core Development`_. (These are the Discourse equivalents to the
python-dev mailing list)

The `Committers`_ category restricts posting to core developers only, and is
used more for announcements and notifications, rather than for discussions. It
is also the venue for core developer promotion votes. (This category is the
equivalent of the python-committers mailing list)

There is a final, rarely used, core development category on Discourse that is
only visible to core developers. This can be used to share administrative
information with all core developers in a non-public forum (e.g. logistics for
in person core development sprints), as well as for individual core developers
to share info that they'd like other core devs to be aware of, but would prefer
not to have permanently archived on the internet.

.. _Discourse: https://discuss.python.org/
.. _PEPs: https://discuss.python.org/c/peps/
.. _Core Development: https://discuss.python.org/c/core-dev/
.. _Committers: https://discuss.python.org/c/committers/


Discord (private chat server)
-----------------------------

For more real-time discussions, the core development team have a private Discord
server available. Core developers, Steering Council members, triagers, and
documentarians on the project are eligible to join the server. Joining the
Discord server is entirely optional, as all essential communications occur on
the mailing lists and Discourse forums.

For core developers, a long lived multiple use invitation link for this server
can be found in the private core developer only section of the Discourse forum.

For triagers and documentarians joining the Discord server, a single use invitation
link should be generated and sent to them directly.

When first joining the server, new users will only have access to the ``#welcome``
and ``#rules-and-info`` channels. To link their Discord ID with their project
role, core developers may update their Steering Council `voter record`_ with
their Discord ID before posting in the ``#welcome`` channel to request access
to the rest of the server channels. Triagers, documentarians, and core developers
that would prefer not to add their Discord ID to their Steering Council voter
record may instead be vouched for by an existing member of the Discord server.

As a private, non-archived, forum, final decisions on design and development
questions should not be made on Discord. Any conclusions from Discord discussions
should be summarised and posted to the issue tracker, Discourse forum, or
mailing list (the appropriate venue for sharing conclusions will depend on the
specific discussion).

Note: existing Discord users may want to right click on their username in the
automatic Discord welcome message and choose "Edit Server Profile" in order to
set a specific `Server Nickname`_

.. _voter record: https://github.com/python/voters/blob/main/python-core.toml
.. _Server Nickname: https://support.discord.com/hc/en-us/articles/219070107-Server-Nicknames



IRC
---

Some core developers still participate in the ``#python-dev`` IRC channel on
``irc.libera.chat``. This is not a place to ask for help with Python, but to
discuss issues related to Python's own development. See also the
``#python-dev-notifs`` channel for bots notifications.


Blogs
-----

Several core developers are active bloggers and discuss Python's development
that way. You can find their blogs (and various other developers who use Python)
at https://planetpython.org/.


Setting Expectations for Open Source Participation
--------------------------------------------------

Burn-out is common in open source due to a misunderstanding of what users, contributors,
and maintainers should expect from each other. Brett Cannon gave a `talk <https://www.youtube.com/watch?v=-Nk-8fSJM6I>`_
about this topic that sets out to help everyone set reasonable expectations of each other in
order to make open source pleasant for everyone involved.

Additional Repositories
-----------------------

`Python Core Workflow`_ hosts the codebase for tools such as `cherry_picker`_
and `blurb`_.

Python `Performance Benchmark`_ project is intended to be an authoritative
source of benchmarks for all Python implementations.

.. _Python Core Workflow: https://github.com/python/core-workflow
.. _cherry_picker: https://pypi.org/project/cherry_picker/
.. _blurb: https://pypi.org/project/blurb
.. _Performance Benchmark: https://github.com/python/pyperformance
