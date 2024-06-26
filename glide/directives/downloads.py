"""Downloads directive.

.. dl-code::
.. dl-solution::
.. dl-demo::
.. dl-generic::

Can provide a title for these (must for dl-generic):

.. dl-code::
    :title: Download our super-special code!

Can provide a path to use instead of default:

.. dl-code:: ../../../code.tar.gz

These are ignored in non-handouts builders.
"""

from docutils import nodes
from docutils.nodes import SkipNode
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged_required
from docutils.statemachine import StringList

from glide import version


class dl_label(nodes.General, nodes.TextElement):
    """Download label."""


# noinspection PyPep8Naming
class dl_link(nodes.Admonition, nodes.Element):
    """Download link node."""


class DownloadsLinkDirective(Directive):
    """The directive just adds a node for builder to find."""

    has_content = False
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "class": "directives.class_option",
        "title": unchanged_required,
    }

    PATHS = {
        "dl-code": "../code.zip",
        "dl-solution": "../solution.zip",
        "dl-demo": "../demo.zip",
    }

    TITLES = {
        "dl-code": "|i-file-code| Download starter code",
        "dl-solution": "|i-file-solution| Download solution",
        "dl-demo": "|i-file-code| Download demo",
    }

    def run(self):
        path = self.arguments[0] if self.arguments else self.PATHS.get(self.name)
        node = dl_link()
        node.path = path

        title = self.options.get("title", self.TITLES.get(self.name))
        parsed = nodes.Element()
        self.state.nested_parse(
            StringList([title], source=''),
            self.content_offset,
            parsed)
        node += dl_label(parsed[0].rawsource, '', *parsed[0].children)
        return [node]


# noinspection PyUnusedLocal
def ignore(self, node):
    """All non-handouts builders should use this."""
    raise SkipNode


# noinspection PyUnusedLocal
def visit_link(translator, node):
    """Add link."""

    prefix = "../" * translator.builder.current_docname.count("/")
    translator.body.append(
        f"""<p class="dl-link"><a href="{prefix}{node.path}">""")


def visit_label(translator, node: dl_label):
    return node


def depart_label(translator, node: dl_label):
    return


def depart_link(translator, node):
    translator.body.append("</a></p>")


def setup(app):
    app.add_node(
        dl_link,
        epub=(ignore, None),
        html=(ignore, None),
        handouts=(visit_link, depart_link),
        singlehandouts=(ignore, None),
        latex=(ignore, None),
        revealjs=(ignore, None),
        text=(ignore, None),
        man=(ignore, None),
    )
    app.add_node(dl_label, handouts=(visit_label, depart_label))
    app.add_directive('dl-code', DownloadsLinkDirective)
    app.add_directive('dl-solution', DownloadsLinkDirective)
    app.add_directive('dl-demo', DownloadsLinkDirective)
    app.add_directive('dl-generic', DownloadsLinkDirective)
    return {'version': version, 'parallel_read_safe': True}
