# You can set these variables from the command line.
SPHINXOPTS    = -c .. -T -W --keep-going
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

prince-open:
	make clean && make singlehandouts SPHINXOPTS="$(SPHINXOPTS) -D html_math_renderer=imgmath"
	prince -j _build/singlehandouts/index.html
	open _build/singlehandouts/index.pdf

handouts-open: handouts
	open _build/handouts/index.html

revealjs-open: revealjs
	open _build/revealjs/index.html

singlehandouts-open: singlehandouts
	open _build/singlehandouts/index.html

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
