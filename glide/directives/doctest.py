"""Improved versions of doctest-related directives.

The standard doctest directives are awesome, but they don't have all of the features
of code-block directives. This adds back in:

- :caption:
- :class:

It does so by registering the subclassed versions, below, under the original names.

Joel Burton <joel@joelburton.com>
"""

# BUG: allows emphasize-lines but doesn't do the emphasizing; bug 112


from docutils.parsers.rst import directives
from sphinx.ext.doctest import DoctestDirective, TestcodeDirective, TestoutputDirective
from sphinx.directives.code import CodeBlock


class AllowCaptionMixin:
    """Mixin that adds features from CodeBlock (dedent, captions, classes, etc)."""

    def run(self):
        """Fake a language argument, then call CodeBlock's run method."""

        self.arguments = ["python"]
        return CodeBlock.run(self)


# class JDoctestDirective(AllowCaptionMixin, DoctestDirective):
class JDoctestDirective(CodeBlock):
    """Subclass of DoctestDirective to allow caption & class options."""

    option_spec = {
        'hide': directives.flag,
        'options': directives.unchanged,
        'caption': directives.unchanged,
        'class': directives.class_option,
        'emphasize-lines': directives.unchanged,
    }


# class JTestcodeDirective(AllowCaptionMixin, TestcodeDirective):
class JTestcodeDirective(CodeBlock):
    """Subclass of TestcodeDirective to allow caption & class options."""

    option_spec = {
        'hide': directives.flag,
        'options': directives.unchanged,
        'caption': directives.unchanged,
        'class': directives.class_option,
        'emphasize-lines': directives.unchanged,
    }


# class JTestoutputDirective(AllowCaptionMixin, TestoutputDirective):
class JTestoutputDirective(CodeBlock):
    """Subclass of TestoutputDirective to allow caption & class options."""

    option_spec = {
        'hide': directives.flag,
        'caption': directives.unchanged,
        'class': directives.class_option,
        'emphasize-lines': directives.unchanged,
    }


def setup(app):
    """Re-register our directives."""

    from logging import Filter
    from sphinx.application import logger

    class ReregisterDirectiveNotAWarningFilter(Filter):
        """Don't warn about re-registering a directive.

        We hide these so that Sphinx can be run with warnings-as-errors without these
        (expected) warnings always causing a failure.
        """

        def filter(self, record):
            """Filter out expected warnings."""

            return record.getMessage() not in [
                ("while setting up extension glide.directives.doctest: "
                 "directive 'doctest' is already registered, it will be overridden"),
                ("while setting up extension glide.directives.doctest: "
                 "directive 'testcode' is already registered, it will be overridden"),
                ("while setting up extension glide.directives.doctest: "
                 "directive 'testoutput' is already registered, it will be overridden"),
            ]

    noWarningFilter = ReregisterDirectiveNotAWarningFilter()
    # logger.logger.addFilter(noWarningFilter)

    app.add_directive('doctest', JDoctestDirective)
    app.add_directive('testcode', JTestcodeDirective)
    app.add_directive('testoutput', JTestoutputDirective)

    logger.logger.removeFilter(noWarningFilter)
