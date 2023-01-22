# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
PYTHON        = python3
VENVDIR       = ./venv
BUILDDIR      = _build
SPHINXOPTS    = -W --keep-going -n
SPHINXBUILD   = $(VENVDIR)/bin/sphinx-build
SPHINXLINT    = $(VENVDIR)/bin/sphinx-lint
PAPER         =

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  venv       to create a venv with necessary tools"
	@echo "  html       to make standalone HTML files"
	@echo "  htmlview   to open the index page built by the html target in your browser"
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
		$(PYTHON) -m venv $(VENVDIR); \
		$(VENVDIR)/bin/python3 -m pip install --upgrade pip; \
		$(VENVDIR)/bin/python3 -m pip install -r requirements.txt; \
		echo "The venv has been created in the $(VENVDIR) directory"; \
	fi

.PHONY: html
html: ensure-venv versions
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

.PHONY: dirhtml
dirhtml: ensure-venv versions
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

.PHONY: singlehtml
singlehtml: ensure-venv
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

.PHONY: pickle
pickle: ensure-venv
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

.PHONY: json
json: ensure-venv
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

.PHONY: htmlhelp
htmlhelp: ensure-venv
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

.PHONY: qthelp
qthelp: ensure-venv
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/PythonDevelopersGuide.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/PythonDevelopersGuide.qhc"

.PHONY: devhelp
devhelp: ensure-venv
	$(SPHINXBUILD) -b devhelp $(ALLSPHINXOPTS) $(BUILDDIR)/devhelp
	@echo
	@echo "Build finished."
	@echo "To view the help file:"
	@echo "# mkdir -p $$HOME/.local/share/devhelp/PythonDevelopersGuide"
	@echo "# ln -s $(BUILDDIR)/devhelp $$HOME/.local/share/devhelp/PythonDevelopersGuide"
	@echo "# devhelp"

.PHONY: epub
epub: ensure-venv
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

.PHONY: latex
latex: ensure-venv
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

.PHONY: latexpdf
latexpdf: ensure-venv
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	make -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

.PHONY: text
text: ensure-venv
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

.PHONY: man
man: ensure-venv
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."

.PHONY: changes
changes: ensure-venv
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck: ensure-venv
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

.PHONY: doctest
doctest: ensure-venv
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

.PHONY: htmlview
htmlview: html
	$(PYTHON) -c "import os, webbrowser; webbrowser.open('file://' + os.path.realpath('_build/html/index.html'))"

.PHONY: check
check: ensure-venv
	# Ignore the tools and venv dirs and check that the default role is not used.
	$(SPHINXLINT) -i tools -i $(VENVDIR) --enable default-role

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
