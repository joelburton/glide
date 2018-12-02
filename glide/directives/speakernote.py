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

def ignore_visit_speaker(self, node):
    raise SkipNode


def setup(app):
    app.add_node(speakernote,
                 latex=(ignore_visit_speaker, None))
    app.add_directive('speaker', speakernoteDirective)


class speakernote(nodes.General, nodes.Element):
    """speaker note node."""


class speakernoteDirective(Directive):
    """The directive just adds a node"""

    has_content = True

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)

        node = speakernote(text)
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]
