====
Test
====

.. nope

   Text here fails. todo


Core Typography
===============

Paragraph
---------

The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog. The quick brown fox
jumped over the lazy dog.

The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog. The quick brown fox
jumped over the lazy dog.

Subheadings
-----------

Heading 4
~~~~~~~~~

This is a heading 4.

Heading 5
+++++++++

This is a heading 5.

Heading 6
@@@@@@@@@

This is a heading 6.

Links
-----

An external link: `Google <http://google.com>`_

An internal link: `Close by <./not-here.html>`_

Email: `joel@joelburton.com <mailto:joel@joelburton.com>`_

Bold and Italics
----------------

I am **bold** and I am `strong`:strong:.

I am *italics* and I am `emphasis`:emphasis:.

(these should be 100% the same)

Cite
----

Cite `made using :title:`:title:

Cite `as default role`

Code ``as code``

Code `as :code:`:code:

Definition List
---------------

Term
  Definition

Another
  Definition

Long Definition List
--------------------

Term
  Definition. The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

Another
  Definition

Definition List Paragraph Defs
------------------------------

Term
  Paragraph definition.

  This is a separate paragraph.

Term
  This does not have separate paragraph.

Miscellaneous Typography
------------------------

This is an em dash: word1---word2 with spaces: word1 --- word2

This is an en dash: word1--word2 with spaces: word1 -- word2

"Curly quotes"

¿Accénted characters?


Roles
=====

.. _sphinx-roles:

Sphinx Roles
------------

.. hlist::
  :columns: 3

  - :abbr:`abbr (with expansion)` / :abbr:`no definition`
  - :command:`command`
  - :dfn:`dfn`
  - :doc:`doc <index>`
  - :download:`download <index.rst>`
  - :envvar:`envvar`
  - :file:`file with {x}`
  - :guilabel:`Guilabel`
  - :kbd:`Kbd-c`
  - :literal:`literal`
  - :mailheader:`Mail-Header`
  - :manpage:`man(1)`
  - :math:`math \pi`
  - :menuselection:`menuselection --> choice`
  - :mimetype:`text/mimetype`
  - :program:`program`
  - :ref:`ref <sphinx-roles>`
  - :regexp:`regexp .*`
  - :samp:`samp with {x}`
  - :term:`term`
  - subscript\ `2`:sub:
  - superscript\ `2`:sup:

.. complain about -- investigate fixme

  - :keyword:`if`
  - :option:`option`
  - :numref:

Glide Added Roles
-----------------

.. hlist::
  :columns: 3

  - :small-muted:`small-muted`
  - :danger:`span.danger`
  - :warning:`span.warning`
  - :success:`span.success`
  - :muted:`span.muted`
  - :red:`red`
  - :green:`green`
  - :orange:`orange`
  - :tan:`tan`
  - :blue:`blue`
  - :cmd:`cmd`
  - :white:`white` (white)
  - :gray:`gray`
  - :comment:`comment`
  - :gone:`gone`
  - :inv-red:`inv-red`
  - :text-heavy:`text-heavy`


.. fixme: kill cmd text-heavy tan

Emoji
-----

Once upon a time, there was an |br|
awesome 🧑‍💻 named Fluffy and she |br|
had a nice laptop.

normal - 2x - 5x - 10x :
`🧑‍💻`:emoji: |sp| `🧑‍💻`:emoji-2x: |sp| `🧑‍💻`:emoji-5x: |sp| `🧑‍💻`:emoji-10x:

Substitutions
-------------

release: |release|

version: |version|

today: |today| (build date, not JS date)

Glide Symbol Substitutions
--------------------------

.. hlist::
  :columns: 3

  - nbsp     word\ |nbsp|\ word
  - rarr     |rarr|
  - larr     |larr|
  - darr     |darr|
  - uarr     |uarr|
  - lrarr    |lrarr|
  - plus     |plus|
  - times    |times|
  - divide   |divide|
  - check    |check|
  - wrong    |wrong|
  - approx   |approx|
  - sub2     |sub2|
  - super2   |super2|
  - spades   |spades|
  - hearts   |hearts|
  - diamonds |diamonds|
  - clubs    |clubs|

