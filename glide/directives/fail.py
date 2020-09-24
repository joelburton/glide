"""Stop document processing altogether with an error.

This stop Sphinx in its tracks until the RST file is edited to remove this
directive.

The point is to prevent the user from building the doc before they've fixed some
problem with material (like if lecture wasn't finished, or the exercise had
serious bugs.)
"""

from docutils.parsers.rst import Directive
from sphinx.errors import DocumentError

from glide import version


class FailDirective(Directive):
    """Directive that raises an error and prevents building."""

    has_content = True

    def run(self):
        content = "\n".join(self.content)
        raise DocumentError(f"""
This document contains a `fail` directive to signal that it should not be used 
until a serious error is addressed. Please read the contents of this directive,
below. Once you've fixed the problem, edit the RST file to remove the `fail`
directive that caused this, and try your build again.

Reason for failure:

{content}

---""")


def setup(app):
    app.add_directive('fail', FailDirective)
    return {'version': version, 'parallel_read_safe': True}
