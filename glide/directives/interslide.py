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

from glide import version


# noinspection PyPep8Naming
class interslide(nodes.General, nodes.Element):
    """Interslide node."""

    pass


class InterslideDirective(Directive):
    """The directive just adds a node"""

    has_content = True

    option_spec = {
        'background': unchanged,
        'transition': unchanged,
        'transition-speed': unchanged,
        'class': unchanged,
    }

    def run(self):
        # content is optional (some interslides may just be an image background)
        text = '\n'.join(self.content)

        node = interslide(text)
        node['background'] = self.options.get('background')
        node['transition'] = self.options.get('transition')
        node['transition_speed'] = self.options.get('transition-speed')
        node['class'] = self.options.get('class')
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


# noinspection PyUnusedLocal
def ignore_visit_interslide(self, node):
    """Interslides only appear in revealjs, so ignore by other builders."""
    raise SkipNode


def revealjs_visit_interslide(revealjs_translator, node):
    """Interslides should make a new slide (but there's no header, etc.)

    If our parent is a normal slide, close it.

    In any case, start a new slide for the interslide.
    """

    if revealjs_translator.section_level > 2:
        revealjs_translator.body.append("</section>")

    revealjs_translator.add_new_slide(node)


# noinspection PyUnusedLocal
def revealjs_depart_interslide(revealjs_translator, node):
    """Close an interslide.

    If this is a top-level interslide (ie, our parent is a section, not a slide)
    we need to close the interslide itself.

    If our parent was a slide, we closed that slide to make the interslide,
    so when the translator "closes" the parent slide, that will actually be
    us --- so we don't want to close this here.
    """

    if revealjs_translator.section_level == 2:
        revealjs_translator.body.append("</section>")


def setup(app):
    app.add_node(
        interslide,
        # Ignore on any builder except revealjs --- if there are newer builders,
        # these should be added here.
        epub=(ignore_visit_interslide, None),
        html=(ignore_visit_interslide, None),
        latex=(ignore_visit_interslide, None),
        revealjs=(revealjs_visit_interslide, revealjs_depart_interslide),
        text=(ignore_visit_interslide, None),
    )
    app.add_directive('interslide', InterslideDirective)
    return {'version': version, 'parallel_read_safe': True}
