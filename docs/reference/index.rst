===============
Glide Reference
===============

.. sectionauthor:: joel

.. meta::
    :description: Reference to Glide document system.


.. only:: not revealjs

  :author: Joel Burton <joel@joelburton.com>
  :version: |version|
  :updated: |date|

  .. container:: noprint

    You may find it useful to review the source of this document while reading it:
    `index.rst`:download:.

.. todo:: Finish indexing and include index page.

.. todo:: Add new styles

  - code-highlight-wrong/good/pop

  - code-comments-wrong/good/pop


Overall document format
=======================

Source indentation
------------------

RST files should always use an :index:`indent` of **2 spaces.**

.. container:: compare

  .. code-block:: rst
    :class: code-cols-20

    .. image::
      :class: border
      :width: 2em

  .. container:: width-5 margin-top-4 text-align-center

    not

  .. code-block:: rst
    :class: code-wrong code-cols-20

    .. image::
       :class: border
       :width: 2em

  .. container:: width-5 margin-top-4 text-align-center

    or

  .. code-block:: rst
    :class: code-wrong code-cols-20

    .. image::
        :class: border
        :width: 2em

.. attention:: Please be consistent on this.

.. versionadded:: 2.0

  Added specific requirement of 2-space indenting.

.. index:: comments

Comments
--------

.. code-block:: rst

  .. line with two dots but no double-colons is a comment

    And everything under here is ignored

    .. warning:: You'll never see this

.. index:: sections; structure

Document structure
------------------

.. index:: rubric

.. code-block:: rst

  =========
  Doc title  *(only cap first word)*
  =========

  Chapter title
  =============

  Slide or section
  ----------------

  Inner subsection
  ~~~~~~~~~~~~~~~~

  .. rubric:: Title

A `rubric` makes a heading-style title, |br|
but it doesn't add it to the table of contents.

.. versionchanged:: 2.0

  Added specific advice on the the heading characters.

Introducing sections
--------------------

At the top of a section, can introduce the "`highlights`:index:" of that section:

.. container:: compare

  .. code-block:: rst

    .. highlights:: Interesting stuff ahead

      - React

      - CSS

  .. container::

    .. highlights:: Interesting stuff ahead

      - React

      - CSS

.. newslide::

Can also introduce a menu of subheadings below this level:

.. index:: contents

.. code-block:: rst

  My section
  ==========

  .. contents::
    :local:

  (that will show links to the subsection heads)

The contents menu does not appear in slides.

.. index::
  single: slides
  pair: newslide; directive
  pair: interslide; directive

Slide-specific structure
------------------------

.. code-block:: rst

  .. newslide::

  Adds new slide, without adding a section in handouts.
  Note content following it is not indented!

  .. newslide:: New Title

  Change slide title, but, again, nothing in handouts.

  .. newslide:: +(continued)

  A new slide with an addition to the title.

  .. newslide:: Colors
    :background: yellow

  Can get background colors

  .. newslide:: Images
    :background: porcupine.jpg

  Or images

.. newslide:: Interslide

.. code-block:: rst

  .. interslide::

    Oh no!

Interslides never appear on the handouts and don't have a title. |br|
They're useful for fun, silly things, like large images and text. |br|
Can take a background or color, like ``newslide``.

.. attention:: Notice the content of interslide is inside the interslide.


.. index::
  single: divider
  pair: dash; em
  pair: dash; en


Typography
==========

.. container:: compare

  .. code-block:: rst

    **Bold**, *Italic*

    Em---dash En--dash

    Spaces     are collapsed

    Line of just ---- creates break
    *(example below)*

  .. container::

    **Bold**, *Italic*

    Em---dash En--dash

    Spaces     are collapsed

----

.. versionadded:: 2.0

  Add divider with ``----``

.. index:: links

Links
-----

.. container:: compare

  .. code-block:: rst

    `Google <http://google.com>`_ is a
    search engine.

  .. container::

    `Google <http://google.com>`_ is a
    search engine.


.. index:: roles


Roles
=====

.. code-block:: rst

  Roles can be used as :role:`Text` or `Text`:role:

  :code:`Code` can use shortcut ``Code``

  :title:`Title` can use shortcut `Title`

.. newslide::

.. index::
  pair: abbr; role
  pair: code; role
  pair: command; role
  pair: dfn; role
  pair: envvar; role
  pair: file; role
  pair: guilabel; role
  pair: kbd; role
  pair: math; role
  pair menuselection; role
  pair: mimetype; role
  pair: program; role
  pair: samp; role
  pair: sub; role
  pair: sup; role
  pair: title; role

.. table:: Standard sphinx roles

  ==================== ===================== ==================================
  Name                 Example               Meaning
  ==================== ===================== ==================================
  ``:abbr:``           `XY (x and y)`:abbr:  Abbreviation, put definition in ()
  ``:code:``           `x = 1`:code:         Code *snippets*
  ``:command:``        `rm -rf`:command:     Executable command
  ``:dfn:``            is a `closure`:dfn:   Mark when term first defined
  ``:envvar:``         `FLASK_ENV`:envvar:   Environmental variable
  ``:file:``           `python-{x}`:file:    Filename, can have ``{var}`` in it
  ``:guilabel:``       `Save`:guilabel:      GUI button/window
  ``:kbd:``            `⌘-s`:kbd: `⇧S`:kbd:  Keyboard sequence
  ``:math:``           `n = {x}^2`:math:     Inlined MathTex
  ``:menuselection:``  `File -->             Menu choice
                       Open`:menuselection:
  ``:mimetype:``       `text/html`:mimetype: MIME type
  ``:program:``        `Insomnia`:program:   Program
  ``:samp:``           `text {x}`:samp:      Output/sample (can have ``{var}``)
  ``:sub:``            n log\ `2`:sub:\ n    Subscript
  ``:sup:``            x\ `2`:sup:           Superscript
  ``:title:``          `var` or `func()`     General title, code *names*
  ==================== ===================== ==================================

.. versionchanged:: 2.0

  More focus on semantic roles.

.. newslide::

.. index::
  pair: doc; role
  pair: download; role
  pair: ref; role