.. fixme: kill sub2 and sup2

.. fixme: kill suits bc they're emoji now?

Glide Functional Substitutions
------------------------------

- :raw-reveal:`<input type="checkbox">` (checkbox only for revealjs)
- :raw-handouts:`<input type="checkbox">` (checkbox only for handouts)
- Hello |reveal-br| RevealBR
- Hello |br| BR
- Hello |handouts-br| HandoutsBR
- Hello |all-br| all-br
- Hello |sp| |sp| sp
- |demo-link|

Line Blocks and Lists
=====================

Line Block
----------

| Hello
| These is ok

Add space between me...

|

...snd me. And again, but double:

|
|

Done, now again with spaces between bars

|

|

Too much?

Text Align
----------

Testing this idea

.. container:: text-left

  Hello
  There
  Joel

Works?
------

- | Hello
  | There

- Ok?

.. todo repurpose as replacement for |br| -- these work fine in ul, etc

  - | Hello
    | There

Bulleted Lists: Simple
----------------------

- One

- Two

  - Two A

  - Two B

    - Three

      - Four

Bulleted Lists: Long
--------------------

- One.   The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

- Two

  - Two A

  - Two B

    - Three

      - Four

Bulleted Lists: Not Simple
--------------------------

- One

  Two paras

- Two

  - Two A

  - Two B

    - Three

      - Four

Numbered Lists: Simple
----------------------

#. One.

#. Two

   #. Two A

   #. Two B

      #. Three

         #. Four

Numbered Lists: Long
--------------------

#. One.  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
   the lazy dog. The quick brown fox jumped over the lazy dog.

#. Two

   #. Two A

   #. Two B

      #. Three

         #. Four

Numbered Lists: Not Simple
--------------------------

#. One

   Two paras

#. Two

   #. Two A

   #. Two B

      #. Three

      #. Four

HLists
------

.. hlist::

  - one
  - two
  - three
  - four
  - five

.. hlist::
  :columns: 3

  - one
  - two
  - three
  - four
  - five

Tables
======

Table
-----

=== === ===========
One Two Description
=== === ===========
A   B   Descrip
C   D   Descrip
E   F   Descrip
=== === ===========

Table Unstriped
---------------

.. rst-class:: table-not-striped

=== === ===========
One Two Description
=== === ===========
A   B   Descrip
C   D   Descrip
E   F   Descrip
=== === ===========

Center-Justified Table
----------------------

.. rst-class:: td-center-all

=== === ===========
One Two Description
=== === ===========
A   B   All Right
C   D   Descrip
E   F   Descrip
=== === ===========

|

.. rst-class:: td-center

=== === ===========
One Two Description
=== === ===========
A   B   All But 1st
C   D   Descrip
E   F   Descrip
=== === ===========


Right-Justified Table
---------------------

.. rst-class:: td-right-all

=== === ===========
One Two Description
=== === ===========
A   B   All Right
C   D   Descrip
E   F   Descrip
=== === ===========

|

.. rst-class:: td-right

=== === ===========
One Two Description
=== === ===========
A   B   All But 1st
C   D   Descrip
E   F   Descrip
=== === ===========

Control Alignment Table
-----------------------

right, center, left

.. rst-class:: td-right-1 td-center-2 td-left-3

=== === ===========
One Two Description
=== === ===========
A   B   All Right
C   D   Descrip
E   F   Descrip
=== === ===========

Control Padding
---------------

0 padding then 1em

.. rst-class:: td-padding-0

=== === ===========
One Two Description
=== === ===========
A   B   All Right
C   D   Descrip
E   F   Descrip
=== === ===========

.. rst-class:: td-padding-4

=== === ===========
One Two Description
=== === ===========
A   B   All Right
C   D   Descrip
E   F   Descrip
=== === ===========

Wide Table
----------

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

Field Lists
-----------

Two field lists:

:This is a field: And this is the data
:Also this: And this is the data

.. rst-class:: td-padding-3

:This is a field: And this is the data
:Also this: And this is the data

``Code`` and `Title` in title
-----------------------------

That was a :code: and :title: in title


Code Blocks
===========

Code
----

This is ``code``

