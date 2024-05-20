"""Speaker notes directive.

Adds a "speaker" directive for RevealJS speaker notes.

For example:

  Dictionaries are cool.

  .. speaker::

    Explain this part really well!

These are ignored in non-RevealJS builders.
"""

from docutils import nodes
from docutils.nodes import SkipNode
from docutils.parsers.rst import Directive

from glide import version


# noinspection PyPep8Naming
class speakernote(nodes.General, nodes.Element):
    """speaker note node."""


class SpeakernoteDirective(Directive):
    """The directive just adds a node for revealjs builder to find."""

    has_content = True

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)

        node = speakernote(text)
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


# noinspection PyUnusedLocal
def ignore(self, node):
    """All non-revealjs builders should use this."""
    raise SkipNode


# noinspection PyUnusedLocal
def visit(revealjs_translator, node):
    """Wrap contents in an aside element, which is used by revealjs JS."""
    revealjs_translator.body.append("<aside class='notes'>")


# noinspection PyUnusedLocal
def depart(revealjs_translator, node):
    """End the aside element we started."""
    revealjs_translator.body.append("</aside>")


def setup(app):
    app.add_node(
        speakernote,
        # Ignore on any builder except revealjs --- if there are newer builders,
        # these should be added here.
        epub=(ignore, None),
        html=(ignore, None),
        handouts=(ignore, None),
        singlehandouts=(ignore, None),
        latex=(ignore, None),
        revealjs=(visit, depart),
        text=(ignore, None),
        man=(ignore, None),
    )
    app.add_directive('speaker', SpeakernoteDirective)
    return {'version': version, 'parallel_read_safe': True}
