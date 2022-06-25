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

html_theme = 'furo'
html_theme_options = {}
html_static_path = ['_static']
html_css_files = [
    'devguide_overrides.css',
]
html_logo = "_static/python-logo.svg"

# Set to '' to prevent appending "documentation" to the site title
html_title = ""

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
