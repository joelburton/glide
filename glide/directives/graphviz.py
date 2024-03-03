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

import re

from sphinx.util.i18n import search_image_for_language
from toolz import curry, merge
from docutils.parsers.rst.directives import unchanged
from docutils import nodes
from sphinx.ext.graphviz import graphviz, render_dot_latex, render_dot_html, figure_wrapper
from sphinx.ext.graphviz import Graphviz, GraphvizSimple
from docutils.nodes import Node
from sphinx.locale import _, __


from glide import version


# noinspection PyUnresolvedReferences
class Sizeable:
    """Add sizeable feature for Graphviz subclasses.

    It adds one new options:
    - size: "x,y"
    """

    required_arguments = 0
    optional_arguments = 1

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
            node['options']['singlehandouts'] = "-Gsize=%s,%s" % (x / 2, y / 2)

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
            if len(self.arguments) == 0:
                self.arguments = [""]
            if not self.arguments[0].startswith('"'):
                self.arguments[0] = f'"{self.arguments[0]}"'

        # use underlying run() and tweak the resulting nodelist to add size
        node = super().run()[0]

        if isinstance(node, graphviz):
            self.add_builder_size_option_to_graphviz_node(node)
        elif isinstance(node, nodes.figure):
            self.add_builder_size_option_to_graphviz_node(node.children[0])

        return [node]


def merge_graphs(graphs):
    """Takes a list of graphs and merges them into a single graph.

        >>> a = "  graph { a -- b }"
        >>> b = "graph { b -- c }"
        >>> c = "graph { node [color=green] }"
        >>> print(merge_graphs([a, b, c]))
        graph {
        a -- b
        b -- c
        node [color=green]
        }
    """

    ptn = re.compile(r"([^{]+){(.+)}", re.DOTALL)
    graphs = [g.strip() for g in graphs]
    graphs = [ptn.match(g).groups() for g in graphs]
    opens = graphs[0][0]
    assert all(g[0] == opens for g in graphs), f"All must start with: {opens}"
    return "\n".join([opens + "{"] + [*(g[1].strip() for g in graphs)] + ["}"])


class JGraphvizMergeable(Graphviz):
    optional_arguments = 9

    # this is copied directly from the orig graphviz module; it adds the
    # ability for there to be multiple arguments PLUS content, and it merges
    # it all together
    def run(self) -> list[Node]:
        dot_code = []
        rel_filename = None
        for path in self.arguments:
            document = self.state.document
            argument = search_image_for_language(path, self.env)
            rel_filename, filename = self.env.relfn2path(argument)
            self.env.note_dependency(rel_filename)
            try:
                with open(filename, encoding='utf-8') as fp:
                    dot_code += [fp.read()]
            except OSError:
                return [document.reporter.warning(
                    __('External Graphviz file %r not found or reading '
                       'it failed') % filename, line=self.lineno)]
        if self.content:
            dot_code += ['\n'.join(self.content)]

        node = graphviz()
        node['code'] = merge_graphs(dot_code)
        node['options'] = {'docname': self.env.docname}

        if 'graphviz_dot' in self.options:
            node['options']['graphviz_dot'] = self.options['graphviz_dot']
        if 'layout' in self.options:
            node['options']['graphviz_dot'] = self.options['layout']
        if 'alt' in self.options:
            node['alt'] = self.options['alt']
        if 'align' in self.options:
            node['align'] = self.options['align']
        if 'class' in self.options:
            node['classes'] = self.options['class']
        if rel_filename:
            node['filename'] = rel_filename

        if 'caption' not in self.options:
            self.add_name(node)
            return [node]
        else:
            figure = figure_wrapper(self, node, self.options['caption'])
            self.add_name(figure)
            return [figure]


class JGraphviz(Sizeable, JGraphvizMergeable):
    """Monkey-patchy subclass of the standard Sphinx graphviz directive."""

    optional_arguments = 9
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
        epub=(visit_jgraphviz(render_dot_html), None),
        handouts=(visit_jgraphviz(render_dot_html), None),
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