.. table:: Standard sphinx roles for linking

  ==================== ===================== ==================================
  Name                 Example               Meaning
  ==================== ===================== ==================================
  ``:doc:``            `index`:doc:          Link to RST document
  ``:download:``       `file <f>`:download:  Puts file in build, links to it
  ``:ref:``            `colors`:ref:         Internal link in document
  ==================== ===================== ==================================

.. newslide::

.. index::
  pair: role; small
  pair: role; small-muted
  pair: role; muted
  pair: role; danger
  pair: role; warning
  pair: role; success
  pair: role; ins
  pair: role; del
  pair: role; gone
  pair: role; comment
  pair: role; wrong

.. table:: Glide roles

  ==================== ===================== ==================================
  Name                 Example               Meaning
  ==================== ===================== ==================================
  ``:small:``          `Legal text`:small:   Make smaller
  ``:small-muted:``    `Shhhh`:small-muted:  Smaller *and* muted
  ``:muted:``          `Quiet`:muted:        Muted (lighter colored)
  ``:danger:``         `Oh no`:danger:       Danger semantic color
  ``:warning:``        `Achtung!`:warning:   Warning semantic color
  ``:success:``        `Yay`:success:        Success semantic color
  ``:ins:``            `New thing`:ins:      Insertion/added-in diff
  ``:del:``            `Deleted`:del:        Removed/gone-in-diff
  ``:gone:``           `Gone`:gone:          Mark as moved
  ``:comment:``        `// see...`:comment:  Mark as code-like comment
  ``:wrong:``          `var x=7`:wrong:      Wrong way to do it
  ==================== ===================== ==================================

.. versionadded:: 2.0

  Added semantic names to discourage direct colors.


.. index:: substitutions

Substitutions
=============

Symbols
-------

.. hlist::
  :columns: 3

  - ``|nbsp|``
  - ``|rarr|``     |rarr|
  - ``|larr|``     |larr|
  - ``|darr|``     |darr|
  - ``|uarr|``     |uarr|
  - ``|lrarr|``    |lrarr|
  - ``|plus|``     |plus|
  - ``|times|``    |times|
  - ``|divide|``   |divide|
  - ``|check|``    |check|
  - ``|wrong|``    |wrong|
  - ``|approx|``   |approx|

.. deprecated:: 2.0

  Deprecated card suits, which are now handled by emoji.

Glide Functional Substitutions
------------------------------

.. container:: compare

  .. code-block:: rst

    Today: |date|
    Version: |version|, Release: |release|

    Force HTML directly only on slides:
    :raw-reveal:`<input type=checkbox>`

    Force HTML directly only on handouts:
    :raw-handouts:`<input type=checkbox>`

    Linebreak only on slides: |br|
    New line.

    Linebreak only on handouts: |handouts-br|
    New line

  .. container::

    Today: |date|
    Version: |version|, Release: |release|

    Force HTML directly only on slides:
    :raw-reveal:`<input type=checkbox>`

    Force HTML directly only on handouts:
    :raw-handouts:`<input type=checkbox>`

    Linebreak only on slides: |br|
    New line.

    Linebreak only on handouts: |handouts-br|
    New line

.. container:: small

  (``|reveal-br|`` is an alias for ``|br|``.)

.. versionadded:: 2.0 Added ``|br|`` and  ``|handouts-br|``.

Variable interpolation
----------------------

.. container:: compare

  .. code-block:: rst
    :class: code-font-size-90 code-fit-content

    - |demo-link| = demo zip file for this
    - |version| = `version` in `conf.py`:file:
    - |release| = `release` in `conf.py`:file:
    - |today| shows day of build

  .. container::

    - |demo-link| shows link to demo for project
    - |version| shows version number in `conf.py`:file:
    - |release| shows release number in `conf.py`:file:
    - |today| shows day of build

At Rithm, `version` becomes the code for our cohorts, eg ``"r15"``.


.. index:: emoji


Emoji
=====

Paste in actual emoji symbol (we use `Twemoji <https://twemoji.twitter.com/>`_)

To size:

Size with role :samp:`:emoji-{1,2,3,5,7}x:` |br|
:emoji-1x:`🌮` :emoji-2x:`🌮` :emoji-3x:`🌮` :emoji-5x:`🌮` :emoji-7x:`🌮`

.. versionadded:: 2.0

  Handle emoji in all output formats. Added SVG images for emoji and
  resizing ability.


.. index:: colors

.. _colors:


Colors
======

.. raw:: html

  <style>
    .color-table span { color: transparent;  }
    .color-table ul { list-style-type: none; margin: 0; padding: 0; font-size: 80% }
  </style>

.. container:: color-table

  .. hlist::
    :columns: 4

    - `╳`:bg-black:  black
    - `╳`:bg-near-black:  near-black
    - `╳`:bg-dark-gray:  dark-gray
    - `╳`:bg-mid-gray:  mid-gray
    - `╳`:bg-gray:  gray
    - `╳`:bg-silver:  silver
    - `╳`:bg-light-silver:  light-silver
    - `╳`:bg-moon-gray:  moon-gray
    - `╳`:bg-light-gray:  light-gray
    - `╳`:bg-near-white:  near-white
    - `╳`:bg-white:  white
    - `╳`:bg-dark-red:  dark-red
    - `╳`:bg-red:  red
    - `╳`:bg-light-red:  light-red
    - `╳`:bg-orange:  orange
    - `╳`:bg-gold:  gold
    - `╳`:bg-yellow:  yellow
    - `╳`:bg-light-yellow:  light-yellow
    - `╳`:bg-purple:  purple
    - `╳`:bg-light-purple:  light-purple
    - `╳`:bg-dark-pink:  dark-pink
    - `╳`:bg-hot-pink:  hot-pink
    - `╳`:bg-pink:  pink
    - `╳`:bg-light-pink:  light-pink
    - `╳`:bg-dark-green:  dark-green
    - `╳`:bg-green:  green
    - `╳`:bg-light-green:  light-green
    - `╳`:bg-navy:  navy
    - `╳`:bg-dark-blue:  dark-blue
    - `╳`:bg-blue:  blue
    - `╳`:bg-light-blue:  light-blue
    - `╳`:bg-lightest-blue:  lightest-blue
    - `╳`:bg-washed-blue:  washed-blue
    - `╳`:bg-washed-green:  washed-green
    - `╳`:bg-washed-yellow:  washed-yellow
    - `╳`:bg-washed-red:  washed-red

