#!/usr/bin/env python

# Since it dives deeply into the semi-public API of Sphinx, this product is very
# sensitive to Sphinx versions. If you use a version outside of the accepted
# ranges, expect problems.
#
# Changelog of Sphinx versions:
# v1.4.0           : tested on Sphinx 2.2
# v1.5.0 (sep 2020): tested on Sphinx 3.2.1

from setuptools import setup

setup(
    name='Glide',
    version='1.5.0',
    description='Curriculum presentation system.',
    author='Joel Burton',
    author_email='joel@joelburton.com',
    url='https://github.com/joelburton/glide',
    packages=['glide', 'glide/directives', 'glide/writers'],
    python_requires=">= 3.6.9",
    install_requires=[
        "Sphinx (>=3.2.1,<4)",
        "jsx-lexer",
        "toolz",
    ],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'revealjs = glide',
            'handouts = glide',
        ]
    },
    package_data={'themes': ['*']}
)
