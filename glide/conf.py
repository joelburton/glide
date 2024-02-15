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

    # Add html disclosure arrows
    'glide.directives.details',

    # Allow external links
    'sphinx.ext.extlinks',

    # Allow mermaid
    "sphinxcontrib.mermaid",

    # Markdown support
    "myst_parser",

    # Uncopyable prompts
    "sphinx_prompt",

    # Copy button
    "sphinx_copybutton",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [
    '_*',
    'Thumbs.db',
    '.DS_Store',
    'node_modules/*', '*/node_modules/*',
    'venv/*', '*/venv/*',
    'meta',
    'retired',
]

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
.. role:: prompt

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
.. |key-legend| replace:: ``⌘`` Command |sp| |sp| ``⌃`` Ctrl |sp| |sp| ``⌥`` Alt/Opt |sp| |sp| ``⇧`` Shift |sp| |sp| ``fn`` Function |sp| |sp| ``⦿`` Click |sp| |sp| ``␣`` Space |sp| |sp| ``↵`` Enter |sp| |sp| ``⌫`` Backspace 
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
.. role:: raw-html(raw)
    :format: html
.. |reveal-br| replace:: :raw-reveal:`<br/>`
.. |br| replace:: :raw-reveal:`<br/>`
.. |handouts-br| replace:: :raw-handouts:`<br/>`
.. |all-br| replace:: :raw-reveal:`<br/>`\\ :raw-handouts:`<br/>`
.. |sp| replace:: :raw-handouts:`&nbsp;`

.. |i-macos|    replace:: :raw-html:`<i class="dark-gray bi bi-apple" alt="MacOS" title="MacOS"></i>`
.. |i-windows|  replace:: :raw-html:`<i class="blue bi bi-windows" alt="Windows" title="Windows"></i>`
.. |i-linux|    replace:: :raw-html:`<i class="orange bi bi-ubuntu" alt="Ubuntu Linux" title="Ubuntu Linux"></i>`
.. |i-chrome|   replace:: :raw-html:`<i class="dark-blue bi bi-browser-chrome" alt="Google Chrome" title="Google Chrome"></i>`
.. |i-git|      replace:: :raw-html:`<i class="orange bi bi-git" alt="Git" title="Git"></i>`
.. |i-github|   replace:: :raw-html:`<i class="bi bi-github" alt="GitHub" title="GitHub"></i>`
.. |i-advanced| replace:: :raw-html:`<i class="bi bi-rocket-takeoff" alt="Advanced" title="Advanced"></i>`
.. |i-detail|   replace:: :raw-html:`<i class="bi bi-detail" alt="Detail" title="Detail"></i>`
.. |i-terminal| replace:: :raw-html:`<i class="bi bi-terminal" alt="Terminal/Shell" title="Terminal/Shell"></i>`
.. |i-youtube|  replace:: :raw-html:`<i class="red bi bi-youtube" alt="YouTube" title="YouTube"></i>`
.. |i-amazon|  replace:: :raw-html:`<i class="orange bi bi-amazon" alt="Amazon" title="Amazon"></i>`
.. |i-linkedin|  replace:: :raw-html:`<i class="blue bi bi-linkedin" alt="Linkedin" title="Linkedin"></i>`
.. |i-android|  replace:: :raw-html:`<i class="green bi bi-android2" alt="Android" title="Android"></i>`
.. |i-facebook|  replace:: :raw-html:`<i class="green bi bi-facebook" alt="Facebook" title="Facebook"></i>`
.. |i-google|  replace:: :raw-html:`<i class="red bi bi-google" alt="Google" title="Google"></i>`
.. |i-slack|  replace:: :raw-html:`<i class="red bi bi-slack" alt="Slack" title="Slack"></i>`
.. |i-stack-overflow|  replace:: :raw-html:`<i class="red bi bi-stack-overflow" alt="Stack Overflow" title="Stack Overflow"></i>`
.. |i-twitter|  replace:: :raw-html:`<i class="blue bi bi-twitter" alt="Twitter" title="Twitter"></i>`
.. |i-pair|  replace:: :raw-html:`<i class="purple bi bi-people-fill" alt="Pair" title="Pair"></i>`
.. |i-security|  replace:: :raw-html:`<i class="red bi bi-lock-fill" alt="Security" title="Security"></i>`
.. |i-bookmark|  replace:: :raw-html:`<i class="purple bi bookmark-star-fill" alt="Bookmark" title="Bookmark"></i>`
.. |i-angellist|  replace:: :emoji:`🤞`
.. |i-star|     replace:: :emoji:`⭐`    

.. |bigo-1|      replace:: :math:`O(1)`
.. |bigo-logn|   replace:: :math:`O(\\log{}n)`
.. |bigo-logn2|  replace:: :math:`O(\\log_2{}n)`
.. |bigo-n|      replace:: :math:`O(n)`
.. |bigo-nlogn|  replace:: :math:`O(n\\log{}n)`
.. |bigo-ndlogn| replace:: :math:`O(n\\cdot\\log{}n)`
.. |bigo-nlog2n| replace:: :math:`O(n\\log_2{}n)`
.. |bigo-n2|     replace:: :math:`O(n^2)`
.. |bigo-2n|     replace:: :math:`O(2^n)`
.. |bigo-nfact|  replace:: :math:`O(n!)`
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

copybutton_exclude = '.linenos, .gp, .go, .c'
copybutton_selector = ".add-copybutton pre"

