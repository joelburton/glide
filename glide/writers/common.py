from docutils import nodes


class FixCompactParagraphsTranslatorMixin:
    """Centralizes this feature, since all our writers use it."""

    def should_be_compact_paragraph(self, node):
        """Can this text be 'compacted' into a non-paragraph?

        Sphinx will try to 'compact' text into not being a paragraph when
        possible. For example, for:

          - hello

          - reader

        It realizes that since those are simple lines, it doesn't need to put
        <p> tags around the text inside the <li> tags---whereas for::

          - hello

          - reader

            I love readers!

        It would need to keep paragraphs inside the <li> tags.

        We often put text inside containers for incremental-appearance, like::

          The answer is:

          .. container:: one-incremental

            Forty-two

        With just a simple thing inside a container, Sphinx doesn't wrap it in a
        paragraph, just <div>. This makes for ugly line breaks. Therefore, when
        directly inside a container, never compact paragraphs. Otherwise, follow
        Sphinx's rules.

        Should you want to compact things directly inside a container, you can
        add a 'non-paragraph' class to it.
        """

        if isinstance(node.parent, nodes.container):
            if 'non-paragraph' not in node.parent.attributes['classes']:
                return False

        # noinspection PyUnresolvedReferences
        return super().should_be_compact_paragraph(node)
