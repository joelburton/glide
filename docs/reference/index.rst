===============
Glide Reference
===============

.. todo:: nodejsrepl

.. todo:: list-tight




.. sectionauthor:: joel

.. meta::
    :description: Reference to Glide document system.


.. only:: not revealjs

  :author: Joel Burton <joel@joelburton.com>
  :version: |version|
  :updated: |date|

  .. container:: noprint

    You may find it useful to review the source of this document while reading it:
    :download:`index.rst`.

.. topic:: :emoji-2x:`‼️` New/Changed in v2.6

  - Added :ref:`Iframes in interslides <interslide>`

  - While it's not a new feature, added :ref:`no-target-created <no-target-links>` links to these docs

  - Added ``:err:`` and ``:type:`` :ref:`Glide roles <glide-roles>`

  - Add :ref:`inline code highlighting <inline-code>`

  - Added :ref:`nonbreaking spaces <glide-func>`: ``|sp|``

  - Add ``:emoji:`` :ref:`1.5, 4, 6, and 7 sizes <emoji>`

  - Added `.table-paras` to :ref:`add paragraph margins in tables <table-options>`

  - Lots of :ref:`code languages <languages>` added.

  - Added :ref:`styling highlights <styling-highlights>`

  - Added :ref:`styling comments <styling-comments>`

  - Restored :ref:`Mermaid diagrams <mermaid>`

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


Introducing sections
--------------------

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

.. _interslide:

Interslide
----------

.. code-block:: rst

  .. interslide::

    Oh no!

Interslides never appear on the handouts and don't have a title. |br|
They're useful for fun, silly things, like large images and text. |br|
Can take a background or color, like ``newslide``.

You can also have a navigable web page as an iframe for your background.
The class `iframe-popup-light` shows a short message floating on top of
the iframe (black text on white box, in this case, but there's also
`iframe-popup-dark`).

.. code-block:: rst

  .. interslide::
    :iframe: https://www.typescriptlang.org/

    .. container:: iframe-popup-light

      :emoji:`😻` It has awesome docs!

.. attention:: Notice the content of interslide is inside the interslide.

.. versionadded: 2.6

  Added iframe interslides.

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

.. _no-target-links:

.. tip:: No-target links

  The example above creates a reference, `Google`, which can be used elsewhere in the document
  to jump to the same link, by using :py:`_Google` in running text.

  This does mean if you use the same link text for two different links,
  you'll get an error:

  .. code-block:: rst
    :class: code-wrong

    `here <http://google.com>`_ or `here <http://bing.com>`_

  If you don't need/want internal links or often use casual link-captions
  (like "here" in this example), just end your link with two underscores,
  and it won't create an internal target or care about duplication:

  .. code-block:: rst
    :class: code-good

    `here <http://google.com>`__ or `here <http://bing.com>`__

  .. versionadded:: 2.6

    While it's not a new feature, added no-target-created links to these docs.



.. index:: roles


Roles
=====

.. code-block:: rst

  Roles can be used as :role:`Text` or :role:`Text`

  :code:`Code` can use shortcut ``Code``

  :title:`Title` can use shortcut `Title`

.. _role-as-prefix:

.. important:: Please use role as prefix, not suffix

  While it's valid to put the role name at the end, like
  :rst:`\:rolename:`text\``, many editors won't highlight that.
  :rst:`\`text\`:rolename:rolename:`, many editors won't highlight that.
  To help others, please always use the prefix form:
  :rst:`\`text\``.

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

  ==================== =============================== ==================================
  Name                 Example                         Meaning
  ==================== =============================== ==================================
  ``:abbr:``           :abbr:`XY (x and y)`            Abbreviation, put definition in ()
  ``:code:``           :code:`x = 1`                   Code *snippets*
  ``:command:``        :command:`rm -rf`               Executable command
  ``:dfn:``            is a :dfn:`closure`             Mark when term first defined
  ``:envvar:``         :envvar:`FLASK_ENV`             Environmental variable
  ``:file:``           :file:`python-{x}`              Filename, can have ``{var}`` in it
  ``:guilabel:``       :guilabel:`Save`                GUI button/window
  ``:kbd:``            :kbd:`⌘-s` :kbd:`⇧S`            Keyboard sequence
  ``:math:``           :math:`n = {x}^2`               Inlined MathTex
  ``:menuselection:``  :menuselection:`File --> Open`  Menu choice
  ``:mimetype:``       :mimetype:`text/html`           MIME type
  ``:program:``        :program:`Insomnia`             Program
  ``:samp:``           :samp:`text {x}`                Output/sample (can have ``{var}``)
  ``:sub:``            n log\ :sub:`2`\ n              Subscript
  ``:sup:``            x\ :sup:`2`                     Superscript
  ``:title:``          `var` or `func()`               General title, code *names*
  ==================== =============================== ==================================

