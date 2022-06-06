============
Demo Lecture
============

.. todo

   .. general ideas for improving our build system

     FIXME: do we need compound support, so that things in a compound are closed together?
        we don't use this now, but is it useful?

     FIXME: can we set latex title, etc in body, so we don't have to change conf for, say,
       the employee handbook?

     FIXME: add docs for fail

   |:cat:|

Shell
=====

Hey this is an :err:`error message`.

.. code-block:: simple-console
   :class: console

   $ ls
   a b c
   $ ls
   a b c
   /Path/to/here $ ls
   (venv) here $ ls
   a b c
   $ ls
   > also
   (venv) here % ls
   # this is a comment
   $ ls
   a b c  # this is a comment
   a b c#not a comment
   a b c  #! this is an error
   % ls
   a b c
   $ ls   # <-- notice!
   $ ls#not-comment x
   #! this gets their attention

Admonitions
===========

Rainbow Lines
-------------

.. code-block:: rainbow-lines

   one
   two
   three
   four
   five
   six
   seven
   eight

.. code-block:: rainbow-2-lines

   one
   one
   two
   two
   three
   three
   four
   four
   five
   five
   six
   six
   seven
   seven
   eight
   eight

Shell
-----


.. code-block:: js

   /** For x */

   /** For
     x */

   function foo() { }

   // foo foo

.. code-block:: rst
   :caption: a likely rst

   For our own work, `x` becomes

   .. code-block:: python

      if x == 17


.. code-block:: psql
   :caption: ``psql movies``

   psql (12.4)
   Type "help" for help.

   joel=# \d
   Did not find any relations.
   joel=#

.. code-block:: postgres

   CREATE TABLE countries (
     code VARCHAR(2) PRIMARY KEY,
     country TEXT NOT NULL UNIQUE);

   -- SQL Comment
   CREATE TABLE flights (
     id SERIAL PRIMARY KEY,
     airline_code VARCHAR(3) NOT NULL REFERENCES airlines,
     depart_at TIMESTAMPTZ NOT NULL,
     arrive_at TIMESTAMPTZ NOT NULL,
     depart_city_id INT NOT NULL REFERENCES cities,
     arrive_city_id INT NOT NULL REFERENCES cities);

