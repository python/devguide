.. _become-core-developer:
.. _coredev:
.. _join-core-team:

=========================
How to join the core team
=========================

What it takes
=============

When you have consistently made contributions which meet quality standards
without requiring extensive rewrites prior to being committed,
you may qualify for commit privileges and join the core team of Python.
You must also work well with other core team members (and people in general)
as you become an ambassador for the Python project.

Typically a core team member will offer you the chance to gain commit privilege.
The person making the offer will become your mentor and watch your commits for
a while to make sure you understand the development process. If other core
developers agree that you should gain commit privileges you are then extended
an official offer. How core team members come to that agreement are outlined in
:pep:`13`.


Gaining commit privileges
=========================

After a candidate has demonstrated consistent contributions, commit privileges
are granted through these steps:

#. A core team member (submitter, usually the mentor) starts a poll
   (see the :ref:`template <coredev-template>` below) in
   the `Committers category`_ on the `Python Discourse`_.

   - open for 7 days
   - results shown only upon closing

#. If the candidate receives at least two-thirds positive votes when the poll closes
   (as per :pep:`13`), the submitter `emails the steering council
   <mailto:steering-council@python.org>`_ with the candidate's email address
   requesting that the council either accept or reject the proposed membership.  Technically, the
   council may only `veto a positive vote <https://peps.python.org/pep-0013/#membership>`_.

#. Assuming the steering council does not veto the positive vote, a member of the council or its
   delegate (approver, usually in practice a :ref:`Developer-in-Residence <current owners>`) will
   email the candidate:

   - A request for account details as required by
     `🔒 python/voters <https://github.com/python/voters>`_.
   - A reminder about the `Code of Conduct`_ and guidance on reporting issues
     to the PSF Conduct WG.

#. Once the candidate has provided the pertinent details, the approver will:

   - Enable the various new privileges.
   - Remove the new committer from the triage team, if applicable.
   - Add their details to `🔒 python/voters <https://github.com/python/voters>`_.
   - Once the python/voters update is merged, regenerate the public team membership
     list at :ref:`developers`.
     See "Public list of members" in the ``voters`` README.
   - Post an announcement in the `Committers Discourse category
     <https://discuss.python.org/c/committers/5>`_.  The past few announcements
     were in the form of a separate post on the already open topic with
     the poll.

Getting a python.org email address
----------------------------------

Members of the core team can get an email address on the python.org domain.
For more details refer to the `python.org email policy
<https://www.python.org/psf/records/board/policies/email/>`_.


Poll template
=============

.. _coredev-template:

While Discourse uses Markdown for formatting, the poll functionality is
custom and somewhat resembles BBcode. There's a creator for polls in the
UI (click the cog icon in the edit box toolbar and choose "Build Poll").
Here's what it outputs, you can copy and paste it for your poll:

.. code-block:: bbcode

   [poll type=regular results=on_close public=false chartType=bar groups=committers close=2024-07-15T21:15:00.000Z]
   * Promote Basil Fawlty
   * Do not promote
   [/poll]

The important options in the poll builder set to get this result:

- Show who voted: **disabled** (``public=false``)
- Limit voting to these groups: **committers** (``groups=committers``)
- Automatically close poll: **in 7 days** (``close=...``)
- Show results: **When poll is closed** (``results=on_close``)

.. raw:: html

    <script>
    for (let span of document.querySelectorAll('span')) {
      if (span.textContent === '2024-07-15T21:15:00.000Z') {
         const nextWeek = new Date();
         nextWeek.setDate(nextWeek.getDate() + 7);
         nextWeek.setSeconds(0);
         nextWeek.setMilliseconds(0);
         span.textContent = nextWeek.toISOString();
         break;
      }
    }
    </script>

.. _Code of Conduct: https://policies.python.org/python.org/code-of-conduct/
.. _Committers category: https://discuss.python.org/c/committers/5
.. _Python Discourse: https://discuss.python.org
