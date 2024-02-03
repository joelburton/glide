"""Sphinx translator and builder for handouts."""

from docutils.nodes import SkipNode, section, Node, Element
from sphinx.application import Sphinx
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.builders.singlehtml import SingleFileHTMLBuilder
from sphinx.environment import BuildEnvironment
from sphinx.writers.html import HTMLTranslator

from glide import version, logger
from .common import FixCompactParagraphsTranslatorMixin


class HandoutsTranslator(FixCompactParagraphsTranslatorMixin, HTMLTranslator):
    """Translator for Sphinx structure -> HTML handouts."""

    # Keep track of previous title so that we don't repeat ourselves
    _previous_title = ""

    def __init__(self, *args):
        super().__init__(*args)
        # The default value here is silly-low, and this is the only way to fix.
        # These are used for "fields" used to describe documents (often, but
        # not always at the top), like:
        #
        # :author: Elmo
        # :color: red
        self.settings.field_name_limit = 50

    def visit_title(self, node: Element) -> None:
        """Handle titles.

        Two changes from the standard HTML Writer:

        1) For ".. note" and ".. warning", don't make "Note" or "Warning" the
           title -- use the first paragraph of the body as the title.

        2) When a section has the same title as the previous, don't show it.

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

    def visit_admonition(self, node, name=""):
        """Subclass to add marker class to generic admonitions."""

        if not name:
            node.attributes['classes'] += ["admonition-generic"]
        return super().visit_admonition(node, name)

    def unknown_visit(self, node: Node) -> None:
        """We should never get here, so warn user."""

        logger.warning("Handouts hit unexpected node: %s", node)
        raise SkipNode

    # todo doc:
    # doing this so highlgiht and literals both have a wrapper around pre

    # add newline after opening tag, don't use <code> for code

    # super()._visit_literal_block = super().visit_literal_block

    def grand_visit_literal_block(self, node):
        self.body.append(self.starttag(node, 'div', CLASS='parsed-literal-wrapper'))
        # prob should make this <pre> myself, so it doesn't get the classes
        self.body.append("<pre>")
        # self.body.append(self.starttag(node, 'pre', CLASS='literal-block'))

    # add newline
    def grand_depart_literal_block(self, node):
        self.body.append('\n</pre>\n</div>\n')

# need to do this to make a wrapper for parsed-literal::
from docutils.writers.html4css1 import HTMLTranslator as Grandparent
Grandparent.visit_literal_block = HandoutsTranslator.grand_visit_literal_block
Grandparent.depart_literal_block = HandoutsTranslator.grand_depart_literal_block


class HandoutsBuilder(StandaloneHTMLBuilder):
    """Builder for making HTML handouts using Sphinx."""

    name = 'handouts'

    # Do not generate any support for search
    search = None

    def init_js_files(self) -> None:
        """Override to remove not-needed JS files."""

        # This is what we're overriding to remove
        # self.add_js_file('jquery.js')
        # self.add_js_file('underscore.js')
        # self.add_js_file('doctools.js')
        # self.add_js_file('language_data.js')

        for filename, attrs in self.app.registry.js_files:
            self.add_js_file(filename, **attrs)

        for filename, attrs in self.get_builder_config('js_files', 'html'):
            self.add_js_file(filename, **attrs)

        if self.config.language and self._get_translations_js():
            self.add_js_file('translations.js')


class SingleFileHandoutsBuilder(SingleFileHTMLBuilder):
    """Builder for making HTML handouts using Sphinx."""

    name = 'singlehandouts'

    # Do not generate any support for search
    search = None

    def __init__(self, app: Sphinx, env: BuildEnvironment) -> None:
        super().__init__(app, env)
        self.config.mermaid_output_format = "png"

    def init_js_files(self) -> None:
        """Override to remove not-needed JS files."""

        # This is what we're overriding to remove
        # self.add_js_file('jquery.js')
        # self.add_js_file('underscore.js')
        # self.add_js_file('doctools.js')
        # self.add_js_file('language_data.js')

        for filename, attrs in self.app.registry.js_files:
            self.add_js_file(filename, **attrs)

        for filename, attrs in self.get_builder_config('js_files', 'html'):
            self.add_js_file(filename, **attrs)

        if self.config.language and self._get_translations_js():
            self.add_js_file('translations.js')


def setup(app):
    app.add_builder(HandoutsBuilder)
    app.add_builder(SingleFileHandoutsBuilder)
    app.set_translator('handouts', HandoutsTranslator)
    app.set_translator('singlehandouts', HandoutsTranslator)
    return {'version': version, 'parallel_read_safe': True}
