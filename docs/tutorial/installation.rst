Curric Installation
===================

.. code-block:: simple-console
  :class: console

  $ python -m venv venv               # python 3.8 or 3.9
  $ source venv/bin/activate
  $ pip install -r requirements.txt

Graphviz
--------

If you're building our technical lectures, you'll need this:

.. code-block:: simple-console
  :class: console

  $ brew install Graphviz     # if you use Homebrew
  $ brew install graphviz     # if you use MacPorts

Mermaid
-------

Some lectures will start to use diagram described in the Mermaid language:

.. code-block:: simple-console
  :class: console

  $ cd /anywhere/you/want
  $ npm install @mermaid-js/mermaid-cli
  $ ln -s /absolute-path/to/this/node_modules/.bin/mmdc /usr/local/bin

Draw.io
-------

Some lectures will start to use Draw.io diagrams, so you'll need
`Draw.io Desktop <https://github.com/jgraph/drawio-desktop/releases>`_.
(Install that like a normal Mac application; Glide will find it).

PDFs
----

Joel is experimenting with giving students PDFs (in addition to HTML) for our
lectures: some students print our lectures, and it's much easier to make
nice printable PDFs than HTML pages, given the semi-broken state of printing in
some browsers.

If you make PDF handouts, you'll need `PrinceXML
<https://www.princexml.com/latest/>`_ (there's a new ``make prince`` command
for lectures).

LaTeX
-----

**Nothing to do here.**

Since LaTeX is a lot to install, Joel has been trying to rewrite any Sphinx
extensions that rely on it. The only remaining place where a LaTeX installation
is needed is to make PDFs of lectures with math equations embedded in, and there
are no instances of this in our curriculum as of Oct 2020. So you do not need
to install anything here. If this changes, our previous installation
instructions for this were:

  If you did want to install it, you
  can do so with `LaTeX for Mac (aka MacTeX)
  <https://www.tug.org/mactex/mactex-download.html>`_
