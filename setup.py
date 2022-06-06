#!/usr/bin/env python

# Since it dives deeply into the semi-public API of Sphinx, this product is very
# sensitive to Sphinx versions. If you use a version outside of the accepted
# ranges, expect problems.
#
# Changelog of Sphinx versions:
# v1.4.0           : tested on Sphinx 2.2
# v2.0.0 (sep 2020): tested on Sphinx 3.2.1

from setuptools import setup

setup(
    name='Glide',
    version='2.3.7',
    description='Curriculum presentation system.',
    author='Joel Burton',
    author_email='joel@joelburton.com',
    url='https://github.com/joelburton/glide',
    packages=['glide', 'glide/directives', 'glide/writers', 'glide/lexers'],
    python_requires=">= 3.8.6",
    install_requires=[
        "Sphinx (>=3.2.1,<5)",
        "jsx-lexer",
        "toolz",
        "aafigure",
        # "diagrams",
        "aafigure",
        "sphinxcontrib-drawio",
        "sphinxemoji",
    ],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'revealjs = glide',
            'handouts = glide',
        ],
        'pygments.lexers': [
            'simpleconsole = glide.lexers.simpleconsole:SimpleConsoleLexer',
            'commentablehttp = glide.lexers.commentablehttp:CommentableHttpLexer',
            'rainbow-lines =   glide.lexers.rainbow:RainbowLinesLexer',
            'rainbow-2-lines = glide.lexers.rainbow:RainbowTwoLinesLexer',
        ],
    },
    package_data={'themes': ['*']}
)
