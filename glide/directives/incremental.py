"""Incremental items for RevealJS.

RevealJS has "fragments", which allows items to change appearance (roll-in, out,
change color, etc.) as the user forward/back navigates.


Nested
------

For each "part" to be a separate fragment, deeply nesting:

  .. container:: nest-incremental

    - 1
    - 2
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

This works on `<ul>`, `<ol>`, `|-blocks`, `:fields:`, `<dl>`, option lists,
and table rows.

Non-Nested
----------

For a list with a pause before each top-list-level::

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

This works on `<ul>`, `<ol>`, `|-blocks`, `:fields:`, `<dl>`, option lists,
and table rows.

All at Once
-----------

To have only a single pause, before everything is shown at once::

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

This works on anything.

Additional Classes
------------------

Note that for *all* of these (nest-, item-, one-), you can add additional
RevealJS fragment styles, like `fade-out` or `highlight-blue`::

  .. container:: one-incremental fade-out highlight-blue

    - 1
    - 1
      - 1
      - 1

Incremental Single List Items
-----------------------------

To be more flexible and note exactly which list items are fragmented::

  - 1
  - 1
  - :incremental-li:`2`

This creates::

  <ul>
    <li>1</li>
    <li>1</li>
    <li class='fragment'>2</li>
  </ul>

This can use a fragment style of RevealJS by adding it, like::

  - 1
  - 1
  - :incremental-li-roll-on:`2`

This creates::

  <ul>
    <li>1</li>
    <li>1</li>
    <li class='fragment roll-on'>2</li>
  </ul>

This only works for <li> and <dd> (not <dl>!).

Incremental Inline Text
-----------------------

You can also use :incremental:`Hello` to have any text appear as fragments.

You can add a fragment style class, too: :incremental-highlight-red:`Hello`.
"""

from docutils import nodes
from docutils.parsers.rst import roles
from sphinx.errors import ExtensionError

from glide import version

###############################################################################
# Incremental classes

# These are all item-increment-able thing where the parts are immediate
# children of the sequential item

DEEP_1 = (
    nodes.list_item,
    nodes.option_list_item,
    nodes.line,
    nodes.field,
)

# ... where the parts are grandchildren
DEEP_2 = (
    nodes.term,
    nodes.definition,
)

# ... where the parts are great-grandchildren
DEEP_3 = (
    nodes.row,
)

# for nesting, the depth doesn't matter: all are made incrementing
# noinspection PyTypeChecker
DEEP_ALL = DEEP_1 + DEEP_2 + DEEP_3


# noinspection PyUnusedLocal
def process_incremental(app, doctree, fromdocname):
    """Process incremental classes."""

    # Loop through doctree and for every item w/an incremental class:
    # - remove those classes [they're not useful after this]
    # - if building slides, add appropriate "fragment" class

    building_slides = (app.builder.name == 'revealjs')

    for node in doctree.traverse(nodes.Element):

        # nest-incremental: Make all items appear one-at-a-time
        if 'nest-incremental' in node['classes']:
            node['classes'].remove('nest-incremental')
            if not building_slides:
                continue

            for item in node.traverse(
                    lambda n:
                    isinstance(n, DEEP_ALL)):
                item['classes'].extend(['fragment'] + node['classes'])

        # item-incremental: Make top-level items appear one-at-a-time
        elif 'item-incremental' in node['classes']:
            node['classes'].remove('item-incremental')
            if not building_slides:
                continue

            lst = None
            # Figure out where list is: are we the list? or its parent?
            # (normally, we'll be the parent, but if the class was put
            # directly on the list rather than a container (as it would be
            # if we used .. rst-class), we could be the list:
            if isinstance(node, nodes.compound):
                for lst in node.traverse():
                    if isinstance(lst, nodes.Sequential):
                        break
            else:
                lst = (node if isinstance(node, nodes.Sequential)
                       else node.children[0])

            if not lst or not isinstance(lst, nodes.Sequential):
                raise ExtensionError(
                    message=f"{lst} is not a list",
                    modname="glide.directives.incremental")

            # Add to children 1 deep
            for item in lst.traverse(
                    lambda n:
                    isinstance(n, DEEP_1) and n.parent is lst):
                item['classes'].extend(['fragment'] + node['classes'])

            # Add to children 2 deep
            for item in lst.traverse(
                    lambda n:
                    isinstance(n, DEEP_2) and n.parent.parent is lst):
                item['classes'].extend(['fragment'] + node['classes'])

            # Add to children 3 deep
            for item in lst.traverse(
                    lambda n:
                    isinstance(n, DEEP_3) and n.parent.parent.parent is lst):
                item['classes'].extend(['fragment'] + node['classes'])

        # one-incremental: make the whole item appear at once
        elif 'one-incremental' in node['classes']:
            node['classes'].remove('one-incremental')

            if not building_slides:
                continue

            if "literal-block-wrapper" in node.parent["classes"]:
                node = node.parent

            node['classes'].extend(['fragment'] + node['classes'])


###############################################################################
# Interpreted text roles

# noinspection PyUnusedLocal,PyDefaultArgument
def incremental_li(name,
                   rawtext,
                   text,
                   lineno,
                   inliner,
                   options={},
                   content=[]):
    """Add an incremental class to an `<li>` or `<dd>`::

        - :incremental-li:`Appears`

    Can have a fragment style added to name like::

        - :incremental-li-highlight-red:`Turns Red`
    """

    if inliner.document.settings.env.app.builder.name == 'revealjs':
        # ["fragment"] or with a fragment style, like ["fragment", "fade-out"]
        classes = ['fragment'] + name.split("-", 2)[2:]

        node = inliner.parent
        node['classes'].extend(classes)

    return [nodes.inline(text=text)], []


# noinspection PyUnusedLocal,PyDefaultArgument
def incremental_text(name,
                     rawtext,
                     text,
                     lineno,
                     inliner,
                     options={},
                     content=[]):
    """Add incremental class around inlined text.

        :incremental:`Appears`

    Can have a fragment style added to name like::

        :incremental-highlight-red:`Turns Red`
    """

    if inliner.document.settings.env.app.builder.name == 'revealjs':
        # ["fragment"] or with a fragment style, like ["fragment", "fade-out"]
        classes = ['fragment'] + name.split("-", 1)[1:]
    else:
        classes = []

    return [nodes.inline(text=text, classes=classes)], []


###############################################################################
# Register extension

FRAGMENT_STYLES_INLINE = [
    "current-visible",
    "fade-out",
    "semi-fade-out",
    "fade-in-then-out",  # doesn't currently work
    "fade-in-then-semi-out",  # doesn't currently work
    "strike",
    "highlight-red",
    "highlight-green",
    "highlight-blue",
    "highlight-current-red",
    "highlight-current-green",
    "highlight-current-blue",
]

FRAGMENT_STYLES_BLOCK = FRAGMENT_STYLES_INLINE + [
    "fade-up",
    "fade-down",
    "fade-left",
    "fade-right",
    "grow",
    "shrink",
    "zoom-in",
]


def setup(app):
    roles.register_local_role("incremental", incremental_text)
    for fs in FRAGMENT_STYLES_INLINE:
        roles.register_local_role("incremental-%s" % fs, incremental_text)

    roles.register_local_role("incremental-li", incremental_li)
    for fs in FRAGMENT_STYLES_BLOCK:
        roles.register_local_role("incremental-li-%s" % fs, incremental_li)

    app.connect('doctree-resolved', process_incremental)
    return {'version': version, 'parallel_read_safe': True}