.. code-block:: html+jinja

   {% extends 'base.html' %}
   <!-- hello -->   {# comment #}
   {% block title %} FlaskCafe {% endblock %}

   {% block content %}

   <div class="homepage">
     <h1 class="display-1">Flask Cafe</h1>
     <h3 class="display-5">Where Coffee Dreams Come True.</h3>
     <a class="mt-5 btn btn-primary" href="/cafes">View Our Cafes</a>
   </div>

   <style>
       body {
         background: url(/static/images/homepage.jpg) no-repeat center center fixed;
         background-size: cover;
       }

       .display-1, .display-5 {
         color: white;
         text-shadow: black 3px 3px !important;
         letter-spacing: 0.05em
       }
   </style>

   {% endblock %}

.. code-block:: commentable-http

  HTTP/1.1 200 OK                          # Yay
  Date: Mon, 20 Apr 2018 07:09:16 GMT      # Yay
  Server: Apache
  Content-Type: text/html

  <!doctype html>
  <html>...</html>

.. code-block:: commentable-http

  HTTP/1.1 200 OK
  Date: Mon, 20 Apr 2018 07:09:16 GMT      # Yay
  Server: Apache
  Content-Type: text/html

  <!doctype html>
  <html>...</html>

.. code-block:: commentable-http

  GET / HTTP/1.1
  Date: Mon, 20 Apr 2018 07:09:16 GMT      # Yay
  Server: Apache
  Content-Type: text/html

  let x == 7;


.. code-block:: commentable-http

  GET / HTTP/1.1                           # Yay
  Date: Mon, 20 Apr 2018 07:09:16 GMT      # Yay
  Server: Apache
  Content-Type: text/html

  let x == 7;


.. code-block:: simple-console
   :force:

   # comment?
   $ echo "foo"   # comment

   (venv) $ echo "foo"

   $ ls
   hi
   there
   joel

.. sidebar:: Understanding This
   :class: sidebar40

   While the computer executes this from the
   bottom, it's helpful to think about the smallest
   case first: **the sum of an empty list of numbers is zero.**
   That's our *base case*.

.. code-block:: rainbow-2-lines
   :class: line-height-1 code-140  code-35c

           n: []  base    ⭣0
           ──────────────────
         n: [1]     3 + ⭡[] ⭣3
         ──────────────────────
       n: [2,3]      2 + ⭡[3] ⭣5
       ──────────────────────────
     n: [1,2,3]     1 + ⭡[2,3] ⭣6
     ──────────────────────────────
   add([1,2,3])              ⭡[1,2,3]
   ──────────────────────────────────

.. parsed-literal::
   :class: line-height-1 code-140  code-30c

   │ diagram here
   │ with lines
   │ like this
   │
   │ │ :blue:`recursion`
   │ │
   │ │ |larr| `x`

CSV Tables
----------

.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 10, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

Another Section
+++++++++++++++

Ok?

Hide Me
~~~~~~~

Nope

Function
--------

.. py:function:: spam(eggs)
                 ham(eggs)

.. py:function:: filterwarnings(action, message='', category=Warning, \
                                module='', lineno=0, append=False)

   Spam or ham the foo.

Container Hover?
----------------

For example if we have code like this:

.. code-block:: python

   x = 12

.. code-block:: python

   x = 12


.. code-block:: python
   :class: hover-reveal-code

   x == 17

.. container:: hover-reveal

   Secret?

Topic
-----

Before

.. topic:: Ends with Para

   This is foo

.. topic:: Foo Bar Baz

   This is foo

   .. container::

      And bar

.. topic:: Foo Bar Baz
   :class: hover-reveal

   This is foo

After

Containers
----------

Before

.. container::

   Hey

   There

After

.. container::

   - one

   - two

After

| Then
| This

After

.. code-block:: python

   x == 2

After

Text
----

Hello *italic* **bold**. Also, `this is a variable`, :title:`Book Title`, and ``x = 10``

Use :kbd:`Control-R` to refresh.

First
-----

.. parsed-literal::

   foo bar x

.. parsed-literal::

    `red`:red: `green`:green: `orange`:orange: `tan`:tan: `blue`:blue: `gray`:gray: `gone`:gone: `inv-red`:inv-red:

And in a console:

.. parsed-literal::
    :class: console

    This is a `shell`:tan: `minor`:gray:

    `cmd`:cmd: `red`:red: `green`:green: `orange`:orange: `tan`:tan: `blue`:blue: `gray`:gray: `gone`:gone: `inv-red`:inv-red:

Console w/nothing:

.. parsed-literal::
   :class: console

   Hey


Long Code
---------

Let's see some code:

.. code-block:: python
   :caption: oh
   :class: foo

   class A:
      pass


And more:

.. code-block:: python

    class Cat5(object):
        """Cat with class methods."""

        _SELECT = "SELECT name, hunger FROM Cats WHERE name = :name"
        _UPDATE = "UPDATE Cats SET hunger = :hunger WHERE name = :name and so on"234

        def __init__(self, name, hunger):     # special method
            self.name = name                  # object attribute
            self.hunger = hunger

        def feed(self, calories):
            """Feed cat, update hunger, and update database."""

            self.hunger = self.hunger - calories
            db.session.execute(
                self._UPDATE, {f'{hunger}': self.hunger,'name': self.name})
            db.session.commit()

        def feed(self, calories):
            """Feed cat, update hunger, and update database."""

            self.hunger = self.hunger - calories
            db.session.execute(
                self._UPDATE, {'hunger': self.hunger,'name': self.name})
            db.session.execute(
                self._UPDATE, {'hunger': self.hunger,'name': self.name})
            db.session.commit()


Runtime
-------

`link here <http://foo.com>`_

"Hello"

.. sectionauthor:: Joel
.. codeauthor:: Joel

:func:`format`


.. code-block:: python

   if x == 2:

.. code-block:: python
   :force:

   if x == 2:


.. versionadded:: woot

   Why?

.. versionchanged:: 3.4
   Why?

.. deprecated:: 5.6
   Why?


.. danger:: foo

   Bear!

.. danger:: foo
   Bear3!

.. seealso:: One More!

   Why?


:command:`ls`

:file:`/foo/bar/{x}/baz`

:abbr:`LIFO (la la)`

:program:`vim`

:samp:`foo{x}bar`

|today|

how is rst-class diff than class?

----

gwllo

runs in |On^2| or |Onlogn| or |On| or |O!| but not |O2^n| or |O1| or |Ologn|

.. |log2| replace:: log\ :sub:`2`
.. |Ologn| replace:: O(log\ :sub:`2`\ *n*)
.. |On^2| replace:: O(*n*\ :sup:`2`)
.. |Onlogn| replace:: O(*n* log\ :sub:`2`\ *n*)
.. |On| replace:: O(*n*)
.. |O!| replace:: O(*n!*)
.. |O2^n| replace:: O(2\ :sup:`n`)
.. |O1| replace:: O(1)
.. |italn| replace:: *n*

Line Breaks
-----------

.. role:: js(code)
   :language: js

:js:`x == "hello"` and ``x == "hello"``

Hello, how is this looking -- is it |handouts-br|
okay?

Just checking!

| Hello, how is this looking -- is it
| okay?
|
| Just checking!

omg prefer to reveal-br -- wait, that affects all builders

Test usage like this:

|

Ok?

.. highlights::

    - This

    - This

.. pull-quote::

    And I knew

.. epigraph::

    And also

    -- Eliot

.. compound::

    Hello, this a
    normal thing.

        not me
        i'm different

    Back to the normal
    thing


Admin
-----

attention
caution
danger
error
hint
important
note
tip
warning



.. attention:: Attention Title

    Body

.. admonition:: Fluffy!
   :class: caution

   Body This One Is Merged?

.. caution:: Caution Title

    Body

.. danger:: Danger Title

    Body

.. error:: Error Title

    Body

.. hint:: Hint Title

    Body

.. important:: Important Title

    Body

.. note:: Notex Title

    Body

.. tip:: Tip Title

    Body

.. warning:: Warning Title

    Body

.. sidebar:: This is an sidebar

    Aside body

.. topic:: Topic

    Topic

Doctest
=======

JSX
---

`JoelBurton.com <http://joelburton.com/>`__

.. code-block:: jsx

  return <p>Hello</p>

Math
----

Adding math:

.. math::

    r = \frac{\sum^n_{i=1}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\Sigma^n_{i=1}(x_i - \bar{x})^2 \times \Sigma^n_{i=1}(y_i - \bar{y})^2}}

Or `n = {x}^2`:math: for inline.

Doctest
-------

https://graphs.grevian.org/
https://renenyffenegger.ch/notes/tools/Graphviz/examples/index
http://magjac.com/graphviz-visual-editor/
https://github.com/fcurella/jsx-lexer
imgmath_image_format = 'svg'
imgmath_font_size  12


.. doctest:: python

    >>> 1 + 1
    2

Graphviz
========

Graphviz
--------

