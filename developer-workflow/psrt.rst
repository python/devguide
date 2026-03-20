Python Security Response Team (PSRT)
====================================

The Python Security Response Team (PSRT) is responsible for handling
vulnerability reports for CPython and pip.

Members
-------

The PSRT publishes a full
list of members and admins, included in the table below:

.. csv-table::
   :header: "Name", "GitHub username", "Notes"
   :file: psrt.csv
   :encoding: "utf-8"

How can I join the PSRT?
~~~~~~~~~~~~~~~~~~~~~~~~

Anyone can join the PSRT following a nomination process
`similar to core team nominations`_. Nomination for a new member
is brought to the PSRT by an existing PSRT member and then
this nomination is voted on by existing PSRT members.
The nomination succeeds if the nomination receives at least
two-thirds positive votes from a vote of existing PSRT members
that is open for one week and not vetoed by the Steering Council.

Once per year the Steering Council will receive a report of inactive members
of the PSRT with the recommendation to remove the inactive users from the PSRT.
“Inactive” is defined as a member who hasn’t coordinated or commented on a
vulnerability report in the past year since the last report was generated.
The Steering Council may remove members of the PSRT with a simple vote.

Members of the PSRT who are a Release Manager or Steering Council member may
remain in the PSRT regardless of inactivity in vulnerability reports.

.. _similar to core team nominations: https://devguide.python.org/core-team/join-team/

Responsibilities of PSRT members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below are the responsibilities of PSRT members:

* Being knowledgeable about typical software vulnerability report handling
  processes, such as CVE IDs, patches, coordinated disclosure, embargoes.
* Not sharing or acting on embargoed information about the reported
  vulnerability. Examples of disallowed behavior include sharing information
  with colleagues or publicly deploying unpublished mitigations or patches ahead
  of the advisory publication date.
* Acting as a “Coordinator” of vulnerability reports that are submitted to
  projects. A Coordinator’s responsibility is to move a report through the PSRT
  process to a “finished” state, either rejected or as a published advisory and
  mitigation, within the industry standard timeline of 90 days.
* As a Coordinator, involving relevant core team members or triagers where
  necessary to make a determination whether a report is a vulnerability and
  developing a patch. Coordinators are encouraged to involve members of the core
  team to make the best decision for each report rather than working in isolation.
* As a Coordinator, calculating the severity using CVSSv4 and authoring advisories
  to be shared on `security-announce@python.org`_. These advisories are used for
  CVE records by the `PSF CVE Numbering Authority`_.
* Coordinators that can no longer move a report forwards for any reason must
  delegate their Coordinator role to someone else in the PSRT.

.. _security-announce@python.org: https://mail.python.org/archives/list/security-announce@python.org/
.. _PSF CVE Numbering Authority: https://www.python.org/cve-numbering-authority/

Responsibilities of PSRT admins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PSRT members who are designated as admins by the Steering Council have the
following additional responsibilities:

* Triaging the ``security@python.org`` mailing list.
* Managing PSRT membership access including the GitHub team, the mailing list,
  and Discord channel, to ensure they are synchronized with the canonical list
  of PSRT members.
* On a yearly basis, providing the Steering Council with a report including a
  list of inactive PSRT members.
* Running nomination elections, including counting final votes and giving
  the Steering Council an opportunity to veto nominations via email.

Triaging a vulnerability report
-------------------------------

PSRT members coordinate reports from when they are first submitted
to a "finished" state. Finished states include
marking a report as a "non-issue", opening a public issue on GitHub,
or a merged patch with an accompanying CVE and advisory to
``security-announce@python.org``. Reports should reach a finished
state within 90 days of being received by the PSRT.

Reports enter the system through ``security@python.org`` or
on a project GitHub Security Advisory (GHSA) ticketing system.
For projects that use GHSA, reports to ``security@python.org``
should have reporters `re-open their report using GHSA`_.

.. raw:: html
   :file: ../_static/psrt-coordinator-report.html

.. _re-open their report using GHSA: #submit-using-github-security-advisories