.. newslide::

.. index::
  pair: doc; role
  pair: download; role
  pair: ref; role

.. table:: Standard sphinx roles for linking

  ==================== ===================== ==================================
  Name                 Example               Meaning
  ==================== ===================== ==================================
  ``:doc:``            :doc:`index`          Link to RST document
  ``:download:``       :download:`file <f>`  Puts file in build, links to it
  ``:ref:``            :ref:`colors`         Internal link in document
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


.. _glide-roles:

.. table:: Glide roles

  ==================== ===================== ==================================
  Name                 Example               Meaning
  ==================== ===================== ==================================
  ``:small:``          :small:`Legal text`   Make smaller
  ``:small-muted:``    :small-muted:`Shhhh`  Smaller *and* muted
  ``:muted:``          :muted:`Quiet`        Muted (lighter colored)
  ``:danger:``         :danger:`Oh no`       Danger semantic color
  ``:warning:``        :warning:`Achtung!`   Warning semantic color
  ``:success:``        :success:`Yay`        Success semantic color
  ``:ins:``            :ins:`New thing`      Insertion/added-in diff
  ``:del:``            :del:`Deleted`        Removed/gone-in-diff
  ``:gone:``           :gone:`Gone`          Mark as moved
  ``:comment:``        :comment:`// see...`  Mark as code-like comment
  ``:wrong:``          :comment:`var x=7`    Wrong way to do it
  ``:err:``            :err:`Crashed!`       Report an error
  ``:type:``           :type:`string[]`      Show as TS or Python type
  ==================== ===================== ==================================

.. versionadded:: 2.6

  Added ``:err:`` and ``:type:``.

For a block of code, use code-blocks_, but for short inline highlighting,
these are useful:

.. _inline-code:

.. table:: Glide roles for code highlights

  ==================== ===================== =====================================
  Name                 Language              Example
  ==================== ===================== =====================================
  ``:py:``             Python                :py:`def x(a): return "hello"`
  ``:js:``             JavaScript            :js:`function x(a) { return "hi" }`
  ``:ts:``             TypeScript            :ts:`let nums: numbers[] = [];`
  ``:sql:``            SQL (generic)         :sql:`SELECT f FROM table`
  ``:postgresql:``     PostgreSQL            :postgresql:`TRUNCATE`
  ``:zsh:``            ZShell                :zsh:`export $MSG="hi"`
  ``:css:``            CSS                   :css:`b { color: rebeccapurple; }`
  ``:html:``           HTML                  :html:`<div id="a">hi</div>`
  ``:jsx:``            JSX                   :jsx:`<Todo id={id} />`
  ``:html+jinja:``     HTML + Jinja          :html+jinja:`<b> {{ name }}</b>`
  ``:json:``           JSON                  :json:`{"a": 1, "b": 2}`
  ``:rb:``             Ruby                  :rb:`print "a = #{a}\n";`
  ``:erb:``            ERB (Ruby)            :erb:`<% if @keys_enable -%>`
  ``:graphql:``        GraphQL               :graphql:`query foo { }`
  ``:psql:``           Postgres console      :psql:`mydb=# SELECT "foo";`
  ``:pycon:``          Python console        :pycon:`>>> def f(): ...`
  ``:rst::``           RST                   :rst:`\`oh so meta\``
  ``:scss:``           SASS                  :scss:`b { i { color: red; } }`
  ==================== ===================== =====================================


.. versionadded:: 2.6

  Add inline code highlighting.


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

.. _glide-func:

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

    Forced |sp| non-breaking-space

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

    Forced |sp| non-breaking-space

.. container:: small

  (``|reveal-br|`` is an alias for ``|br|``.)

.. versionadded:: 2.6 Added ``|sp|``


Variable interpolation
----------------------

