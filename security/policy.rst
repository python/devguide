===============
Security Policy
===============

Python Security Response Team (PSRT) members balance this work against
many other responsibilities. Please be thoughtful about the time and attention
your report requires.  Repeated failure to respect the security policy will
result in future reports being rejected or being banned from the ``python``
GitHub organization, regardless of technical merit.

What types of bugs are vulnerabilities?
---------------------------------------

Not all bugs are vulnerabilities. To avoid causing
duplicate work for PSRT members all potential reports
must be evaluated against the relevant threat models
prior to being submitted to the PSRT.
Where possible, cite the relevant threat model to show that
the threat model has been considered while determining whether
to report a bug as a vulnerability.

Vulnerabilities must be exploitable from code, configurations,
pre-conditions, and deployments that might feasibly exist in
the real world. For example, a vulnerability only affecting code
that does not make sense in a production program
will not be accepted as a vulnerability.

Documented functionality will not be considered a vulnerability.
For example, :mod:`pickle`, :mod:`marshal`, :mod:`shelve`, :mod:`eval`,
and :mod:`exec` are documented to execute arbitrary Python code that is supplied
as data. The :mod:`ctypes` module is documented to enable modifying arbitrary
locations in memory.

Vulnerabilities must not depend on malicious control of Python's launch
conditions, including command line arguments, environment variables, or
modifications to files on the target system. We assume that, at the time Python
is executed, the environment is as intended by the legitimate user, and any
malicious variation from this cannot be mitigated by Python itself.

Vulnerabilities that affect availability (such as DoS, ReDoS) must be
triggerable with data inputs that are reasonably sized for the use-case.
Availability vulnerabilities must also demonstrate an "upward" change in posture
for the attacker, rather than a "lateral" change in posture.
This is to avoid handling performance improvements as security vulnerabilities.

Vulnerabilities in dependencies of Python (such as zlib, Tcl/Tk, or OpenSSL)
are not vulnerabilities in Python unless Python's use of the dependency
interferes with secure use of the dependency.
For example, a vulnerability in the bundled copy of zlib in Python is a
vulnerability in zlib, not Python.

What versions of Python are accepting reports?
----------------------------------------------

Python accepts security vulnerabilities and will
assign CVE IDs for `supported Python versions <branchstatus>`_ that have a status of
`"bugfix" or "security" <version-status-key>`_. Versions that are not yet
stable (status of `"feature" or "prerelease" <version-status-key>`_) are not
eligible for CVE IDs. If the vulnerability only exists in prerelease versions
(alphas, betas, release candidates), then the issue should be reported as a
regular bug.
Prior to submitting a report, check whether the issue has already been
resolved on the ``main`` branch and only requires backporting.

Sometimes features may be marked as
"experimental" in Python, even in a stable Python version.
These features are not eligible for security vulnerabilities.
Instead open a public GitHub issue.

If a vulnerability is platform-dependent, check if the platform is
supported per :pep:`11`.
Vulnerabilities that exclusively affect unsupported platforms
may not be accepted.

What to include and how to structure a vulnerability report?
------------------------------------------------------------

For your vulnerability report to be handled efficiently by
the PSRT, the report must include certain information and
be formatted correctly:

* For the initial report and follow-up communications, avoid
  overly long, verbose, or excessive structure (such as headers or tables).
  Ideally reports should be a few sentences describing the vulnerability and
  a proof-of-concept script that reproduces the issue and provides a clear
  indication whether the vulnerability is still present (such as exiting with
  ``1`` if vulnerable and ``0`` if not vulnerable).
* When reporting large numbers or "batches" of vulnerabilities or
  searching for potential vulnerabilities using an LLM, you as a reporter must
  verify the validity of all reports prior to submission to the PSRT.
  PSRT members WILL NOT spend time confirming the validity of reports, only
  whether a valid bug report is a vulnerability or not.
* Do not include severity or CVSS information in your initial report,
  this information will be determined by the PSRT.
* Ideally, include a minimal patch with the mitigation for the report.
* If the vulnerability only affects certain Python versions, optionally
  include the versions of Python that are affected.
* Reports that do not contain a potential security vulnerability (such as spam
  or requesting compliance or due-diligence work)
  will be discarded without a reply.

How to submit a vulnerability report?
-------------------------------------

Submit all potential security vulnerability reports for CPython
to GitHub Security Advisories
by `opening a new ticket <GHSA>`__.
Do not open a public GitHub issue to report a security vulnerability.
For all other projects (such as pip, python.org and tools) or if you're
not sure where to send your report, send an email to
`security@python.org <mailto:security@python.org>`__.

Here's what to expect for how a vulnerability report will be handled:

* Reporter reports the vulnerability privately to the PSRT.
* If the PSRT determines the report isn't a vulnerability, the issue
  can be opened in the public issue tracker.
* If the PSRT determines the report is a vulnerability, the PSRT will
  accept your report and a CVE ID will be assigned by the PSF CNA.
* Once a public pull request containing a fix is merged to CPython,
  the advisory and CVE record will be published with attribution.

For more information about how the PSRT handles vulnerabilities,
`consult the Python Developer Guide <psrt-vulnerability-process>`__.

PSF Code of Conduct
-------------------

Well-being and safety of the Python Security Response Team members is
prioritized over the technical merit of vulnerability reports.
Despite communications being private, vulnerability reporting is subject
to the `PSF Code of Conduct`_. Violations will be reported to the Code of Conduct
team with undisclosed vulnerability information removed, if applicable.

.. _GHSA: https://github.com/python/cpython/security/advisories/new
.. _PSF Code of Conduct: https://policies.python.org/python.org/code-of-conduct/

CVE Numbering Authority (CNA)
-----------------------------

The Python and pip projects are scoped under the
`Python Software Foundation CVE Numbering Authority <CNA>`__
(CNA). This means you must submit all security
vulnerability reports to the PSRT to receive
a CVE ID for Python or pip. To reach the PSF
CNA contact directly, send an email to
`cna@python.org <mailto:cna@python.org>`__.

.. _CNA: https://www.python.org/cve-numbering-authority/