.. graphviz:: animals.dot
    :align: right
    :caption: wut wut
    :size: 12,12

.. digraph:: animals-two
    :caption: wut wut
    :size: 8,8

    a -> b

.. graph:: animals
    :caption: wut wut
    :size: 8,8

    a -- b




Section Heading
===============

Works on Definition Lists
-------------------------

Hello
    :incremental-li:`There`

Hello2
    :incremental-li:`2`


.. container::

    - One

    - :incremental-li:`Two`

      - Three

Incremental Text
----------------

|  :incremental-current-visible:`current-visible`
|  :incremental-fade-out:`fade-out`
|  :incremental-semi-fade-out:`semi-fade-out`
|  :incremental-strike:`strike`
|  :incremental-highlight-red:`highlight-red`
|  :incremental-highlight-green:`highlight-green`
|  :incremental-highlight-blue:`highlight-blue`
|  :incremental-highlight-current-red:`highlight-current-red`
|  :incremental-highlight-current-green:`highlight-current-green`
|  :incremental-highlight-current-blue:`highlight-current-blue`
|  :incremental-fade-in-then-out:`fade-in-then-out` (not working)
|  :incremental-fade-in-then-semi-out:`fade-in-then-semi-out` (not working)

Incremental Parts
-----------------

TODO here

Not just for list items --- anything "incremental-able"

.. container:: compare

    .. container::

        - :incremental-current-visible:`current-visible`
        - :incremental-fade-out:`fade-out`
        - :incremental-semi-fade-out:`semi-fade-out`
        - :incremental-strike:`strike`
        - :incremental-highlight-red:`highlight-red`
        - :incremental-highlight-green:`highlight-green`
        - :incremental-highlight-blue:`highlight-blue`
        - :incremental-highlight-current-red:`highlight-current-red`
        - :incremental-highlight-current-green:`highlight-current-green`
        - :incremental-highlight-current-blue:`highlight-current-blue`

    .. container::

        - :incremental-li-fade-up:`fade-up`
        - :incremental-li-fade-down:`fade-down`
        - :incremental-li-fade-left:`fade-left`
        - :incremental-li-fade-right:`fade-right`
        - :incremental-li-grow:`grow`
        - :incremental-li-shrink:`shrink`
        - :incremental-li-zoom-in:`zoom-in`
        - :incremental-fade-in-then-out:`fade-in-then-out` (not working)
        - :incremental-fade-in-then-semi-out:`fade-in-then-semi-out` (not working)

Not just for list items --- anything "incremental-able"

.. container:: compare

    .. container::

      .. code-block:: python

         x = 1

    .. container::

      .. container::

        - :incremental-li-fade-up:`fade-up`
        - :incremental-li-fade-down:`fade-down`
        - :incremental-li-fade-left:`fade-left`

      .. container::

        - :incremental-li-fade-right:`fade-right`
        - :incremental-li-grow:`grow`
        - :incremental-li-shrink:`shrink`
        - :incremental-li-zoom-in:`zoom-in`
        - :incremental-fade-in-then-out:`fade-in-then-out` (not working)
        - :incremental-fade-in-then-semi-out:`fade-in-then-semi-out` (not working)

Quotation
---------

.. epigraph::

   In the beginning, there was Unix.

   -- Joel Burton

Does This Look Ok?
------------------

- a

- b

.. newslide::

- c

- d

Block Fades
-----------

.. container:: one-incremental fade-up

    fade-up

.. container:: one-incremental fade-down

    fade-down

.. container:: one-incremental fade-left

    fade-left

.. container:: one-incremental fade-right

    fade-right

.. container:: one-incremental fade-out

    fade-out

.. container:: one-incremental semi-fade-out

    semi-fade-out

.. container:: one-incremental fade-in-then-out

    fade-in-then-out

.. container:: one-incremental fade-in-then-semi-semi-out

    fade-in-then-semi-out

Block Grow
----------

.. container:: one-incremental grow

    grow

.. container:: one-incremental shrink

    shrink

.. container:: one-incremental zoom-in

    zoom-in

Typography & Color
------------------

.. container:: one-incremental strike

    strike

.. container:: one-incremental strike highlight-red

    strike highlight-red (combining)

.. container:: one-incremental highlight-red

    highlight-red

.. container:: one-incremental highlight-current-red

    highlight-current-red

.. container:: one-incremental highlight-green

    highlight-green

.. container:: one-incremental highlight-current-green

    current-highlight-green

.. container:: one-incremental highlight-blue

    highlight-blue

.. container:: one-incremental highlight-current-blue

    highlight-current-blue



Option List
-----------

.. container:: item-incremental

    -x    X
    -a    Y

.. container:: item-incremental

    | Hey
    | Jude

.. container:: item-incremental

    ====== =======
    Hey    Jude
    ====== =======
    One    Thing
    And    Another
    ====== =======


Field List
----------

.. container:: item-incremental

    :hey: you
    :there: me

Works on Definition Lists
-------------------------

.. container:: item-incremental

    Item Incremental
        Works on definition lists, too

        Inner
            Is this valid?

        Or
            Is this?

    Just
        Put it on a container around the list

.. container:: item-incremental

    - One

      - Two

    - Three

Slide Title
-----------

- This is a fake lecture

- But it should show lots of feature of our Sphinx system

- It is also a test case for our builders/CSS stylesheets

- As you add features/CSS classes/etc, please add them here

Another Slide Title
-------------------

- It's Pretty Rare

- But You Can Have a Subsection!

Subsection
++++++++++

Like This


Basic Styling
=============

Typography
----------

Put blank lines between paragraphs.


