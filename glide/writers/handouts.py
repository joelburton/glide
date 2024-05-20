"""Sphinx translator and builder for handouts."""
from typing import Any

from docutils.nodes import SkipNode, section, Element
from sphinx.application import Sphinx
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.builders.singlehtml import SingleFileHTMLBuilder
from sphinx.environment import BuildEnvironment
from sphinx.writers.html5 import HTML5Translator

from glide import version


class HandoutsTranslator(HTML5Translator):
    """Translator for Sphinx structure -> HTML handouts."""

    # Keep track of previous title so that we don't repeat ourselves
    _previous_title = ""

    def visit_title(self, node: Element) -> None:
        """Handle titles.

        When a section has the same title as the previous, don't show it.

           Since we're also generating slides, we often have this:

             Using jQuery
             ------------

             Using jQuery
             ------------

           We need this to make two separate slides---but we don't want the
           handouts to have a new heading for the second heading.
        """

        if isinstance(node.parent, section):
            if str(node) == self._previous_title:
                # Don't make a title if our title would be same as previous
                raise SkipNode
            self._previous_title = str(node)

        return super().visit_title(node)


class HandoutsBuilder(StandaloneHTMLBuilder):
    """Builder for making HTML handouts using Sphinx."""

    name = 'handouts'

    # Do not generate any support for search
    search = None


class SingleFileHandoutsBuilder(SingleFileHTMLBuilder):
    """Builder for making HTML->PDF handouts using Sphinx."""

    name = 'singlehandouts'

    # Do not generate any support for search
    search = None

    def __init__(self, app: Sphinx, env: BuildEnvironment) -> None:
        super().__init__(app, env)
        self.config.mermaid_output_format = "png"
        self.config.html_math_renderer = "imgmath"


def setup(app):
    app.add_builder(SingleFileHandoutsBuilder)
    app.add_builder(HandoutsBuilder)
    app.set_translator('singlehandouts', HandoutsTranslator)
    app.set_translator('handouts', HandoutsTranslator)
    return {'version': version, 'parallel_read_safe': True}
