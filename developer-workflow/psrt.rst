Python Security Response Team (PSRT)
====================================

The Python Security Response Team (PSRT) is responsible for handling
vulnerability reports for CPython and pip.

Vulnerability report triage
---------------------------

Vulnerability reports are sent to one of two locations,
the long-standing ``security@python.org`` mailing list
or using the private vulnerability reporting feature
of GitHub Security Advisories (GHSA).

For reports sent to ``security@python.org``, a PSRT admin
will triage the report and if the report seems plausible
(that is, not spam and for the correct project) will reply with
instructions on how to report the vulnerability on GitHub.

If the reporter doesn't want to use GitHub's Security Advisories feature
then the PSRT admins can create a draft report on behalf of the reporter.

Coordinating a vulnerability report
-----------------------------------

Each report will have a member of the PSRT assigned as the "coordinator".
The coordinator will be responsible for following the below process and
will be publicly credited on vulnerability records post-publication.

If a coordinator can't complete the process for any reason (time obligation,
vacation, etc.) they must find a replacement coordinator in the PSRT
and reassign the vulnerability report appropriately.

Coordinators are expected to collaborate with other PSRT members and core developers
when needed for guidance on whether the report is an actual vulnerability,
severity, advisory text, and fixes.

**The vulnerability coordination process is:**

* Coordinator will determine whether the report constitutes a vulnerability. If the report isn't a vulnerability,
  the reporter should be notified appropriately. Close the GHSA report, the report can be reopened if
  sufficient evidence is later obtained that the report is a vulnerability.

* After a vulnerability report is accepted, a Common Vulnerabilities and Exposures (CVE) ID must be assigned. If this is not done
  automatically, then a CVE ID can be obtained by the coordinator sending an email to ``cna@python.org``.
  No details about the vulnerability report need to be shared with the PSF CVE Numbering Authority (CNA) for a CVE ID to be reserved.

* If the report is a vulnerability, the coordinator will determine the severity of the vulnerability. Severity is one of:
  **Low**, **Medium**, **High**, and **Critical**. Coordinators can use their knowledge of the code, how the code is likely used,
  or another mechanism like Common Vulnerability Scoring System (CVSS) for determining a severity. Add this information to the GitHub Security Advisory.

* Once a CVE ID is assigned, the coordinator will share the acceptance and CVE ID with the reporter.
  Use this CVE ID for referencing the vulnerability. The coordinator will ask the reporter
  if the reporter would like to be credited publicly for the report and if so, how they would like to be credited.
  Add this information to the GitHub Security Advisory.

* The coordinator authors the vulnerability advisory text. The advisory must include the following information:

  * Title should be a brief description of the vulnerability and affected component
    (for example, "Buffer over-read in SSLContext.set_npn_protocols()")

  * Short description of the vulnerability, impact, and the conditions where the affected component is vulnerable, if applicable.

  * Affected versions. This could be "all versions", but if the vulnerability exists in a new feature
    or removed feature then this could be different. Include versions that are end-of-life in this calculation
    (for example, "Python 3.9 and earlier", "Python 3.10 and later", "all versions of Python").

  * Affected components and APIs. The module, function, class, or method must be specified so users can
    search their codebase for usage. For issues affecting the entire project, this can be omitted.

  * Mitigations for the vulnerability beyond upgrading to a fixed version, if applicable.

  This can all be done within the GitHub Security Advisory UI for easier collaboration between reporter and coordinator.

* The coordinator determines the fix approach and who will provide a fix.
  Some reporters are willing to provide or collaborate to create a fix,
  otherwise relevant core developers can be invited to collaborate by
  the coordinator.

  * For **Low** and **Medium** severity vulnerabilities it is acceptable
    to develop a fix in public.
    The pull request must be marked with the ``security`` and ``release-blocker``
    labels so that a release is not created without including the fix.

  * For **High** and **Critical** severity vulnerabilities the fix must be
    developed privately using GitHub Security Advisories' "Private Forks" feature.
    Core developers can be added to the GitHub Security Advisory via "collaborators"
    to work on the fix together. Once a fix is approved privately and tested,
    a public issue and pull request can be created with
    the ``security`` and ``release-blocker`` labels.

* Once the pull request is merged the advisory can be published. The coordinator will send the advisory by email
  to ``security-announce@python.org`` using the below template. Backport labels must be added as appropriate.
  After the advisory is published a CVE record can be created.

Template responses
------------------

These template responses should be used as guidance for messaging
in various points in the process above. They are not required to be sent as-is,
please feel free to adapt them as needed for the current context.

**Directing to GitHub Security Advisories:**

.. highlight:: none

::

   Thanks for submitting this report.
   We use GitHub Security Advisories for triaging vulnerability reports,
   are you able to submit your report directly to GitHub?

   https://github.com/python/cpython/security/advisories/new

   If you're unable to submit a report to GitHub (due to not having a GitHub
   account or something else) let me know and I will create a GitHub Security
   Advisory on your behalf, although you won't be able to participate directly
   in discussions.

**Rejecting a vulnerability report:**

::

   Thanks for your report. We've determined that the report doesn't constitute
   a vulnerability. Let us know if you disagree with this determination.
   If you are interested in working on this further, you can optionally open a
   public issue on GitHub.

**Accepting a vulnerability report:**

::

   Thanks for your report. We've determined that the report
   is a vulnerability. We've assigned {CVE-YYYY-XXXX} and determined
   a severity of {Low,Medium,High,Critical}. Let us know if you disagree
   with the determined severity.

   If you would like to be publicly credited for this vulnerability as the
   reporter, please indicate that, along with how you would like to be
   credited (name or organization).

   Please keep this vulnerability report private until we've published
   an advisory to ``security-announce@python.org``.

**Advisory email:**

::

   Title: [{CVE-YYYY-XXXX}] {title}

   There is a {LOW, MEDIUM, HIGH, CRITICAL} severity vulnerability
   affecting {project}.

   {description}

   Please see the linked CVE ID for the latest information on
   affected versions:

   * https://www.cve.org/CVERecord?id={CVE-YYYY-XXXX}
   * {pull request URL}