Basic Styling
-------------

- For emphasis, use *italics*

- For more emphasis, use **bold**

- For link, use `Go to Google <http://google.com>`_

Citations
---------

Citations use single backticks: \`like this\`. Use for:

- variable names

  - eg: We can now set `x`

- file or path names

  - eg: Store this in `secrets.sh`

- class names

  - eg: Remember our `Cat` class?

- function or method names

  - eg: Never call `lets_play_global_thermonuclear_war`

**Do not use this for general emphasis, please!** Use bold or italics for that.

Code Literals
-------------

Code literals use double backticks: \`\`like this\`\`

These are for literal code blocks or literal coding values:

- things like ``x = 0``

- but not for just talking *about* a variable, function, etc.

  - use `citations` for that

- eg: call `set_color` like this: ``set_color('blue')``

Dashes
------

Use 3 dashes for an em dash---like this.

Two dashes makes an "en dash"--it's too short!

Superscripts and Subscripts
---------------------------

O(n\ `2`:sup:\ )

log\ `2`:sub:\ n

.. only:: not revealjs

  Notice how we use a backslashed space there---it's not legal
  to have styles right next to a word (like O(n`2`:sup:), which
  doesn't look right). The backslash space separates the tokens,
  but does't add a real space.

Line Breaks
-----------

As an example:

| You can force line breaks
| by doing this

Or, you can add a slide-only break |reveal-br|
like this.

Symbols
-------

- |nbsp|    NONBREAKING SPACE

- |rarr|    RIGHTWARDS ARROW

- |larr|    LEFTWARDS ARROW

- |lrarr|  ↔  BOTH ARROW   ↩ ⇔  ⇄

- |plus|    PLUS SIGN

- |times|   MULTIPLICATION SIGN

- |check|   CHECK MARK

- |approx|  ALMOST EQUAL TO

- |sub2|    SUBSCRIPT 2

- |super2|  SUPERSCRIPT 2

Lists
=====

Lists
-----

- Always put blank line between bulleted list items

- Otherwise bad things will happen!

  - You can have many levels

  - Just indent them

    - Useful for further explanations

  - Try to stick to 2

    - Our CSS only stylizes up to level 4

    - So stop here

      - Or here

- And back to level one

Complex Lists
-------------

Here is a list:

- You can also have lists that are not "simple"

  This is where you have multiple paragraphs in a list

  - You can still nest these

    Like so

.. newslide::

More about complex lists:

- This happens with things like code blocks::

    x = 0

- See?

.. newslide::

More about complex lists:

- Another case is

- Where you have a simple list

  - Containing a complex list

    This has a second paragraph

- The spacing should work out

Numbered Lists
--------------

Simple:

1. One

2. Two

   - Inner point

Not Simple:

1. Paragraph about one.

   And another.

2. Two

   - Inner point.

Horizontal Lists
----------------

You can make short, side-by-side lists like this:

.. hlist::

  - one
  - two
  - three
  - four
  - five

You can specify # columns, too:

.. hlist::
  :columns: 3

  - one
  - two
  - three
  - four
  - five
  - six
  - seven

Organization
============

Organization
------------

If your slide title is the same as the section title, like this,
the handouts won't repeat it. So do this for things like the "Goals"
slide in a "Goals" section.

New Slides
----------

When you want slide break that shouldn't cause a new
heading in the handouts, |reveal-br| use the `newslide` directive.

.. newslide::

This is a new slide with the same title, but on the handouts, it
just flows.

Note: slide content isn't contained in `newslide`,
it just appears after it.

.. newslide:: New Title

This is a new slide with a new title, but on the handouts, it just
flows.

.. newslide:: +(continued)

A new slide with an addition to the title.

.. newslide:: Colors
  :background: yellow

You can also use newslide to get background colors

.. newslide:: Images
  :background: porcupine.jpg

`Or images!`:white:

.. interslide::

  Interslides never appear on the handouts and don't have a title.

  They're useful for fun, silly things, like large images and text.

  Notice the content of interslide is inside the interslide.

.. interslide::

  .. image:: porcupine.jpg

.. interslide::
  :background: red

  You can set the background for them!

.. interslide::
  :background: porcupine.jpg


Images
======

Images
------

Add images like so:

.. image:: porcupine.jpg
  :width: 50%

It's good to set a width on it---otherwise, these are huge on the handouts.

.. newslide::

To make an image smaller on handouts, size it with ems:

.. image:: porcupine.jpg
  :width: 10em

(since ems are so much bigger on slides than handouts)

.. only:: not revealjs

    This is especially good for things like book cover images,
    since we want them to appear big on slides for visual pop,
    but they can appear much smaller on handouts.

.. newslide::

For images without good definition, you can add a border:

.. image:: porcupine.jpg
  :width: 50%
  :class: image-border

.. newslide::

For less-important images that should appear in handouts but not
on printed material, use the `noprint` class:

.. image:: porcupine.jpg
  :width: 50%
  :class: noprint




Fragments
=========

Single Items
------------

To make things appear, use the `one-incremental` class

.. container:: one-incremental

  Like this

.. container:: one-incremental

  Using it multiple times works, too!

Using `class` Directive
-----------------------

You can also do this with class:

.. rst-class:: one-incremental

    Like This

    Each Of These

    Gets that class

    (this puts the class on each paragraph)

Lists
-----

You can use on lists, too!

.. container:: item-incremental

  - This causes each top-level bullet point

  - To appear at once

    - But secondary points

    - Appear with parents

  - Like so

.. newslide::

The `nest-incremental` class makes each bullet appear incrementally:

.. container:: nest-incremental

  - Each bullet

    - Now appears

      - Incrementally

  - Like so

.. newslide::

Works on numbered lists:

.. container:: item-incremental

    1. One

    2. Two

    3. Three

.. newslide::

Can also use `rst-class` for this kind of stuff:

.. rst-class:: item-incremental

- Hello

- There

- Joel

Works on Definition Lists
-------------------------

.. container:: item-incremental

    Item Incremental
        Works on definition lists, too

    Just
        Put it on a container around the list

Effects
-------

.. container:: one-incremental grow

  This Grows!

.. container:: one-incremental fade-out

  This fades out

.. container:: one-incremental current-visible

  This is visible then goes away

.. container:: one-incremental highlight-current-red

  This turns red when current

.. container:: one-incremental highlight-red

  This turns and stays red

(there is also blue and green)


Individual Text Fragments
-------------------------

- This :incremental:`appears incrementally`

- This :incremental-fade-out:`fades out incrementally`

- This :incremental-current-visible:`is visible, then vanishes`

- This :incremental-highlight-current-blue:`is blue when current`

- This :incremental-highlight-current-red:`is red when current`

- This :incremental-highlight-current-green:`is green when current`

- This :incremental-highlight-blue:`turns then stays blue`

- This :incremental-highlight-green:`turns then stays green`

- This :incremental-highlight-red:`turns then stays red`

List Fragments
--------------

.. it's subtle, but the difference is that these change the entire
   bulleted line, not the text

- This :incremental-li:`appears incrementally`

- This :incremental-li-fade-out:`fades out incrementally`

- This :incremental-li-current-visible:`is visible, then vanishes`

- This :incremental-li-highlight-current-blue:`is blue when current`

- This :incremental-li-highlight-current-red:`is red when current`

- This :incremental-li-highlight-current-green:`is green when current`

- This :incremental-li-highlight-blue:`turns and then stays blue`

- This :incremental-li-highlight-green:`turns and then stays green`

- This :incremental-li-highlight-red:`turns and then stays red`

Literal Blocks
==============

Literal Blocks
--------------

To show literal text blocks, use \:\: like this::

  Hello! *not italics*

If you don't want to see a colon at the end, put space before it ::

  Hello `not a citation`

Or you can say it like so

::

  Hello! ``not code block``

Parsed Literal
--------------

You can use parsed literal for literal blocks that still parse for
style stuff.

.. parsed-literal::

  Hello *italics* and `citation` and `red`:red:

Console
-------

We use a special class on parsed literal for showing shell commands:

.. parsed-literal::
  :class: console

  $ `echo "this is a command"`:cmd:
  this is a command

  $ `echo`:cmd:  `# comment`:comment:

