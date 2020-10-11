import posixpath
import re
import subprocess
from os import path
from toolz import merge
from shutil import move
from subprocess import CalledProcessError, PIPE
from typing import Any, Dict, List, Tuple

from docutils import nodes
from docutils.nodes import Node
from docutils.parsers.rst import Directive, directives

import sphinx
from sphinx.application import Sphinx
from sphinx.errors import SphinxError
from sphinx.locale import _, __
from sphinx.util import logging, sha1
from sphinx.util.docutils import SphinxDirective, SphinxTranslator
from sphinx.util.fileutil import copy_asset
from sphinx.util.i18n import search_image_for_language
from sphinx.util.nodes import set_source_info
from sphinx.util.osutil import ensuredir
from sphinx.writers.html import HTMLTranslator
from sphinx.writers.latex import LaTeXTranslator
from sphinx.writers.manpage import ManualPageTranslator
from sphinx.writers.texinfo import TexinfoTranslator
from sphinx.writers.text import TextTranslator
from sphinx.ext.graphviz import figure_wrapper, align_spec

logger = logging.getLogger(__name__)


class DiagramError(SphinxError):
    category = 'Diagram error'


# noinspection PyPep8Naming
class diagram(nodes.General, nodes.Inline, nodes.Element):
    pass


class DiagramDirective(SphinxDirective):
    """
    Directive to insert arbitrary dot markup.
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = False
    option_spec = {
        'alt': directives.unchanged,
        'align': align_spec,
        'caption': directives.unchanged,
        'name': directives.unchanged,
        'class': directives.class_option,
        'width': directives.unchanged,
        'height': directives.unchanged,
    }

    def run(self) -> List[Node]:
        if self.arguments:
            document = self.state.document
            if self.content:
                return [document.reporter.warning(
                    __('Diagram directive cannot have both content and '
                       'a filename argument'), line=self.lineno)]
            argument = search_image_for_language(self.arguments[0], self.env)
            rel_filename, filename = self.env.relfn2path(argument)
            self.env.note_dependency(rel_filename)
            try:
                with open(filename, encoding='utf-8') as fp:
                    diagram_code = fp.read()
            except OSError:
                return [document.reporter.warning(
                    __('External Diagram file %r not found or reading '
                       'it failed') % filename, line=self.lineno)]
        else:
            diagram_code = '\n'.join(self.content)
            if not diagram_code.strip():
                return [self.state_machine.reporter.warning(
                    __('Ignoring "diagram" directive without content.'),
                    line=self.lineno)]
        node = diagram()
        node['code'] = diagram_code
        node['options'] = {'docname': self.env.docname}

        node['alt'] = self.options.get('alt', 'diagram')
        if 'align' in self.options:
            node['align'] = self.options['align']
        if 'class' in self.options:
            node['classes'] = self.options['class']
        if 'width' in self.options:
            node['width'] = self.options['width']
        if 'height' in self.options:
            node['height'] = self.options['height']

        if 'caption' not in self.options:
            self.add_name(node)
            return [node]
        else:
            # noinspection PyTypeChecker
            figure = figure_wrapper(self, node, self.options['caption'])
            self.add_name(figure)
            return [figure]


def render_diagram(self: SphinxTranslator, code: str, options: Dict,
                   prefix: str = 'graphviz') -> Tuple[str, str]:
    """Render diagram code into a PNG output file."""
    hashkey = (code + str(options)).encode()

    fname = '%s-%s.png' % (prefix, sha1(hashkey).hexdigest())
    relfn = posixpath.join(self.builder.imgpath, fname)
    outfn = path.join(self.builder.outdir, self.builder.imagedir, fname)

    if path.isfile(outfn):
        return relfn, outfn

    ensuredir(path.dirname(outfn))

    # Pull in the real Diagram class from diagrams and wrap it so that when
    # it's used, it will force a predictable filename
    from diagrams import Diagram

    class MyDiagram(Diagram):
        _default_graph_attrs = merge(Diagram._default_graph_attrs, {
            "pad": "0",
            "dpi": "300",
            "size": "10,7",
        })

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs,
                             filename=fname.split(".png")[0],
                             show=False)

    try:
        code_env = {"Diagram": MyDiagram}
        exec(code, code_env)
        move(fname, outfn)

        if not path.isfile(outfn):
            raise DiagramError(f'did not produce an output file at {outfn}')
        return relfn, outfn
    except ValueError as exc:
        raise DiagramError(f"Error creating diagram: {exc}")


def render_diagram_html(self: HTMLTranslator, node: diagram, code: str,
                        options: Dict,
                        prefix: str = 'diagram', imgcls: str = None,
                        alt: str = None
                        ) -> Tuple[str, str]:
    try:
        fname, outfn = render_diagram(self, code, options, prefix)
    except DiagramError as exc:
        logger.warning(__('dot code %r: %s'), code, exc)
        raise nodes.SkipNode from exc

    classes = [imgcls, 'diagram', 'graphviz'] + node.get('classes', [])
    imgcls = ' '.join(filter(None, classes))

    if fname is None:
        self.body.append(self.encode(code))
    else:
        if alt is None:
            alt = node.get('alt', self.encode(code).strip())
        if 'align' in node:
            self.body.append('<div align="%s" class="align-%s">' %
                             (node['align'], node['align']))

        self.body.append(f'<div class="graphviz diagram">')
        style = ""
        if "height" in node:
            style = "height: " + node['height'] + ";"
        if "width" in node:
            style = "width: " + node['width']
        self.body.append(
            f'<img src="{fname}" alt="{alt}" class="{imgcls}" style="{style}" />')
        self.body.append('</div>\n')

        if 'align' in node:
            self.body.append('</div>\n')

    raise nodes.SkipNode


def html_visit_diagram(self: HTMLTranslator, node: diagram) -> None:
    render_diagram_html(self, node, node['code'], node['options'])
    import ipdb; ipdb.set_trace()


def render_diagram_latex(self: LaTeXTranslator, node: diagram, code: str,
                         options: Dict, prefix: str = 'graphviz') -> None:
    try:
        fname, outfn = render_diagram(self, code, options, 'pdf', prefix)
    except DiagramError as exc:
        logger.warning(__('dot code %r: %s'), code, exc)
        raise nodes.SkipNode from exc

    is_inline = self.is_inline(node)

    if not is_inline:
        pre = ''
        post = ''
        if 'align' in node:
            if node['align'] == 'left':
                pre = '{'
                post = r'\hspace*{\fill}}'
            elif node['align'] == 'right':
                pre = r'{\hspace*{\fill}'
                post = '}'
            elif node['align'] == 'center':
                pre = r'{\hfill'
                post = r'\hspace*{\fill}}'
        self.body.append('\n%s' % pre)

    self.body.append(r'\sphinxincludegraphics[]{%s}' % fname)

    if not is_inline:
        self.body.append('%s\n' % post)

    raise nodes.SkipNode


def latex_visit_diagram(self: LaTeXTranslator, node: diagram) -> None:
    render_diagram_latex(self, node, node['code'], node['options'])


def render_diagram_texinfo(self: TexinfoTranslator, node: diagram, code: str,
                           options: Dict, prefix: str = 'diagram') -> None:
    try:
        fname, outfn = render_diagram(self, code, options, 'png', prefix)
    except DiagramError as exc:
        logger.warning(__('diagram code %r: %s'), code, exc)
        raise nodes.SkipNode from exc
    if fname is not None:
        self.body.append('@image{%s,,,[diagram],png}\n' % fname[:-4])
    raise nodes.SkipNode


def texinfo_visit_diagram(self: TexinfoTranslator, node: diagram) -> None:
    render_diagram_texinfo(self, node, node['code'], node['options'])


def text_visit_diagram(self: TextTranslator, node: diagram) -> None:
    if 'alt' in node.attributes:
        self.add_text(_('[diagram: %s]') % node['alt'])
    else:
        self.add_text(_('[diagram]'))
    raise nodes.SkipNode


def man_visit_diagram(self: ManualPageTranslator, node: diagram) -> None:
    if 'alt' in node.attributes:
        self.body.append(_('[diagram: %s]') % node['alt'])
    else:
        self.body.append(_('[diagram]'))
    raise nodes.SkipNode


#
# def on_build_finished(app: Sphinx, exc: Exception) -> None:
#     if exc is None and app.builder.format == 'html':
#         src = path.join(sphinx.package_dir, 'templates', 'graphviz', 'graphviz.css')
#         dst = path.join(app.outdir, '_static')
#         copy_asset(src, dst)


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_node(diagram,
                 html=(html_visit_diagram, None),
                 handouts=(html_visit_diagram, None),
                 revealjs=(html_visit_diagram, None),
                 latex=(latex_visit_diagram, None),
                 texinfo=(texinfo_visit_diagram, None),
                 text=(text_visit_diagram, None),
                 man=(man_visit_diagram, None))
    app.add_directive('diagram', DiagramDirective)
    # app.add_css_file('graphviz.css')
    # app.connect('build-finished', on_build_finished)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