.. container:: compare

  .. code-block:: rst
    :class: code-font-size-90 code-fit-content

    - |demo-link| = demo zip file for this
    - |version| = `version` in :file:`conf.py`
    - |release| = `release` in :file:`conf.py`
    - |today| shows day of build

  .. container::

    - |demo-link| shows link to demo for project
    - |version| shows version number in :file:`conf.py`
    - |release| shows release number in :file:`conf.py`
    - |today| shows day of build

At Rithm, `version` becomes the code for our cohorts, eg ``"r15"``.


.. index:: emoji

.. _emoji:

Emoji
=====

Paste in actual emoji symbol (we use `Twemoji <https://twemoji.twitter.com/>`_)

- ``:emoji:``: :emoji:`🌮`

To size:

Size with role :samp:`:emoji-{1,15,2,3,4,5,6,7}:`

- ``:emoji-1x:``: :emoji-1x:`🌮`
- ``:emoji-15x:``: :emoji-15x:`🌮`
- ``:emoji-2x:``: :emoji-2x:`🌮`
- ``:emoji-3x:``: :emoji-3x:`🌮`
- ``:emoji-4x:``: :emoji-4x:`🌮`
- ``:emoji-5x:``: :emoji-5x:`🌮`
- ``:emoji-6x:``: :emoji-6x:`🌮`
- ``:emoji-7x:``: :emoji-7x:`🌮`

.. versionadded:: 2.6

  Add 1.5, 4, 6, and 7 sizes.

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

    - :bg-black:`╳`  black
    - :bg-near-black:`╳`  near-black
    - :bg-dark-gray:`╳`  dark-gray
    - :bg-mid-gray:`╳`  mid-gray
    - :bg-gray:`╳`  gray
    - :bg-silver:`╳`  silver
    - :bg-light-silver:`╳`  light-silver
    - :bg-moon-gray:`╳`  moon-gray
    - :bg-light-gray:`╳`  light-gray
    - :bg-near-white:`╳`  near-white
    - :bg-white:`╳`  white
    - :bg-dark-red:`╳`  dark-red
    - :bg-red:`╳`  red
    - :bg-light-red:`╳`  light-red
    - :bg-orange:`╳`  orange
    - :bg-gold:`╳`  gold
    - :bg-yellow:`╳`  yellow
    - :bg-light-yellow:`╳`  light-yellow
    - :bg-purple:`╳`  purple
    - :bg-light-purple:`╳`  light-purple
    - :bg-dark-pink:`╳`  dark-pink
    - :bg-hot-pink:`╳`  hot-pink
    - :bg-pink:`╳`  pink
    - :bg-light-pink:`╳`  light-pink
    - :bg-dark-green:`╳`  dark-green
    - :bg-green:`╳`  green
    - :bg-light-green:`╳`  light-green
    - :bg-navy:`╳`  navy
    - :bg-dark-blue:`╳`  dark-blue
    - :bg-blue:`╳`  blue
    - :bg-light-blue:`╳`  light-blue
    - :bg-lightest-blue:`╳`  lightest-blue
    - :bg-washed-blue:`╳`  washed-blue
    - :bg-washed-green:`╳`  washed-green
    - :bg-washed-yellow:`╳`  washed-yellow
    - :bg-washed-red:`╳`  washed-red

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

Key/value mappings should be a `field list:file:` table:

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

  CSV tables can also take a :samp:`` option to read data from file.

.. index:: tables; options
.. _table-options:

Table options
-------------

========================================== ====================================
Class                                      Meaning
========================================== ====================================
:samp:`.table-unstriped`                   Turn off striping
:samp:`.td-{center,left,right}`            Justify columns (1st stays left)
:samp:`.td-{center,left,right}-all`        Justify all columns
:samp:`.td-center-{center,left,right}-{n}` Justify column #\ *n*
                                           :small-muted:`(can use many times)`
:samp:`.td-bold-{n}`                       Bold column
:samp:`.td-padding-{0,1,2,3,4,5}`          0.00, 0.25, 0.50, 0.75, 1.00, 1.25em
:samp:`.table-paras`                       Put para w/margins around tds
========================================== ====================================

.. versionadded:: 2.6

  Added `.table-paras`, since now :program:`docutils`
  adds paragraphs inside `td`\ s.


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


.. _code-blocks:

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

.. _languages:

