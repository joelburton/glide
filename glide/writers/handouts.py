"""Sphinx translator and builder for handouts."""

from docutils import nodes
from docutils.nodes import SkipNode, section, note, warning
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.writers.html import HTMLTranslator

__author__ = "Joel Burton <joel@joelburton.com>"


# Updated for Sphinx 1.7


class HandoutsTranslator(HTMLTranslator):
    """Translator for Sphinx structure -> HTML handouts.

    Overrides Sphinx HTML translator.
    """

    _previous_title = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings.field_name_limit = 50

    def visit_title(self, node):
        """Handle titles.

        Two changes from the standard HTML Writer:

        1) For ".. note" and ".. warning", don't make "Note" or "Warning" the
           title -- use the first paragraph of the body as the title.

        2) When a section has the same title as the previous, don't show it.

           Since we're also generating slides, we often have this:

             Using jQuery
             ------------

             blah, blah

             Using jQuery
             ------------

             more blah

           We need this to make two separate slides---but we don't want the handouts
           to have a new heading for the second heading.
        """

        # Notes and Warnings normally automatically get a admonition-title of "Note" or
        # "Warning". We want to use the first paragraph as the title, so skip making
        # the normal title
        if isinstance(node.parent, note) or isinstance(node.parent, warning):
            raise SkipNode

        if isinstance(node.parent, section):

            if str(node) == self._previous_title:
                raise SkipNode

            self._previous_title = str(node)

        return super().visit_title(node)

    def should_be_compact_paragraph(self, node):
        """Can this text be 'compacted' into a non-paragraph?

        Sphinx will try to 'compact' text into not being a paragraph when possible.
        For example, for:

          - hello

          - there

          - reader

        It realizes that since those are simple lines, it doesn't need to put
        <p> tags around the text inside the <li> tags---whereas for::

          - hello

          - there

          - reader

            I love readers!

        It would need to keep paragraphs inside the <li> tags.

        We often put text inside containers for incremental-appearance, like this:

          The answer is:

          .. container:: one-incremental

            Forty-two

        Seeing just a simple thing inside the container, Sphinx wouldn't wrap it
        in a paragraph, just <div>. This makes for ugly line breaks.

        Therefore, when we're directly inside a container, we should never
        compact paragraphs. Otherwise, follow Sphinx's rules.

        Should you want to compact things directly inside a container, you can
        add a 'non-paragraph' class to it.
        """

        if isinstance(node.parent, nodes.container):
            if 'non-paragraph' not in node.parent.attributes['classes']:
                return False

        return super().should_be_compact_paragraph(node)


class HandoutsBuilder(StandaloneHTMLBuilder):
    """Builder for making HTML handouts using Sphinx."""

    name = 'handouts'

    # Do not generate any support for search
    search = None


def setup(app):
    app.add_builder(HandoutsBuilder)
    app.set_translator('handouts', HandoutsTranslator)