Here is long ``The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.``


Code Block
----------

.. code-block:: js

  //3456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_
  "This program needs full default 80 columns"
  function add(x, y) { return x + y; }
  /** Hello world. */

.. code-block:: js

  //3456789_123456789_123456789_123456789_123456789_
  "This program needs full 50 columns"
  function add(x, y) { return x + y; }
  /** Hello world. */

.. code-block:: js
  :emphasize-lines: 2

  //3456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_
  "This program needs full 80 columns"
  function add(x, y) { return x + y; }
  /** Hello world. */

Longest Required Code Block
---------------------------

.. code-block:: python

  # 3456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_
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

Code Block Sizes
----------------

.. code-block:: js
  :class: unsized

  //3456789_123456789_123456789_123456789
  "This program is unsized"
  function add(x, y) { return x + y; }
  /** Hello world. */

.. code-block:: js
  :class: code-50c

  //3456789_123456789_123456789_123456789_123456789_
  "This program is code-50c"
  function add(x, y) { return x + y; }
  /** Hello world. */

.. code-block:: js
  :class: code-100c

  //3456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_
  "This program is code-100c"
  function add(x, y) { return x + y; }
  /** Hello world. */

Code Text Sizes
---------------

.. code-block:: js

  //3456789_123456789_123456789_123456789_123456789_123456789_
  "This program is normal sized"
  function add(x, y) { return x + y; }
  /** Hello world. */

.. code-block:: js
  :class: code-80

  //3456789_123456789_123456789_123456789_123456789_123456789_
  "This program is code-80"
  function add(x, y) { return x + y; }
  /** Hello world. */

.. code-block:: js
  :class: code-120

  //3456789_123456789_123456789_123456789_123456789_123456789_
  "This program is code-120"
  function add(x, y) { return x + y; }
  /** Hello world. */


Line Numbers
------------

.. code-block:: js
  :linenos:

  //3456789_123456789_123456789_123456789_123456789_123456789_
  "This program is normal sized"
  function add(x, y) { return x + y; }
  /** Hello world. */

.. code-block:: js
  :linenos:
  :class: code-120

  //3456789_123456789_123456789_123456789_123456789_123456789_
  "This program is code-120"
  function add(x, y) { return x + y; }
  /** Hello world. */

.. code-block:: js
  :linenos:

  //3456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_
  "This program needs full default 80 columns"
  function add(x, y) { return x + y; }
  /** Hello world. */

Parsed literals
===============

Parsed literals
---------------

Need something RST-y in it else it is handled like code:

.. parsed-literal::

  //3456789_123456789_123456789_123456789_123456789_123456789_123456789_1234567890
  "This program needs full default 80 columns"
  function add(x, y) { return x + y; } `hello`:red:

Line art
--------

.. parsed-literal::
  :class: code-fit-content

  Hello

.. parsed-literal::
   :class: code-fit-content

           **n: []**  *base*    ⭣0
           `──────────────────`:red:
         **n: [1]**     3 + ⭡[] ⭣3
         `──────────────────────`:green:
       **n: [2,3]**      2 + ⭡[3] ⭣5
       `──────────────────────────`:blue:
     **n: [1,2,3]**     1 + ⭡[2,3] ⭣6
     `──────────────────────────────`:tan:
   **add([1,2,3])**              ⭡[1,2,3]
   ──────────────────────────────────

Console
=======

Console
-------

.. code-block:: simple-console
  :class: console

  $ ls
  one
  two      # Notice this!
  three

.. parsed-literal::
  :class: code-fit-content console

  Hello

Admonitions
===========

Don't normally appear for slides
--------------------------------

.. admonition:: Also with more text

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

.. important:: Hungry penguin ahead!


Admonition
----------

"Admonition" is different; it must have a content block

.. admonition:: Also with more text
  :class: revealjs

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.


Important and Attention
-----------------------

.. important:: Hungry penguin ahead!
  :class: revealjs

.. attention:: Also with more text
  :class: revealjs

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

Caution and Warning
-------------------

.. caution:: Hungry penguin ahead!
  :class: revealjs

.. warning:: Also with more text
  :class: revealjs

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

Error and Danger
----------------

