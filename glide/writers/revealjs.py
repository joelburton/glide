"""Sphinx writer/translator for RevealJS, a browser slideshow."""

from docutils.nodes import SkipNode, Node
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.writers.html import HTMLTranslator

from glide import version, logger
from .common import FixCompactParagraphsTranslatorMixin


class RevealJSTranslator(FixCompactParagraphsTranslatorMixin, HTMLTranslator):
    """Translator for Sphinx structure -> RevealJS HTML structure.

    Sphinx normally turns a document like this into::

        ===============
        My Presentation     =>    <section>                           (level 1)
        ===============             <h1>My Presentation</h1>

        Intro                       <section>                         (level 2)
        =====                         <h2>Intro</h2>

        Welcome                       <section>                       (level 3)
        -------                         <h3>Welcome</h3>
                                        <ul><li>bullet</li></ul>
        - bullet                      </section>

        ...
                                    </section>                   (end of Intro)
                                  </section>                  (end of doc body)

    However, RevealJS considers the title slide "just another slide" and the
    concept groups, like Intro, are the only hierarchy. Also, the actual slide
    of a concept group is slide, not just an arbitrary title floating. So we
    build this::

        ===============           <section>
        My Presentation     =>      <h1>My Presentation</h1>
        ===============           </section>

        Intro                     <section>                       (start Intro)
        =====                       <section>       (make title slide of Intro)
                                      <h2>Intro</h2>
                                    </section>

        Welcome                     <section>
        -------                       <h3>Welcome</h3>
                                      <ul><li>A bullet point</li></ul>
        - A bullet point            </section>
        ...
                                  </section>                     (end of Intro)


    Therefore, a lot of the work in this translator is doing things differently
    depending on it the current state is section_level 1, 2, or 3. If the RST
    doc has additional sections beyond depth 3, they don't make new slides---
    just become minor headings on the existing slide.

    Note that this class doesn't output the required `<div class=reveal>` around
    the entire presentation, nor does it make the title slide, nor does it
    include the JS for revealjs and kick off the presentation. All of those
    things are handled in the themes/revealjs/layout.html document.
    """

    def __init__(self, *args):
        super().__init__(*args)
        # The default value here is silly-low, and this is the only way to fix.
        # These are used for "fields" used to describe documents (often, but
        # not always at the top), like:
        #
        # :author: Elmo
        # :color: red

        self.settings.field_name_limit = 50

    def add_new_slide(self, node):
        """Add new grouping or content slide, allowing for revealjs options."""

        assert self.section_level in [2, 3], "Incorrect slide depth."

        # Get revealjs options so we can add them to section element
        attr_to_html_attr = {
            'transition': 'data-transition',
            'transition-speed': 'data-transition-speed',
            'class': 'class',
        }

        attrs = {
            html_attr: f"{node.attributes.get(attr)}"
            for attr, html_attr in attr_to_html_attr.items()
            if node.attributes.get(attr)
        }

        # Slide backgrounds can be specified (either a color or image)
        background = node.attributes.get('background')
        background_option = ""

        if background:
            # Assume it's not an image (it's a color)
            attrs['data-background'] = f"{background}"

            if "." in background:
                _, upper_ext = background.upper().rsplit(".", 1)
                if upper_ext in ['JPG', 'APNG', 'PNG', 'GIF', 'SVG', 'WEBP']:
                    attrs['data-background'] = f"'_images/{background}'"
                    # If background is an image, add it to the images the
                    # builder is tracking --- otherwise, it won't get copied
                    # into build directory's images folder and things won't work
                    self.builder.images[background] = background

        self.body.append(self.starttag(node, "section", **attrs))

    def visit_section(self, node):
        """Handle starting a section.

        The input structure has two levels: the overall section surrounding all
        of the material and the section for each slide. We omit the overall
        section (we don't want or need any wrapper elements) and emit a
        <section> for each slide.
        """

        self.section_level += 1

        # If this is a new slide, add it (don't do this for sub-slide sections)
        if self.section_level in [2, 3]:
            self.add_new_slide(node)

    # noinspection PyUnusedLocal
    def depart_section(self, node):
        """Close sections.

        We didn't create any structure for sections other than slide-level, so
        only close those.
        """

        # Close the slide (but don't do this for sub-slide sections)
        if self.section_level in [2, 3]:
            self.body.append("</section>\n\n")

        self.section_level -= 1

    def visit_title(self, node):
        """Handle section titles in slide-aware way."""

        # We don't want to print the overall presentation title here
        if self.section_level == 1:
            raise SkipNode

        # If this is the top of second-level section, wrap in <section> so that
        # the title becomes a slide of its own, so we get a "group" title slide
        if self.section_level == 2:
            self.body.append(self.starttag(node, 'section'))

        return super().visit_title(node)

    def depart_title(self, node):
        """Handle leaving section titles in a slide-away way."""

        super().depart_title(node)

        # If this is the end of a second-level section, close our <section>
        # that was opened above
        if self.section_level == 2:
            self.body.append("</section>\n\n")

    def visit_sidebar(self, node):
        """These should never appear in slides."""

        if "revealjs" in node.attributes['classes']:
            return super().visit_sidebar(node)

        raise SkipNode

    def visit_admonition(self, node, name=""):
        """These should never appear in slides."""

        if "revealjs" in node.attributes['classes']:
            # add marker class onto generic-type admonition
            if not name:
                node.attributes['classes'] += ["admonition-generic"]
            return super().visit_admonition(node, name)

        raise SkipNode

    def visit_topic(self, node):
        """These should never appear in slides."""

        raise SkipNode

    def unknown_visit(self, node: Node) -> None:
        """We should never get here, so warn user."""

        logger.warning("Revealjs hit unexpected node: %s", node)
        raise SkipNode


class RevealJSBuilder(StandaloneHTMLBuilder):
    """Builder for making RevealJS using Sphinx."""

    name = 'revealjs'

    # Do not generate any support for search
    search = None

    def init(self):
        """Override revealjs-specific settings."""

        self.config.html_theme = self.config.revealjs_theme
        return super().init()


def setup(app):
    app.add_builder(RevealJSBuilder)
    app.set_translator('revealjs', RevealJSTranslator)
    return {'version': version, 'parallel_read_safe': True}
