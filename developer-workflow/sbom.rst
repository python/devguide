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
:cpy-file:`Misc/sbom.spdx.json`. When updating a dependency to a new version
you'll need to edit the version and other metadata about this dependency in
the SBOM.

The recommended workflow is:

1. Download the new dependency as an archive. Take note of the new version, download
   URL, and checksum of the downloaded archive.
2. Update the vendored code in the CPython source tree.
3. Edit :cpy-file:`Misc/sbom.spdx.json` to add the new ``versionInfo``,
   ``downloadLocation``, ``checksums``, and ``externalReferences`` for the
   corresponding ``package``. For most of these updates all that's needed is to
   update the embedded version within URLs and project identifiers.
   Don't update any information in ``files`` and ``relationships`` as this will
   be generated automatically by the SBOM tool.
4. Run ``make regen-sbom`` or ``python Tools/build/generate_sbom.py``.
   Ensure that this doesn't fail with validation errors.
5. Run ``git diff Misc/sbom.spdx.json`` and check the diff matches the
   expected changes.
6. Commit the changes to :cpy-file:`Misc/sbom.spdx.json` along with the
   update to the dependency code.

Adding a new dependency
-----------------------

When adding a dependency it's important to have the following information:

* Name, version, and download URL of the project
* License of the project as an `SPDX License Expression <https://spdx.org/licenses/>`_
* Software identifiers that match values in vulnerability databases
  (`CPE <https://nvd.nist.gov/products/cpe>`_ and
  `Package URLs <https://github.com/package-url/purl-spec/blob/master/PURL-SPECIFICATION.rst>`_
  or "PURLs")
* Paths to include and exclude in the CPython source tree corresponding to this dependency

After gathering this information:

1. Add the information into a new entry in ``packages`` in the file
   :cpy-file:`Misc/sbom.spdx.json`. Don't worry about formatting, the tool will
   auto-format your manually written JSON. The fields to fill out include:

   * ``name`` for the project name.
   * ``SPDXID`` which will be ``"SPDXRef-PACKAGE-{name}"``.
   * ``licenseConcluded`` for the SPDX license identifier of the project license.
   * ``versionInfo`` for the version of the project.
   * ``downloadLocation`` should be an HTTPS URL for the project download as an archive.
   * ``checksums[0].checksumValue`` and ``.algorithm`` will be the SHA-256
     checksum of the downloaded archive.
   * ``originator`` for the original author information, prefix with either an
     ``Organization:`` or ``Person:`` depending on the author/maintenance situation.
   * ``primaryPackagePurpose`` will likely be ``"SOURCE"``.
   * ``externalReferences`` is a list of one or more project identifiers,
     either CPE or Package URL. The value for ``referenceLocator`` must include
     the value in ``versionInfo`` to ensure the identifier
     corresponds to the correct release of the software. You can read more about
     external references in the `SPDX SBOM specification`_.
2. If a new license ID is to be used, add the license expression to
   ``ALLOWED_LICENSE_EXPRESSIONS`` in the :cpy-file:`Tools/build/generate_sbom.py`.
3. Add the paths to include and exclude into a ``PackageFiles`` instance
   with a key corresponding to the SBOM ID for the package (``SPDXID`` without the
   ``SPDXRef-PACKAGE-*`` prefix) in :cpy-file:`Tools/build/generate_sbom.py`.
4. Run the tool with ``make regen-sbom`` or ``python Tools/build/generate_sbom.py``.
   Ensure that the tool doesn't fail with any validation errors.
5. Compare the changes to :cpy-file:`Misc/sbom.spdx.json` with ``git diff``, check
   that all information appears correct.
6. Commit the changes to :cpy-file:`Misc/sbom.spdx.json` and
   :cpy-file:`Tools/build/generate_sbom.py`.

.. _SPDX SBOM specification: https://spdx.github.io/spdx-spec/v2-draft/external-repository-identifiers/

Removing a dependency
---------------------

When removing a dependency:

1. Remove the entry from the :cpy-file:`Misc/sbom.spdx.json`
   under the ``packages`` field.
2. Remove the corresponding ``PackageFiles`` entry in :cpy-file:`Tools/build/generate_sbom.py`
3. Run the tool with ``make regen-sbom`` or ``python Tools/build/generate_sbom.py``.
   Ensure that the tool doesn't fail with any validation errors.
4. Compare the changes to :cpy-file:`Misc/sbom.spdx.json` with ``git diff``, check
   that correct package is removed from the SBOM.
5. Commit the changes to :cpy-file:`Misc/sbom.spdx.json` and
   :cpy-file:`Tools/build/generate_sbom.py`.
