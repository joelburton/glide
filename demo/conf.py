# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import datetime
import subprocess
import sys
import imp
import logging


# -- Project information -----------------------------------------------------

project = 'Demo'
copyright = '2018, Joel Burton'
author = 'Joel Burton'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    # 'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'glide.writers.handouts',
    'glide.writers.revealjs',

    'glide.directives.newslide',  # Add new slide without a section break
    'glide.directives.incremental',  # Support for RevealJS fragments
    'glide.directives.interslide',  # Adds Reveal-only interstitial slides
    'glide.directives.speakernote',  # Adds Reveal-only speaker notes
    'sphinx.ext.graphviz',  # Sphinx's standard Graphviz directive
    'glide.directives.graphviz',  # Joel's customizations of standard Graphviz directive
    'glide.directives.required',  # break makefiles until directive is read and removed
    'glide.directives.doctest',  # our special override-doctest class

]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_copy_source = False
html_use_index = False


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Demodoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Demo.tex', 'Demo Documentation',
     'Joel Burton', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'demo', 'Demo Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Demo', 'Demo Documentation',
     author, 'Demo', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True





import glide
import os

html_theme_path = [
    os.path.join(*glide.__path__, 'themes')
]

def setup(app):
    # New settings we want to refer to in the config file; these need to be declared
    app.add_config_value('revealjs_theme', 'alabaster', 'env')
    app.add_config_value('revealjs_imgmath_dvipng_args', [], 'env')
    # app.add_config_value('answerkey', 'ANSWERKEY' in os.environ, 'env')

    # try:
    #     imp.find_module('pygmentslexerbabylon')
    #     import pygmentslexerbabylon
    #     app.add_lexer("jsx", pygmentslexerbabylon.BabylonLexer())
    # except ImportError:
    #     logging.warn("Pygmentslexerbabylon missing -- required to highlight JSX.")

revealjs_theme="revealjs"
html_theme = "handouts"
html_add_permalinks = ""


# RST Prolog
#
# This stuff is added to every RST file before it's processed

# Colors; you'll also need to add CSS classes to your theme if you want these
# colors to actually appear, of course. You'll also need to edit the LaTeX
# writer to get them to appear in PDFs.

_colors = """
.. role:: red
.. role:: green
.. role:: orange
.. role:: tan
.. role:: blue
.. role:: cmd
.. role:: white
.. role:: gray
.. role:: comment
.. role:: gone
.. role:: inv-red
.. role:: text-heavy
"""

# Additional symbols to include
#
# Be cautious about just adding things here; not all symbols appear in all fonts
# nor will some obscure ones work in LaTeX

# We use some of these to make our curriculum more agile and to help make the
# py2->py3 easier:
#
# |py|      - unstylized name of python executable:    python         or  python3
# |pyi|     - emphasized-name:                         `python`       or  `python3`
# |pycmd|   - as command, for inside console blocks    `python`:cmd:  or  `python3`:cmd:
# |pyname|  - not as exec, but friendly name           Python         or  Python 3
# PY3: make sure these get changed for Python 3 :)