.. error:: Hungry penguin ahead!
  :class: revealjs

.. danger:: Also with more text
  :class: revealjs

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

See Also, Hint, Tip
-------------------

.. seealso:: Hungry penguin ahead!
  :class: revealjs

.. hint:: Also with more text
  :class: revealjs

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

.. tip:: Also with more text
  :class: revealjs

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

Note
----

.. note:: Hungry penguin ahead!
  :class: revealjs

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.


Things in These
---------------

.. hint:: Let's try with a code block!
  :class: revealjs

  .. code-block:: js

    //3456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_
    "This program needs full default 80 columns"
    function add(x, y) { return x + y; }
    /** Hello world. */

.. hint:: Let's try with a compare block
  :class: revealjs

  .. container:: compare

    .. code-block:: js

      //3456789_123456789_123456789_123456789
      "This program needs 40 columns"
      function add(x, y) { return x + y; }
      /** Hello world. */

    .. code-block:: js

      //3456789_123456789_123456789_123456789
      "This program needs 40 columns"
      function add(x, y) { return x + y; }
      /** Hello world. */

Topics
======

Topic
-----

(These don't ever appear for slides)

.. topic:: A really interesting story

  There once was this time where a very interesting thing happened.

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

Hover-Reveal
============

Hover-Reveal
------------

Mouse over to see:

.. container:: hover-reveal

  This is some secret text.

Also, this:

.. code-block:: js
  :class: hover-reveal-code

  //3456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_
  "This program needs full default 80 columns"
  function add(x, y) { return x + y; }
  /** Hello world. */

In a Hint
---------

Mouse over to see:

.. hint:: Hover to Reveal
  :class: revealjs

  .. container:: hover-reveal

    This is some secret text.

Also, this:

.. hint:: Hover to Reveal Code
  :class: revealjs

  .. code-block:: js
    :class: hover-reveal-code

    //3456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789_
    "This program needs full default 80 columns"
    function add(x, y) { return x + y; }
    /** Hello world. */

Sidebars
========

.. todo make the width a more general attribute not tied to these

Sidebar hidden from slides
--------------------------

(sidebar shouldn't appear on slides)

.. sidebar:: More about the fox

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.
  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog.

The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.
The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.
The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.

Sidebar on slides
-----------------

.. sidebar:: More about the fox
  :class: revealjs

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.
  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog.

The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.
The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.
The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.


Sidebar 50
----------

.. sidebar:: More about the fox
  :class: revealjs sidebar50

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.
  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog.

The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.
The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.
The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.


Sidebar 45
----------

.. sidebar:: More about the fox
  :class: revealjs sidebar45

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.
  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog.

The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.
The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.
The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.

Sidebar 40
----------

.. sidebar:: More about the fox
  :class: revealjs sidebar40

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.
  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog.

The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.
The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.
The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.

Sidebar Code
------------

.. sidebar:: More about the fox
  :class: revealjs sidebar50

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.
  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog.

.. code-block:: js
  :class: unsized

  //3456789_123456789_123456789_123456789_123456789_
  "This program is code-50c"
  function add(x, y) { return x + y; }
  /** Hello world. */

Utilities
=========

Width
-----

20% paragraph

.. container:: width-20

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog.

Width
-----

100%  and not-set-width paragraphs (should be same)

.. container:: width-100

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog.

The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog.

Border
------

Align text
----------

Float
-----

Line height
-----------

Code line height
----------------

Padding
-------

Margin
------

Fit content
-----------

Font size
---------

Compare blocks
==============

Compare lists
-------------

.. container:: compare

  .. container::

    - one

    - two

    - three

  .. container::

    - one

    - two

    - three

Compare paragraphs
------------------

.. container:: compare

  .. container::

    The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
    the lazy dog. The quick brown fox jumped over the lazy dog.

    The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
    the lazy dog. The quick brown fox jumped over the lazy dog.

  .. container::

    The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
    the lazy dog. The quick brown fox jumped over the lazy dog.

    The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
    the lazy dog. The quick brown fox jumped over the lazy dog.

Compare code
------------

.. container:: compare

  .. code-block:: js

    //3456789_123456789_123456789_123456789_
    "This program needs full 40 columns"
    function add(x, y) { return x + y; }
    /** Hello world. */

  .. code-block:: js

    //3456789_123456789_123456789_123456789_
    "This program needs full 40 columns"
    function add(x, y) { return x + y; }
    /** Hello world. */

Misc
====

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

.. code-block:: rainbow-2-lines

  one
  two
  three
  four
  five
  six
  seven
  eight
  nine
  ten
  eleven
  twelve
  thirteen
  fourteen

.. todo blockquote/epigraph/pull-quote
.. todo float utils
.. todo captions
.. todo page breaks
.. todo editables
.. todo interslide
.. todo newslide
.. todo fragments
.. todo slide transitions
.. todo images
.. todo math

Blockquotes, epigraphs, pull quotes
===================================

Blockquote
----------

.. todo make this left-justified?

The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
the lazy dog. The quick brown fox jumped over the lazy dog.

Tricking into a blockquote
--------------------------

..

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.


Epigraph
--------

Before paragraph

.. epigraph::

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

  -- Joel Burton

After

Pull quote
----------

Before paragraph

.. pull-quote::

  The quick brown fox jumped over the lazy dog. The quick brown fox jumped over
  the lazy dog. The quick brown fox jumped over the lazy dog.

  -- Joel Burton

After

Charts and graphs
=================

Graphviz
--------

.. digraph:: ll
  :size: 6,6

  rankdir=TB

  node [shape=plaintext]
  ll [label=<
    <TABLE BORDER="0"    CELLBORDER="1" CELLPADDING="10" CELLSPACING="0"><TR>
        <TD><B>DLL</B></TD>
        <TD PORT="head"><I>head</I></TD>
        <TD PORT="tail"><I>tail</I></TD>
    </TR></TABLE>>]

  {
  ant [label=<
    <TABLE BORDER="0" CELLBORDER="1" CELLPADDING="7" CELLSPACING="0"><TR>
        <TD PORT="prev"><I>prev</I></TD>
        <TD PORT="data">ant</TD>
        <TD PORT="next"><I>next</I></TD>
    </TR></TABLE>>]
  bee [label=<
    <TABLE BORDER="0" CELLBORDER="1" CELLPADDING="7" CELLSPACING="0"><TR>
        <TD PORT="prev"><I>prev</I></TD>
        <TD PORT="data">bee</TD>
        <TD PORT="next"><I>next</I></TD>
    </TR></TABLE>>]
  caterpillar [label=<
    <TABLE BORDER="0" CELLBORDER="1" CELLPADDING="7" CELLSPACING="0"><TR>
        <TD PORT="prev"><I>prev</I></TD>
        <TD PORT="data">caterpillar</TD>
        <TD PORT="next"><I>next</I></TD>
    </TR></TABLE>>]
  null [shape="plaintext"]
  }

  ll:head -> ant:data;
  ll:tail -> caterpillar;
  ant:next -> bee:data;
  bee:next -> caterpillar:data;
  caterpillar:next -> null

  ant:prev -> null
  bee:prev -> ant:data;
  caterpillar:prev -> bee:data;

Matplotlib
----------

.. plot::
  :width: 13em

  import numpy as np
  import matplotlib.pyplot as plt

  x = np.arange(0, 100000, 5000)
  plt.plot(x, x / 1000, 'bo')
  plt.ylabel('time', fontsize=20)
  plt.xlabel('size of list', fontsize=20)
  plt.title('pop()', fontsize=35)

AAFig
-----

.. aafig::
  :scale: 75

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

Mermaid
-------

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

Mermaid Sequence
----------------

.. mermaid::
  :alt: timeline
  :caption: HTTP

  sequenceDiagram
    participant Browser
    participant Flask
    participant PostgreSQL
    Browser->Flask: GET / HTTP/1.1
    Flask->PostgreSQL: SELECT * FROM cats
    PostgreSQL-->Flask: [cat1, cat2]
    Flask-->Browser: <html>...</html>

draw.io
-------

.. drawio-figure:: sql.drawio

  I think this might make Elie happy.

Glossary
========

Glossary
--------

.. glossary::

  term

    Definition of the term.
