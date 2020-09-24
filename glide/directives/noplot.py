"""Do nothing plot directive for people who don't have matplotlib.

We use matplotlib to draw business charts---but not everyone who uses our build
system may have that installed or need to work on materials that require charts.

Normally, if you try to build a document with the matplotlib plot directive::

  .. plot::

    import matplotlib.pyplot as plt
    ...

it would raise a fatal error if you don't have the matplotlib extension.

Instead, use this extension and it will provide a no-op plot directive.

NOTE: this just SKIPS BUILDING CHARTS. That may not be a good idea --- the chart
might be important for the presentation. This is just a workaround!

Much better idea: install matplotlib, yo! ::

  $ pip install matplotlib
  $ pip install scipy

This may require a C compiler and other nifty essential-to-be-a-good-person
tools. If your computer doesn't have all that fun stuff, you can get a Python
distribution, like Enthought, which provides it.

Snarkily and happily yours, Joel <joel@joelburton.com>
"""

from docutils.parsers.rst import Directive

from glide import version, logger


class NoPlotDirective(Directive):
    """No-op directive for people without matplotlib to not get errors."""

    has_content = True

    def run(self):
        logger.warning("Overridden plot directive: skipped matplotlib drawing")
        return []


def setup(app):
    app.add_directive('plot', NoPlotDirective)
    return {'version': version, 'parallel_read_safe': True}
