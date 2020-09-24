import subprocess
import os

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

needs_sphinx = '3.2.1'

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',

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
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'node_modules', 'venv']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

linkcheck_ignore = [r'http://localhost:\d+/']

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
_symbols = """
.. |nbsp|      unicode:: U+000A0 .. NONBREAKING SPACE
.. |rarr|      unicode:: U+02192 .. RIGHTWARDS ARROW
.. |larr|      unicode:: U+02190 .. LEFTWARDS ARROW
.. |darr|      unicode:: U+02193 .. DOWNWARDS ARROW
.. |lrarr|     unicode:: U+02194 .. LEFT RIGHT ARROW
.. |plus|      unicode:: U+0002B .. PLUS SIGN
.. |times|     unicode:: U+000D7 .. MULTIPLICATION SIGN
.. |divide|    unicode:: U+000F7 .. DIVISION SIGN

.. |check|     unicode:: U+02713 .. CHECK MARK
.. |approx|    unicode:: U+02248 .. ALMOST EQUAL TO
.. |sub2|      unicode:: U+02082 .. SUBSCRIPT 2
.. |super2|    unicode:: U+000B2 .. SUPERSCRIPT 2
.. |spades|    unicode:: U+02660 .. SPADES
.. |hearts|    unicode:: U+02665 .. HEARTS
.. |diamonds|  unicode:: U+02666 .. DIAMONDS
.. |clubs|     unicode:: U+02663 .. CLUBS
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
.. |reveal-br| replace:: :raw-reveal:`<br>`
.. |br| replace:: :raw-reveal:`<br>`
.. |handouts-br| replace:: :raw-handouts:`<br>`
.. |all-br| replace:: :raw-reveal:`<br>`\\ :raw-handouts:`<br>`
"""
# Glide 1.5 added |br| as a shorter synonym for this.

# Can use like |demo-link| to show a URL from env var
_demolink = f"""
.. |demo-link|  replace:: `demo <{os.environ.get('DEMO_PATH')}>`__
"""

rst_prolog = _colors + _reveal_br + _demolink
rst_epilog = _symbols

# -- Options for HTML output -------------------------------------------------

html_copy_source = False
html_use_index = False
revealjs_theme = "revealjs"
html_theme = "handouts"
html_add_permalinks = ""
html_codeblock_linenos_style = "inline"


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


def setup(app):
    # In order to use this in config, it must be declared
    app.add_config_value('revealjs_theme', 'alabaster', 'html')

    demo_path = os.environ.get("DEMO_PATH")
    app.add_config_value('demo_path', demo_path, 'env')

    return {'version': version, 'parallel_read_safe': True}