Sometimes this is useful for non-console stuff, like our diagrams:

.. parsed-literal::
  :class: console

  Hello

  This :incremental-highlight-current-blue:`is blue when current`

  There

Code Blocks
===========

Code Blocks
-----------

Ask for a code block like so

.. code-block:: python

  if name == "joel":
      print "hi"

.. code-block:: html

  <a href="yo.html">&copy; <!-- comment --></a>

(also: js, sql, xml, and many others---see "pygments" library)

Emphasizing Lines
-----------------

Can emphasize lines:

.. code-block:: python
  :emphasize-lines: 1, 3-4, 6-

  if name == "joel":
      print "hi"
      print "there"
      print "joel"
      print "and"
      print "everyone"
      print "else"

Add Captions
------------

.. code-block:: python
  :caption: example.py

  if name == "joel":
      print "hi"

.. only:: not revealjs

  It's our style to use this for the filenames of demo files
  or if some explanation is needed of where this code is coming from.

Note that the caption must be a unique identifier---so, to re-use it,
you need to provide a "name" that is unique:

.. code-block:: python
  :caption: example.py
  :name: example-2

  if name == "joel":
      print "hi"


Doctests
--------

Often better than ``.. code-block:: python`` is ``.. doctest``:

.. doctest:: python

    >>> x = 5
    >>> x
    5

You can also have non-doctest-looking but testable code:

.. testcode:: python

    def fun(s):
        return s.upper()

    print(fun("hello"))

.. testoutput:: python

    HELLO

.. newslide::

All of those can take captions, too:

.. doctest:: python
    :caption: one

    >>> x = 5
    >>> x
    5

.. testcode:: python
    :caption: two

    def fun(s):
        return s.upper()

    print(fun("hello"))

.. testoutput:: python
    :caption: three

    HELLO

.. newslide::

You can hide these; they can still be tested, but don't appear.

.. doctest:: python
    :hide:

    >>> x = 5
    >>> x
    5

.. testcode:: python
    :hide:

    def fun(s):
        return s.upper()

    print(fun("hello"))

.. testoutput:: python
    :hide:

    HELLO

Literal Includes
----------------

Whenever possible, don't inline code---it's too easy for it to have bugs!

Instead, keep the code in a separate file, so we can test it and include as demo code

.. newslide::

.. literalinclude:: demo-demo/demo-include.py

.. newslide::

Can use caption/name like for code blocks:

.. literalinclude:: demo-demo/demo-include.py
  :name: demo-include-2
  :caption: A Demo

.. newslide::

Better, if caption is there but blank, it gets file name

.. literalinclude:: demo-demo/demo-include.py
  :name: demo-include-3
  :caption:

Finding Things
--------------

Can only include certain lines and can emphasize:

.. literalinclude:: demo-demo/demo-include.py
  :lines: 1, 2, 14-15
  :emphasize-lines: 3

.. newslide::

Better is to find things with `pyobject`

.. literalinclude:: demo-demo/demo-include.py
  :pyobject: Cat

