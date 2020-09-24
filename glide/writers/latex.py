"""Sphinx writer/translator for LaTeX books.

This has often been one of the more difficult parts to maintain, but since
~2015, Sphinx's default LaTeX has been much nicer, and far less serious stuff
needs to be overridden here.

If this breaks with future versions of Sphinx, one thing that typically works
is to just not use this --- the default appearance of Sphinx in LaTeX is pretty
similar to this. You can comment out the loader for this in the glide conf.py.
"""

from docutils.nodes import SkipNode, Node
from sphinx.writers.latex import LaTeXTranslator as BaseTranslator

from glide import version, logger

COLOR_TO_LATEX = {
    'red': 'red',
    'green': 'olive',
    'orange': 'orange',
    'tan': 'brown',
    'blue': 'blue',
    'gray': 'gray',
    'gone': 'lightgray'
    # inv-red is handled below
}


class LaTeXTranslator(BaseTranslator):
    """Translator for Sphinx structure -> Joel-style LaTeX."""

    def visit_inline(self, node):
        """Handle colors given like :red:`hello`."""

        color = (node.get('classes', [None]) or [None])[0]

        if color in COLOR_TO_LATEX:
            self.body.append('\\textcolor{%s}{' % COLOR_TO_LATEX[color])
            self.context.append("}")

        elif color == "inv-red":
            self.body.append(
                '\\color{white}\\colorbox{%s}{' % COLOR_TO_LATEX['red'])
            self.context.append("}")

        else:
            return BaseTranslator.visit_inline(self, node)

    def visit_topic(self, node):
        """Default Sphinx look is unbearably ugly. Make it look like a note."""

        return BaseTranslator.visit_admonition(self, node)

    def depart_topic(self, node):
        """Default Sphinx look is unbearably ugly. Make it look like a note."""

        return BaseTranslator.depart_admonition(self, node)

    def visit_sidebar(self, node):
        """Default Sphinx look is unbearably ugly. Make it look like a note."""

        return BaseTranslator.visit_admonition(self, node)

    def depart_sidebar(self, node):
        """Default Sphinx look is unbearably ugly. Make it look like a note."""

        return BaseTranslator.depart_admonition(self, node)

    def visit_title_reference(self, node):
        """Change to bold + italics, as that's our style."""
        self.body.append('\\emph{\\textbf{')

    def depart_title_reference(self, node):
        """Close title opening tag."""
        self.body.append(r'}}')

    def visit_reference(self, node):
        """Don't make email into a link."""

        if node.get('refuri', '').startswith("mailto:"):
            self.context.append('')
        else:
            BaseTranslator.visit_reference(self, node)

    def visit_image(self, node):
        """Don't print images with noprint class."""

        if "noprint" in node.get('classes', []):
            raise SkipNode

        return BaseTranslator.visit_image(self, node)

    def unknown_visit(self, node: Node) -> None:
        """We should never get here, so warn user."""

        logger.warning("Handouts hit unexpected node: %s", node)
        raise SkipNode


def setup(app):
    app.set_translator('latex', LaTeXTranslator)
    return {'version': version, 'parallel_read_safe': True}
