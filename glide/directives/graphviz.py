"""Directive for making graphs with Graphviz.

This subclasses Sphinx's standard Graphviz directive, to add one critical feature:
passing options with builder-specific options for dot.

For example::

  .. jdigraph:: cloning
    :handouts: -Grankdir=BT -Gsize=4,4
    :jlatex: -Grankdir=BT -Gsize=3,3
    :revealjs: -Grankdir=BT -Gsize=6,6!

    ... rest of graphviz here

(We need this because we often want to make different sizes for slide versus handouts
versions of graphs)
"""

from docutils.parsers.rst.directives import unchanged
from docutils import nodes
from sphinx.ext.graphviz import graphviz, render_dot_latex, GraphvizError, render_dot
from sphinx.ext.graphviz import Graphviz, GraphvizSimple


class JGraphviz(Graphviz):
    """Directive to insert arbitrary dot markup.

    This is our version of the .. graphviz directive, which is more freeform.
    """

    # We override to allow for our new options, and to pass these to node
    option_spec = {'jlatex': unchanged,
                   'latex': unchanged,
                   'revealjs': unchanged,
                   'handouts': unchanged,
                   'html': unchanged,
                   'epub': unchanged,
                   }

    def run(self):
        # FIXME: incorporate ability to get graphs via file from sphinx graphviz
        node = jgraphviz()
        node['code'] = '\n'.join(self.content)
        node['options'] = self.options
        return [node]


class JGraphvizSimple(GraphvizSimple):
    """Directive to insert arbitrary dot markup.

    This is our version of the .. graph and .. digraph directives, which
    """

    # We override to allow for our new options, and to pass these to node
    option_spec = {'jlatex': unchanged,
                   'latex': unchanged,
                   'revealjs': unchanged,
                   'handouts': unchanged,
                   'html': unchanged,
                   'epub': unchanged,
                   'size': unchanged,
                   }

    def run(self):
        node = jgraphviz()
        node['code'] = '%s %s {\n%s\n}\n' % \
                       (self.name[1:], self.arguments[0], '\n'.join(self.content))

        if 'size' in self.options:
            x, y = [float(p) for p in self.options['size'].split(",")]

            self.options['revealjs'] = "-Gsize=%s,%s" % (x, y)
            self.options['latex'] = "-Gsize=%s,%s" % (x/2.4, y/2.4)
            self.options['handouts'] = "-Gsize=%s,%s" % (x/2, y/2)

        node['options'] = self.options

        return [node]


class jgraphviz(graphviz):
    pass


def render_dot_html(self,
                    node,
                    code,
                    options,
                    prefix='graphviz',
                    imgcls=None,
                    alt=None):

    # Fix for Sphinx 1.4, where it doesn't use options to look for addt'l
    # graphviz_dot_args -- so we shoehorn them onto the builders' config.
    # Kinda yuck, but works fine. - Joel
    self.builder.config.graphviz_dot_args.extend(options)
    options = {}

    try:
        fname, outfn = render_dot(self, code, options, "svg", prefix)
    except GraphvizError as exc:
        self.builder.warn('dot code %r: ' % code + str(exc))
        raise nodes.SkipNode

    wrapper = "div"
    self.body.append(self.starttag(node, wrapper, CLASS='graphviz'))
    self.body.append('<img src="%s" />\n' % fname)
    self.body.append('</%s>\n' % wrapper)

    raise nodes.SkipNode


def html_visit_jgraphviz(self, node):
    """What to do when we encounter one of our directives in an HTML-based builder.

    Our version adds options based upon the current builder, so we can set
    builder-specific options.
    """

    buildoptions = node['options'].get(self.builder.name)
    if buildoptions:
        options = [o.strip() for o in buildoptions.split(' ')]
    else:
        options = []

    render_dot_html(self, node, node['code'], options, alt="")


def latex_visit_jgraphviz(self, node):
    """What to do when we encounter one of our directives in the LaTeX/PDF builder.

    Our version adds options based upon the current builder, so we can set
    builder-specific options.
    """

    buildoptions = node['options'].get(self.builder.name)
    if buildoptions:
        options = [o.strip() for o in buildoptions.split(' ')]
    else:
        options = []

    self.builder.config.graphviz_dot_args.extend(options)
    options = {}

    render_dot_latex(self, node, node['code'], options)


def setup(app):
    app.add_node(jgraphviz,
                 html=(html_visit_jgraphviz, None),
                 latex=(latex_visit_jgraphviz, None))
    app.add_directive('jgraphviz', JGraphviz)
    app.add_directive('jgraph', JGraphvizSimple)
    app.add_directive('jdigraph', JGraphvizSimple)