.. container:: small

  Reference & hex codes at `Tachyons colors
  <https://tachyons.io/docs/themes/skins/>`_

Using colors
------------

Inline as role:

- ``:pink:`` |rarr| :pink:`pink`

- ``:bg-pink:`` |rarr| :bg-pink:`bg-pink`

- ``:inv-pink:`` |rarr| :inv-pink:`inv-pink`

Can use where classes are allowed:

.. code-block:: rst

  .. container:: blue

    Blue stuff here.

.. versionadded:: 2.0

  All colors can now be used inline using roles.

Line blocks
-----------

.. container:: compare

  .. code-block:: rst

    | Lines can be broken
    | at specific places
    |
    | This affects all builders.

  .. container::

    | Lines can be broken
    | at specific places
    |
    | This affects all builders.


Lists
=====

.. contents:: Different kinds of lists
  :local:

.. index:: definition lists

Definition lists
----------------

.. container:: compare

  .. code-block:: rst

    Definition list item
      Definition

    Another term
      And definition

  .. container::

    Definition list item
      Definition

    Another term
      And definition

.. tip:: Definition terms are already put in strong text. They do not need
  to be bolded.

.. index:: lists

Lists
-----

.. container:: compare

  .. code-block:: rst

    - Item A

      - Item A1

    - Item B

  .. container::

    - Item A

      - Item A1

    - Item B

.. container:: compare

  .. code-block:: rst

    1. Item A

       - Item A1

    2. Item B

  .. container::

    1. Item A

       - Item A1

    2. Item B

.. newslide:: +autonumbering

.. index:: lists; auto-numbering

.. container:: compare

  .. code-block:: rst

    #. Item A

    #. Item B

       #. Inner item

  .. container::

    #. Item A

    #. Item B

       #. Inner item

.. _putting_lists_side_by_side:

Putting lists side-by-side
--------------------------

.. index:: lists; side-by-side

Two or more lists can be side-by-side on slides automatically, while being
linear for handouts (this is useful if the side-by-side nature isn't integral
to the material and is instead to conserve space on slides). You can use an
empty comment to trigger the parser to see these as separate lists.

.. container:: compare

  .. code-block:: rst

    - Item A
    - Item B

    ..

    - Another list
    - Second item

  .. container::

    - Item A
    - Item B

    ..

    - Another list
    - Second item

.. versionadded:: 2.0

  New technique for slides-only side-by-side lists.


.. index::
  single: lists; side-by-side
  single: hlist
  single: columns

HLists
------

Simple list that should always be in columns can use `hlist`:

.. container:: compare

  .. code-block:: rst

    .. hlist::
      :columns: 3

      - a
      - b
      - c
      - d
      - e
      - f

  .. hlist::
    :columns: 3

    - a
    - b
    - c
    - d
    - e
    - f

.. index:: tables


Tables
======

.. contents:: Different kinds of tables
  :local:

.. index:: tables; field lists

Field lists
-----------

Key/value mappings should be a `field list` table:

.. container:: compare

  .. code-block:: rst

    :apple: red
    :berry: blue
    :cherry: red

  .. container::

    :apple: red
    :berry: blue
    :cherry: red

Simple Tables
-------------

Simple tables can be made like so:

.. container:: compare

  .. code-block:: rst
    :class: code-font-size-90

    ==== ======== ========
    ID   First    Last
    ==== ======== ========
    1    James    White
    2    Aliya    Maitez
    ==== ======== ========

  .. table::

    ==== ======== ========
    ID   First    Last
    ==== ======== ========
    1    James    White
    2    Aliya    Maitez
    ==== ======== ========

.. newslide::

.. index:: tables; column width

You can add a caption (or classes) to a table by using the full directive form,
and can also add column widths:

.. container:: compare

  .. code-block:: rst
    :class: code-font-size-90

    .. table:: My table
      :class: dark-blue
      :widths: 1 1 1

      ==== ======== ========
      ID   First    Last
      ==== ======== ========
      1    James    White
      2    Aliya    Maitez
      ==== ======== ========

  .. table:: My table
    :class: dark-blue
    :widths: 1 1 1

    ==== ======== ========
    ID   First    Last
    ==== ======== ========
    1    James    White
    2    Aliya    Maitez
    ==== ======== ========

Complex tables
--------------

.. index::
  single: tables; complex
  single: tables; grid

Complex tables, where there are spanning rows or columns, can be made like so:

.. container:: compare

  .. code-block:: rst
    :class: code-font-size-75 code-fit-content width-45

    +-----------------+-------+-------+-------+
    | Header, col 1   | Head2 | Head3 | Head4 |
    | header optional |       |       |       |
    +=================+=======+=======+=======+
    | body 1, col 1   | col 2 | col 3 | col 4 |
    +-----------------+-------+-------+-------+
    | body row 2      | Cells may span cols.  |
    +-----------------+-------+---------------+
    | body row 3      | May   | - Table cells |
    +-----------------+ span  | - contain     |
    | body row 4      | rows  | - body elems  |
    +-----------------+-------+---------------+

  .. table::
    :class: font-size-85 width-50

    +-----------------+-------+-------+-------+
    | Header, col 1   | Head2 | Head3 | Head4 |
    | header optional |       |       |       |
    +=================+=======+=======+=======+
    | body 1, col 1   | col 2 | col 3 | col 4 |
    +-----------------+-------+-------+-------+
    | body row 2      | Cells may span cols.  |
    +-----------------+-------+---------------+
    | body row 3      | May   | - Table cells |
    +-----------------+ span  | - contain     |
    | body row 4      | rows  | - body elems  |
    +-----------------+-------+---------------+

.. index:: tables; list

List tables
-----------

Can also make tables from lists:

