"""Incremental items for RevealJS.

RevealJS has "fragments", which allows items to change appearance (roll-in, out, change color,
etc.) as the user forward/back navigates.


Nested
------

Sometimes we want a bullet list to have each list item to appear individually::

  .. container:: nest-incremental

  - 1
  - 2
  .. don't forget this blank line
    - 3
    - 4

This creates::

  <ul>
    <li class='fragment'>1</li>
    <li class='fragment'>2
      <ul>
        <li class='fragment'>3</li>
        <li class='fragment'>4</li>
      </ul>
    </li>
  </ul>

Non-Nested
----------

Sometimes we want a bullet list to have each top-level list item to appear individually::

  .. container:: item-incremental

  - 1
  - 2
    - 2
    - 2

This creates::

  <ul>
    <li class='fragment'>1</li>
    <li class='fragment'>2
      <ul>
        <li>2</li>
        <li>2</li>
      </ul>
    </li>
  </ul>

All at Once
-----------

Sometimes we want an item to appear all at once::

  .. container:: one-incremental

  - 1
  - 1
    - 1
    - 1

This creates::

  <ul class='fragment'>
    <li>1</li>
    <li>1
      <ul>
        <li>1</li>
        <li>1</li>
      </ul>
    </li>
  </ul>

Note that `one-incremental` can be used an *any* type of thing; the others
can only be used on lists.


Additional Classes
------------------

Note that for *all* of these (nest-, item-, one-), you can add additional RevealJS classes,
like `roll-in` or `highlight-blue`::

  .. container:: one-incremental roll-in

  - 1
  - 1
    - 1
    - 1


Interpreted Text Roles
----------------------

Sometimes we want to be more flexible and note exactly which list items are fragmented::

  - 1
  - 1
  - :incremental-li:`2`

This creates::

  <ul>
    <li>1</li>
    <li>1</li>
    <li class='fragment'>2</li>
  </ul>

We can use the extra fragment classes of RevealJS by adding them to the 'incremental' role,
like so::

  - 1
  - 1
  - :incremental-roll-on:`2`

This creates::

  <ul>
    <li>1</li>
    <li>1</li>
    <li class='fragment roll-on'>2</li>
  </ul>


You can also use :incremental`Hello` to have single words appear as fragments.

You can extra classes of RevealJS like this too, :incremental-highlight-current-red:`Ah`.

"""

from docutils import nodes
from docutils.parsers.rst import roles


def setup(app):
    app.connect('doctree-resolved', process_incremental)


def process_incremental(app, doctree, fromdocname):
    """Process incremental roles."""

    # Only add the classes for slides; for other things, we remove all
    # mention of this stuff
    slides = (app.builder.name == 'revealjs')

    for node in doctree.traverse(nodes.Element):

        # nest-incremental: Make all items appear one-at-a-time

        if 'nest-incremental' in node['classes']:
            node['classes'].remove('nest-incremental')
            # Put 'fragment' on all descendant li's
            if slides:
                for li in node.traverse(nodes.list_item):
                    li['classes'].extend(['fragment'] + node['classes'])

        # item-incremental: Make top-level bullet items appear one-at-a-time

        if 'item-incremental' in node['classes']:
            node['classes'].remove('item-incremental')

            # Put 'fragment' on direct child li's of our direct child ul:
            if slides:
                # import pdb; pdb.set_trace()

                lst = node if isinstance(node, nodes.Sequential) else node.children[0]

                if isinstance(lst, nodes.definition_list):
                    # For definition lists, we put a fragment on the DL itself,
                    # and then in the writer, on the individual dt/dd pairs, we'll
                    # put out the HTML class + data attributes we need.
                    lst['classes'].append('dl-fragment')

                else:
                    # Must be a <ul>
                    for ul in lst.traverse(nodes.Sequential,
                                           descend=0,
                                           siblings=1):
                        for li in ul.children[0].traverse(nodes.list_item,
                                                          descend=0,
                                                          siblings=1):
                            li['classes'].extend(['fragment'] + node['classes'])

        # one-incremental: make the whole item appear at once

        if 'one-incremental' in node['classes']:
            node['classes'].remove('one-incremental')

            # Put 'fragment' on the wrapper around the list
            if slides:
                node['classes'].extend(['fragment'] + node['classes'])


###############################################################################
# Interpreted text roles


def incremental_parent(parent_node_type,
                       name,
                       rawtext,
                       text,
                       lineno,
                       inliner,
                       options={},
                       content=[]):
    """Add an incremental class onto the given parent node.

    Used to add incremental class onto li, paragraph, etc.
    """

    builder = inliner.document.settings.env.app.builder.name
    if builder == 'revealjs':
        classes = ['fragment'] + name.split("-", 2)[2:]

        # keep going up until we have the requested parent_node_type
        anode = inliner.parent
        while anode.__class__ != parent_node_type:
            anode = anode.parent

        anode['classes'].extend(classes)

    return [nodes.inline(text=text)], []


def incremental_li(*args, **kwargs):
    """Make list item incremental.

    Example:

        - Appears normally
        - :incremental-li:`Appears as fragment`
        - :incremental-li-highlight-current-red:`Can use other classes`
    """

    return incremental_parent(nodes.list_item, *args, **kwargs)


def inline_incremental(name,
                       rawtext,
                       text,
                       lineno,
                       inliner,
                       options={},
                       content=[]):
    """Add incremental class around inlined item.

    For when you want :incremental:`text to appear` as fragments.

    You can add other classes :incremental-roll-in:`also`.
    """

    if inliner.document.settings.env.app.builder.name == 'revealjs':
        classes = ['fragment'] + name.split("-", 1)[1:]
    else:
        classes = []

    return [nodes.inline(text=text, classes=classes)], []


######################################
# Register Interpreted text roles

FRAGMENT_STYLES = [
    "grow",  # doesn't work on inlines; is always there
    "shrink",  # doesn't work on inlines; is always there
    "roll-in",  # doesn't work on inlines; is always there
    "fade-out",
    "current-visible",
    "highlight-current-blue",
    "highlight-current-red",
    "highlight-current-green",
    "highlight-red",
    "highlight-green",
    "highlight-blue",
]

roles.register_local_role("incremental", inline_incremental)
for fs in FRAGMENT_STYLES:
    roles.register_local_role("incremental-%s" % fs, inline_incremental)

roles.register_local_role("incremental-li", incremental_li)
for fs in FRAGMENT_STYLES:
    roles.register_local_role("incremental-li-%s" % fs, incremental_li)