.. newslide::

Can also use `start-after` and `end-before` to match text:

.. literalinclude:: demo-demo/demo-include.py
  :start-after: Do other stuff

.. literalinclude:: demo-demo/demo-include.py
  :lines: 3-
  :end-before: Do other stuff

.. newslide::

This lets us show only one method on a class:

.. literalinclude:: demo-demo/demo-include.py
  :pyobject: Cat.meow
  :prepend: class Cat(object):  # ...

This is used when we want to highlight part of a longer class.

.. newslide::

Or, if we want to pull the method out to show it simply:

.. literalinclude:: demo-demo/demo-include.py
  :pyobject: Cat.meow
  :dedent: 4

(The `dedent` removes four leading spaces)

Don't Use `code`
----------------

There's also a `code` directive that works for Sphinx but it
appears to be undocumented. We style it the same, but don't use it---use
`code-block`, instead.


Notes, Sidebars, Hints, etc.
============================

Notes
-----

Notes only appear in handouts:

.. note:: This is a *note*.

  It goes on.

  And on.


Use notes for sidebar-style information.

.. newslide::

.. note:: Other Stuff In Notes

  Notes should with with ``code_literals()`` and code:

  .. code-block:: python

    if name == "joel":
        print "hi"

Warnings
--------

Warnings only appear in handouts:

.. warning:: This is a warning.

  Don't do this.


General
-------

"Admonition" is the general class of this stuff. These only appear in handouts.

.. admonition:: Requires a Title!

  It doesn't have a color, but is otherwise the same.

Sidebars
--------

.. sidebar:: Side Note Here

  This is a quick note about the main thing.

When you want to have a sidebar, put it before the content it goes with.

These only appear
in handouts---so don't use them for anything too important.

.. newslide::

An important case is sidebar-next-to-code:

.. sidebar:: Lightly implemented

  Note that that isn't a very complete implementation: it should include
  methods for things like finding the number of items in the `ODict`,
  creating an `ODict` with an initial set of values, and so on.

  It does,
  however, highlight the two important points: it's easy to build this implemetation,
  and it suffers from O(n) when deleting items from the `ODict`.

.. code-block:: python
   :class: code-90 code-65c

   class OrderedDict(object):
       """Ordered dictionary, built from dictionary and list."""

       def __init__(self):
           self._dict = {}
           self._list = []

       def get(self, key):
           """Get a key. O(1)."""

           return self._dict.get(key)  # O(1)

       def set(self, key, value):
           """Set a key. O(1)."""

           if key not in self._dict:   # O(1)
               self._list.append(key)  # O(1)
           self._dict[key] = value     # O(1)

       def delete(self, key):
           """Remove a key. O(n)."""

           del self._dict[key]         # O(1)
           self._list.remove(key)      # O(n)  <-- :(

Topics
------

This is a topic:

.. topic:: A Hint

    We use topics for hints

    Like this

Hints
-----

We also have a specific CSS class for hints:

.. topic:: **Linked List**
  :class: hover-reveal

  You could solve this in other ways, but using a linked list (or a doubly-linked list)
  is often a good way to solve this problem. You can do so by making the list
  "circular"---having the last item in the linked list point back to the first item.

  This will let you traverse the list, removing items until one remains.

  If you want to try it this way, you may find this node class helpful:

Containers
==========

Containers
----------

The `container` directive just adds a div.

.. container::

  Boring!

This is useful if you want to put a class on it:

.. container:: someclass

  Now I have `someclass` on my `div`

.. newslide::

Can put class on without a div with `rst-class`:

.. rst-class:: someclass

This para has `someclass`

.. rst-class:: someclass

  Each of these paras

  Has `someclass`, independently

Big Code
--------

`big` makes code blocks and literal blocks bigger

.. rst-class:: big

    .. code-block:: python

        if name == "joel":
            print "hi"


.. newslide:: Works with Parsed Literals

.. rst-class:: big

  .. parsed-literal::

    Hey, I'm `red`:red: and big!

.. parsed-literal::
  :class: big

  Hey, I'm also `red`:red: and big!

.. newslide:: Works with Literals

.. rst-class:: big

  ::

    I'm big!

Small Code
----------

For longer listings:

.. container:: compare

  .. container::

    .. literalinclude:: demo-demo/demo-include.py
      :caption: (normal size)

  .. container:: small

    .. literalinclude:: demo-demo/demo-include.py
      :caption: (smaller)

.. container:: compare compare23

  .. container::

    .. literalinclude:: demo-demo/demo-include.py
      :caption: (normal size)

  .. container:: small

    .. literalinclude:: demo-demo/demo-include.py
      :caption: (smaller)

.. container:: compare compare21

  .. container::

    .. literalinclude:: demo-demo/demo-include.py
      :caption: (normal size)

  .. container:: small

    .. literalinclude:: demo-demo/demo-include.py
      :caption: (smaller)

Small Code
----------

Sizes 150% down

.. literalinclude:: demo-demo/wide.py
  :class: code-150

.. literalinclude:: demo-demo/wide.py
  :class: code-140

.. literalinclude:: demo-demo/wide.py
  :class: code-130

.. literalinclude:: demo-demo/wide.py
  :class: code-120

.. literalinclude:: demo-demo/wide.py
  :class: code-110

.. literalinclude:: demo-demo/wide.py
  :class: code-100

.. literalinclude:: demo-demo/wide.py
  :class: code-90

.. literalinclude:: demo-demo/wide.py
  :class: code-80

.. literalinclude:: demo-demo/wide.py
  :class: code-70

.. literalinclude:: demo-demo/wide.py
  :class: code-60