.. container:: compare

  .. code-block:: rst
    :class: code-font-size-85 code-fit-content

    .. list-table::
      :header-rows: 1

      * - Heading row 1, column 1
        - Heading row 1, column 2
        - Heading row 1, column 3
      * - Row 1, column 1
        -
        - Row 1, column 3
      * - Row 2, column 1
        - Row 2, column 2
        - Row 2, column 3

  .. list-table::
    :header-rows: 1
    :class: font-size-85
    :width: 60%

    * - Heading row 1, column 1
      - Heading row 1, column 2
      - Heading row 1, column 3
    * - Row 1, column 1
      -
      - Row 1, column 3
    * - Row 2, column 1
      - Row 2, column 2
      - Row 2, column 3

.. index:: tables; csv

CSV tables
----------

Can also make tables from CSV:

.. container:: compare

  .. code-block:: rst
    :class: code-font-size-90

    .. csv-table::
      :header-rows: 1

      ID,First,Last
      1,James,White
      2,Aliya,Maitez

  .. csv-table::
    :widths: 1 2 3
    :header-rows: 1

    ID,First,Last
    1,James,White
    2,Aliya,Maitez

.. container:: small

  CSV tables can also take a :samp:`:file:` option to read data from file.

.. index:: tables; options

Table options
-------------

========================================== ====================================
Class                                      Meaning
========================================== ====================================
:samp:`.table-not-striped`                 Turn off striping
:samp:`.td-{center,left,right}`            Justify columns (1st stays left)
:samp:`.td-{center,left,right}-all`        Justify all columns
:samp:`.td-center-{center,left,right}-{n}` Justify column #\ *n*
                                           :small-muted:`(can use many times)`
:samp:`.td-padding-{0,1,2,3,4,5}`          0.00, 0.25, 0.50, 0.75, 1.00, 1.25em
========================================== ====================================

.. newslide::

For example, combining options to make a grid:

.. container:: compare

  .. code-block:: rst

    .. table::
      :class: table-unstriped td-padding-3
        td-center-all

      == == ==
      A  B  C
      D  E  F
      G  H  I
      == == ==

  .. table::
    :class: table-unstriped td-padding-3 td-center-all

    == == ==
    A  B  C
    D  E  F
    G  H  I
    == == ==


Code blocks
===========

.. index::
  pair: languages; css
  pair: languages; docker
  pair: languages; html+jinja
  pair: languages; html
  pair: languages; http
  pair: languages; ini
  pair: languages; jinja
  pair: languages; js
  pair: languages; javascript
  pair: languages; json
  pair: languages; jsx
  pair: languages; markdown
  pair: languages; postgresql
  pair: languages; python
  pair: languages; text
  pair: languages; toml
  pair: languages; ts
  pair: languages; typescript
  pair: languages; yaml
  pair: languages; zsh

Languages we use
----------------

.. hlist::
  :columns: 5

  - `css`
  - `docker`
  - `html+jinja`
  - `html`
  - `http`
  - `ini`
  - `js`
  - `json`
  - `jsx`
  - `markdown`
  - `postgresql`
  - `python`
  - `text`
  - `toml` `(markup)`:small-muted:
  - `ts` `(TypeScript)`:small-muted:
  - `yaml`
  - `zsh`

.. container:: small

  Full list at `Pygments Lexers <https://pygments.org/docs/lexers/>`_

.. versionchanged:: 2.0

  Added preference for `html+jina`, `json`, and `postgresql` over
  `html` (for Jinja2), `js`, and `sql` for those types, as they get more of the
  syntax properly highlighted.

Basic blocks
------------

.. index::
  single: code-block
  pair: code-block; directive
  pair: code-block; emphasize lines
  pair: code-block; line numbers

.. container:: compare

  .. code-block:: rst

    .. code-block:: python
      :emphasize-lines: 1,6
      :caption: my_file.py
      :linenos:

      """Math library."""

      def add(x: int, y: int):
          """Add together x and y."""

          return x + y

  .. code-block:: python
    :emphasize-lines: 1,6
    :caption: my_file.py
    :linenos:

    """Math library."""

    def add(x: int, y: int):
        """Add together x and y."""

        return x + y

.. index::
  pair: literalinclude; directive

Including from other files
--------------------------

.. container:: compare

  .. code-block:: rst

    .. literalinclude:: include.py
      :language: python
      :caption: *(empty becomes path)*
      :lines: 1, 3-4

  .. literalinclude:: include.py
    :language: python
    :caption:
    :lines: 1, 3-4

.. newslide::

.. index::
  pair: code-block; py-object

**Python:** can include by name:

.. container:: compare

  .. code-block:: rst

    .. literalinclude:: include.py
      :language: python
      :pyobject: Cat

  .. literalinclude:: include.py
    :language: python
    :pyobject: Cat

.. newslide::

**All languages:** can include by matching lines:

.. index::
  pair: code-block; start-at
  pair: code-block; end-at

.. container:: compare

  .. code-block:: rst

    .. literalinclude:: start-at.js
      :language: js
      :start-at: gameOver
      :end-at: }

  .. literalinclude:: start-at.js
    :language: js
    :start-at: gameOver
    :end-at: }

.. newslide::

.. index::
  pair: code-block; indent
  pair: code-block; dedent

Can fix indentation:

.. container:: compare

  .. code-block:: rst

    .. literalinclude:: start-at.js
      :language: js
      :start-at: gameOver
      :end-at: }
      :dedent: 2

  .. literalinclude:: start-at.js
    :language: js
    :start-at: gameOver
    :end-at: }
    :dedent: 2

.. index::
  pair: code-block; start-after
  pair: code-block; end-after

.. tip:: Matching hard-to-match parts of the code with comment markers

  .. literalinclude:: start-after.js
    :language: js
    :class: code-cols-40

  .. container:: compare

    .. code-block:: rst
      :class: code-cols-40

      .. literalinclude:: start-after.js
        :language: js
        :start-after: //>
        :end-before: //<

    .. literalinclude:: start-after.js
      :class: code-cols-35
      :language: js
      :start-after: //>
      :end-before: //<

  .. versionchanged:: Add specific recommendation for start/end markers:
    ``<`` and ``>``.

