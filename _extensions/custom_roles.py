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
    def role(name, rawtext, text, lineno, inliner, _options=None, _content=None):
        """Combine literal + reference (unless the text is prefixed by a !)."""
        if " " in text:
            url_text = urllib.parse.quote(text)
        else:
            url_text = text
        url = pattern.format(url_text)
        # don't create a reference if the text starts with !
        if text.startswith('!'):
            node = nodes.literal(rawtext, text[1:])
        else:
            node = nodes.reference(rawtext, '', nodes.literal(rawtext, text),
                                   refuri=url, internal=False)
        return [node], []

    return role
