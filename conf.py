import json
import os
from urllib.request import urlopen

extensions = [
    'linklint.ext',
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
copyright = '2011 Python Software Foundation'

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
    "navigation_with_keys": True,
    "source_repository": "https://github.com/python/devguide",
    "source_branch": "main",
}
templates_path = ['_templates']
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

# Deployment preview information
# (See .readthedocs.yaml and https://docs.readthedocs.io/en/stable/reference/environment-variables.html)
is_deployment_preview = os.getenv("READTHEDOCS_VERSION_TYPE") == "external"

html_context = {
    "is_deployment_preview": is_deployment_preview,
}

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
    r"https://github.com/orgs/python/teams.*": r"https://github.com/login.*",  # noqa: E501
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
    # Checks fail due to rate limits
    r'https://github.com/.*',
    r'https://www.gnu.org/software/autoconf/',
    # The Discourse groups are private unless you are logged in
    'https://discuss.python.org/groups/staff',
    'https://discuss.python.org/groups/moderators',
    'https://discuss.python.org/groups/admins',
    # "Anchor not found":
    r'https://packaging.python.org/.*#',
    # "-rate limited-", causing a timeout
    r'https://stackoverflow.com/.*',
    # Discord doesn't allow robot crawlers: "403 Client Error: Forbidden"
    r'https://support.discord.com/hc/en-us/articles/219070107-Server-Nicknames',
    # Patreon also gives 403 to the GHA linkcheck runner
    r'https://www.patreon.com/.*',
]