Languages we use
----------------

.. hlist::
  :columns: 3

  - `awk`
  - `c`
  - `css`
  - `django` :small-muted:`(templates)`
  - `docker`
  - `doscon` :small-muted:`(cmd.com)`
  - `erb` :small-muted:`(ruby)`
  - `graphql`
  - `html+jinja`
  - `html`
  - `http`
  - `ini`
  - `irb` :small-muted:`(Ruby)`
  - `js` :muted:`|` `javascript`
  - `json`
  - `jsx`
  - `markdown`
  - `nginx` :small:`(config)`
  - `postgresql`
  - `postgres-explain`
  - `psql` :small-muted:`(console)`
  - `py` :muted:`|` `python`
  - `pycon` :small-muted:`(console)`
  - `pytb` :small-muted:`(traceback)`
  - `rst`
  - `ruby`
  - `scss`
  - `sql` :small-muted:`(generic)`
  - `text`
  - `toml` :small-muted:`(markup)`
  - `ts` :muted:`|` `typescript`
  - `xml`
  - `yaml` :small-muted:`(markup)`
  - `zsh` :muted:`|` `sh` :muted:`|` `bash` :small-muted:`(all same)`

Lexers I'd really like
++++++++++++++++++++++

In case anyone wants to pair and learn how to write a lexer :emoji-1x:`😀`.

.. hlist::
  :columns: 3

  - `jscon` :small-muted:`(JS console)`
  - `tsx` :small-muted:`(ts + jsx)`

.. container:: small

  Full list at `Pygments Lexers <https://pygments.org/docs/lexers/>`_

.. versionchanged:: 2.6

  Lots of languages added.

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

.. _styling-highlights:

Styling highlights
------------------

You can add classes to style emphasized lines:

.. code-block:: rst

  .. code-block:: js
    :class: code-highlight-pop
    :emphasize-lines: 2

    const x = 1;
    x = x + 10;

.. code-block:: js
  :class: code-highlight-pop
  :emphasize-lines: 2

  const x = 1;
  x = x + 10;

.. code-block:: rst

  .. code-block:: js
    :class: code-highlight-good
    :emphasize-lines: 2

    const x = 1;
    x = x + 10;

.. code-block:: js
  :class: code-highlight-good
  :emphasize-lines: 2

  const x = 1;
  x = x + 10;

.. code-block:: rst

  .. code-block:: js
    :class: code-highlight-wrong
    :emphasize-lines: 2

    const x = 1;
    x = x + 10;

.. code-block:: js
  :class: code-highlight-wrong
  :emphasize-lines: 2

  const x = 1;
  x = x + 10;

.. versionadded:: 2.6 Added styling highlights

.. _styling-comments:

Styling Comments
----------------

You can add classes to style comments:

.. code-block:: rst

  .. code-block:: js
    :class: code-comments-pop

    const x = 1;
    // x = x + 10;

.. code-block:: js
  :class: code-comments-pop

  const x = 1;
  // x = x + 10;


.. code-block:: rst

  .. code-block:: js
    :class: code-comments-good

    const x = 1;
    // x = x + 10;

.. code-block:: js
  :class: code-comments-good

  const x = 1;
  // x = x + 10;

.. code-block:: rst

  .. code-block:: js
    :class: code-comments-wrong

    const x = 1;
    // x = x + 10;

.. code-block:: js
  :class: code-comments-wrong

  const x = 1;
  // x = x + 10;

.. versionadded:: 2.6 Added styling comments


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
  - `psql`: PostgreSQL console
  - `doscon`: Windows console
  - `irb`: Ruby console
  - `jscon`: Javascript console :small-muted:`(planned in the works!)`


Then add a `console` class to make it look like a console (rounded borders, etc):

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

  .. code-block:: text
    :class: code-fit-content code-font-size-80

    .. parsed-literal::

               **n: []**  *base*    ⭣0
               :red:`──────────────────`
             **n: [1]**     3 + ⭡[] ⭣3
             :green:`──────────────────────`
           **n: [2,3]**      2 + ⭡[3] ⭣5
           :blue:`──────────────────────────`
         **n: [1,2,3]**     1 + ⭡[2,3] ⭣6
         :pink:`──────────────────────────────`
       **add([1,2,3])**              ⭡[1,2,3]
       ──────────────────────────────────

  .. parsed-literal::
     :class: code-fit-content code-font-size-80

             **n: []**  *base*    ⭣0
             :red:`──────────────────`
           **n: [1]**     3 + ⭡[] ⭣3
           :green:`──────────────────────`
         **n: [2,3]**      2 + ⭡[3] ⭣5
         :blue:`──────────────────────────`
       **n: [1,2,3]**     1 + ⭡[2,3] ⭣6
       :pink:`──────────────────────────────`
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

  See :ref:`utility_classes` for useful classes to control width of blocks.

  For only-on-slides side-by-side of lists, see :ref:`putting_lists_side_by_side`


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