.. literalinclude:: demo-demo/wide.py
  :class: code-50

Widths 100 down

.. literalinclude:: demo-demo/wide.py
  :class: code-85c

.. literalinclude:: demo-demo/wide.py
  :class: code-80c

.. literalinclude:: demo-demo/wide.py
  :class: code-70c

.. literalinclude:: demo-demo/wide.py
  :class: code-60c

.. literalinclude:: demo-demo/wide.py
  :class: code-50c

.. literalinclude:: demo-demo/wide.py
  :class: code-40c

.. literalinclude:: demo-demo/wide.py
  :class: code-30c

.. literalinclude:: demo-demo/wide.py
  :class: code-20c

.. literalinclude:: demo-demo/wide.py
  :class: code-10c

Combined

.. literalinclude:: demo-demo/wide.py
  :class: code-10c code-200

.. literalinclude:: demo-demo/demo-include.py
  :class: code-60c code-120
  :linenos:
  :emphasize-lines: 4,5

Text-Heavy
----------

For big, bold text on slides, use text-heavy:

.. rst-class:: text-heavy

  Like this

Or even `like this`:text-heavy:

Comparing Things
================

Comparing Things
----------------


Instead of just one thing:

.. code-block:: js

      if (name == "joel")
          console.log("hi");


Side-by-side comparisons are useful:

.. container:: compare

  .. container::

    .. code-block:: js

          if (name == "joel")
              console.log("hi");

  .. container::

    .. code-block:: python

      if name == "joel":
          print "hi"

.. newslide::

.. container:: compare

  .. container::

    The spacing should look right even if we lead with compare, or
    if the compares are textual.

  .. container::

    .. code-block:: python

      if name == "joel":
          print "hi"

    .. code-block:: python

      if name == "joel2":
          print "hi"


Only
====

Only
----

To have things only appear on slides:

.. only:: revealjs

  This only appears on slides

To have things not appear on slides, but everywhere else:

.. only:: not revealjs

  This does not appear on slides.

  Don't ever say "only:: handouts"---since we have other possible
  non-slide formats (LaTeX, epub, etc). Always say "only:: not revealjs".

ifconfig
--------

You can use ifconfig for logical conditions:

.. ifconfig:: 1 + 1 == 2

  Math works!

.. ifconfig:: 1 + 1 == 3

  Ut Oh.

.. ifconfig:: 'Fall 2015' in project

  You can refer to variables in the conf.py




Definition Lists
================

Definition Lists
----------------

A Definition List
  Is useful for things like

Glossary Terms
  And stuff like that

.. newslide::

Also Works
  When the things are multi-paragraph

  like here.

Should Look Ok
  Even if some thing are not multi-paragraph

Tables
======

Standard Table
--------------

====================== =========== =========== =========== ============ ============
Data Structure         Get         Add         Delete      Iterate      Memory
====================== =========== =========== =========== ============ ============
Tree                   `O(n)`:red: O(1)        O(1)        O(1)         `*`:green:
Binary Search Tree     O(log n)    `O(n)`:red: `O(n)`:red: O(1)         `*`:green:
Dictionary (Hash Map)  O(1)        O(1)        O(1)        `O(n)`:red:  `**`:orange:
Set (Hash Map)         O(1)        O(1)        O(1)        `O(n)`:red:  `**`:orange:
OSet (HashMap+DLL)      O(1)       O(1)        O(1)        O(1)         `***`:red:
ODict (HashMap+DLL)     O(1)       O(1)        O(1)        O(1)         `***`:red:
====================== =========== =========== =========== ============ ============

Two In A Row
------------

====================== =========== =========== =========== ============ ============
Data Structure         Get         Add         Delete      Iterate      Memory
====================== =========== =========== =========== ============ ============
Tree                   `O(n)`:red: O(1)        O(1)        O(1)         `*`:green:
Binary Search Tree     O(log n)    `O(n)`:red: `O(n)`:red: O(1)         `*`:green:
====================== =========== =========== =========== ============ ============

====================== =========== =========== =========== ============ ============
Data Structure         Get         Add         Delete      Iterate      Memory
====================== =========== =========== =========== ============ ============
Tree                   `O(n)`:red: O(1)        O(1)        O(1)         `*`:green:
Binary Search Tree     O(log n)    `O(n)`:red: `O(n)`:red: O(1)         `*`:green:
====================== =========== =========== =========== ============ ============

Arranging Columns
-----------------

Can center columns other than first:

.. rst-class:: td-center

  ====================== =========== =========== =========== ============ ============
  Data Structure         Get         Add         Delete      Iterate      Memory
  ====================== =========== =========== =========== ============ ============
  Tree                   `O(n)`:red: O(1)        O(1)        O(1)         `*`:green:
  Binary Search Tree     O(log n)    `O(n)`:red: `O(n)`:red: O(1)         `*`:green:
  ====================== =========== =========== =========== ============ ============

Can right justify columns other than first:

.. rst-class:: td-right

  ====================== =========== =========== =========== ============ ============
  Data Structure         Get         Add         Delete      Iterate      Memory
  ====================== =========== =========== =========== ============ ============
  Tree                   `O(n)`:red: O(1)        O(1)        O(1)         `*`:green:
  Binary Search Tree     O(log n)    `O(n)`:red: `O(n)`:red: O(1)         `*`:green:
  ====================== =========== =========== =========== ============ ============

Right Columns
-------------

Can right-justify columns other than first:

