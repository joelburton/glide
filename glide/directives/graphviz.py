"""Directive for making graphs with Graphviz.

This subclasses Sphinx's standard Graphviz directive, to add one critical
feature: resizing based on the which builder will be used.

For example::

  .. jdigraph:: cloning
    :size: 10,10

    ... rest of graphviz here

This same capability is also added onto the normal directives, so that you can
use the directives named "graphviz", "digraph", and "graph" rather than having
to use the "j" versions. In time, the "j" names will be deprecated.

(We need this because we often want to make different sizes for slide versus
handouts versions of graphs)
"""

from toolz import curry, merge
from docutils.parsers.rst.directives import unchanged
from docutils import nodes
from sphinx.ext.graphviz import graphviz, render_dot_latex, render_dot_html
from sphinx.ext.graphviz import Graphviz, GraphvizSimple

from glide import version


# noinspection PyUnresolvedReferences
class Sizeable:
    """Add sizeable feature for Graphviz subclasses.

    It adds one new options:
    - size: "x,y"
    """

    def add_builder_size_option_to_graphviz_node(self, node):
        """Add builder-specific sizes to graphviz node.

        These size option can be on the directive for our subclasses, and this
        is used to decide the size for the graph, scaled appropriately for the
        different builders. Later in the process, the writer will find the
        builder-specific setting added here and use that in the actual graphviz
        generation process. """

        if 'size' in self.options:
            x, y = [float(p) for p in self.options['size'].split(",")]

            node['options']['revealjs'] = "-Gsize=%s,%s" % (x, y)
            node['options']['latex'] = "-Gsize=%s,%s" % (x / 2.4, y / 2.4)
            node['options']['handouts'] = "-Gsize=%s,%s" % (x / 2, y / 2)

    # noinspection PyAttributeOutsideInit
    def run(self):
        # Strip off the "j" in front of the directives because the name of
        # the directive is used to decide if it creates a digraph or graph.
        self.name = self.name[1:] if self.name.startswith("j") else self.name

        # Perform a minor convenience: the name of a graph cannot contain
        # special punctuation other unless it is in double-quotes. Since this
        # is a common and annoying mistake for people who try to create graphs
        # with names like 'search-tree', this will automatically make that named
        # '"search-tree"'.
        if self.name == "digraph" or self.name == "graph":
            if not self.arguments[0].startswith('"'):
                self.arguments[0] = f'"{self.arguments[0]}"'

        # use underlying run() and tweak the resulting nodelist to add size
        node = super().run()[0]

        if isinstance(node, graphviz):
            self.add_builder_size_option_to_graphviz_node(node)
        elif isinstance(node, nodes.figure):
            self.add_builder_size_option_to_graphviz_node(node.children[0])

        return [node]


class JGraphviz(Sizeable, Graphviz):
    """Monkey-patchy subclass of the standard Sphinx graphviz directive."""

    option_spec = merge(Graphviz.option_spec, {'size': unchanged})


class JGraphvizSimple(Sizeable, GraphvizSimple):
    """Monkey-patchy subclass of the standard Sphinx (di)graph directive."""

    option_spec = merge(GraphvizSimple.option_spec, {'size': unchanged})


@curry
def visit_jgraphviz(render_function, self, node):
    """Handle node in html or latex documents, depending on render_func.

    Our version adds options based upon the current builder, so we can set
    builder-specific options. It's a bit of a hack, but these are put directly
    on the builder.
    """

    options = []
    if self.builder.name in node['options']:
        builder_specific_options = node['options'][self.builder.name]
        options = [o.strip() for o in builder_specific_options.split(' ')]
    orig_graphviz_dot_args = self.builder.config.graphviz_dot_args
    self.builder.config.graphviz_dot_args = orig_graphviz_dot_args + options

    try:
        render_function(self, node, node['code'], node['options'])
    finally:
        self.builder.config.graphviz_dot_args = orig_graphviz_dot_args


def setup(app):
    app.setup_extension("sphinx.ext.graphviz")
    app.add_node(
        graphviz,
        override=True,
        html=(visit_jgraphviz(render_dot_html), None),
        revealjs=(visit_jgraphviz(render_dot_html), None),
        latex=(visit_jgraphviz(render_dot_latex), None),
    )
    app.add_directive('jgraphviz', JGraphviz)
    app.add_directive('jgraph', JGraphvizSimple)
    app.add_directive('jdigraph', JGraphvizSimple)
    app.add_directive('graphviz', JGraphviz, override=True)
    app.add_directive('graph', JGraphvizSimple, override=True)
    app.add_directive('digraph', JGraphvizSimple, override=True)
    return {'version': version, 'parallel_read_safe': True}
