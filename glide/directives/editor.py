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
        node.content = self.content
        self.add_name(node)
        # self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


# noinspection PyUnusedLocal
def ignore_visit_editor(self, node):
    """All non-revealjs builders should use this."""
    raise SkipNode


# noinspection PyUnusedLocal
def xhtml_visit_editor(translator, node):
    """Wrap contents in an editor."""

    content = "\n".join(node.content).replace("`", r"\`")

    translator.body.append(f"""
<script type="module">
import * as monaco from 'https://cdn.jsdelivr.net/npm/monaco-editor/+esm';
monaco.editor.create(document.querySelector('#my-monaco'), {{
    value: `{content}`,
    language: '{node.mode}',
    theme: 'vs-light',
    minimap: {{ enabled: false }},
    fontFamily: "Source Code Pro",
    fontSize: "{node['font_size']}",
    fontWeight: 500,
    lineNumbers: "off",
folding: false,
}});
</script>
<div class="glide-editor" style="width: {node['width']}; margin-left: auto; margin-right: auto">
<div 
    id="my-monaco" 
    class="monaco" 
    style="min-height: {node['height']};">
</div>
<codapi-snippet
    engine="browser"
    sandbox="javascript"
    editor="external">
    </codapi-snippet>
</div>
<script src="https://unpkg.com/@antonz/codapi/dist/settings.js"></script>
<script src="https://unpkg.com/@antonz/runno/dist/runno.js"></script>
<script src="https://unpkg.com/@antonz/codapi/dist/engine/wasi.js"></script>
<script src="https://unpkg.com/@antonz/codapi/dist/snippet.js"></script>
""")

# noinspection PyUnusedLocal
def html_visit_editor(translator, node):
    """Wrap contents in an editor."""

    content = "\n".join(node.content).replace("`", r"\`")

    translator.body.append(f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css" integrity="sha512-hasIneQUHlh06VNBe7f6ZcHmeRTLIaQWFd43YriJ0UND19bvYRauxthDg8E4eVNPm9bRUhr5JGeqH7FRFXQu5g==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js" integrity="sha512-D9gUyxqja7hBtkWpPWGt9wfbfaMGVt9gnyCvYa+jojwwPHLCzUm5i8rpk7vD7wNee9bA35eYIjobYPaQuKS1MQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
       <style>
       codapi-output {{ left: {node['width']} }}
       </style>
<div class="glide-editor" style="width: {node['width']}; font-size: {node['font_size']}; margin: 0 auto; padding-right: 30px; position: relative">
<div id="my-editor" style="min-height: {node['height']}; padding: 0.5em">
</div>
<codapi-snippet
    engine="browser"
    sandbox="javascript"
    editor="external">
    </codapi-snippet>
</div>
    
    <script type="module">
        import * as CodeJar from "https://cdn.jsdelivr.net/npm/codejar@4.2.0/dist/codejar.min.js";
        const editor = document.querySelector("#my-editor");
        function highlight(editor) {{
            editor.innerHTML = hljs.highlight(editor.textContent, {{ language: 'javascript' }}).value ; 
        }}
        const jar = new CodeJar.CodeJar(editor, highlight, {{ "tab": "  ", addClosing: false }});
        jar.updateCode(`{ content }`);      
    </script>
<!-- <script src="https://unpkg.com/@antonz/codapi/dist/settings.js"></script> -->
<script src="https://unpkg.com/@antonz/runno/dist/runno.js"></script>
<!-- <script src="https://unpkg.com/@antonz/codapi/dist/engine/wasi.js"></script> -->
<script src="https://unpkg.com/@antonz/codapi/dist/snippet.js"></script>
""")


# noinspection PyUnusedLocal
def html_depart_editor(translator, node):
    """End the editor element we started."""


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