.. rst-class:: td-right

  ====================== =========== =========== =========== ============ ============
  Data Structure         Get         Add         Delete      Iterate      Memory
  ====================== =========== =========== =========== ============ ============
  Tree                   `O(n)`:red: O(1)        O(1)        O(1)         `*`:green:
  Binary Search Tree     O(log n)    `O(n)`:red: `O(n)`:red: O(1)         `*`:green:
  Dictionary (Hash Map)  O(1)        O(1)        O(1)        `O(n)`:red:  `**`:orange:
  Set (Hash Map)         O(1)        O(1)        O(1)        `O(n)`:red:  `**`:orange:
  OSet (HashMap+DLL)      O(1)       O(1)        O(1)        O(1)         `***`:red:
  ODict (HashMap+DLL)     O(1)       O(1)        O(1)        O(1)         `***`:red:
  ====================== =========== =========== =========== ============ ============

Quotes
======

Quote
-----

You can introduce a quote by indenting:

  "A rose is a rose is a rose."

  -- Gertrude Stein

.. newslide::

.. epigraph::

  "A rose is a rose is a rose."

  -- Gertude Stein

(you have to use epigraph here, since just indenting would
make RST think this was the content of the `newslide` directive)


Plots
=====

Plots
-----

Add `matplotlib` plots:

.. plot::
  :width: 20em

  import numpy as np
  import matplotlib.pyplot as plt

  x = np.arange(0, 100000, 5000)
  plt.plot(x, x / 1000, 'bo')
  plt.ylabel('time', fontsize=20)
  plt.xlabel('size of list', fontsize=20)
  plt.xticks([])
  plt.yticks([])
  plt.title('pop()', fontsize=35)

Math
====

Math
----

Adding math:

.. math::

    r = \frac{\sum^n_{i=1}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\Sigma^n_{i=1}(x_i - \bar{x})^2 \times \Sigma^n_{i=1}(y_i - \bar{y})^2}}

Or `n = {x}^2`:math: for inline.


Graphs
======


Graphs
------

.. nope

    Graphviz graphs are super-common and useful:

    .. jdigraph:: org
      :revealjs: -Grankdir=TB -Gsize=11,6.5!
      :handouts: -Grankdir=TB -Gsize=5.5,4!
      :latex: -Grankdir=TB -Gsize=5.5,4!

      Organisms -> { Plants, Fungi, Animals, Bacteria, Protists };
      Animals -> { Cnidaria, Molluscs, Chordata, Arthropods, Echinoderms };
      Chordata -> { Actinopterygii, Mammalia, Chondrichthyes, Aves, Amphibia, Reptilia };
      Mammalia -> { Carnivora, Primate, Artiodactyla, Rodentia };

    Put in sizes for `revealjs`, `handouts`, and `latex`.

    Generally, `handouts` and `latex` will be about half the size of `revealjs`.

Newer Style
-----------

Now, you can simplify that with a single "size" --- we'll scale down for handouts and LaTeX:

.. jdigraph:: org
  :size: 11,6.5

  rankdir=TB

  Organisms -> { Plants, Fungi, Animals, Bacteria, Protists };
  Animals -> { Cnidaria, Molluscs, Chordata, Arthropods, Echinoderms };
  Chordata -> { Actinopterygii, Mammalia, Chondrichthyes, Aves, Amphibia, Reptilia };
  Mammalia -> { Carnivora, Primate, Artiodactyla, Rodentia };

(take the `revealjs` size, add any other options, like `rankdir`, to the body)


Colors
======

Colors
------


You can use colors:

- `red`:red:

- `green`:green:

- `orange`:orange:

- `tan`:tan:

- `blue`:blue:

- `gray`:gray:

- `gone`:gone:

- `inv-red`:inv-red:

.. newslide::

How these look in a literal block:

.. parsed-literal::

    `red`:red: `green`:green: `orange`:orange: `tan`:tan: `blue`:blue: `gray`:gray: `gone`:gone: `inv-red`:inv-red:

And in a console:

.. parsed-literal::
    :class: console

    `cmd`:cmd: `red`:red: `green`:green: `orange`:orange: `tan`:tan: `blue`:blue: `gray`:gray: `gone`:gone: `inv-red`:inv-red:

z

Speaker Notes
=============

Speaker Notes
-------------

You can add speaker notes with the `speaker` directive. These appear in "speaker notes" view
(press **S** in revealjs). This never appears on handouts.

.. speaker::

  Example speaker note.


.. comment

  If you change the font or sizes, make sure this looks ok---these are stress tests
  for sizes

Stress Test Longest Possible Section Title
==========================================

Stress Test Longest Possible Slide Title Is This One
----------------------------------------------------

- One This Should Fit On One Line Even Though It's Really Really Long

- Two

- Three

- Four

- Five

- Six

- Seven

- Eight

- Nine

- Ten

- Eleven

Code Stress Test
----------------

.. code-block:: python

    class Cat5(object):
        """Cat with class methods."""

        _SELECT = "SELECT name, hunger FROM Cats WHERE name = :name"
        _UPDATE = "UPDATE Cats SET hunger = :hunger WHERE name = :name"

        def __init__(self, name, hunger):     # special method
            self.name = name                  # object attribute
            self.hunger = hunger

        def feed(self, calories):
            """Feed cat, update hunger, and update database."""

            self.hunger = self.hunger - calories
            db.session.execute(
                self._UPDATE, {'hunger': self.hunger,'name': self.name})
            db.session.commit()

        def feed(self, calories):
            """Feed cat, update hunger, and update database."""

            self.hunger = self.hunger - calories
            db.session.execute(
                self._UPDATE, {'hunger': self.hunger,'name': self.name})
            db.session.execute(
                self._UPDATE, {'hunger': self.hunger,'name': self.name})
            db.session.commit()