New report in GitHub Security Advisories (GHSA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once a report is in GHSA, a "Coordinator" must be assigned
to be responsible for moving the report through the process.
The "Coordinator" role is assigned using a "Credit" in a GHSA ticket
(Select 'Edit' > 'Credit' > Add GitHub username and the role 'Coordinator').

.. warning::
   Assigning the "Coordinator" role to each GHSA ticket is important,
   as this metadata records whether a PSRT member is
   `"active" according to PEP 811`_ to avoid being removed due to inactivity.

.. _"active" according to PEP 811: https://peps.python.org/pep-0811/#psrt-membership-policy

If a GHSA ticket is idle for three days without a coordinator
assigned a PSRT member who is not a Release Manager
or Steering Council member will be automatically assigned
as coordinator by the PSRT bot.
If a coordinator can't complete the process
they must find a replacement coordinator in the PSRT
and re-assign the GHSA ticket.

.. raw:: html
   :file: ../_static/psrt-coordinator-triage.html

Determining whether a report is a vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The coordinator will make a determination about a report, either
marking the ticket as a non-issue, as an issue that isn't a security
vulnerability, or as a security vulnerability. If the Coordinator needs
help from core team experts in making the determination, the
experts may be added as 'Collaborators' to the GHSA ticket.
Accepted security vulnerabilities will be moved to the 'Draft' state in GHSA.

If the report isn't a vulnerability, coordinators close the GHSA ticket
after optionally opening a public GitHub issue. Note that reporters often
will not open a GitHub issue on their own, as there is no longer an incentive
for them to do so without a CVE being assigned.

Remediating a vulnerability report
----------------------------------

Once a report has been accepted as a vulnerability, the remediation
development process begins. Coordinators move the GHSA ticket to a 'Draft'
state using the green 'Accept as Draft' button. Once in this state,
the PSRT bot will automatically assign a CVE ID from the Python Software
Foundation CVE Numbering Authority.

Once a vulnerability has been accepted there are three things
the Coordinator must prepare before sending an advisory and
closing the GHSA ticket:

* Severity calculated using CVSSv4.
* Pull request containing the fix merged with a public GitHub issue.
* Advisory title and short description of the vulnerability.

Severity scoring
~~~~~~~~~~~~~~~~

Severity of a vulnerability can be difficult to assess
objectively due to not knowing how software is used
in all situations. Severity is calculated from expected
or known use, not from worst-case hypothetical scenarios.

The PSRT and PSF CNA use `CVSSv4`_ for calculating
the severity of a vulnerability. GHSA tickets provide a
CVSSv4 calculator within the ticket UI. Note that GitHub defaults to CVSSv3,
change the scoring algorithm to CVSSv4 before scoring in the ticket UI.
As with all aspects of PSRT operations, coordinators are encouraged to ask
for help in calculating a severity from other PSRT members.

.. _CVSSv4: https://www.first.org/cvss/v4.0/

Developing a patch privately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Patch development can initially be done privately by selecting the
'Start a temporary private fork' button within the GHSA ticket. Note that
due to the size of Git repositories, this fork repository may
take several minutes to create. Once the fork has been created any PSRT member
or GHSA collaborator can clone the fork and develop a fix and push a branch:

.. code-block:: shell

    git clone https://github.com/python/cpython-ghsa-abcd-efgh-ijkl.git
    cd cpython-ghsa-abcd-efgh-ijkl
    git checkout -b advisory-fix-1

    # (develop a fix)

    git add ...
    git commit -m "Fix"
    git push origin advisory-fix-1

From here a pull request can be opened within the GHSA ticket
to be reviewed privately. The coordinator can add core team experts
as collaborators as necessary to the GHSA to develop the patch and to review
the patch if the expertise for patch development or review
aren't available within PSRT. Coordinators are not necessarily responsible
with developing patches themselves: only with seeing that a patch is
developed in a timely fashion by involving experts as necessary.

Once the patch has been approved
a public GitHub issue and pull request can be opened.
Generate a blurb in the category ``Security`` for the public pull request.
Public issues and pull requests for security fixes should use the
:gh-label:`type-security` label.

To quickly pull a patch file from a GHSA pull request, you
can append ``.patch`` to the pull request URL, like so:

.. code-block:: shell

   curl https://github.com/python/cpython-ghsa-abcd-efgh-ijkl/pull/1.patch \
        --output ghsa-abcd-efgh-ijkl.patch

This patch can then be applied and pushed to the public GitHub repository:

.. code-block:: shell

    git remote -v
    origin    ssh://git@github.com/.../cpython (fetch)
    origin    ssh://git@github.com/.../cpython (fetch)

    git checkout -b branch-name
    git apply ./ghsa-abcd-efgh-ijkl.patch
    git push origin branch-name

.. warning:: **IMPORTANT:** CPython's backport infrastructure
    is used for tracking backported patches. Use **one GitHub issue
    per CVE** to accurately track backports of vulnerability fixes.
    For new CVEs, even when related to a previous issue, **open a
    new GitHub issue** to accurately track fixed versions.

.. warning:: **IMPORTANT:** Don't select the green 'Merge pull request'
    or 'Publish advisory' buttons within GHSA. Advisories are published
    to the mailing list, and the 'Merge pull request' button within
    GHSA bypasses all continuous integration and branch protection
    steps. Use a public pull request instead.

Publishing an advisory
~~~~~~~~~~~~~~~~~~~~~~

Once the vulnerability fix has been merged into the main branch via a
public GitHub pull request, an advisory must be published.
The advisory requires the severity,
a title, and a short description of the vulnerable module, functions,
behavior and fix. This short description can optionally include mitigation steps
if applying the patch isn't the only way to mitigate the vulnerability.

* Send an email to the ``security-announce@python.org`` mailing list
  using the `advisory template`_, including title, severity, description.
* The advisory email will be received by PSF CVE Numbering Authority
  operators and used to publish a CVE record.
* Begin the backporting process for all Python branches still receiving
  security updates. Add the :gh-label:`type-security` and :gh-label:`release-blocker` labels
  to each backport pull request so that release managers can find them prior
  to releasing.

After an advisory email is sent, the GHSA ticket can be closed.

.. _advisory template: #advisory-email

Handling code signing certificate reports
-----------------------------------------

Python signs binaries using Azure Trusted Signing and Apple Developer ID
certificates. If a code signing certificate is reported as "compromised" or
"malware signed with certificate", the Python Security Response Team must
request the following information from the reporter:

* Checksum(s) of binaries signed by certificate.
* Signature(s) of binaries signed by certificate.

To avoid unnecessary user confusion and churn around revoking code signing
certificates, any reports **must be verifiable independently by the PSRT before
taking destructive actions**, such as revoking certificates. With this
information the PSRT can take investigative steps to verify the report, such as:

* Downloading and checking artifacts from the associated Azure Pipelines
  executions against the reported list of checksums.
* Verifying the validity of the signatures. `Past reports
  <https://discuss.python.org/t/103356/2>`__ have contained signatures that
  purported to be from Python code signing certificates, but were not valid.
* Checking the Azure Pipelines and Azure Trusted Signing audit logs for signs of
  compromise.

If any signs of compromise or incorrectly signed binaries are discovered by the
PSRT, only then will certificates be revoked and an advisory published.
If compromise is reported, the following non-destructive actions can be taken by
the PSRT without verifying the reported information as a precaution, if
relevant:

* Rotating secrets associated with code signing (``TrustedSigningSecret`` for
  Azure Trusted Publishing).
* Resetting passwords for accounts with access to signing certificates.

Template responses
------------------

These template responses should be used as guidance for messaging
in various points in the process above. They are not required to be sent as-is,
please feel free to adapt them as needed for the current context.

Submit using GitHub Security Advisories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. highlight:: none

::

   Thanks for submitting this report.
   We use GitHub Security Advisories for triaging vulnerability reports,
   please submit your report here:

   https://github.com/python/cpython/security/advisories/new

Rejecting a vulnerability report
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   Thanks for your report. We've determined that the report doesn't constitute
   a vulnerability. Let us know if you disagree with this determination.
   If you are interested in working on this further, you can optionally open a
   public issue on GitHub.

Advisory email
~~~~~~~~~~~~~~

::

   Title: [{CVE-YYYY-XXXX}] {title}

   There is a {LOW, MEDIUM, HIGH, CRITICAL} severity vulnerability affecting {project}.

   {description}

   Please see the linked CVE ID for the latest information on affected versions:

   * https://www.cve.org/CVERecord?id={CVE-YYYY-XXXX}
   * {pull request URL}
