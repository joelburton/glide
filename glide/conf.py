import subprocess
import os

from sphinx.ext.todo import todo_node, visit_todo_node, depart_todo_node, \
    latex_visit_todo_node, latex_depart_todo_node
from sphinxcontrib.mermaid import html_visit_mermaid, latex_visit_mermaid, texinfo_visit_mermaid, text_visit_mermaid, \
    man_visit_mermaid, mermaid

from glide import version, logger

# -- Project information -----------------------------------------------------
# Define these in actual usage conf.py files

# project = 'Demo'
# copyright = '2018, Joel Burton'
# author = 'Joel Burton'
#
# # The short X.Y version -- shows on generated docs
# version = ''
# # The full version, including alpha/beta/rc tags
# release = ''

# -- General configuration ---------------------------------------------------

needs_sphinx = '7'

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'sphinx.ext.imgmath',
    'sphinxcontrib.drawio',
    'sphinxemoji.sphinxemoji',
    # 'sphinxcontrib.aafig',
    'aafigure.sphinxext',
    'glide.directives.diagram',

    'glide.writers.handouts',
    'glide.writers.revealjs',
    'glide.writers.latex',

    # Make any building of doc w/this hard-fail; use to mark broken docs
    'glide.directives.fail',

    # Adds revealjs-only interstitial slides
    'glide.directives.interslide',

    # Adds Reveal-only speaker notes
    'glide.directives.speakernote',

    # Add new slide without a section break
    'glide.directives.newslide',

    # Support for RevealJS fragments
    'glide.directives.incremental',

    # Mildly-customized version of standard graphviz extension
    'glide.directives.graphviz',

    # Give doctest-related directives extra functionality
    'glide.directives.doctest',

    # Allow external links
    'sphinx.ext.extlinks',

    # Allow mermaid
    "sphinxcontrib.mermaid",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'node_modules', 'venv', 'meta', 'retired']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

linkcheck_ignore = [r'http://localhost:\d+/']

# This stuff is added to every RST file before it's processed

# Colors; you'll also need to add CSS classes to your theme if you want these
# colors to actually appear, of course. You'll also need to edit the LaTeX
# writer to get them to appear in PDFs.
_colors = """
.. role:: black
.. role:: near-black
.. role:: dark-gray
.. role:: mid-gray
.. role:: gray
.. role:: silver
.. role:: light-silver
.. role:: moon-gray
.. role:: light-gray
.. role:: near-white
.. role:: white

.. role:: dark-red
.. role:: red
.. role:: light-red
.. role:: orange
.. role:: gold
.. role:: yellow
.. role:: light-yellow
.. role:: purple
.. role:: light-purple
.. role:: dark-pink
.. role:: hot-pink
.. role:: pink
.. role:: light-pink
.. role:: dark-green
.. role:: green
.. role:: light-green
.. role:: navy
.. role:: dark-blue
.. role:: blue
.. role:: light-blue
.. role:: lightest-blue
.. role:: washed-blue
.. role:: washed-green
.. role:: washed-yellow
.. role:: washed-red

.. role:: bg-black
.. role:: bg-near-black
.. role:: bg-dark-gray
.. role:: bg-mid-gray
.. role:: bg-gray
.. role:: bg-silver
.. role:: bg-light-silver
.. role:: bg-moon-gray
.. role:: bg-light-gray
.. role:: bg-near-white
.. role:: bg-white

.. role:: bg-dark-red
.. role:: bg-red
.. role:: bg-light-red
.. role:: bg-orange
.. role:: bg-gold
.. role:: bg-yellow
.. role:: bg-light-yellow
.. role:: bg-purple
.. role:: bg-light-purple
.. role:: bg-dark-pink
.. role:: bg-hot-pink
.. role:: bg-pink
.. role:: bg-light-pink
.. role:: bg-dark-green
.. role:: bg-green
.. role:: bg-light-green
.. role:: bg-navy
.. role:: bg-dark-blue
.. role:: bg-blue
.. role:: bg-light-blue
.. role:: bg-lightest-blue
.. role:: bg-washed-blue
.. role:: bg-washed-green
.. role:: bg-washed-yellow
.. role:: bg-washed-red

.. role:: inv-black
.. role:: inv-near-black
.. role:: inv-dark-gray
.. role:: inv-mid-gray
.. role:: inv-gray
.. role:: inv-silver
.. role:: inv-light-silver
.. role:: inv-moon-gray
.. role:: inv-light-gray
.. role:: inv-near-white
.. role:: inv-white

.. role:: inv-dark-red
.. role:: inv-red
.. role:: inv-light-red
.. role:: inv-orange
.. role:: inv-gold
.. role:: inv-yellow
.. role:: inv-light-yellow
.. role:: inv-purple
.. role:: inv-light-purple
.. role:: inv-dark-pink
.. role:: inv-hot-pink
.. role:: inv-pink
.. role:: inv-light-pink
.. role:: inv-dark-green
.. role:: inv-green
.. role:: inv-light-green
.. role:: inv-navy
.. role:: inv-dark-blue
.. role:: inv-blue
.. role:: inv-light-blue
.. role:: inv-lightest-blue
.. role:: inv-washed-blue
.. role:: inv-washed-green
.. role:: inv-washed-yellow
.. role:: inv-washed-red

.. role:: ins
.. role:: del
.. role:: comment
.. role:: gone
.. role:: wrong
.. role:: muted
.. role:: small
.. role:: small-muted
.. role:: danger
.. role:: warning
.. role:: success
.. role:: err
.. role:: type

.. role:: gp
.. role:: c
.. role:: gs

.. role:: emoji
.. role:: emoji-1x
.. role:: emoji-15x
.. role:: emoji-2x
.. role:: emoji-3x
.. role:: emoji-4x
.. role:: emoji-5x
.. role:: emoji-6x
.. role:: emoji-7x

.. role:: py(code)
   :language: python

.. role:: ts(code)
   :language: ts

.. role:: js(code)
   :language: js

.. role:: sql(code)
  :language: postgresql

.. role:: postgresql(code)
  :language: postgresql

.. role:: zsh(code)
  :language: zsh

.. role:: css(code)
  :language: css

.. role:: html(code)
  :language: html

.. role:: jsx(code)
  :language: jsx

.. role:: html+jinja(code)
  :language: html+jinja

.. role:: json(code)
  :language: json

.. role:: rb(code)
  :language: rb

.. role:: erb(code)
  :language: erb

.. role:: graphql(code)
  :language: graphql

.. role:: psql(code)
  :language: psql

.. role:: pycon(code)
  :language: pycon

.. role:: rst(code)
  :language: rst

.. role:: scss(code)
  :language: scss

"""

