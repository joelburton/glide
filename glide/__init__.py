import pathlib
from os import path

from sphinx.application import Sphinx
from sphinx.util.logging import getLogger
from pathlib import Path
import sys

version = "2.8.0"

logger = getLogger("glide")


def find_conf(p=None):
    if not p:
        p = Path.cwd()
    while p != Path.root:
        if (p / "conf.py").exists():
            return p.resolve()
        p = p.parent
    else:
        raise Exception("No conf.py")


def use_parent_confdir(curr_file, debug=False):
    curr_dir = Path(curr_file).parent
    parent_confdir = str(find_conf(curr_dir.parent))
    sys.path.insert(0, parent_confdir)
    if debug: print(parent_confdir)
    return parent_confdir


def build_me(builder, extra_conf):
    app = None
    # try:
    confdir = find_conf()
    app = Sphinx(".", confdir, f"_build/{builder}",
                 ".", builder, extra_conf, None,
                 None, None, True,
                 None, 1, 0, False,
                 False)
    cwd = pathlib.Path.cwd()

    app.build(False, [])

    return app.statuscode
    # except (Exception, KeyboardInterrupt) as exc:
    #     handle_exception(app, {"pdb": False}, exc, [])
    #     return 2


def copy_translation_handlers(
        app,
        node,
        handouts="html",
        singlehandouts="html",
        revealjs="html"):
    """Copy translation handlers from html for Glide new builder types."""

    th = app.registry.translation_handlers
    name = node.__name__
    app.registry.add_translation_handlers(
        node,
        handouts=th[handouts][name],
        singlehandouts=th[singlehandouts][name],
        revealjs=th[revealjs][name],
    )



def setup(app):
    app.add_html_theme(
        'revealjs',
        path.abspath(path.join(path.dirname(__file__), "themes", "revealjs")))
    app.add_html_theme(
        'handouts',
        path.abspath(path.join(path.dirname(__file__), "themes", "handouts")))
