Software Bill-of-Materials (SBOM)
=================================

Software Bill-of-Materials (abbreviated as "SBOM") is a document for sharing
information about software and how it's been composed. This format is used
most often in the security space for checking software and its dependencies
for vulnerabilities using vulnerability databases like
`CVE <https://www.cve.org/>`_ and `OSV <https://osv.dev/>`_. The SBOM format
that the CPython project uses is `SPDX <https://spdx.github.io/spdx-spec/v2.3/>`_
which can be transformed into other formats if necessary by consumers.

There are multiple sources of third-party dependencies for CPython.
Some are vendored into the source code of CPython itself (like ``mpdecimal``
vendored at :cpy-file:`Modules/_decimal/libmpdec`) or they could be optionally pulled
in during builds like Windows using dependencies from the
`python/cpython-source-deps <https://github.com/python/cpython-source-deps>`_
repository.

Whenever adding or updating a third-party dependency, an update will likely
need to be done to the SBOM in order to track the version and software identifiers.

Updating a dependency
---------------------

The SBOM for CPython's bundled dependencies is kept at
:cpy-file:`Misc/sbom.spdx.json`. Instead of updating this document directly,
there is a tool for automatically updating the document at
:cpy-file:`Tools/build/generate_sbom.py`. The recommended workflow is:

1. Update the vendored code in-place. Take note of the new version, download
   URL, and checksum of the downloaded archive.
2. Edit :cpy-file:`Misc/sbom.spdx.json` to add the new ``versionInfo``,
   ``downloadLocation``, ``checksums``, and ``externalReferences`` for the
   corresponding ``package``.
   Don't update any information in ``files`` and ``relationships`` as this will
   be generated automatically later.
3. Run ``$ make regen-sbom`` or :cpy-file:`Tools/build/generate_sbom.py`.
   Ensure that this doesn't fail with validation errors.
4. Run ``$ git diff Misc/sbom.spdx.json`` and check the diff matches the
   expected changes.
5. Commit the changes to :cpy-file:`Misc/sbom.spdx.json` along with the
   update to the dependency code.

Adding or removing a dependency
-------------------------------

When adding a dependency it's important to have the following information:

1. Name, version, and download URL of the project
2. License of the project as an `SPDX License Expression <https://spdx.org/licenses/>`_
3. Software identifiers that match values in vulnerability databases
   (`CPE <https://nvd.nist.gov/products/cpe>`_ and
   `Package URLs <https://github.com/package-url/purl-spec/blob/master/PURL-SPECIFICATION.rst>`_
   or "PURLs")

Add the information into a new entry in ``packages`` in the file
:cpy-file:`Misc/sbom.spdx.json`. If a new license ID is to be used, add the
license expression to ``ALLOWED_LICENSE_EXPRESSIONS`` in the SBOM generation tool.

When removing a dependency, remove the entry from the :cpy-file:`Misc/sbom.spdx.json`
under the ``packages`` field and then remove the corresponding entry in
:cpy-file:`Tools/build/generate_sbom.py` and then run ``make regen-sbom``.