# Additional symbols to include
#
# Be cautious about just adding things here; not all symbols appear in all fonts
# nor will some obscure ones work in LaTeX
_symbols = """
.. |nbsp|      unicode:: U+000A0 .. NONBREAKING SPACE
.. |rarr|      unicode:: U+02192 .. RIGHTWARDS ARROW
.. |larr|      unicode:: U+02190 .. LEFTWARDS ARROW
.. |uarr|      unicode:: U+02191 .. UPWARDS ARROW
.. |darr|      unicode:: U+02193 .. DOWNWARDS ARROW
.. |lrarr|     unicode:: U+021C4 .. LEFT RIGHT ARROW
.. |plus|      unicode:: U+0002B .. PLUS SIGN
.. |times|     unicode:: U+000D7 .. MULTIPLICATION SIGN
.. |divide|    unicode:: U+000F7 .. DIVISION SIGN

.. |check|     unicode:: U+02713 .. CHECK MARK
.. |wrong|     unicode:: U+02717 .. BALLOT X 
.. |approx|    unicode:: U+02248 .. ALMOST EQUAL TO

.. |date| date::
.. |key-legend| replace:: ``⌘`` Command |sp| |sp| ``⌃`` Ctrl |sp| |sp| ``⌥`` Alt/Opt |sp| |sp| ``⇧`` Shift |sp| |sp| ``Ⓕ`` Fn |sp| |sp| ``⦿`` Click |sp| |sp| ``␣`` Space |sp| |sp| ``↵`` Enter
"""

# A new role for raw output that should only appear in HTML, and a
# directive that causes a linebreak <br> to appear only in revealjs
# This is useful for when we have a long line that we don't need to break in
# handouts-html or LaTeX, but looks better broken in RevealJS. Note: the
# handouts CSS needs to have ``.raw-reveal { display: none }``
_reveal_br = """
.. role:: raw-reveal(raw)
   :format: html
.. role:: raw-handouts(raw)
   :format: html 
.. |reveal-br| replace:: :raw-reveal:`<br/>`
.. |br| replace:: :raw-reveal:`<br/>`
.. |handouts-br| replace:: :raw-handouts:`<br/>`
.. |all-br| replace:: :raw-reveal:`<br/>`\\ :raw-handouts:`<br/>`
.. |sp| replace:: :raw-handouts:`&nbsp;`
"""

