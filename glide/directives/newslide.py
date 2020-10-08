"""New slide directive for RevealJS.

Hierarchical sections in Sphinx are interpreted in this way in revealjs docs:
- 1: the highest level (the title of the document), becomes title slide
- 2: major section (these become the group-slides-by-topic slides)
- 3: slide (becomes an individual slide)

Sections smaller than 3 are just shown as subsections on a single slide.

Tying handouts (or other non-slide) organization to the exact visual slide
breaks can make too many sections, as the same topic is split over many slides
because of presentation size, but shouldn't really be split in non-slide
documents.

This directive provides a directive that makes a new slide (#3 above) by adding
the "slide" wrapper at that point. These new sections are ignored by all other
builders.

Can use alone, in which case title of new slide is same as previous::

  .. newslide::

  New content goes here; notice it is *not* content of the slide!

Can provide a title for new slide::

  .. newslide:: Full Title

Can provide an additional title, in which case it is appended to previous slide
title because of the "+"; this becomes "Full Title Part Two"::

  .. newslide:: +Part Two

It can take options for:

- transition: revealjs transitions, like "slide", or "concave"
- transition_speed: fast|slow|normal
- background: an image ("lemur.jpg") or CSS Color ("red" or "#f00")
- class: a CSS class that gets added onto the slide section tag
"""
from sphinx import addnodes
from toolz import first
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged

from glide import version


# noinspection PyPep8Naming
class newslide(nodes.General, nodes.Element):
    """newslide node.

    This node won't survive past the process_newslides event, so no one should
    have to write a visit_ method in a writer for it.
    """


class NewslideDirective(Directive):
    """The directive just adds a node"""

    # Can take a title as the optional argument
    optional_arguments = 1
    final_argument_whitespace = True

    option_spec = {
        'background': unchanged,
        'transition': unchanged,
        'transition-speed': unchanged,
        'class': unchanged,
    }

    def run(self):
        local_title = self.arguments[0] if self.arguments else ""
        node = newslide('', local_title=local_title)
        node['background'] = self.options.get('background')
        node['transition'] = self.options.get('transition')
        node['transition_speed'] = self.options.get('transition-speed')
        node['class'] = self.options.get('class')
        return [node]


# noinspection PyUnusedLocal,SpellCheckingInspection
def process_newslides(app, doctree, fromdocname):
    """Process newslide nodes, ->slides for slides, removing for html/latex"""

    # Walkthrough the entire fully-formed doctree, and at each newslide node:
    # - add a new section (figuring out the title from the directive and/or
    #   the title of a previous section
    # - move all content following the newslide directive into this new section
    # - remove all traces of the no-longer-needed newslide directive

    while doctree.traverse(newslide):
        # In docutils<=0.16, the result of doctree.traverse() is a list, but in
        # (as-yet-unreleaed) later versions, it will become an iterator (and, in
        # the meantime, shows an annoying warning). Doing this in a way that
        # doesn't raise a warning in either, but gives us the first item lazily:
        node = first(doctree.traverse(newslide))

        # For non-slide builders, remove this node & continue to next
        if app.builder.name != 'revealjs':
            node.parent.remove(node)
            continue

        # Find the parent slide at the point of the newslide directive
        current_slide = node.parent

        # Find last slide that wasn't a "newslide"-made one, starting here
        prev_real_slide = current_slide
        while "local_title" in prev_real_slide.attributes:
            # Move to slide before this one, albeit in a kludgy fashion, ugh
            idx = prev_real_slide.parent.index(prev_real_slide)
            prev_real_slide = prev_real_slide.parent.children[idx - 1]

        # Determine title for section, from argument on directive:
        # .. newslide::         use title of last real slide
        # .. newslide:: A       use "A"
        # .. newslide:: +A      use "{title of last real slide} A"
        newslide_directive_title = node.attributes['local_title'].strip()
        prev_real_title = prev_real_slide.children[0].astext().strip()
        if newslide_directive_title.startswith('+'):
            title = f"{prev_real_title} {newslide_directive_title[1:]}"
        elif newslide_directive_title:
            title = newslide_directive_title
        else:
            title = prev_real_title

        # Make a new section, and add title node with newslide title
        new_slide = nodes.section()
        new_slide.attributes = node.attributes
        doctree.set_id(new_slide)
        new_slide += nodes.title(text=title)

        # Find newslide directive in the real slide section
        new_slide_index = current_slide.index(node)

        # Get the nodes following the newslide node and move into new section
        for node_after_directive in current_slide[new_slide_index + 1:]:
            new_slide.append(node_after_directive.deepcopy())
            current_slide.remove(node_after_directive)

        # Move this new section to after our current section (grandparent)
        chapter = current_slide.parent
        chapter.insert(chapter.index(current_slide) + 1, new_slide)

        # Get rid of the newslide node itself, leaving just the new section.
        # This is all done pre-builder, so the builder has no idea that this
        # section was made artificially, and there are no strange nodes left.
        current_slide.remove(node)


# noinspection PyUnusedLocal,SpellCheckingInspection
def add_intro_slides(app, doctree, fromdocname):
    """Process sections, adding initial slides where needed.

    Often, the first slide for a group has the same name as the group, like::

        Redux
        =====

        Redux
        -----

        Blah blah.

    This is ok, but mildly annoying for handouts, since its TOC gets cluttered
    with needless "intro" sections.

    As of Glide 2.0, we don't need the second heading there---this processor
    will find raw content inside of a group section and wrap it in a new
    section.
    """

    # We only need to add these sections for slides, so bail out if not slides.
    if app.builder.name != 'revealjs':
        return

    # Find each "group level" section and walk through its children: as soon
    # as we find an actual section stop. If we encounter content-generating
    # stuff before that, create a section for it.

    for top_sect in doctree.children:
        if not isinstance(top_sect, nodes.section):
            continue

        for group_sect in top_sect.children:
            if not isinstance(group_sect, nodes.section):
                continue

            found_title = ""
            # This will become true when content is found before section
            found_content = False

            for node in list(group_sect.children):
                if isinstance(node, nodes.section):
                    # May or may not have already found content-before-section,
                    # but in either case, we stop looking now.
                    break

                if isinstance(node, nodes.title):
                    found_title = node.astext()
                    continue

                if isinstance(
                        node,
                        (nodes.target, nodes.topic, addnodes.index)):
                    # Ignore things that don't produce content --- it is
                    # possible that this list is incomplete, so you can add
                    # things to it
                    continue

                if not found_content:
                    # Found content before first section, so add a section
                    # for this content, using the title we found on the group
                    new_intro_section = nodes.section()
                    doctree.set_id(new_intro_section)
                    assert found_title != "", \
                        "Shouldn't happen: found content before title"
                    new_intro_section.append(nodes.title(text=found_title))
                    group_sect.insert(1, new_intro_section)
                    found_content = True

                # For all content found, remove from directly in group, and add
                # to the new section being created,
                group_sect.remove(node)
                # noinspection PyUnboundLocalVariable
                new_intro_section.append(node)


def setup(app):
    app.add_node(newslide)
    app.add_directive('newslide', NewslideDirective)
    # Ensure before process_newslides --- there needs to be a slide to newslide!
    app.connect('doctree-resolved', add_intro_slides)
    app.connect('doctree-resolved', process_newslides)
    return {'version': version, 'parallel_read_safe': True}
