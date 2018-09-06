"""Newslide directive for RevealJS.

Creates a break that slides can use to make a new slide, but that latex/html will ignore.

Can use alone, in which case title of new slide is same as previous::

  .. newslide::

Can provide a title for new slide::

  .. newslide:: Full Title

Can provide an additional title, in which case it is appended to
previous slide title::

  .. newslide:: +Part Two

It can take options for:

  transition: revealjs transitions, like "slide", or "concave"
  transition_speed: fast|slow|normal
  background: an image ("lemur.jpg") or CSS Color ("red" or "#f00")
  class: a CSS class that gets added onto the slide section tag
"""

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged


def setup(app):
    app.add_node(newslide)
    app.add_directive('newslide', NewslideDirective)
    app.connect('doctree-resolved', process_newslides)


def process_newslides(app, doctree, fromdocname):
    """Process newslide nodes, ->slides for slides, removing for html/latex"""

    while doctree.traverse(newslide):
        node = doctree.traverse(newslide)[0]

        # for non-slide builders, remove this node
        if app.builder.name != 'revealjs':
            node.parent.remove(node)
            continue

        # Get the "real slide" (ie, the non-virtual slide we're in)
        realslide = node.parent

        # Get text title of the curr sect; we'll use this for our title, too
        localtitle = node.attributes['localtitle'].strip()

        # Find the last slide that wasn't a "newslide"-made one
        checkslide = realslide
        while "localtitle" in checkslide.attributes:
            # Move to slide before this one
            idx = checkslide.parent.index(checkslide)
            checkslide = checkslide.parent.children[idx - 1]

        realtitle = checkslide.children[0].astext().strip()
        if localtitle and localtitle.startswith('+'):
            title = "%s %s" % (realtitle, localtitle[1:])
        elif localtitle:
            title = localtitle
        else:
            title = realtitle

        # Make a new section, with a title in it
        newsect = nodes.section('')
        newsect.attributes = node.attributes
        doctree.set_id(newsect)

        # Add the same title to it
        newsect += nodes.title('', title)

        # Find "..newslide" in the real slide section
        myidx = realslide.index(node)

        # Get the nodes right after me and paste it into new section
        for afterme in realslide[myidx + 1:]:
            newsect.append(afterme.deepcopy())
            realslide.remove(afterme)

        # Move this new section to after my current section
        chapter = realslide.parent
        chapter.insert(chapter.index(realslide) + 1, newsect)

        # Get rid of the newslide node itself
        realslide.remove(node)


class newslide(nodes.General, nodes.Element):
    """newslide node.
    
    This will never survive past the event, so no one should
    have to write a visit_ method in a writer for it.
    """
    pass


class NewslideDirective(Directive):
    """The directive just adds a node"""

    optional_arguments = 1
    final_argument_whitespace = True

    option_spec = {
        'background': unchanged,
        'transition': unchanged,
        'transition-speed': unchanged,
        'class': unchanged,
    }

    def run(self):
        if self.arguments:
            local_title = self.arguments[0]
        else:
            local_title = ""
        node = newslide('', localtitle=local_title)
        node['background'] = self.options.get('background')
        node['transition'] = self.options.get('transition')
        node['transition_speed'] = self.options.get('transition-speed')
        node['class'] = self.options.get('class')
        return [node]
