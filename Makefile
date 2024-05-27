# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
PYTHON        = python3
VENVDIR       = ./venv
SPHINXBUILD   = $(VENVDIR)/bin/sphinx-build
SPHINXOPTS    = --fail-on-warning --keep-going
BUILDDIR      = _build
BUILDER       = html
JOBS          = auto
PAPER         =
SPHINXLINT    = $(VENVDIR)/bin/sphinx-lint

# Internal variables.
PAPEROPT_a4     = --define latex_paper_size=a4
PAPEROPT_letter = --define latex_paper_size=letter
ALLSPHINXOPTS   = --builder $(BUILDER) \
                  --doctree-dir $(BUILDDIR)/doctrees \
                  --jobs $(JOBS) \
                  $(PAPEROPT_$(PAPER)) \
                  $(SPHINXOPTS) \
                  . $(BUILDDIR)/$(BUILDER)

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  venv       to create a venv with necessary tools"
	@echo "  html       to make standalone HTML files"
	@echo "  htmlview   to open the index page built by the html target in your browser"
	@echo "  htmllive   to rebuild and reload HTML files in your browser"
	@echo "  clean      to remove the venv and build files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"
	@echo "  check      to run a check for frequent markup errors"
	@echo "  lint       to lint all the files"
	@echo "  versions   to update release cycle after changing release-cycle.json"

.PHONY: clean
clean: clean-venv
	-rm -rf $(BUILDDIR)/*

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
		if uv --version > /dev/null; then \
			uv venv $(VENVDIR); \
			VIRTUAL_ENV=$(VENVDIR) uv pip install -r requirements.txt; \
		else \
			$(PYTHON) -m venv $(VENVDIR); \
			$(VENVDIR)/bin/python3 -m pip install --upgrade pip; \
			$(VENVDIR)/bin/python3 -m pip install -r requirements.txt; \
		fi; \
		echo "The venv has been created in the $(VENVDIR) directory"; \
	fi

.PHONY: html
html: ensure-venv versions
	$(SPHINXBUILD) $(ALLSPHINXOPTS)

.PHONY: dirhtml
dirhtml: BUILDER = dirhtml
dirhtml: html

.PHONY: singlehtml
singlehtml: BUILDER = singlehtml
singlehtml: html

.PHONY: pickle
pickle: BUILDER = pickle
pickle: html
	@echo
	@echo "Build finished; now you can process the pickle files."

.PHONY: json
json: BUILDER = json
json: html
	@echo
	@echo "Build finished; now you can process the JSON files."

.PHONY: htmlhelp
htmlhelp: BUILDER = htmlhelp
htmlhelp: html
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/$(BUILDER)."

.PHONY: qthelp
qthelp: BUILDER = qthelp
qthelp: html

.PHONY: devhelp
devhelp: BUILDER = devhelp
devhelp: html

.PHONY: epub
epub: BUILDER = epub
epub: html
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/$(BUILDER)."

.PHONY: latex
latex: BUILDER = latex
latex: html

.PHONY: latexpdf
latexpdf: BUILDER = latex
latexpdf: html
	@echo "Running LaTeX files through pdflatex..."
	make -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/$(BUILDER)."

.PHONY: text
text: BUILDER = text
text: html

.PHONY: man
man: BUILDER = man
man: html
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/$(BUILDER)."

.PHONY: changes
changes: BUILDER = changes
changes: html

.PHONY: linkcheck
linkcheck: BUILDER = linkcheck
linkcheck: html
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/$(BUILDER)/output.txt."

.PHONY: doctest
doctest: BUILDER = doctest
doctest: html
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/$(BUILDER)/output.txt."

.PHONY: htmlview
htmlview: html
	$(PYTHON) -c "import os, webbrowser; webbrowser.open('file://' + os.path.realpath('_build/html/index.html'))"

.PHONY: htmllive
htmllive: SPHINXBUILD = $(VENVDIR)/bin/sphinx-autobuild
htmllive: SPHINXOPTS = --re-ignore="/\.idea/|/venv/" --open-browser --delay 0 --port 55311
htmllive: html

.PHONY: check
check: ensure-venv
	# Ignore the tools and venv dirs and check that the default role is not used.
	$(SPHINXLINT) -i tools -i $(VENVDIR) --enable default-role

.PHONY: lint
lint: venv
	if uv --version > /dev/null; then \
		$(VENVDIR)/bin/python3 -m pre_commit --version > /dev/null || VIRTUAL_ENV=$(VENVDIR) uv pip install pre-commit; \
	else \
		$(VENVDIR)/bin/python3 -m pre_commit --version > /dev/null || $(VENVDIR)/bin/python3 -m pip install pre-commit; \
	fi;
	$(VENVDIR)/bin/python3 -m pre_commit run --all-files

.PHONY: serve
serve:
	@echo "The 'serve' target was removed, use 'htmlview' instead" \
	      "(see https://github.com/python/cpython/issues/80510)"

include/branches.csv: include/release-cycle.json
	$(VENVDIR)/bin/python3 _tools/generate_release_cycle.py

include/end-of-life.csv: include/release-cycle.json
	$(VENVDIR)/bin/python3 _tools/generate_release_cycle.py

include/release-cycle.svg: include/release-cycle.json
	$(VENVDIR)/bin/python3 _tools/generate_release_cycle.py

.PHONY: versions
versions: venv include/branches.csv include/end-of-life.csv include/release-cycle.svg
	@echo Release cycle data generated.
