# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
PYTHON       = python3
VENVDIR      = ./venv
UV           = uv
SPHINXBUILD  = $(VENVDIR)/bin/sphinx-build
# Temporary: while we are using ..include:: to show the reorganization,
# there are duplicate labels.  These cause warnings, which prevent the
# build from finishing.  Turn off --fail-on-warning so we can see the
# finished results.
#SPHINXOPTS   = --fail-on-warning --keep-going
SPHINXOPTS   = --keep-going
BUILDDIR     = _build
BUILDER      = html
JOBS         = auto
SPHINXLINT   = $(VENVDIR)/bin/sphinx-lint
REQUIREMENTS = requirements.txt

# Internal variables.
_ALL_SPHINX_OPTS = --jobs $(JOBS) $(SPHINXOPTS)
_RELEASE_CYCLE   = include/branches.csv \
                   include/end-of-life.csv \
                   include/release-cycle.svg

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  venv       to create a venv with necessary tools"
	@echo "  html       to make standalone HTML files"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  htmlview   to open the index page built by the html target in your browser"
	@echo "  htmllive   to rebuild and reload HTML files in your browser"
	@echo "  clean      to remove the venv and build files"
	@echo "  check      to run a check for frequent markup errors"
	@echo "  lint       to lint all the files"

.PHONY: clean
clean: clean-venv
	-rm -rf $(BUILDDIR)/*
	-rm -rf $(_RELEASE_CYCLE)

.PHONY: clean-venv
clean-venv:
	rm -rf $(VENVDIR)

.PHONY: venv
venv:
	@if [ -d $(VENVDIR) ] ; then \
		echo "venv already exists."; \
		echo "To recreate it, remove it first with \`make clean-venv'."; \
	else \
		$(MAKE) ensure-venv; \
	fi

.PHONY: ensure-venv
ensure-venv:
	@if [ ! -d $(VENVDIR) ] ; then \
		echo "Creating venv in $(VENVDIR)"; \
		if $(UV) --version >/dev/null 2>&1; then \
			$(UV) venv --python=$(PYTHON) $(VENVDIR); \
			VIRTUAL_ENV=$(VENVDIR) $(UV) pip install -r $(REQUIREMENTS); \
		else \
			$(PYTHON) -m venv $(VENVDIR); \
			$(VENVDIR)/bin/python3 -m pip install --upgrade pip; \
			$(VENVDIR)/bin/python3 -m pip install -r $(REQUIREMENTS); \
		fi; \
		echo "The venv has been created in the $(VENVDIR) directory"; \
	fi

.PHONY: htmlview
htmlview: html
	$(PYTHON) -c "import os, webbrowser; webbrowser.open('file://' + os.path.realpath('_build/html/index.html'))"

.PHONY: htmllive
htmllive: SPHINXBUILD = $(VENVDIR)/bin/sphinx-autobuild
# Arbitrarily selected ephemeral port between 49152–65535
# to avoid conflicts with other processes:
htmllive: SPHINXOPTS = --open-browser --delay 0 --port 55301
htmllive: html

.PHONY: check
check: ensure-venv
	# Ignore the tools and venv dirs and check that the default role is not used.
	$(SPHINXLINT) -i tools -i $(VENVDIR) --enable default-role

.PHONY: _ensure-package
_ensure-package: venv
	if $(UV) --version >/dev/null 2>&1; then \
		VIRTUAL_ENV=$(VENVDIR) $(UV) pip install $(PACKAGE); \
	else \
		$(VENVDIR)/bin/python3 -m pip install $(PACKAGE); \
	fi

.PHONY: _ensure-pre-commit
_ensure-pre-commit:
	make _ensure-package PACKAGE=pre-commit

.PHONY: lint
lint: _ensure-pre-commit
	$(VENVDIR)/bin/python3 -m pre_commit run --all-files

# Defined so that "include/release-cycle.json"
# doesn't fall through to the catch-all target.
include/release-cycle.json:
	@exit

$(_RELEASE_CYCLE): include/release-cycle.json
	$(VENVDIR)/bin/python3 _tools/generate_release_cycle.py
	@echo Release cycle data generated.

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.
.PHONY: Makefile
%: Makefile ensure-venv $(_RELEASE_CYCLE)
	$(SPHINXBUILD) -M $@ "." "$(BUILDDIR)" $(_ALL_SPHINX_OPTS)