_symbols = """
.. |nbsp|      unicode:: U+000A0 .. NONBREAKING SPACE
.. |rarr|      unicode:: U+02192 .. RIGHTWARDS ARROW
.. |larr|      unicode:: U+02190 .. LEFTWARDS ARROW
.. |darr|      unicode:: U+02193 .. DOWNWARDS ARROW
.. |lrarr|     unicode:: U+02194 .. LEFT RIGHT ARROW
.. |plus|      unicode:: U+0002B .. PLUS SIGN
.. |times|     unicode:: U+000D7 .. MULTIPLICATION SIGN
.. |check|     unicode:: U+02713 .. CHECK MARK
.. |approx|    unicode:: U+02248 .. ALMOST EQUAL TO
.. |sub2|      unicode:: U+02082 .. SUBSCRIPT 2
.. |super2|    unicode:: U+000B2 .. SUPERSCRIPT 2
.. |spades|    unicode:: U+02660 .. SPADES
.. |hearts|    unicode:: U+02665 .. HEARTS
.. |diamonds|  unicode:: U+02666 .. DIAMONDS
.. |clubs|     unicode:: U+02663 .. CLUBS
.. |py|        replace:: python
.. |pyi|       replace:: `python`
.. |pycmd|     replace:: `python`:cmd:
.. |ipy|       replace:: python
.. |ipyi|      replace:: `python`:cmd:
.. |ipycmd|    replace:: `python`:cmd:
.. |ipyname|   replace:: Python
.. |editor|    replace:: subl 
.. |editori|   replace:: `subl`
.. |editcmd|   replace:: `subl`:cmd:
.. |editorname|  replace:: Sublime Text
.. |pip|       replace:: pip
.. |pipi|      replace:: `pip`
.. |pipcmd|    replace:: `pip`:cmd:
.. |venv|      replace:: virtualenv
.. |venvi|     replace:: `virtualenv` 
.. |venvcmd|   replace:: `virtualenv`:cmd: 
"""

# A new role for raw output that should only appear in HTML, and a
# directive that causes a linebreak <br> to appear only in revealjs
# This is useful for when we have a long line that we don't need to break in
# handouts-html or LaTeX, but looks better broken in RevealJS. Note: the
# handouts CSS needs to make this display:none

_reveal_br = """
.. role:: raw-reveal(raw)
   :format: html
.. |reveal-br| replace:: :raw-reveal:`<br>`
"""

# Concatenate that, the only thing that matters is what appears in rst_prolog itself
rst_prolog = _colors + _reveal_br
rst_epilog = _symbols

# Check for graphviz
#
# About 30% of our lectures/exercises uses Graphviz--so sooner or later,
# you'll need it (see the INSTALL directions). However, some people will use
# this without graphviz. You'll get an error when you build a presentation
# that requires it; our goal here it to provide better feedback for when you
# hit that

try:
    subprocess.check_output("which dot", shell=True)

except subprocess.CalledProcessError:
    logging.warn(
        "Graphviz not installed -- required to build graphs. See INSTALL.rst      <-- READ ME")

# How will generate math equations?
#
# If we have `pdflatex` installed, we'll use that. That makes the prettiest
# math equations and doesn't require any kind of browser support. However,
# some users of our build system won't easily get LaTeX installed, so we
# have a fallback to mathjax. (Our themes include the JS support for MathJax)
# already.

try:
    subprocess.check_output("which pdflatex", shell=True)
    extensions.append('sphinx.ext.imgmath')
    logging.debug("Found imgmath; using it.")

except subprocess.CalledProcessError:
    extensions.append('sphinx.ext.mathjax')
    logging.warn("LaTeX not installed; falling back to mathjax for equations. See INSTALL.rst.")

# Safely see if matplotlib and scipy are installed and, if so, add Sphinx
# extension for it
#
# We use matplotlib and scipy to draw charts and business graphs.
#
# Over time, we'll no doubt use more of it, and everyone will need it --- but for
# now (Nov 2015), this will allow people w/o matplotlib  or scipy to build the
# 98% of our talks that don't rely on it. (As a test case, the comp-sci-ds
# lecture has a graph in it)
#
# For unknown reasons, we need to do this in an odd way, by using the imp module
# rather than doing a more traditional import. For some reason, that nukes sphinx
# finding other writers---perhaps sphinx somehow relies on imports not having failed?
# In any event, while a less conventional way to write this, it works. -- Joel

try:
    imp.find_module('matplotlib')
    extensions.append('matplotlib.sphinxext.plot_directive')

except ImportError:
    # You don't have matplotlib installed, but you're probably still a good person
    extensions.append("glide.directives.noplot")
    logging.warn(
        "Matplotlib not installed; skipping drawing charts. See INSTALL.rst       <-- READ ME")

try:
    imp.find_module('scipy')

except ImportError:
    # You don't have scipy installed, but you're probably still a good person
    logging.warn(
        "Scipy not installed; skipping drawing charts. See INSTALL.rst       <-- READ ME")

