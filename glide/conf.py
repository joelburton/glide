import subprocess

from sphinx.environment import BuildEnvironment
from sphinx.ext.todo import todo_node
from sphinxcontrib.mermaid import mermaid
from sphinxcontrib.youtube.youtube import youtube

from glide import version, logger, copy_translation_handlers
from .rst_epilog import glide_rst_epilog, glide_rst_prolog
from .relfn2path_patch import relfn2path_patched

# -- Project information -----------------------------------------------------
# Define these in actual usage conf.py files

# project = 'Demo'
# copyright = '2018, Joel Burton'
# author = 'Joel Burton'
#
#
# version = ''    # The short X.Y version -- shows on generated docs
# release = ''    # The full version, including alpha/beta/rc tags

# -- General configuration ---------------------------------------------------

BuildEnvironment.relfn2path = relfn2path_patched

needs_sphinx = '7'

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'sphinx.ext.imgmath',
    'sphinxcontrib.drawio',
    'sphinxemoji.sphinxemoji',
    'aafigure.sphinxext',
    'glide.directives.diagram',

    'glide.writers.handouts',
    'glide.writers.revealjs',
    # 'glide.writers.latex',

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

    # Add download links
    'glide.directives.downloads',

    # Allow external links
    'sphinx.ext.extlinks',

    # Allow mermaid
    "sphinxcontrib.mermaid",

    # Markdown support
    "myst_parser",

    # Copy button
    "sphinx_copybutton",

    # Editor
    "glide.directives.editor",

    # YouTube
    "sphinxcontrib.youtube"
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
    'raw',
    '**/_index.rst',
    '**/.pytest_cache',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

linkcheck_ignore = [r'http://localhost:\d+/']

rst_prolog = glide_rst_prolog
rst_epilog = glide_rst_epilog


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

# Need this because else linkcheck issues warning about building aafig stuff
# noinspection PyUnresolvedReferences
aafig_format = {'': None, 'html': 'svg'}

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
    app.add_config_value('glide_root', '', 'env')

    # Copy visit/depart handlers for new Glide builder types
    copy_translation_handlers(app, todo_node)
    copy_translation_handlers(app, mermaid)
    copy_translation_handlers(app, youtube, singlehandouts="epub")

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
copybutton_copy_empty_lines = False

myst_suppress_warnings = ["myst.header"]  # FIXME does this do anything?

html_show_sphinx = False

sphinxemoji_source = 'twemoji-patched.js'
