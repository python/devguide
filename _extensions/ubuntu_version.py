"""Sphinx extension to update the required Ubuntu version.

The UBUNTU_VERSION must be synchronized with the Ubuntu version used by
https://github.com/python/cpython/blob/main/Tools/build/regen-configure.sh.
"""

from sphinx.errors import ExtensionError


def replace_ubuntu_version(app, docname, source):
    if (ubuntu_version := app.config.configure_ubuntu_version) is None:
        raise ExtensionError('configure_ubuntu_version is not set in conf.py')
    source[0] = source[0].replace('$CONFIGURE_UBUNTU_VERSION$', ubuntu_version)


def setup(app):
    app.add_config_value('configure_ubuntu_version', None, 'env', types=(str,))
    app.connect('source-read', replace_ubuntu_version)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
