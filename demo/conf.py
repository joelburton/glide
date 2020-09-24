from glide.conf import *

# -- Project information -----------------------------------------------------

project = 'Demo'
# noinspection PyShadowingBuiltins
copyright = '2020, Joel Burton'
author = 'Joel Burton'

# The short X.Y version
version = '(Version)'
# The full version, including alpha/beta/rc tags
release = '(Demo Release)'

# -- General configuration ---------------------------------------------------

pygments_style = 'sphinx'

# RST Prolog: this stuff is added to every RST file before it's processed
_curric_name = f"""
.. |curric-name|   replace:: {os.environ.get('CURRIC_NAME')}
"""

rst_prolog += _curric_name

# -- Options for HTML output -------------------------------------------------

# revealjs_theme = "revealjs"
# html_theme = "handouts"

# Path to logo used on slides and handouts: if given, replace theme logo
# html_logo = ""

# Can override options in the themes (XXX provide list)
# html_theme_options = {}

# -- Options for LaTeX output ------------------------------------------------

# latex_elements = {
#   'papersize': 'letterpaper',
#   'pointsize': '10pt',
#   'preamble': '',
#   'figure_align': 'htbp',
# }

# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'Demo.tex', 'Demo Documentation', 'Joel Burton', 'manual'),
]

latex_engine = "xelatex"
latex_show_urls = "inline"

# -- Extension configuration -------------------------------------------------

# If false, this extension produces no output
todo_include_todos = True
