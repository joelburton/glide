"""Ace editor.

For example:

  .. editor:: typescript
    :height: 10em
    :width: 40em
    :font-size: 20px

    function foo(x: number): void {
        bar();
    }

These are ignored in non-RevealJS builders.
"""

from docutils import nodes
from docutils.nodes import SkipNode
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive

from glide import version


# noinspection PyPep8Naming
class editor(nodes.Element):
    """editor node."""


#         class MyDirective(Directive):
#                has_content = True
#                required_arguments = 1
#                optional_arguments = 0
#                final_argument_whitespace = True
#                option_spec = {
#                    'class': directives.class_option,
#                    'name': directives.unchanged,
#                }

class EditorDirective(Directive):
    """The directive just adds a node for builder to find."""

    has_content = True
    required_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "class": directives.class_option,
        "height": directives.length_or_percentage_or_unitless,
        "width": directives.length_or_percentage_or_unitless,
        "font-size": directives.length_or_percentage_or_unitless,
    }

    def run(self):
        # self.assert_has_content()
        text = "\n".join(self.content)
        node = editor(text, height=self.options['height'], width=self.options['width'], font_size=self.options['font-size'])
        node.mode = self.arguments[0]
        self.add_name(node)
        # self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


# noinspection PyUnusedLocal
def ignore_visit_editor(self, node):
    """All non-revealjs builders should use this."""
    raise SkipNode


# noinspection PyUnusedLocal
def html_visit_editor(translator, node):
    """Wrap contents in an editor."""
    breakpoint()
    translator.body.append(f"""
    <div styles="height: {node['height']}; width: {node['width']}">
    <div class='editor-wrapper' styles="height: {node['height']}; width: {node['width']}">
    <div id='editor' style="font-size: {node['font_size']}">""")


# noinspection PyUnusedLocal
def html_depart_editor(translator, node):
    """End the editor element we started."""
    translator.body.append("</div></div></div>")
    translator.body.append(f"""
    <script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.32.6/ace.min.js" integrity="sha512-kiECX53fzPhY5cnGzxTUZUOefsjR7gY3SD2OOgcsxZ0nAMZ3e+lkqxhXzGAFm05KjIaQ49/OyNryGTcbLb2V9w==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

<script>
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/chrome");
    editor.session.setMode("ace/mode/{node.mode}");
</script>
    
    """)


def setup(app):
    app.add_node(
        editor,
        # Ignore on any builder except revealjs --- if there are newer builders,
        # these should be added here.
        epub=(ignore_visit_editor, None),
        html=(ignore_visit_editor, None),
        handouts=(ignore_visit_editor, None),
        latex=(ignore_visit_editor, None),
        revealjs=(html_visit_editor, html_depart_editor),
        text=(ignore_visit_editor, None),
        man=(ignore_visit_editor, None),
    )
    app.add_directive('editor', EditorDirective)
    return {'version': version, 'parallel_read_safe': True}
