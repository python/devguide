import time

extensions = [
    'custom_roles',
    'ubuntu_version',
    'notfound.extension',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx_copybutton',
    'sphinx_inline_tabs',
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

nitpicky = True


html_theme = 'furo'
html_theme_options = {
    "source_repository": "https://github.com/python/devguide",
    "source_branch": "main",
}
html_static_path = ['_static']
html_css_files = [
    'devguide_overrides.css',
]
html_js_files = [
    "activate_tab.js",
]
html_logo = "_static/python-logo.svg"
html_favicon = "_static/favicon.png"

# Set to '' to prevent appending "documentation" to the site title
html_title = ""

linkcheck_allowed_redirects = {
    # Edit page
    r"https://docs.google.com/document/d/.*/": r"https://docs.google.com/document/d/.*/edit",  # noqa: E501
    # Canonical
    r"https://docs.python.org/": r"https://docs.python.org/3/",
    # Translations with country codes
    r"https://docs.python.org/[a-z-]+/": r"https://docs.python.org/[a-z-]+/3/",
    # Personal /my/ links redirect to login page
    r"https://discuss.python.org/my/.*": r"https://discuss.python.org/login-preferences",  # noqa: E501
    # Category number URL to full slug
    r"https://discuss.python.org/c/\d+": r"https://discuss.python.org/c/.*",
    # Login page
    r"https://github.com/python/buildmaster-config/issues/new.*": r"https://github.com/login.*",  # noqa: E501
    r"https://github.com/python/core-workflow/issues/new.*": r"https://github.com/login.*",  # noqa: E501
    # Archive redirect
    r"https://github.com/python/cpython/archive/main.zip": r"https://codeload.github.com/python/cpython/zip/refs/heads/main",  # noqa: E501
    # Blob to tree
    r"https://github.com/python/cpython/blob/.*": r"https://github.com/python/cpython/tree/.*",  # noqa: E501
    # HackMD shortcuts
    r"https://hackmd.io/s/.*": r"https://hackmd.io/@.*",
    # Read the Docs
    r"https://python-docs-tr.readthedocs.io/": r"https://python-docs-tr.readthedocs.io/tr/.*",  # noqa: E501
    r"https://virtualenv.pypa.io/": r"https://virtualenv.pypa.io/en/latest/",
    r"https://www.sphinx-doc.org/": r"https://www.sphinx-doc.org/en/master/",
    # Cookie consent
    r"https://www.youtube.com/playlist.*": r"https://consent.youtube.com/.*",
}

# ignore linkcheck anchors for /#/$ANCHOR since it is used for
# dynamic pages such as http://buildbot.python.org/all/#/console
# http://www.sphinx-doc.org/en/stable/config.html?highlight=linkcheck#confval-linkcheck_anchors_ignore
linkcheck_anchors_ignore = [
    # match any anchor that starts with a '/' since this is an invalid HTML anchor
    r'\/.*',
]

linkcheck_ignore = [
    # The voters repo is private and appears as a 404
    'https://github.com/python/voters',
    # The python-core team link is private, redirects to login
    'https://github.com/orgs/python/teams/python-core',
    # The Discourse groups are private unless you are logged in
    'https://discuss.python.org/groups/staff',
    'https://discuss.python.org/groups/moderators',
    'https://discuss.python.org/groups/admins',
    # The crawler gets "Anchor not found" for GitHub anchors
    r'https://github.com.+?#L\d+',
    r'https://github.com/cli/cli#installation',
    r'https://github.com/github/renaming#renaming-existing-branches',
    r'https://github.com/python/bedevere/#pr-state-machine',
    # "Anchor not found":
    r'https://packaging.python.org/.*#',
    # Discord doesn't allow robot crawlers: "403 Client Error: Forbidden"
    r'https://support.discord.com/hc/en-us/articles/219070107-Server-Nicknames',
]

rediraffe_redirects = {
    # Development Tools
    "clang.rst": "development-tools/clang.rst",
    "coverity.rst": "development-tools/coverity.rst",
    "gdb.rst": "development-tools/gdb.rst",
    # Advanced Tools was renamed Development Tools in gh-1149
    "advanced-tools/clang.rst": "development-tools/clang.rst",
    "advanced-tools/coverity.rst": "development-tools/coverity.rst",
    "advanced-tools/gdb.rst": "development-tools/gdb.rst",
    # Core Developers
    "coredev.rst": "core-developers/become-core-developer.rst",
    "committing.rst": "core-developers/committing.rst",
    "developers.rst": "core-developers/developer-log.rst",
    "experts.rst": "core-developers/experts.rst",
    "motivations.rst": "core-developers/motivations.rst",
    # Developer Workflow
    "c-api.rst": "developer-workflow/c-api.rst",
    "communication.rst": "developer-workflow/communication-channels.rst",
    "devcycle.rst": "developer-workflow/development-cycle.rst",
    "extensions.rst": "developer-workflow/extension-modules.rst",
    "grammar.rst": "developer-workflow/grammar.rst",
    "langchanges.rst": "developer-workflow/lang-changes.rst",
    "porting.rst": "developer-workflow/porting.rst",
    "stdlibchanges.rst": "developer-workflow/stdlib.rst",
    # Documentation
    "docquality.rst": "documentation/help-documenting.rst",
    "documenting.rst": "documentation/start-documenting.rst",
    # Getting Started
    "fixingissues.rst": "getting-started/fixing-issues.rst",
    "help.rst": "getting-started/getting-help.rst",
    "gitbootcamp.rst": "getting-started/git-boot-camp.rst",
    "pullrequest.rst": "getting-started/pull-request-lifecycle.rst",
    "setup.rst": "getting-started/setup-building.rst",
    # CPython Internals
    "compiler.rst": "internals/compiler.rst",
    "exploring.rst": "internals/exploring.rst",
    "garbage_collector.rst": "internals/garbage-collector.rst",
    "parser.rst": "internals/parser.rst",
    # Testing and Buildbots
    "buildbots.rst": "testing/buildbots.rst",
    "coverage.rst": "testing/coverage.rst",
    "buildworker.rst": "testing/new-buildbot-worker.rst",
    "runtests.rst": "testing/run-write-tests.rst",
    "silencewarnings.rst": "testing/silence-warnings.rst",
    # Issues and Triaging
    "gh-faq.rst": "triage/github-bpo-faq.rst",
    "tracker.rst": "triage/issue-tracker.rst",
    "gh-labels.rst": "triage/labels.rst",
    "triaging.rst": "triage/triaging.rst",
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'diataxis': ('https://diataxis.fr/', None),
}

todo_include_todos = True

# sphinx-notfound-page
notfound_urls_prefix = "/"

# sphinx.ext.extlinks
# This config is a dictionary of external sites,
# mapping unique short aliases to a base URL and a prefix.
# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
_repo = "https://github.com/python/cpython"
extlinks = {
    "cpy-file": (f"{_repo}/blob/main/%s", "%s"),
    "gh-label": (f"{_repo}/labels/%s", "%s"),
    "github": ("https://github.com/%s", "%s"),
    "github-user": ("https://github.com/%s", "@%s"),
    "pypi": ("https://pypi.org/project/%s/", "%s"),
}

# sphinxext-opengraph config
ogp_site_url = "https://devguide.python.org/"
ogp_site_name = "Python Developer's Guide"
ogp_image = "_static/og-image-200x200.png"
ogp_custom_meta_tags = [
    '<meta property="og:image:width" content="200">',
    '<meta property="og:image:height" content="200">',
    '<meta name="theme-color" content="#3776ab">',
]

# Strip the dollar prompt when copying code
# https://sphinx-copybutton.readthedocs.io/en/latest/use.html#strip-and-configure-input-prompts-for-code-cells
copybutton_prompt_text = "$ "
# https://sphinx-copybutton.readthedocs.io/en/latest/use.html#honor-line-continuation-characters-when-copying-multline-snippets
copybutton_line_continuation_character = "\\"

configure_ubuntu_version = '22.04'
