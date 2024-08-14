"""Sphinx extension to update the required Ubuntu version.

The required Ubuntu version should be specified in conf.py by::

    configure_ubuntu_version = "MAJOR.MINOR"  # e.g., "22.04"

The version must match the one used to regenerate the configure script in
https://github.com/python/cpython/blob/main/Tools/build/regen-configure.sh.
"""

from sphinx.errors import ExtensionError


def replace_ubuntu_version(app, docname, source):
    """Replace all occurrences of $CONFIGURE_UBUNTU_VERSION$.

    This is needed since RST replacement via ``|...|`` is not supported
    in code-blocks directives.
    """
    if (ubuntu_version := app.config.configure_ubuntu_version) is None:
        raise ExtensionError('configure_ubuntu_version is not set in conf.py')
    source[0] = source[0].replace('$CONFIGURE_UBUNTU_VERSION$', ubuntu_version)


def setup(app):
    app.add_config_value('configure_ubuntu_version', None, 'env', types=(str,))
    app.connect('source-read', replace_ubuntu_version)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
