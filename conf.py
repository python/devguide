import time

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx_copybutton',
]

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = "Python Developer's Guide"
copyright = f'2011-{time.strftime("%Y")}, Python Software Foundation'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    'venv*',
    'env*',
    'README.rst',
    '.github',
]

# Use the upstream python-docs-theme
html_theme = 'furo'
html_theme_options = {}

# The name for this set of Sphinx documents.
html_title = ""

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "python-logo.png"

# ignore linkcheck anchors for /#/$ANCHOR since it is used for
# dynamic pages such as http://buildbot.python.org/all/#/console
# http://www.sphinx-doc.org/en/stable/config.html?highlight=linkcheck#confval-linkcheck_anchors_ignore
linkcheck_anchors_ignore = [
    # match any anchor that starts with a '/' since this is an invalid HTML anchor
    '\/.*',
]

linkcheck_ignore = [
    # The voters repo is private and appears as a 404
    'https://github.com/python/voters/',
    # The python-core team link is private, redirects to login
    'https://github.com/orgs/python/teams/python-core',
    # The Discourse groups are private unless you are logged in
    'https://discuss.python.org/groups/staff',
    'https://discuss.python.org/groups/moderators',
    'https://discuss.python.org/groups/admins',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

todo_include_todos = True
