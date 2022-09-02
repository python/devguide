.. _getting-help:
.. _help:

Where to Get Help
=================

If you are working on Python it is very possible you will come across an issue
where you need some assistance to solve it (this happens to core developers
all the time).

Should you require help, there are a :ref:`variety of options available
<communication>` to seek assistance. If the question involves process or tool
usage then please check the rest of this guide first as it should answer your
question.


.. _help-discourse:

Discourse
---------

Python has a hosted Discourse instance at `discuss.python.org <Discourse_>`_.
This forum has many different categories,
of which all but `Committers`_ are open for all users to read and post.
For most general questions and help related to the development
of the Python language, interpreter and standard library itself
(as opposed to developing your own libraries and applications *with* Python),
the `Core Development category`_ is the place to ask.
The `Ideas category`_ is the place to propose and discuss new ideas
for the Python language and standard library,
while the `Core Workflow category`_ is the place to post
about questions, concerns and issues with the dev infrastructure and bots.

.. seealso::
  :ref:`discourse_discuss` for more information on how to get started.

.. _Discourse: https://discuss.python.org/
.. _Committers: https://discuss.python.org/c/committers/5
.. _Core Development category: https://discuss.python.org/c/core-dev/23
.. _Core Workflow category: https://discuss.python.org/c/core-workflow/8
.. _Ideas category: https://discuss.python.org/c/ideas/6


.. _help-mailing-lists:

Mailing Lists
-------------

Further options for seeking assistance include the
`python-ideas`_ and `python-dev`_ mailing lists,
which respectively correspond to the Ideas and Core Development
:ref:`help-discourse` categories, respectively.
The Discourse categories are generally more active
and are the preferred venue for new discussions,
but the mailing lists are still monitored and responded to.
These mailing lists are for questions involving the
development *of* Python, **not** for development *with* Python.

.. _python-ideas: https://mail.python.org/mailman3/lists/python-ideas.python.org
.. _python-dev: https://mail.python.org/mailman3/lists/python-dev.python.org/


Ask #python-dev
---------------

If you are comfortable with IRC you can try asking on ``#python-dev`` (on
the `Libera.Chat`_ network). Typically there are a number of experienced
developers, ranging from triagers to core developers, who can answer
questions about developing for Python.  As with the mailing lists,
``#python-dev`` is for questions involving the development *of* Python
whereas ``#python`` is for questions concerning development *with* Python.

.. note::

  You may not be able to access the history of this channel, so it cannot
  be used as a "knowledge base" of sorts.

.. _Libera.Chat: https://libera.chat/

Zulip
-----

An alternative to IRC is our own `Zulip`_ instance.  There are different streams
for asking help with core development, as well as core developers' office
hour stream. It is preferred that you ask questions here first or schedule
an office hour, before posting to python-dev mailing list or filing bugs.

.. warning::

  This is no longer actively monitored by core devs.
  Consider asking your questions in the relevant
  :ref:`Discourse <discourse_discuss>` category instead.

.. _Zulip: https://python.zulipchat.com


Core Mentorship
---------------

If you are interested in improving Python and contributing to its development,
but don’t yet feel entirely comfortable with the public channels mentioned
above, `Python Mentors`_ are here to help you.  Python is fortunate to have a
community of volunteer core developers willing to mentor anyone wishing to
contribute code, work on bug fixes or improve documentation.  Everyone is
welcomed and encouraged to contribute.

.. _Python Mentors: https://www.python.org/dev/core-mentorship/


.. _office hour:

Core Developers Office Hours
----------------------------

Several core developers have set aside time to host mentorship office hours.
During the office hour, core developers are available to help contributors with
our process, answer questions, and help lower the barrier of contributing and
becoming Python core developers.

The PSF's code of conduct applies for interactions with core developers
during office hours.

+------------------+-------------------------------+------------------------------------------------+
| Core Developer   | Schedule                      | Details                                        |
+==================+===============================+================================================+
| Zachary Ware     | See details link              | Schedule at https://calendly.com/zware         |
+------------------+-------------------------------+------------------------------------------------+
| Mariatta Wijaya  | Thursdays 7PM - 8PM Pacific   | In `Python's Zulip Chat`_, Core > Office       |
|                  | (Vancouver, Canada Timezone)  | Hour stream. A reminder will be posted to both |
|                  |                               | Zulip and `Mariatta's twitter`_ account        |
|                  |                               | 24 hours before the start.                     |
+------------------+-------------------------------+------------------------------------------------+

.. _Python's Zulip Chat: https://python.zulipchat.com/login/#narrow/stream/116503-core/topic/Office.20Hour
.. _Mariatta's twitter: https://twitter.com/mariatta


File a Bug
----------

If you strongly suspect you have stumbled on a bug (be it in the build
process, in the test suite, or in other areas), then open an issue on the
`issue tracker`_.  As with every bug report it is strongly advised that
you detail which conditions triggered it (including the OS name and version,
and what you were trying to do), as well as the exact error message you
encountered.

.. _issue tracker: https://github.com/python/cpython/issues
