"""Details directive.

Adds expanding disclosure-arrow details.

These are ignored in non-RevealJS builders.
"""

from docutils import nodes
from docutils.nodes import SkipNode
from docutils.parsers.rst import Directive

from glide import version


# noinspection PyPep8Naming
class details(nodes.Element):
    """Details node."""


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
def ignore(self, node):
    raise SkipNode


# noinspection PyUnusedLocal
def visit(translator, node):
    """Wrap contents in details node."""
    translator.body.append("<details>")
    if title := getattr(node, "title", ""):
        translator.body.append(f"<summary>{title}</summary>")


# noinspection PyUnusedLocal
def depart(translator, node):
    """End the details element we started."""
    translator.body.append("</details>")


def setup(app):
    app.add_node(
        details,
        epub=(ignore, None),
        html=(visit, depart),
        handouts=(visit, depart),
        latex=(ignore, None),
        revealjs=(ignore, None),
        text=(ignore, None),
        man=(ignore, None),
    )
    app.add_directive('details', DetailsDirective)
    return {'version': version, 'parallel_read_safe': True}
