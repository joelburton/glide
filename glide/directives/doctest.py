"""Improved versions of doctest-related directives.

The standard doctest directives are awesome, but they don't have all of the
features of code-block directives. This adds back in:

- :caption:
- :class:

It does so by registering the subclassed versions, below, under the original
names.

Joel Burton <joel@joelburton.com>
"""

# BUG: allows emphasize-lines but doesn't do the emphasizing; bug 112


from docutils.parsers.rst import directives
from sphinx.directives.code import CodeBlock

from glide import version


class JDoctestDirective(CodeBlock):
    """Subclass of DoctestDirective to allow caption & class options."""

    option_spec = {
        'hide': directives.flag,
        'options': directives.unchanged,
        'caption': directives.unchanged,
        'class': directives.class_option,
        'emphasize-lines': directives.unchanged,
    }


class JTestcodeDirective(CodeBlock):
    """Subclass of TestcodeDirective to allow caption & class options."""

    option_spec = {
        'hide': directives.flag,
        'options': directives.unchanged,
        'caption': directives.unchanged,
        'class': directives.class_option,
        'emphasize-lines': directives.unchanged,
    }


class JTestoutputDirective(CodeBlock):
    """Subclass of TestoutputDirective to allow caption & class options."""

    option_spec = {
        'hide': directives.flag,
        'caption': directives.unchanged,
        'class': directives.class_option,
        'emphasize-lines': directives.unchanged,
    }


def setup(app):
    app.setup_extension("sphinx.ext.doctest")
    app.add_directive('doctest', JDoctestDirective, override=True)
    app.add_directive('testcode', JTestcodeDirective, override=True)
    app.add_directive('testoutput', JTestoutputDirective, override=True)
    return {'version': version, 'parallel_read_safe': True}
