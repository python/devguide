.. _triaging:

Triaging an Issue
=================

This section of the devguide documents the `issue tracker`_ for users
and developers.

Contributors with the Developer role on the `issue tracker`_ can triage issues
directly without any assistance.

Additionally, this section provides an overview of the Python triage team.

Python triage team
------------------

The Python triage team is a group dedicated towards improving workflow
efficiency through thoughtful review and triage of open issues and pull
requests. This helps contributors receive timely feedback and enables core 
developers to focus on reviewed items which reduces their workload. The 
expectations of this role expand upon the "Developer" role on the 
`issue tracker`_. The responsibilities listed below are primarily centered 
around the Python GitHub repositories. This extends beyond CPython, and, as 
needed, to other repos such as devguide and core-workflow.

Responsibilities include:

* PR/issue management
    - Renaming PRs
    - Reviewing PRs
    - Assisting contributors
    - Notifying appropriate core developers
* Applying appropriate labels to PRs/Issues
    - Skip news
    - Skip issue
    - Good first issue
    - Other categorizations

As triagers gain experience, they may have some intuition of when a PR should
be closed. Triagers can recommend closing a PR, but the final decision must be
made by a core developer. By having triagers and core developers work together,
the author receives a careful consideration of their PR. This encourages future
contributions, regardless of whether their PR is accepted or closed.

Triagers can make use of the ``invalid`` and ``stale`` labels to suggest that a
PR may be suitable for closure. For more information, see the
:ref:`GitHub PR labels <github-pr-labels>` section.

It is also of paramount importance to treat every contributor to the Python
project kindly and with respect. Regardless of whether they're entirely new
or a veteran core developer, they're actively choosing to voluntarily donate their
time towards the improvement of Python. As is the case with any member of
the Python Software Foundation, always follow the `PSF Code of Conduct`_.

Becoming a member of the Python triage team
-------------------------------------------

Any Python core developers are welcome to invite a Python contributor to the
Python triage team. Do note that the responsibilities of a Python triager
are more elevated than a developer on bpo. For example, the Python triager
has access to more repositories than just CPython. Triagers will be responsible
to handle not just issues, but also pull requests, and even managing backports.

Any existing developers on b.p.o can transition into becoming a Python triager.
They can request this to any core developer, and the core developer
can pass the request to the `Python organization admin
<https://devguide.python.org/devcycle/?highlight=organization%20admin#current-owners>`_
on GitHub. The request
can be made confidentially via a DM in Discourse, or publicly by opening
an `issue in the core-workflow repository
<https://github.com/python/core-workflow/issues/new?template=triage_membership.md>`_.

Any contributor who is not already a developer on b.p.o can also self-nominate
to be a member of Python triage team. They can request this to any core developer,
confidentially via DM in Discourse, or publicly by opening an issue in core-workflow.
If a core developer agrees and is willing to vouch for them, the core developer
can pass the request to the GitHub administrator. They should also be added as
developer on bpo.

For every new triager, it would be great to announce them in the python-committers
mailing list and core-workflow category in Discourse. `Example announcement
<https://discuss.python.org/t/abhilash-raj-has-been-granted-triage-role-on-github/2089>`_.

.. _github-pr-labels:

GitHub Labels for PRs
'''''''''''''''''''''

An important component of triaging PRs for the CPython repo involves
appropriately categorizing them through the usage of labels.

Labels for PRs include:

DO-NOT-MERGE
    Used on PRs to prevent miss-islington from being able
    to automatically merge the pull request. This label is appropriate when a PR
    has a non-trivial conflict with the branch it 

