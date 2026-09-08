.. _threat-model:

====================
CPython Threat Model
====================

This document describes the threat model for the CPython reference implementation of the Python programming language. It defines the security boundaries, trusted capabilities, and assumptions under which CPython operates.

All security vulnerability reports submitted to the :ref:`Python Security Response Team (PSRT) <psrt>` must be evaluated against this threat model prior to submission.


Interpreter Trust Model & Assumptions
--------------------------------------

CPython operates under specific baseline assumptions regarding execution environment, trusted input, and security boundaries.

Trusted Launch Conditions
~~~~~~~~~~~~~~~~~~~~~~~~~

CPython assumes that the execution environment at interpreter startup is trusted and controlled by the legitimate system user or operator. The following are **not** considered attack vectors or security vulnerabilities:

* **Command-Line Flags & Environment Variables:** Manipulating environment variables (such as ``PYTHONPATH``, ``PYTHONHOME``, ``PYTHONSTARTUP``) or command-line arguments is assumed to be an execution privilege of the running user.
* **Local Filesystem Permissions:** Modifying installed Python packages, standard library C-extensions, or system shared libraries is an OS-level file permission issue, not a CPython vulnerability.
* **Process Memory & C API:** The C-API and extensions (e.g., :mod:`ctypes`) permit direct memory access and modification. CPython does not enforce internal isolation between C extensions or Python code running in the same process.


Sandboxing Untrusted Code
~~~~~~~~~~~~~~~~~~~~~~~~~

**CPython does not support sandboxing untrusted Python code as a security boundary.**

Features intended to execute arbitrary code (such as :func:`eval`, :func:`exec`, :mod:`pickle`, :mod:`marshal`, :mod:`shelve`, and :mod:`code`) are explicitly designed to execute Python code as supplied. Escaping a Python-based sandbox or abusing documented reflection and code execution features is not a CPython vulnerability. If sandboxing is required, it must be enforced at the OS level (e.g., via containers, seccomp, or WebAssembly).


Multi-Threading & Availability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Resource Exhaustion:** Denial of service (DoS), memory exhaustion, or CPU consumption must be triggerable with reasonably sized inputs for normal application use cases. High memory consumption resulting from processing gigabytes of data is expected.
* **Race Conditions:** Thread-safety issues are bugs, but only constitute security vulnerabilities if they lead to unexpected privilege escalation or memory corruption in standard non-sandboxed operations.


Standard Library Module Threat Models
-------------------------------------

Certain standard library modules handle untrusted data and have specific security considerations:

Network & TLS (``ssl``, ``urllib.request``, ``http.client``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Security Boundary:** The :mod:`ssl` module relies on the system's underlying OpenSSL/ LibreSSL installation. Improper TLS certificate validation or hostname verification failures are treated as security issues.
* **Untrusted Data:** Remote server responses or malicious HTTP headers should not crash the interpreter or corrupt memory.

Data Formats & Parsing (``xml``, ``json``, ``tarfile``, ``zipfile``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **XML Parsing:** Standard :mod:`xml.etree.ElementTree` and :mod:`xml.dom.minidom` are vulnerable to XML entity expansion attacks (Billion Laughs) when parsing untrusted inputs. Users requiring secure XML parsing must use defusedxml.
* **Archive Files:** Extracting untrusted archives using :mod:`tarfile` or :mod:`zipfile` without explicit path sanitization (e.g., using `filter='data'` in Python 3.12+) can overwrite arbitrary files.

Process Execution (``subprocess``, ``os``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Shell Injection:** Using ``shell=True`` in :mod:`subprocess` with unsanitized user inputs exposes applications to shell injection. Passing arguments as a list with ``shell=False`` is the intended secure usage.


See Also
--------

* :ref:`security-policy`
* :ref:`psrt`