Or :rst:`:math:\`n = {x}^2\`` for inline: :math:`n = {x}^2`

.. _mermaid:

Mermaid
-------

Can make diagrams using `Mermaid JS <https://mermaid.js.org/>`__.

.. tip:: Prefer Graphviz

  These are a bit more finicky, particularly for printing, where they need to
  be turned into PNGs rather than rendered as crisply. They're useful because
  of all the different diagram types that Mermaid makes but, if it's easy to do
  this with Graphviz, you should.

.. code-block:: rst

  .. container:: with-50 mermaid-wrapper  # `mermaid-wrapper is required

    .. mermaid::

      timeline
          w1-2   <br> 1/1-1/14  : JS : Comp Sci Intro : HoS
          w3     <br> 1-15-1/30 : Python : Databases : Auth : 🏃 Warbler
          w6     <br> 2/1-2/14  : Node : Express

.. container:: width-50 mermaid-wrapper

  .. mermaid::

    timeline
        w1-2   <br> 1/1-1/14  : JS : Comp Sci Intro : HoS
        w3     <br> 1-15-1/30 : Python : Databases : Auth : 🏃 Warbler
        w6     <br> 2/1-2/14  : Node : Express


.. versionchanged:: 2.6 Restored.

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
  :samp:`.width-{percent}`            Block width ``5-100 by 5s``
  :samp:`.float-{side}`               Float block: `left` or `right`
  :samp:`.float-clear`                Clear above float
  :samp:`.text-align-{just}`          Align text `left`, `right`, `center`, `justify`
  :samp:`.align-{just}`               Align box `left`, `right`, `center`
  :samp:`.border`                     Add border
  :samp:`.border-none`                Remove default border
  :samp:`.line-height-{height}`       Text line height: ``10..20``
  :samp:`.code-line-height-{height}`  Code block text line height: ``10..20``
  :samp:`.padding-{n}`                Padding from ``0..5``
  :samp:`.code-padding-{n}`           Code block padding from ``0..5``
  :samp:`.margin-{dir}-{n}`           Margin `top`, `left`, `right`, `bottom` from ``0..5``
  :samp:`.font-size-{n}`              Font size as percentage: ``25..200 by 5s``
  :samp:`.code-font-size-{n}`         Code block font size as percentage: ``25..200 by 5s``
  :samp:`.code-cols-{n}`              Number of columns in code block, ``1..120``
  :samp:`.code-fit-content`           Auto-size number of columns in code block
  :samp:`.display-none`               Do not display element
  :samp:`.font-cursive`               Cursive font
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

Don't use :samp:`only:: handouts` --- since we have other possible
non-slide formats (LaTeX, epub, et al). Always say :samp:`only:: not revealjs`.

ifconfig
--------

.. code-block:: rst

  .. ifconfig:: 1 + 1 == 2

    Math works!

  .. ifconfig:: 1 + 1 == 3

    Ut Oh.

  .. ifconfig:: version == "2.0"

    You can refer to variables in the :file:`conf.py`.


Force building to fail
======================

.. code-block:: rst

  .. fail::

    This exercise is hopelessly borked. Don't use.

This prevents the document from being built |br|
until that directive is removed.



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


.. newslide::

.. table:: Glide secondary commands

  ================== =====================================================
  Builder            Description
  ================== =====================================================
  `handouts-open`    Makes handouts and opens in browser
  `revealjs-open`    Makes slides and opens in browser
  `watch-revealjs`   Makes slides and continually refreshes in browser
  `watch-handouts`   Makes handouts and continually refreshes in browser
  `zip`              Makes :file:`zip` file of code or demo
  `soln`             For assessment, makes solution :file:`zip`
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

