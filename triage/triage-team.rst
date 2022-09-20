.. _triage-team:
.. _triagers:

===========
Triage Team
===========

The Python triage team is a group dedicated towards improving workflow
efficiency through thoughtful review and triage of open issues and pull
requests. This helps contributors receive timely feedback and enables core
developers to focus on reviewed items which reduces their workload. The
expectations of this role expand upon the "Triager" role on the
:ref:`issue tracker <tracker>`. The responsibilities listed below are primarily centered
around the Python GitHub repositories. This extends beyond CPython, and, as
needed, to other repos such as devguide and core-workflow.

Responsibilities include:

* PR/issue management
    - Reviewing PRs
    - Assisting contributors
    - Notifying appropriate core developers
* Applying appropriate labels to PRs/Issues
    - Skip news
    - Skip issue
    - Good first issue
    - Other categorizations

Although triagers have the power to close PRs, they should generally not do so
without first consulting a core developer. By having triagers and core developers work together,
the author receives a careful consideration of their PR. This encourages future
contributions, regardless of whether their PR is accepted or closed.

Nonetheless, triagers should feel free to close a PR if they judge that the
chance of the PR being merged would be exceedingly low, even if substantial
revisions were made to the PR. This includes (but is not limited to) the
following:

* PRs proposing solely cosmetic changes
* PRs proposing changes to deprecated modules
* PRs that are no longer relevant. This includes:
    - PRs proposing fixes for bugs that can no longer be reproduced
    - PRs proposing changes that have been rejected by Python core developers
      elsewhere (e.g. in an issue or a PEP rejection notice)

If a triager has any doubt about whether to close a PR, they should consult a core
developer before taking any action.

Triagers can also make use of the ``invalid`` and ``stale`` labels to suggest that a
PR may be suitable for closure. For more information, see the
:ref:`GitHub PR labels <github-pr-labels>` section.

Note that it is of paramount importance to treat every contributor to the Python
project kindly and with respect. Regardless of whether they're entirely new
or a veteran core developer, they're actively choosing to voluntarily donate their
time towards the improvement of Python. As is the case with any member of
the Python Software Foundation, always follow the `PSF Code of Conduct`_.

.. _PSF Code of Conduct: https://www.python.org/psf/conduct/


Becoming a member of the Python triage team
===========================================

All Python core developers are welcome to invite a Python contributor to the
Python triage team. Triagers will be responsible to handle not just issues, but
also pull requests, and even managing backports. A Python triager has access to
more repositories than just CPython.

When you have consistently shown the ability to properly
help triage issues without guidance, you may request that you
be given the "Triager" role on the :ref:`issue tracker <tracker>`. You can make the request
to any core developer. If they decide you are ready
to gain the extra privileges on the tracker they will then act as a mentor to
you until you are ready to do things entirely on your own. There is no set rule
as to how many issues you need to have helped with before or how long you have
been participating. The key requirements are that you show the desire to
help, you are able to work well with others (especially those already with the
Triager role), and that have a firm grasp of how to do things on the issue
tracker properly on your own.

Gaining the Triager role will allow you to set any value on any issue in the
tracker, releasing you from the burden of having to ask others to set values on
an issue for you in order to properly triage something. This will not only help
speed up and simplify your work in helping out, but also help lessen the
workload for everyone by gaining your help.

Any existing active contributor to the Python repository on GitHub can
transition into becoming a Python triager. They can request this to any core
developer, either confidentially via a DM in Discourse, or
publicly by opening an `issue in the core-workflow repository
<https://github.com/python/core-workflow/issues/new?template=triage_membership.md>`_.
If the core devloper decides you are ready to gain the extra privileges on the
tracker, they will ask a :ref:`Python organization admin <current owners>`
to invite you to the Python organisation, and then  act as a mentor to you until
you are ready to do things entirely on your own.

For every new triager, it would be great to announce them in the
`Committers category <https://discuss.python.org/c/committers/5>`_
on the `Python Discourse <https://discuss.python.org/>`_
(`example announcement
<https://discuss.python.org/t/abhilash-raj-has-been-granted-triage-role-on-github/2089>`__).
