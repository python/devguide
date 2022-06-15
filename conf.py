import os
import sys
import time

sys.path.append(os.path.abspath('tools'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.intersphinx', 'sphinx.ext.todo', 'sphinx_copybutton']
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
todo_include_todos = True

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Python Developer\'s Guide'
copyright = '2011-%s, Python Software Foundation' % time.strftime('%Y')

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'venv*', 'env*', 'README.rst', '.github']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------

# Use the upstream python-docs-theme
html_theme = 'furo'
html_theme_options = {}


# The name for this set of Sphinx documents.
html_title = ""

# Path to find HTML templates.
templates_path = ['tools/templates']

# Additional static files.
html_static_path = ['tools/static']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "python-logo.png"

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

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

# Use our custom CSS stylesheet to differentiate us from the official python
# docs.
def setup(app):
    app.add_css_file('custom.css')