rediraffe_redirects = {
    # Development Tools
    "clang.rst": "development-tools/clang.rst",
    "gdb.rst": "development-tools/gdb.rst",
    # Advanced Tools was renamed Development Tools in gh-1149
    "advanced-tools/clang.rst": "development-tools/clang.rst",
    "advanced-tools/gdb.rst": "development-tools/gdb.rst",
    # Core team
    "coredev.rst": "core-team/join-team.rst",
    "committing.rst": "core-team/committing.rst",
    "developers.rst": "core-team/team-log.rst",
    "experts.rst": "core-team/experts.rst",
    "motivations.rst": "core-team/motivations.rst",
    # core-developers/ -> core-team/
    "core-developers/become-core-developer.rst": "core-team/join-team.rst",
    "core-developers/committing.rst": "core-team/committing.rst",
    "core-developers/developer-log.rst": "core-team/team-log.rst",
    "core-developers/experts.rst": "core-team/experts.rst",
    "core-developers/index.rst": "core-team/index.rst",
    "core-developers/memorialization.rst": "core-team/memorialization.rst",
    "core-developers/motivations.rst": "core-team/motivations.rst",
    "core-developers/responsibilities.rst": "core-team/responsibilities.rst",
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
    # Translating
    "documentation/translating.rst": "documentation/translations/translating.rst",
    "translating.rst": "documentation/translations/translating.rst",
    "coordinating.rst": "documentation/translations/coordinating.rst",
    # Getting Started
    "fixingissues.rst": "getting-started/fixing-issues.rst",
    "help.rst": "getting-started/getting-help.rst",
    "gitbootcamp.rst": "getting-started/git-boot-camp.rst",
    "pullrequest.rst": "getting-started/pull-request-lifecycle.rst",
    "setup.rst": "getting-started/setup-building.rst",
    # CPython Internals
    "compiler.rst": "internals.rst",
    "exploring.rst": "internals.rst",
    "garbage_collector.rst": "internals.rst",
    "parser.rst": "internals.rst",
    "internals/compiler.rst": "internals.rst",
    "internals/exploring.rst": "internals.rst",
    "internals/garbage_collector.rst": "internals.rst",
    "internals/parser.rst": "internals.rst",
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
    # Contributing guide draft pages
    "contrib/code/git.rst": "getting-started/git-boot-camp.rst",
    "contrib/code/pull-request-lifecycle.rst": "getting-started/pull-request-lifecycle.rst",
    "contrib/code/setup.rst": "getting-started/setup-building.rst",
    "contrib/code/testing.rst": "testing/index.rst",
    "contrib/code/developer-workflow.rst": "developer-workflow/index.rst",
    "contrib/code/index.rst": "index.rst",
    "contrib/code/development-tools.rst": "development-tools/index.rst",
    "contrib/doc/devguide.rst": "documentation/devguide.rst",
    "contrib/doc/help-documenting.rst": "documentation/help-documenting.rst",
    "contrib/doc/markup.rst": "documentation/markup.rst",
    "contrib/doc/pull-request-lifecycle.rst": "getting-started/pull-request-lifecycle.rst",
    "contrib/doc/start-documenting.rst": "documentation/start-documenting.rst",
    "contrib/doc/style-guide.rst": "documentation/style-guide.rst",
    "contrib/doc/translating.rst": "documentation/translations/index.rst",
    "contrib/doc/index.rst": "documentation/index.rst",
    "contrib/intro/index.rst": "index.rst",
    "contrib/project/channels.rst": "developer-workflow/communication-channels.rst",
    "contrib/project/conduct.rst": "index.rst",
    "contrib/project/github.rst": "index.rst",
    "contrib/project/governance.rst": "index.rst",
    "contrib/project/roles.rst": "index.rst",
    "contrib/project/generative-ai.rst": "getting-started/generative-ai.rst",
    "contrib/project/outreach.rst": "index.rst",
    "contrib/project/directory-structure.rst": "getting-started/setup-building.rst",
    "contrib/project/index.rst": "index.rst",
    "contrib/security.rst": "index.rst",
    "contrib/triage/issue-tracker.rst": "triage/issue-tracker.rst",
    "contrib/triage/labels.rst": "triage/labels.rst",
    "contrib/triage/reviewing.rst": "triage/triaging.rst",
    "contrib/triage/triage-team.rst": "triage/triage-team.rst",
    "contrib/triage/triaging.rst": "triage/triaging.rst",
    "contrib/triage/index.rst": "triage/index.rst",
    "contrib/user-success.rst": "index.rst",
    "contrib/core-team/committing.rst": "core-team/committing.rst",
    "contrib/core-team/experts.rst": "core-team/experts.rst",
    "contrib/core-team/index.rst": "core-team/index.rst",
    "contrib/core-team/join-team.rst": "core-team/join-team.rst",
    "contrib/core-team/motivations.rst": "core-team/motivations.rst",
    "contrib/core-team/responsibilities.rst": "core-team/responsibilities.rst",
    "contrib/core-team/team-log.rst": "core-team/team-log.rst",
    "contrib/workflows/codespaces.rst": "getting-started/setup-building.rst",
    "contrib/workflows/compile.rst": "getting-started/setup-building.rst",
    "contrib/workflows/get-source.rst": "getting-started/setup-building.rst",
    "contrib/workflows/index.rst": "getting-started/setup-building.rst",
    "contrib/workflows/install-dependencies.rst": "getting-started/setup-building.rst",
    "contrib/workflows/install-git.rst": "getting-started/setup-building.rst",
    "contrib/workflows/regenerate.rst": "getting-started/setup-building.rst",
    "contrib/workflows/troubleshooting.rst": "getting-started/setup-building.rst",
    "contrib/index.rst": "index.rst",
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'diataxis': ('https://diataxis.fr/', None),
}

todo_include_todos = True

# sphinx-notfound-page
notfound_urls_prefix = "/"

# Dynamically expose the Python version associated with the "main" branch.
# Exactly one entry in ``release-cycle.json`` should have ``"branch": "main"``.
with urlopen("https://peps.python.org/api/release-cycle.json") as _f:
    _cycle = json.loads(_f.read().decode("utf-8"))

_main_version = next(
    version for version, data in _cycle.items() if data.get("branch") == "main"
)

# prolog and epilogs
rst_prolog = f"""

.. |main_version| replace:: {_main_version}

"""

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
    "pypi-org": ("https://pypi.org/org/%s/", "%s"),
}

# sphinxext-opengraph config
ogp_site_url = "https://devguide.python.org/"
ogp_site_name = "Python Developer's Guide"
ogp_image = "_static/og-image-200x200.png"
ogp_custom_meta_tags = (
    '<meta property="og:image:width" content="200">',
    '<meta property="og:image:height" content="200">',
    '<meta name="theme-color" content="#3776ab">',
)

# Strip the dollar prompt when copying code
# https://sphinx-copybutton.readthedocs.io/en/latest/use.html#strip-and-configure-input-prompts-for-code-cells
copybutton_prompt_text = "$ "
# https://sphinx-copybutton.readthedocs.io/en/latest/use.html#honor-line-continuation-characters-when-copying-multline-snippets
copybutton_line_continuation_character = "\\"
