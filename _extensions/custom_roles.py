"""Sphinx extension to add custom roles.

Based on https://protips.readthedocs.io/link-roles.html
"""
import urllib.parse

from docutils import nodes


def setup(app):
    # role to link to cpython files
    app.add_role(
        "cpy-file",
        autolink("https://github.com/python/cpython/blob/main/{}"),
    )
    # role to link to cpython labels
    app.add_role(
        "gh-label",
        autolink("https://github.com/python/cpython/labels/{}"),
    )
    # Parallel safety:
    # https://www.sphinx-doc.org/en/master/extdev/index.html#extension-metadata
    return {"parallel_read_safe": True, "parallel_write_safe": True}


def autolink(pattern):
    def role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        """Combine literal + reference (unless the text is prefixed by a !)."""
        if " " in text:
            url_text = urllib.parse.quote(f"{text}")
        else:
            url_text = text
        url = pattern.format(url_text)
        node = nodes.literal(rawtext, text.lstrip('!'), **options)
        # don't create a reference if the text starts with !
        if not text.startswith('!'):
            node = nodes.reference('', '', node, refuri=url, **options)
        return [node], []

    return role