.. index:: code-block; code-wrong

Marking wrong code
------------------

.. container:: compare

  .. code-block:: rst

    .. code-block:: js
      :class: code-wrong

      const x = 1;
      x = x + 10;

  .. code-block:: js
    :class: code-wrong

    const x = 1;
    x = x + 10;

.. versionadded:: 2.0 Add marking wrong code.


Console displays
================

.. index::
  single: console
  pair: languages; console
  pair: languages; pycon
  pair: languages; pytb
  pair: languages; psql
  pair: languages; node

Use ``code-block`` with a "console" language:

.. hlist::
  :columns: 2

  - `simple-console`: shell
  - `pycon`: Python console
  - `pytb`: Python tracebacks
  - `psql`: PostgreSQL prompt
  - `node`: NodeJS :small-muted:`(planned in the works!)`

Then add a `console` class to make it look like a console:

.. container:: compare

    .. code-block:: rst

        .. code-block:: simple-console
            :class: console

            $ python -m venv venv
            (venv) $ pip install -r reqs.txt
            # Lots of output here ...
            Installed foo==1.0 bar==2.0

    .. code-block:: simple-console
        :class: console

        $ python -m venv venv
        (venv) $ pip install -r reqs.txt
        # Lots of output here ...
        Installed foo==1.0 bar==2.0


Parsed literals
===============

.. index:: parsed-literal, line art

To make line art or markup monospaced text, use ``parsed-literal``.

.. container:: compare

  .. code-block:: rst
    :class: code-fit-content code-font-size-80

    .. parsed-literal::

               **n: []**  *base*    ⭣0
               `──────────────────`:red:
             **n: [1]**     3 + ⭡[] ⭣3
             `──────────────────────`:green:
           **n: [2,3]**      2 + ⭡[3] ⭣5
           `──────────────────────────`:blue:
         **n: [1,2,3]**     1 + ⭡[2,3] ⭣6
         `──────────────────────────────`:pink:
       **add([1,2,3])**              ⭡[1,2,3]
       ──────────────────────────────────

  .. parsed-literal::
     :class: code-fit-content code-font-size-80

             **n: []**  *base*    ⭣0
             `──────────────────`:red:
           **n: [1]**     3 + ⭡[] ⭣3
           `──────────────────────`:green:
         **n: [2,3]**      2 + ⭡[3] ⭣5
         `──────────────────────────`:blue:
       **n: [1,2,3]**     1 + ⭡[2,3] ⭣6
       `──────────────────────────────`:pink:
     **add([1,2,3])**              ⭡[1,2,3]
     ──────────────────────────────────


Compare side-by-side blocks
===========================

.. index:: side-by-side; compare

.. code-block:: rst

  .. container:: compare

    .. code-block:: python

      if x == 7:
          print("hi")

    .. code-block:: js

      if (x === 7) {
        print("hi");
      }

will create:

.. container:: compare

  .. code-block:: python

    if x == 7:
        print("hi")

  .. code-block:: js

    if (x === 7) {
      print("hi");
    }

.. seealso:: Other side-by-side effects

  See `utility_classes`:ref: for useful classes to control width of blocks.

  For only-on-slides side-by-side of lists, see `putting_lists_side_by_side`:ref:


Admonitions
===========

.. index::
  triple: directive; admonitions; important
  triple: directive; admonitions; attention
  triple: directive; admonitions; caution
  triple: directive; admonitions; warning
  triple: directive; admonitions; error
  triple: directive; admonitions; danger
  triple: directive; admonitions; seealso
  triple: directive; admonitions; hint
  triple: directive; admonitions; tip
  triple: directive; admonitions; note
  triple: directive; admonitions; admonition
  triple: directive; admonitions; todo

.. container:: compare

  .. code-block:: rst
    :class: code-fit-content

    .. important:: Stop & get code review

    .. attention:: Check for errors

    .. caution:: Doesn't always work

    .. warning:: Might crash computer

    .. error:: Can't change a constant!

    .. danger:: Grue ahead!

    .. seealso:: Compare this to Python

    .. hint:: There's an O(n) solution

    .. tip:: Add to :file:`{HOME}/.gitignore`

    .. note:: Diving into the details

      All can take text, including notes.

    .. admonition:: Your Label

      These are the most generic.

  .. container::

    .. important:: Stop & get code review

    .. attention:: Check for errors

    .. caution:: Doesn't always work

    .. warning:: Might crash computer

    .. error:: Can't change a constant!

    .. danger:: Grue ahead!

    .. seealso:: Compare this to Python

    .. hint:: There's an O(n) solution

    .. tip:: Add to :file:`{HOME}/.gitignore`

    .. note:: Diving into the details

      All can take text, including notes.

    .. admonition:: Your Label

      These are the most generic.

.. newslide::

None of these appear in slides, unless you add a `class` of :samp:`revealjs`:

.. container:: compare

  .. code-block:: rst

    .. note:: This appears on slides, too

      Along with details.

  .. container::

    .. note:: This appears on slides, too
      :class: revealjs

      Along with details.

.. versionadded:: 2.0 Almost all admonitions are new.

Todo
----

.. container:: compare

  .. code-block:: rst
    :class: code-fit-content

    .. todo:: Fix complex example

  .. container::

    .. todo:: Fix complex example

These only appear if ``todo_include_todos`` is set to true in :file:`conf.py`.


Topics
======

.. index::
  pair: topic; directive

These are for handout notes where there is a side-story:


.. topic:: The history of React
  :class: width-45 float-right

  React was invented in 1962 by Walt Disney, decades before
  JavaScript was invented.

.. code-block:: rst
  :class: float-left code-cols-35

  .. topic:: The history of React

    React was invented in 1962 by
    Walt Disney, decades before
    JavaScript was invented.

