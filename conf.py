import os
import sys
import time

# Location of custom extensions.
sys.path.insert(0, os.path.abspath(".") + "/_extensions")

extensions = [
    'custom_roles',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx_copybutton',
    'sphinxext.opengraph',
    'sphinxext.rediraffe',
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
    r'\/.*',
]
rediraffe_redirects = {
    "clang.rst": "advanced-tools/clang.rst",
    "coverity.rst": "advanced-tools/coverity.rst",
    "gdb.rst": "advanced-tools/gdb.rst",
    "coredev.rst": "core-developers/become-core-developer.rst",
    "committing.rst": "core-developers/committing.rst",
    "developers.rst": "core-developers/developer-log.rst",
    "experts.rst": "core-developers/experts.rst",
    "motivations.rst": "core-developers/motivations.rst",
    "c-api.rst": "developer-workflow/c-api.rst",
    "communication.rst": "developer-workflow/communication-channels.rst",
    "devcycle.rst": "developer-workflow/development-cycle.rst",
    "extensions.rst": "developer-workflow/extension-modules.rst",
    "grammar.rst": "developer-workflow/grammar.rst",
    "langchanges.rst": "developer-workflow/lang-changes.rst",
    "porting.rst": "developer-workflow/porting.rst",
    "stdlibchanges.rst": "developer-workflow/stdlib.rst",
    "docquality.rst": "documentation/help-documenting.rst",
    "documenting.rst": "documentation/start-documenting.rst",
    "fixingissues.rst": "getting-started/fixing-issues.rst",
    "help.rst": "getting-started/getting-help.rst",
    "gitbootcamp.rst": "getting-started/git-boot-camp.rst",
    "pullrequest.rst": "getting-started/pull-request-lifecycle.rst",
    "setup.rst": "getting-started/setup-building.rst",
    "compiler.rst": "internals/compiler.rst",
    "exploring.rst": "internals/exploring.rst",
    "garbage_collector.rst": "internals/garbage-collector.rst",
    "parser.rst": "internals/parser.rst",
    "buildbots.rst": "testing/buildbots.rst",
    "coverage.rst": "testing/coverage.rst",
    "buildworker.rst": "testing/new-buildbot-worker.rst",
    "runtests.rst": "testing/run-write-tests.rst",
    "silencewarnings.rst": "testing/silence-warnings.rst",
    "gh-faq.rst": "triage/github-bpo-faq.rst",
    "tracker.rst": "triage/issue-tracker.rst",
    "gh-labels.rst": "triage/labels.rst",
    "triaging.rst": "triage/triaging.rst",
}

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

# sphinxext-opengraph config
ogp_site_url = "https://devguide.python.org/"
ogp_image = "https://devguide.python.org/_static/og-image.png"
ogp_custom_meta_tags = [
    '<meta property="og:image:width" content="1200">',
    '<meta property="og:image:height" content="630">',
]

# Strip the dollar prompt when copying code
# https://sphinx-copybutton.readthedocs.io/en/latest/use.html#strip-and-configure-input-prompts-for-code-cells
copybutton_prompt_text = "$"
