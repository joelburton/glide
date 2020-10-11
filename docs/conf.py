from glide.conf import *

# -- Project information -----------------------------------------------------

project = 'Documentation'
# noinspection PyShadowingBuiltins
copyright = '2020, Joel Burton'
author = 'Joel Burton'

version = "2.0"
release = f"Glide {version}"

# -- General configuration ---------------------------------------------------

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

# Can override options in the themes
# html_theme_options = {}

# -- Extension configuration -------------------------------------------------

todo_include_todos = True