.. container:: float-clear

  .. need this to clear that float (couldn't use compare blocks because
    you can't put a topic in a container!


Sidebars
========

.. index::
  pair: sidebar; directive
  pair: side-by-side; sidebar

For handouts side material or discussion of code to the right:

.. code-block:: rst
  :class: code-cols-50 code-font-size-80

  .. sidebar:: Notice this!

    There's something
    cool here. (Notice this is
    before the main thing).

  .. code-block:: js

    if (x === 7) {
      console.log("hey");
    }

.. sidebar:: Notice this!

    There's something
    cool here. (Notice this is
    before the main thing).

.. code-block:: js
  :class: code-cols-45

  if (x === 7) {
    console.log("hey");
  }

By default, sidebars are 30% wide --- |br|
can change with :samp:`.sidebar-{n}`, where *n* is 20-80.


Hover reveal
============

.. index::
  single: hover-reveal
  single: hint, hover-reveal

.. container:: compare

  .. code-block:: rst

    Want to know a secret?

    .. container:: hover-reveal

      Put your message here :)

  .. container::

    Want to know a secret?

    .. container:: hover-reveal

      Joel voted for Hillary Clinton in 2016.

To use with code, use `code-hover-reveal`:

.. container:: compare

  .. code-block:: rst

    Stuck on our problem?

    .. code-block:: js
      :code: code-hover-reveal

      if (x === 7) { }

  .. container::

    Stuck on our problem?

    .. code-block:: js
      :class: code-hover-reveal

      if (x === 7) { }

.. versionchanged:: 2.0 `hover-reveal` class can be added to almost anything.


Quotes
======

.. index:: quote, blockquote

.. container:: compare

  .. code-block:: rst

    To quote, just indent like this:

      This is the blockquote, and can be
      as long as you want

  .. container::

    To quote, just indent like this:

      This is the blockquote, and can be
      as long as you want

.. newslide::

.. index:: quote; epigraph

That's best when you're quoting ordinary text. |br|
For a quote that is intended as an epigraph to open a section:

.. container:: compare

  .. code-block:: rst

    Before quote.

    .. epigraph::

      Who run the world? Girls.

      -- Beyoncé

  .. container::

    Before quote.

    .. epigraph::

      Who run the world? Girls.

      -- Beyoncé

.. newslide::

.. index:: quote; pull-quote

For more dramatic presentation, useful for running an inspirational quote:

.. container:: compare

  .. code-block:: rst

    Before quote.

    .. pull-quote::

      Who run the world? Girls.

      -- Beyoncé

  .. container::

    Before quote.

    .. pull-quote::

      Who run the world? Girls.

      -- Beyoncé

Fragments
=========

(most of these have no effect except on slides)

