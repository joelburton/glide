"""Sphinx writer/translator for LaTeX books."""

from docutils import nodes
from docutils.nodes import SkipNode
from sphinx.writers.latex import LaTeXTranslator as BaseTranslator, UnsupportedError

__author__ = "Joel Burton <joel@joelburton.com>"

COLOR_MAP = {
    'red': 'red',
    'green': 'green',
    'orange': 'orange',
    'tan': 'tan',
    'blue': 'blue',
    'gray': 'gray',
}

# Untested since Sphinx 1.7

class LaTeXTranslator(BaseTranslator):
    """Translator for Sphinx structure -> Joel-style LaTeX."""

    def visit_inline(self, node):
        """Handle colors given like :red:`hello`."""

        color = (node.get('classes', [None]) or [None])[0]

        if color == "gone":
            # Change color and add strike-through
            self.body.append("\\color{gray}\\st{")
            self.context.append("}")

        elif color in COLOR_MAP:
            self.body.append('\\textcolor{%s}{' % COLOR_MAP[color])
            self.context.append("}")

        elif color == "inv-red":
            self.body.append('\\color{white}\\colorbox{%s}{' % COLOR_MAP['red'])
            self.context.append("}")

        else:
            return BaseTranslator.visit_inline(self, node)

    def visit_topic(self, node):
        """The default Sphinx look is unbearably ugly. Make it look like a note."""

        # Get the note style but not the "Note: " label
        self.body.append(u'\n\\begin{notice}{note}{}')

    def depart_topic(self, node):
        """The default Sphinx look is unbearably ugly. Make it look like a note."""

        return BaseTranslator.depart_admonition(self, node)

    def visit_sidebar(self, node):
        """The default Sphinx look is unbearably ugly. Make it look like a note."""

        return BaseTranslator.visit_note(self, node)

    def depart_sidebar(self, node):
        """The default Sphinx look is unbearably ugly. Make it look like a note."""

        return BaseTranslator.depart_note(self, node)

    def visit_title_reference(self, node):
        """Change to bold + italics, as that's our style."""
        self.body.append(r'\emph{\textbf{')

    def depart_title_reference(self, node):
        self.body.append(r'}}')

    def visit_literal_block(self, node):
        """Visit literal block/parsed-literal/code block.

        Overridden to change handling of parsed-literal, so we draw a box around it.
        """

        if self.in_footnote:
            raise UnsupportedError('%s:%s: literal blocks in footnotes are '
                                   'not supported by LaTeX' %
                                   (self.curfilestack[-1], node.line))
        if node.rawsource != node.astext():
            # most probably a parsed-literal block -- don't highlight
            # Joel: this is the only line that changed
            self.body.append(r"\begin{Verbatim}[commandchars=\\\{\},frame=none]" + "\n")
        else:
            code = node.astext().rstrip('\n')
            lang = self.hlsettingstack[-1][0]
            linenos = code.count('\n') >= self.hlsettingstack[-1][1] - 1
            highlight_args = node.get('highlight_args', {})
            if 'language' in node:
                # code-block directives
                lang = node['language']
                highlight_args['force'] = True
            if 'linenos' in node:
                linenos = node['linenos']
            if lang is self.hlsettingstack[0][0]:
                # only pass highlighter options for original language
                opts = self.builder.config.highlight_options
            else:
                opts = {}

            def warner(msg):
                self.builder.warn(msg, (self.curfilestack[-1], node.line))
            hlcode = self.highlighter.highlight_block(code, lang, opts=opts,
                                                      warn=warner, linenos=linenos,
                                                      **highlight_args)
            # must use original Verbatim environment and "tabular" environment
            if self.table:
                hlcode = hlcode.replace('\\begin{Verbatim}',
                                        '\\begin{OriginalVerbatim}')
                self.table.has_problematic = True
                self.table.has_verbatim = True
            # get consistent trailer
            hlcode = hlcode.rstrip()[:-14]  # strip \end{Verbatim}
            hlcode = hlcode.rstrip() + '\n'
            self.body.append('\n' + hlcode + '\\end{%sVerbatim}\n' %
                             (self.table and 'Original' or ''))
            raise nodes.SkipNode

    def depart_literal_block(self, node):
        """Since we're changing formatting for parsed-literals, change the closing tag."""

        self.body.append('\n\\end{Verbatim}\n')

    def visit_reference(self, node):
        """Don't make email into a link."""

        if node.get('refuri', '').startswith("mailto:"):
            self.context.append('')
        else:
            BaseTranslator.visit_reference(self, node)

    def visit_image(self, node):
        if "noprint" in node.get('classes', []):
            raise SkipNode

        return BaseTranslator.visit_image(self, node)


def setup(app):
    app.set_translator('latex', LaTeXTranslator)
