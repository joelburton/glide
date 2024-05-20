"""Patch rel2fn to it can handle //snippets/..."""

import os
from os import path

from sphinx.util import os_path
from sphinx.util.osutil import canon_path


def relfn2path_patched(
        self, filename: str, docname: str | None = None) -> tuple[str, str]:
    """Return paths to a file referenced from a document, relative to
    documentation root and absolute.

    In the input "filename", absolute filenames are taken as relative to the
    source dir, while relative filenames are relative to the dir of the
    containing document.
    """
    filename = os_path(filename)

    # Monkey-patched part to support //snippets/
    if filename.startswith("//"):
        rel_fn = filename[2:]
        return (canon_path(path.normpath(rel_fn)),
                path.normpath(path.join(self.config.glide_root, rel_fn)))

    if filename.startswith(('/', os.sep)):
        rel_fn = filename[1:]
    else:
        docdir = path.dirname(self.doc2path(docname or self.docname,
                                            base=False))
        rel_fn = path.join(docdir, filename)

    return (canon_path(path.normpath(rel_fn)),
            path.normpath(path.join(self.srcdir, rel_fn)))
