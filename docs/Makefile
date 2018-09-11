# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = ChainerColabNotebook
SOURCEDIR     = ./source
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	mkdir -p source/notebook
	mkdir -p source_ja/notebook
	cp -r ../hands_on_en source/notebook/hands_on_en
	cp -r ../example source/notebook/example
	cp -r ../official_example_en source/notebook/official_example_en
	cp -r ../hands_on_ja source_ja/notebook/hands_on_ja
	cp -r ../example source_ja/notebook/example
	cp -r ../official_example_ja source_ja/notebook/official_example_ja
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
