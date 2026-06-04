===============
Security policy
===============

.. important::

   :ref:`Python Security Response Team <psrt>` (PSRT) members balance this work
   against many other responsibilities. Please be thoughtful about the time and
   attention your report requires. Repeated failure to respect the security policy
   will result in future reports being rejected, or the reporter being banned
   from the ``python`` GitHub organization, regardless of technical merit.

What types of bugs are vulnerabilities?
---------------------------------------

**Not all bugs are vulnerabilities.**

To avoid causing duplicate work for PSRT members, **all potential** reports
must be evaluated against the relevant threat models
prior to being submitted to the PSRT.
Where possible, cite the relevant threat model to show that
the latter has been considered while determining whether
to report a bug as a vulnerability.

Vulnerabilities must be exploitable from code, configurations,
pre-conditions, or deployments that may exist in the real world.
A vulnerability that only affecting code
unlikely to be used in a production program
will not be accepted.

Documented functionality is not considered a vulnerability.
For example, :mod:`pickle`, :mod:`marshal`, :mod:`shelve`, :func:`eval`,
and :func:`exec` are documented to execute arbitrary Python code that is
supplied as data. The :mod:`ctypes` module is documented to enable modifying
arbitrary locations in memory.

Vulnerabilities must not depend on malicious control of Python's launch
conditions, including (but not limited to) command line arguments, environment variables, or
modifications to files on the target system. We assume that, at the time Python
is executed, the environment is as intended by the legitimate user, and any
malicious variation from this cannot be mitigated by Python itself.

Vulnerabilities that affect availability (such as DoS, ReDoS, crashes,
dead-locks, and resource exhaustion) must be
triggerable with data inputs that are reasonably sized for the use case.
Availability vulnerabilities must also demonstrate an "upward" change in posture
for the attacker, rather than a "lateral" one.
This is to avoid handling performance improvements as security vulnerabilities.

Vulnerabilities in dependencies of Python (such as zlib, Tcl/Tk, or OpenSSL)
are not vulnerabilities in Python unless Python's use of the dependency
interferes with secure use of the dependency.
For example, a vulnerability in the bundled copy of zlib in Python is a
vulnerability in zlib, not Python.

What versions of Python accept reports?
---------------------------------------

Python accepts vulnerability reports and will
assign CVE IDs for :ref:`supported Python versions <branchstatus>` that have a
status of :ref:`"bugfix" or "security" <version-status-key>`. Versions that are
not yet stable (status of :ref:`"feature" or "prerelease" <version-status-key>`)
are not eligible for CVE IDs. If the vulnerability only exists in prerelease
versions (alphas, betas, release candidates), then the issue should be reported
as a regular bug.
Prior to submitting a report, check whether the issue has already been
resolved on the ``main`` branch and only requires backporting.

Sometimes features may be marked as
"experimental" in Python, even in a stable Python version.
These features are not eligible for security vulnerabilities.
Instead, open a public GitHub issue.

If a vulnerability is platform-dependent, check if the platform is
supported per :pep:`11`.
Vulnerabilities that exclusively affect unsupported platforms
are not treated as vulnerabilities in Python.

As per the :pep:`Unsupported Platforms section of PEP 11 <11#unsupported-platforms>`,
porting Python to an unsupported platform is treated as a third-party project.
For these reports, the PSRT treats them as vulnerability reports for a third-party
port, not as Python vulnerabilities.
If you choose to report such an issue to Python, follow the requirements
of this guide and include the relevant platform and maintainer context.
The PSRT forwards these reports to platform maintainers (or other interested
parties) and they are usually handled under the relevant maintainers' security
policies. These reports will be closed if the maintainers are unknown or unresponsive.

What to include and how to structure a vulnerability report?
------------------------------------------------------------

For your vulnerability report to be handled efficiently by
the PSRT, the report must include certain information and
be formatted correctly:

* For the initial report and follow-up communications, avoid
  overly long, verbose, or excessive structure (such as headers or tables).
  Reports should be a few sentences describing the vulnerability. Ideally include
  a proof-of-concept script that reproduces the issue and provides a clear
  indication of whether the vulnerability is still present (such as exiting with
  ``1`` if vulnerable and ``0`` if not vulnerable).
* When reporting large numbers or "batches" of vulnerabilities or
  searching for potential vulnerabilities using an LLM, you as a reporter must
  verify the factual validity (such as whether APIs have been hallucinated)
  of the content in all reports prior to submission to the PSRT.
* Do not include severity or CVSS information in your initial report,
  this information will be determined by the PSRT.
* Ideally, include a minimal patch with the mitigation for the report.
* Always include the versions of Python that were tested,
  and indicate which were found to be vulnerable.
* Submit reports as plain-text only, including attachments.
  No PDFs, binaries, notebooks, or other files that cannot be safely reviewed.
  If your proof-of-concept depends on a specially constructed binary file,
  please include a script to construct it rather than the file itself.
* Proof-of-concept scripts longer than a few lines should be wrapped with a
  `collapsed section`_ using ``<details></details>`` for better readability.
* Reports that do not contain a potential security vulnerability (such as spam
  or requesting compliance or due-diligence work)
  will be discarded without a reply.

.. _collapsed section: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections

How to submit a vulnerability report?
-------------------------------------

Submit all potential security vulnerability reports for CPython
by `opening a new ticket <GHSA>`__.
Do not open a public GitHub issue to report a security vulnerability.
For all other projects (such as pip, python.org and tools) or if you're
not sure where to send your report, send an email to
`security@python.org <mailto:security@python.org>`__.

Here's what to expect for how a vulnerability report will be handled:

* Reporter reports the vulnerability privately to the PSRT.
* If the PSRT determines the report isn't a vulnerability, the reporter
   may open a public issue.
* If the PSRT determines the report is a vulnerability, the PSRT will
  accept the report and a CVE ID will be assigned by the PSF CNA.
* Once a public pull request containing a fix is merged to CPython,
  the advisory and CVE record will be published with attribution.

For more information about how the PSRT handles vulnerabilities,
see :ref:`psrt-vulnerability-process`.

Code of conduct
---------------

Well-being and safety of the Python Security Response Team members is
prioritized over the technical merit of vulnerability reports.
Despite communications being private, vulnerability reporting is subject
to the `PSF Code of Conduct`_. Violations will be reported to the Code of
Conduct team with undisclosed vulnerability information removed, if applicable.

.. _GHSA: https://github.com/python/cpython/security/advisories/new
.. _PSF Code of Conduct: https://policies.python.org/python.org/code-of-conduct/

CVE Numbering Authority (CNA)
-----------------------------

The Python and pip projects are scoped under the
`Python Software Foundation CVE Numbering Authority <CNA>`__
(CNA). This means you must submit all security
vulnerability reports to the PSRT for a CVE ID
to be issued for Python or pip. To reach the PSF
CNA contact directly, send an email to
`cna@python.org <mailto:cna@python.org>`__.

.. _CNA: https://www.python.org/cve-numbering-authority/