# Glide 2.0 added |br| as a shorter synonym for this.

# Can use like |demo-link| to show a URL from env var
# if there is no demo link, just return a pointless localhost,
# since the linkchecker ignores localhost links
demo_link = os.environ.get('DEMO_PATH', 'http://localhost:1234/')
_demolink = f"""
.. |demo-link|  replace:: `demo <{demo_link}>`__
"""

rst_prolog = _colors + _reveal_br + _demolink
rst_epilog = _symbols

# -- Options for HTML output -------------------------------------------------

html_copy_source = False
html_use_index = False
revealjs_theme = "revealjs"
html_theme = "handouts"
html_codeblock_linenos_style = "inline"
show_copyright = True
html_last_updated_fmt = '%b %d, %Y'
html_permalinks_icon = "»"

# These are annoying
html_scaled_image_link = False

# Path to logo used on slides and handouts: if given, replace theme logo
html_logo = ""

# Can override options in the themes (XXX provide list)
html_theme_options = {}

# -- Extension configuration -------------------------------------------------

# Warn about non-installed graphviz
try:
    subprocess.check_output("which dot", shell=True)

except subprocess.CalledProcessError:
    logger.warning("Graphviz is not installed: see README")
    logger.info("An error will occur if you try to build a doc using it")

# If matplotlib and scipy are installed, use them. Else, add stub to bypass:
try:
    import matplotlib
    import scipy

    extensions.append('matplotlib.sphinxext.plot_directive')
    plot_include_source = False
    plot_html_show_source_link = False
    plot_formats = [('png', 144)]
    plot_html_show_formats = False

except ImportError:
    # Use 'noplot.py' to skip drawings; will emit warning for each missing plot
    extensions.append("glide.directives.noplot")
    logger.info("Matplotlib and/or scipy is not installed: see README")
    logger.info("A warning will be show for any chart skipped in this build")

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

graphviz_output_format = 'svg'
graphviz_dot_args = [
    "-Gfontname=Helvetica",
    "-Efontname=Helvetica",
    '-Nfontname=Helvetica'
]

# MathJAX is generally used, but for PDF building, img math can be specified,
# so make sure we have both installed & set imgmath to make SVGs
html_math_renderer = "mathjax"
imgmath_image_format = 'svg'

aafig_default_options = dict(
    scale=450,
    aspect=0.5,
    proportional=True,
    foreground="#666666",
    line_width=1,
)

drawio_binary_path = "/Applications/draw.io.app/Contents/MacOS/draw.io"
drawio_builder_export_format = {
    "html": "svg",
    "latex": "pdf",
    "handouts": "png",
    "revealjs": "svg",
}
# Make drawings large, then scale in document by controlling width
drawio_default_export_scale = 400

sphinxemoji_style = 'twemoji'


def setup(app):
    # In order to use this in config, it must be declared
    app.add_config_value('revealjs_theme', 'revealjs', 'html')

    demo_path = os.environ.get("DEMO_PATH")
    app.add_config_value('demo_path', demo_path, 'env')

    app.add_node(
        todo_node,
        handouts=(visit_todo_node, depart_todo_node),
        revealjs=(visit_todo_node, depart_todo_node),
        html=(visit_todo_node, depart_todo_node),
        latex=(latex_visit_todo_node, latex_depart_todo_node),
        text=(visit_todo_node, depart_todo_node),
        man=(visit_todo_node, depart_todo_node),
        texinfo=(visit_todo_node, depart_todo_node),
        override=True,
    )
    app.add_node(
        mermaid,
        override=True,
        handouts=(html_visit_mermaid, None),
        revealjs=(html_visit_mermaid, None),
        html=(html_visit_mermaid, None),
        latex=(latex_visit_mermaid, None),
        texinfo=(texinfo_visit_mermaid, None),
        text=(text_visit_mermaid, None),
        man=(man_visit_mermaid, None),
    )
    return {'version': version, 'parallel_read_safe': True}


# todo:
# - finish tutorial
# - finish test
# - update demo? or kill it?
# - fix makefiles

mermaid_verbose = True
mermaid_output_format = "svg"
mermaid_params = ['--theme', 'default', '--width', '2200', '--backgroundColor', 'transparent']
