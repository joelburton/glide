# You can set these variables from the command line.
SPHINXOPTS    = -W --keep-going -D revealjs_theme=revealjs-rithm -a
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Demo
SOURCEDIR     = .
BUILDDIR      = _build

prince:
	make handouts
	/tmp/p/bin/prince -j _build/handouts/index.html
	open _build/handouts/index.pdf

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)