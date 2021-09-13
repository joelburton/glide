from os import path
from sphinx.util.logging import getLogger

version = "2.2.0"

logger = getLogger("glide")


def setup(app):
    app.add_html_theme(
        'revealjs',
        path.abspath(path.join(path.dirname(__file__), "themes", "revealjs")))
    app.add_html_theme(
        'handouts',
        path.abspath(path.join(path.dirname(__file__), "themes", "handouts")))
