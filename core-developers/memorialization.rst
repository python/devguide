.. _memorialize-core-developer:

===============
Memorialization
===============

Rationale
=========

When a core developer passes away, memorializing accounts helps create
a space for remembering the contributor and protects against attempted
logins and fraudulent activity.

The process
===========

The memorialization process is performed by a member of the PSF staff
with administrative access to current and historical systems where
core developers have access.

After the status of the core developer in question is confirmed,
access to the systems listed below is revoked and some changes are
made to how the user displays to others.

To respect the choices that someone made while alive, we aim to preserve
content of their accounts without changes after they've passed away.
To support the bereaved, in some instances, we may remove or change
certain content when the legacy contact or family members request it.

GitHub
------

* The user is removed from the `python/ <https://github.com/orgs/python/>`_
  organization on GitHub;
* The user is removed from the `psf/ <https://github.com/orgs/psf/>`_
  organization on GitHub;
* The user is removed from the `pypa/ <https://github.com/orgs/pypa/>`_
  organization on GitHub.

The PSF staff does not follow up with GitHub with regards to GitHub account
cancellation as this action is reserved for next-of-kin or designated by
the deceased GitHub user to act as an account successor.

The general policy regarding deceased users on GitHub is described
`here <https://docs.github.com/en/site-policy/other-site-policies/github-deceased-user-policy>`_.

Repositories in the organization
--------------------------------

* The user's GitHub handle is removed from ``/.github/CODEOWNERS``.
  To see all that need action, perform
  `this query <https://github.com/search?q=org%3Apython+path%3A**%2F.github%2FCODEOWNERS+USERNAME&type=code>`_.
* The user is marked as deceased in the private
  `voters/python-core.toml <https://github.com/python/voters/blob/main/python-core.toml>`_
  file with the ``left=`` field set to the day of passing, if known.

discuss.python.org
------------------

* The user's "custom status" is set to 🕊 ``in memoriam``;
* The user's "about me" is amended with ``$firstname passed away on $date. [In memoriam.]($in_memoriam_post_url)``;
* In the user's security "recently used devices" the staff member
  chooses "Log out all";
* In the user's permissions the staff member chooses "Deactivate account";
* The user's trust level is reset to ``1: basic user`` (trust level 0
  doesn't allow links in "About Me");
* The user's "associated accounts" (like GitHub) that provide an
  alternative login method, are all disconnected;
* The user's API keys are revoked;
* The user's admin or moderator right is revoked;
* The user's primary email address is reset to
  ``USERNAME@in-memoriam.invalid`` and secondary email addresses are
  removed (this step requires the administrator to contact Discourse.org
  staff via ``team@discourse.org``).

The "in memoriam" Discourse topic mentioned above is best created by
a community member close to the deceased.

The general best practice for deceased community members on
Discourse-powered forums is described `here <https://meta.discourse.org/t/best-practices-for-deceased-community-members/146210>`_.

python.org email account
------------------------

The PSF staff member emails ``postmaster@python.org`` to ask the email
administrator to:

* remove SMTP access from ``USERNAME@python.org``;
* reset the password to POP3/IMAP for ``USERNAME@python.org``;
* disable email forwarding, if set up, for ``USERNAME@python.org`` and
  leave a record permanently as "in memoriam" to avoid future account
  name reuse;
* remove this email from all mailing lists under ``@python.org``;
* remove any known alternate emails for the same user from all mailing
  lists under ``@python.org``.

In case the email shutdown causes issues for the estate executors, the
PSF will reasonably try to help if contacted directly.

python.org admin
----------------

* The user's account (``/admin/users/user``) is deactivated (NOT deleted)
  and their staff and superuser status is unchecked;
* The user's password is reset to a long random string;
* The user's primary email address is set to
  ``USERNAME@in-memoriam.invalid`` and set as unverified;
* The user's secondary email addresses are deleted;
* The user's API keys (both on the account and ``tastypie``) are deleted;
* The user's "I would like to be a PSF Voting Member" field is cleared.

devguide.python.org
-------------------

* The user is marked as deceased in `developers.csv <https://github.com/python/devguide/blob/main/core-developers/developers.csv>`_;
* The user is removed from the `Experts Index <https://github.com/python/devguide/blob/main/core-developers/experts.rst>`_.

bugs.python.org
---------------

While the issue tracker was migrated to GitHub, the Roundup instance
is still up for historical purposes.

* the PSF staff member logs into ``bugs.nyc1.psf.io``;
* the PSF staff member runs ``roundup-admin`` to set the user's email
  address to ``USERNAME@in-memoriam.invalid``;
* the user's alternate emails are removed;
* the user's password is reset to a long random string;
* the PSF staff member removes any active login sessions from Postgres.

Other PSF-related infrastructure
--------------------------------

* The PSF staff member notifies administrators of the Python Core Devs
  Discord server to remove the user from the server. The PSF staff
  does not follow up with Discord with regards to Discord account
  cancellation. The general policy regarding deceased users on Discord
  is available `here <https://support.discord.com/hc/en-us/articles/19872987802263--Deceased-or-Incapacitated-Users>`_.

* The user is removed from Salt configuration for the PSF infrastructure
  in `/pillar/base/users <https://github.com/python/psf-salt/tree/main/pillar/base/users>`_
  that allows SSH access to PSF-controlled servers.

* The user might have ran a buildbot worker. The PSF staff member will
  look for that in the
  `buildmaster-config <https://github.com/search?q=repo%3Apython%2Fbuildmaster-config%20USERNAME&type=code>`_
  repository.

PyPI
----

* The PSF staff member notifies PyPI admins by emailing them at
  ``admin@pypi.org`` to mark the user as inactive, remove their email
  addresses, prohibit their password resets, and revoke all API keys.
