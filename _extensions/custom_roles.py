"""Sphinx extension to add custom roles.

Based on https://protips.readthedocs.io/link-roles.html
"""
import urllib.parse

from docutils import nodes


def setup(app):
    app.add_role(
        "gh-label",
        autolink("https://github.com/python/cpython/labels/%s"),
    )
    # Parallel safety:
    # https://www.sphinx-doc.org/en/master/extdev/index.html#extension-metadata
    return {"parallel_read_safe": True, "parallel_write_safe": True}


def autolink(pattern):
    def role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        if " " in text:
            url_text = urllib.parse.quote(f"{text}")
        else:
            url_text = text
        url = pattern % (url_text,)
        node = nodes.reference(rawtext, text, refuri=url, **options)
        return [node], []

    return role