.. container:: compare

  .. code-block:: rst

    .. container:: one-incremental

      - Everything appears at once.
      - Both at once.

    .. container:: item-incremental

      - Each block appears separately.

        - Can be used on most things

      - Lists, tables, etc

    .. container:: nest-incremental

      - Just for lists (bullets/#s)
      - Or for definition lists

        - This appears separately

  .. container::

    .. container:: one-incremental

      - Everything appears at once.
      - Both at once.

    .. container:: item-incremental

      - Each block appears separately.

        - Can be used on most things

      - Lists, tables, etc

    .. container:: nest-incremental

      - Just for lists (bullets/#s)
      - Or for definition lists

        - This appears separately

Incremental transitions
-----------------------

You can add any of these classes:

.. hlist::
  :columns: 2

  - :incremental-li-fade-up:`fade-up`
  - :incremental-li-fade-down:`fade-down`
  - :incremental-li-fade-left:`fade-left`
  - :incremental-li-fade-right:`fade-right`
  - :incremental-li-fade-out:`fade-out`
  - :incremental-li-semi-fade-out:`semi-fade-out`
  - :incremental-li-fade-in-then-out:`fade-in-then-out`
  - :incremental-li-fade-in-then-semi-out:`fade-in-then-semi-out`
  - :incremental-li-strike:`strike`
  - :incremental-li-highlight-red:`highlight-red`
  - :incremental-li-highlight-current-red:`highlight-current-red`
  - :incremental-li-highlight-blue:`highlight-blue`
  - :incremental-li-highlight-current-blue:`highlight-current-blue`
  - :incremental-li-highlight-green:`highlight-green`
  - :incremental-li-highlight-current-green:`highlight-current-green`

.. newslide::

These are more dramatic, and work best on paragraphs/containers:

.. container:: compare

  .. code-block:: rst

    .. container:: one-incremental grow

      `grow`

    .. container:: one-incremental shrink

      `shrink`

    .. container:: one-incremental zoom

      `zoom`

  .. container::

    .. container:: one-incremental grow

      `grow`

    .. container:: one-incremental shrink

      `shrink`

    .. container:: one-incremental zoom

      `zoom`

Individual incremental elements
-------------------------------

.. code-block:: rst

  - When you have a list
  - :incremental-li:`Can make only this one incremental`
  - :incremental-li-fade-out:`Or this, and use a transition`

  Can add to :incremental:`any inline text`, including
  :incremental-highlight-blue:`special transition forms`.


Images
======

.. container:: compare

  .. code-block::

    .. image:: porcupine.jpg
      :width: 7em
      :class: border noprint

  .. container::

    .. image:: porcupine.jpg
      :width: 7em
      :class: border noprint

Images can be given a caption:

.. container:: compare

  .. code-block::

    .. figure:: porcupine.jpg
      :width: 7em

      *Hystrix cristata* in native
      environment.

  .. figure:: porcupine.jpg
    :width: 7em

    *Hystrix cristata* in native environment.

Diagrams
========

.. contents::
  :local:

Graphviz
--------

.. container:: compare

  .. code-block:: rst

    .. digraph::
      :caption: My caption
      :size: 3,3

      graph [rankdir=LR]
      a -> { b c1 }

    .. graph::
      :caption: My caption
      :size: 3,3

      graph [rankdir=LR]
      a -- { b c2 }

  .. container::

    .. digraph::
      :caption: My caption
      :size: 3,3

      graph [rankdir=LR]
      a -> { b c1 }

    .. graph::
      :caption: My caption
      :size: 3,3

      graph [rankdir=LR]
      a -- { b c2 }

.. newslide::

The ``graphviz`` directive  can take a file:

.. container:: compare

  .. container::

    .. code-block:: dot
      :caption: file.dot

      digraph {
        graph [rankdir=LR]
        a -> { b c3 }
      }

    .. code-block:: rst
      :caption: index.rst

      .. graphviz:: file.dot
        :size: 4,4

  .. container::

    .. graphviz::
      :size: 4,4

      digraph {
        graph [rankdir=LR]
        a -> { b c3 }
      }

`See examples of Graphviz
<https://graphviz.readthedocs.io/en/stable/examples.html>`_

.. versionchanged:: 2.0 Moved to standard Sphinx `graph`, `digraph`, `graphviz`

AAFig (line drawing)
--------------------

.. container:: compare

  .. code-block:: rst
    :class: code-font-size-80

    .. aafig::
      :scale: 90

      +-----------+
      |     |  |XX|
      |     |  |XX|
      |     |--+--|
      |     |  |  |
      |     |  |  |
      |-----+-----|
      |XX|  |     |
      |XX|  |     |
      |--+--|     |
      |  |  |     |
      |  |  |     |
      +-----------+

  .. aafig::
    :scale: 90

    +-----------+
    |     |  |XX|
    |     |  |XX|
    |     |--+--|
    |     |  |  |
    |     |  |  |
    |-----+-----|
    |XX|  |     |
    |XX|  |     |
    |--+--|     |
    |  |  |     |
    |  |  |     |
    +-----------+

.. versionadded:: 2.0 Added `aafigure`:program: diagrams.

Matplotlib
----------

.. container:: compare

  .. code-block:: rst
    :class: code-font-size-90 code-fit-content

    .. plot::
      :width: 15em

      import numpy as np
      import matplotlib.pyplot as plt

      x = np.arange(0, 100000, 5000)
      plt.plot(x, x / 1000, 'bo')
      plt.ylabel('time', fontsize=20)
      plt.xlabel('size of list', fontsize=20)
      plt.xticks([])
      plt.yticks([])
      plt.title('pop()', fontsize=35)

  .. plot::
    :width: 15em

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
----

.. container:: compare

  .. code-block:: rst
    :class: code-font-size-70 code-cols-50

    .. math::

      r = \frac{\sum^n_{i=1}(x_i -
        \bar{x})(y_i - \bar{y})}{\sqrt{\Sigma^n_{i=1}
        (x_i - \bar{x})^2 \times \Sigma^n_{i=1}
        (y_i - \bar{y})^2}}

  .. math::

    r = \frac{\sum^n_{i=1}(x_i -
      \bar{x})(y_i - \bar{y})}{\sqrt{\Sigma^n_{i=1}
      (x_i - \bar{x})^2 \times \Sigma^n_{i=1}
      (y_i - \bar{y})^2}}


Or ``:math:`` like `n = {x}^2`:math: for inline.


Mermaid diagrams
----------------

.. code-block:: rst
  :class: code-fit-content code-font-size-90

  .. mermaid::
    :alt: timeline

    gantt
      title The Rithm of your life
      dateFormat  YYYY-MM-DD

      section Core
      Web tech     :2020-11-02, 2w
      Python & dbs :3w

      *(see source for full text)*

.. newslide::

.. container:: print-width-120

  .. mermaid::
    :alt: timeline

    gantt
      title The Rithm of your life
      dateFormat  YYYY-MM-DD
      axisFormat %b %e

      section Core Curriculum
      Web tech                   :2020-11-02, 2w
      Python & databases         :3w
      Node/Express               :2w
      React                      :3w

      section DS/Algs
      DSA                        :dsa, 2021-01-01, 1w

      section Company Projs
      Company Projects           :3w

      section Outcomes
      Intro                      :active, after dsa, 3w
      Tech                       :1w
      Search                     :1w

      section Advising
      Advising                   :active, 2020-11-02,2021-02-14

      section Breaks
      Thanksgiving Break         :done, 2020-11-20, 1w
      Holiday                    :done, 2020-12-20, 2w

|

.. newslide::

.. container:: compare

  .. code-block:: rst
    :class: code-fit-content code-font-size-80 width-40

    .. mermaid::

      sequenceDiagram
        participant Browser
        participant Flask
        participant Postgres
        Browser->>Flask: GET / HTTP/1.1
        Flask->>Postgres: SELECT * FROM cats
        Postgres-->>Flask: [cat1, cat2]
        Flask-->>Browser: <html>...</html>

  .. container::  width-60

    .. mermaid::

      sequenceDiagram
        participant Browser
        participant Flask
        participant Postgres
        Browser->>Flask: GET / HTTP/1.1
        Flask->>Postgres: SELECT * FROM cats
        Postgres-->>Flask: [cat1, cat2]
        Flask-->>Browser: <html>...</html>

.. versionadded:: 2.0 Added Mermaid diagrams.

Diagrams
--------

.. container:: compare

  .. code-block:: rst
    :class:  code-cols-52 code-font-size-85

    .. diagram::
      :width: 10em

      from diagrams.onprem.client import User
      from diagrams.onprem.database import PostgreSQL
      from diagrams.programming.framework import Flask

      with Diagram(direction="LR"):
          User() >> [
              Flask(),
              Flask(),
              Flask(),
          ] >> PostgreSQL()

  .. diagram::
    :width: 10em

    from diagrams.onprem.client import User
    from diagrams.onprem.database import PostgreSQL
    from diagrams.programming.framework import Flask

    with Diagram(direction="LR"):
        User() >> [
            Flask(),
            Flask(),
            Flask(),
        ] >> PostgreSQL()

Draw.io
-------

.. container:: compare

  .. code-block:: rst
    :class: code-fit-content code-font-size-85

    .. drawio-image:: sql.drawio

    also:

    .. drawio-figure:: other.drawio

      This can now have a caption

  .. container::  width-50

    .. drawio-image:: sql.drawio
      :width: 100%

.. versionadded:: 2.0 Added `draw.io`:program: diagrams.


Footnotes
=========

.. container:: compare

  .. code-block:: rst

    Lorem ipsum [#f1]_ dolor sit amet ...
    [#f2]_

    .. rubric:: Footnotes

    .. [#f1] Text of the first footnote.
    .. [#f2] Text of the second footnote.

  .. container::

    Lorem ipsum [#ff1]_ dolor sit amet ... [#ff2]_

    .. rubric:: Footnotes

    .. [#ff1] Text of the first footnote.
    .. [#ff2] Text of the second footnote.

Citations
---------

.. container:: compare

  .. code-block:: rst

    Lorem ipsum [Ref]_ dolor sit amet.

    .. [Ref] Book ref, URL or whatever.

  .. container::

    Lorem ipsum [Rf]_ dolor sit amet.

    .. [Rf] Book ref, URL or whatever.


Controlling styling
===================

.. _utility_classes:

.. table:: Glide utility classes

  =================================== ======================================================
  Class                               Description
  =================================== ======================================================
  `.width-{percent}`:samp:            Block width ``5-100 by 5s``
  `.float-{side}`:samp:               Float block: `left` or `right`
  `.float-clear`:samp:                Clear above float
  `.text-align-{just}`:samp:          Align text `left`, `right`, `center`, `justify`
  `.align-{just}`:samp:               Align box `left`, `right`, `center`
  `.border`:samp:                     Add border
  `.border-none`:samp:                Remove default border
  `.line-height-{height}`:samp:       Text line height: ``10..20``
  `.code-line-height-{height}`:samp:  Code block text line height: ``10..20``
  `.padding-{n}`:samp:                Padding from ``0..5``
  `.code-padding-{n}`:samp:           Code block padding from ``0..5``
  `.margin-{dir}-{n}`:samp:           Margin `top`, `left`, `right`, `bottom` from ``0..5``
  `.font-size-{n}`:samp:              Font size as percentage: ``25..200 by 5s``
  `.code-font-size-{n}`:samp:         Code block font size as percentage: ``25..200 by 5s``
  `.code-cols-{n}`:samp:              Number of columns in code block, ``1..120``
  `.code-fit-content`:samp:           Auto-size number of columns in code block
  `.display-none`:samp:               Do not display element
  `.font-cursive`:samp:               Cursive font
  =================================== ======================================================


Showing and hiding
==================

Only
----

.. code-block:: rst

  .. only:: revealjs

    This only appears on slides

  .. only:: not revealjs

    This does not appear on slides.

Don't use `only:: handouts`:samp: --- since we have other possible
non-slide formats (LaTeX, epub, et al). Always say `only:: not revealjs`:samp:.

ifconfig
--------

.. code-block:: rst

  .. ifconfig:: 1 + 1 == 2

    Math works!

  .. ifconfig:: 1 + 1 == 3

    Ut Oh.

  .. ifconfig:: version == "2.0"

    You can refer to variables in the `conf.py`:file:.


Force building to fail
======================

.. code-block:: rst

  .. fail::

    This exercise is hopelessly borked. Don't use.

This prevents the document from being built |br|
until that directive is removed.

.. versionadded:: 2.0 Add `fail` directive.


Speaker Notes
=============

Add speaker notes; can find these with :kbd:`s` in slides.

.. container::

  .. code-block:: rst

    .. speaker::

      Example speaker note.

  .. speaker::

    Example speaker note.

Document metadata
=================

Adding HTML meta tags
---------------------

.. container::

  .. code-block:: rst

    .. meta::
      :description: Overview of OO
      :keywords: class, instance, oo

  .. code-block:: html

    <meta name="description"
      content="Overview of OO">
    <meta name="keywords"
      content="class, instance, oo">

Marking authors of sections
---------------------------

.. container::

  .. code-block:: rst

    .. codeauthor:: Joel Burton

    .. sectionauthor:: Joel Burton

  .. container::

    (Doesn't appear in output, but is useful metadata for source readers)

===========
Using Glide
===========

Running Glide
=============

.. table:: Glide builder commands

  ================ =====================================================
  Builder          Description
  ================ =====================================================
  `handouts`       Makes presentation handouts.
  `revealjs`       Makes RevealJS slides.
  `linktest`       Reports on link status in document
  `text`           Makes single-file plaintext file
  `changes`        Makes page showing version changes
  ================ =====================================================

.. versionadded:: 2.0 Add `text` and `changes` builders

.. newslide::

.. table:: Glide secondary commands

  ================== =====================================================
  Builder            Description
  ================== =====================================================
  `handouts-open`    Makes handouts and opens in browser
  `revealjs-open`    Makes slides and opens in browser
  `watch-revealjs`   Makes slides and continually refreshes in browser
  `watch-handouts`   Makes handouts and continually refreshes in browser
  `zip`              Makes `zip`:file: file of code or demo
  `soln`             For assessment, makes solution `zip`:file:
  `upload`           Upload everything needed to server
  `prince`           Make print-ready PDF *(requires Prince)*
  ================== =====================================================

Link checking
=============

.. code-block:: simple-console
  :class: console

  $ make linkcheck
  (line  317) broken    None -
  (line 1602) ok        https://graphviz.readthedocs.io/en/stable/examples.html
  (line  332) ok        https://twemoji.twitter.com/
  (line  852) ok        https://pygments.org/docs/lexers/
  (line  403) ok        https://tachyons.io/docs/themes/skins/

Customizing build
=================

.. code-block:: simple-console
  :class: console

  $ make builder SPHINXOPTS="[options]"

.. table:: Useful `SPHINXOPTS`

  ======================= =====================================================
  ``-a``                  Write all files *(default: only new and changed)*
  ``--keep-going``        Continue building even if an error happens
  ``-D setting=value``    Override setting in config files
  ``-A name=value``       Pass a value into HTML templates
  ``-t``                  Pass tag into; can be used in ``only`` directive
  ``-v``                  Increase verbosity
  ``-q``                  Quiet: no output other than warnings
  ======================= =====================================================

.. hint:: Example of re-styling

  .. code-block:: simple-console
    :class: console

    $ make revealjs SPHINXOPTS="-A theme_clientcolor=purple
    >   -A theme_sidebarcolor=rgb(255,238,255) -D version='Rithm at Night'"

.. only:: not revealjs

  ===================
  Index and endmatter
  ===================

  `Concept index <./genindex.html>`_

  Support for the authorship of this document was kindly provided by Rithm School
  and Oxfam International.

