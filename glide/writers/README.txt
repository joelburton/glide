Sphinx Writers
==============

Here be dragons, albeit fascinating ones that will teach you about parsers
and build trees.

In order to tweak the HTML we get for RevealJS and handouts, and to tweak the
LaTeX we ultimately turn into our PDFs, we have custom Sphinx builders, writers,
and translators.

In most cases, these do the same thing as the standard Sphinx ones (they subclass
those, and don't try to override most things).

This code requires an intermediate level of understanding of the Sphinx API.
Joel would probably die of happiness if you asked him about them.
