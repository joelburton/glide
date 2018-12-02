"""Interslide directive for RevealJS.

Creates a new slide that has no heading. This is useful for silly
"omg-wtf-cat.jpg" graphics and such.

These do not appear on other builders than revealjs.

Example:

  A Slide
  -------

  Hi

  .. interslide::

    .. image:: cat.jpg

  Another Slide
  -------------

  There

You can also add an options for the background color and transition::

  .. interslide::
    :background: red
    :transition: fade

    Yay!

"""

from docutils import nodes
from docutils.nodes import SkipNode
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged


def ignore_visit_interslide(self, node):
    raise SkipNode


def setup(app):
    app.add_node(interslide,
                 latex=(ignore_visit_interslide, None))
    app.add_directive('interslide', interslideDirective)


class interslide(nodes.General, nodes.Element):
    """interslide node."""

    pass


class interslideDirective(Directive):
    """The directive just adds a node"""

    has_content = True

    option_spec = {
        'background': unchanged,
        'transition': unchanged,
        'transition-speed': unchanged,
        'class': unchanged,
    }

    def run(self):
        # self.assert_has_content()
        text = '\n'.join(self.content)

        node = interslide(text)
        node['background'] = self.options.get('background')
        node['transition'] = self.options.get('transition')
        node['transition_speed'] = self.options.get('transition-speed')
        node['class'] = self.options.get('class')
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]
