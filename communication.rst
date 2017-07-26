.. _communication:

Following Python's Development
==============================

Python's development is communicated through a myriad of ways, mostly through
mailing lists, but also other forms.

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

Sometimes people post new ideas to python-list_ to gather community opinion before
heading to python-ideas_. The list is also sometimes known as comp.lang.python,
the name of the newsgroup it mirrors (it is also known by the abbreviation
c.l.py).

The python-committers_ mailing list is a private mailing list for core
developers (the archives are publicly available).
If something only affects core developers (e.g., the
tree is frozen for commits, etc.), it is discussed here instead of python-dev
to keep traffic down on the latter.

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
on Freenode_.

A complete list of Python mailing lists can be found at https://mail.python.org.
Most lists are also mirrored at http://news.gmane.org/ and can be read and
posted to in various ways, including via web browsers, NNTP newsreaders, and
RSS feed readers.

.. _issue tracker: http://bugs.python.org
.. _new-bugs-announce: https://mail.python.org/mailman/listinfo/new-bugs-announce
.. _python-bugs-list: https://mail.python.org/mailman/listinfo/python-bugs-list
.. _python-checkins: https://mail.python.org/mailman/listinfo/python-checkins
.. _python-committers: https://mail.python.org/mailman/listinfo/python-committers
.. _python-dev: https://mail.python.org/mailman/listinfo/python-dev
.. _python-help: https://mail.python.org/mailman/listinfo/python-help
.. _python-ideas: https://mail.python.org/mailman/listinfo/python-ideas
.. _python-list: https://mail.python.org/mailman/listinfo/python-list
.. _tutor: https://mail.python.org/mailman/listinfo/tutor
.. _StackOverflow: https://stackoverflow.com/
.. _Freenode: http://freenode.net/


IRC
---

Some core developers enjoy spending time on IRC discussing various issues
regarding Python's development in the ``#python-dev`` channel on
``irc.freenode.net``. This is not a place to ask for help with Python, but to
discuss issues related to Python's own development.  You can use Freenode's
`Web interface <http://webchat.freenode.net/>`_ if you don't have an IRC
client.


Blogs
-----

Several core developers are active bloggers and discuss Python's development
that way. You can find their blogs (and various other developers who use Python)
at http://planetpython.org/.


Standards of behaviour in these communication channels
------------------------------------------------------
We try to foster environments of mutual respect, tolerance and encouragement,
as described in the PSF's `Diversity Statement`_. Abiding by the guidelines
in this document and asking questions or posting suggestions in the
appropriate channels are an excellent way to get started on the mutual respect
part, greatly increasing the chances of receiving tolerance and encouragement
in return.

.. _Diversity Statement: https://www.python.org/psf/diversity/

Additional Repositories
-----------------------

Because Python is not a simple project, we have repositories for several topics,

* the `core-workflow`_ process if you want to contribute and use our tools.
* the Python `Performance Benchmark`_ suite if you are interested by the performance of Python.

.. _core-workflow: https://github.com/python/core-workflow
.. _Performance Benchmark: https://github.com/python/performance
