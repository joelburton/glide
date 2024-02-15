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
class details(nodes.Element):
    """Details node."""


#         class MyDirective(Directive):
#                has_content = True
#                required_arguments = 1
#                optional_arguments = 0
#                final_argument_whitespace = True
#                option_spec = {
#                    'class': directives.class_option,
#                    'name': directives.unchanged,
#                }

class DetailsDirective(Directive):
    """The directive just adds a node for builder to find."""

    has_content = True
    required_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "class": "directives.class_option",
    }

    def run(self):
        self.assert_has_content()
        text = "\n".join(self.content)
        node = details(text)
        node.title = self.arguments[0]
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


# noinspection PyUnusedLocal
def ignore_visit_speakernote(self, node):
    """All non-revealjs builders should use this."""
    raise SkipNode


# noinspection PyUnusedLocal
def html_visit_details(translator, node):
    """Wrap contents in an details."""
    translator.body.append("<details>")
    if title := getattr(node, "title", ""):
        translator.body.append(f"<summary>{title}</summary>")


# noinspection PyUnusedLocal
def html_depart_details(translator, node):
    """End the details element we started."""
    translator.body.append("</details>")


def setup(app):
    app.add_node(
        details,
        # Ignore on any builder except revealjs --- if there are newer builders,
        # these should be added here.
        epub=(ignore_visit_speakernote, None),
        html=(html_visit_details, html_depart_details),
        handouts=(html_visit_details, html_depart_details),
        latex=(ignore_visit_speakernote, None),
        revealjs=(ignore_visit_speakernote, None),
        text=(ignore_visit_speakernote, None),
        man=(ignore_visit_speakernote, None),
    )
    app.add_directive('details', DetailsDirective)
    return {'version': version, 'parallel_read_safe': True}
