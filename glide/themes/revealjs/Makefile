# Turn a pristine copy of revealjs into the version we use
#
# Reveal.js ships with a lot of test files, optional plug-ins, fonts, etc.
# Having all of our lectures include and upload this wastes space and time,
# since we don't reference those files anyway.
#
# To use:
#
# The "revealjs" directory in the same place as this Makefile should be the
# pristine-from-GitHub revealjs directory. Run "make theme" and it will
# make the version in static/revealjs with only the files we need.
#
# joel@joelburton.com, Nov 2015

theme: custom
	rm -rf static/revealjs/
	mkdir -p static/revealjs/css/theme
	mkdir -p static/revealjs/js
	mkdir -p static/revealjs/lib/js
	mkdir -p static/revealjs/plugin/notes
	mkdir -p static/revealjs/lib/font/source-sans-pro
	java -jar yuicompressor.jar revealjs/css/reveal.css > static/revealjs/css/reveal.css
	java -jar yuicompressor.jar revealjs/css/theme/white.css > static/revealjs/css/theme/white.css
	java -jar yuicompressor.jar revealjs/js/reveal.js > static/revealjs/js/reveal.js
	java -jar yuicompressor.jar revealjs/plugin/notes/notes.js > static/revealjs/plugin/notes/notes.js
	java -jar yuicompressor.jar revealjs/lib/js/head.min.js > static/revealjs/lib/js//head.min.js
	cp revealjs/plugin/notes/notes.html static/revealjs/plugin/notes
	# We don't want this CSS, but it's imported from the other CSS
	# So let's just create an empty file for it.
	touch static/revealjs/lib/font/source-sans-pro/source-sans-pro.css

custom:
	# Compress our stylesheet, too
	# java -jar yuicompressor.jar --type css revealjs-sphinx.css_t > static/revealjs-sphinx.css_t
	#
	# FIXME: for now, just copy -- the compression screws up some dynamic variables
	ln -s ../revealjs-sphinx.css_t static