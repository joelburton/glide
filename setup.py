#!/usr/bin/env python

# Since it dives deeply into the semi-public API of Sphinx, this product is very
# sensitive to Sphinx versions. If you use a version outside the accepted
# ranges, expect problems.


from setuptools import setup

setup(
    name='Glide',
    version='2.8.0',
    description='Curriculum presentation system.',
    author='Joel Burton',
    author_email='joel@joelburton.com',
    url='https://github.com/joelburton/glide',
    packages=['glide', 'glide/directives', 'glide/writers', 'glide/lexers'],
    python_requires=">= 3.9",
    install_requires=[
        "Sphinx (>=3.2.1,<8)",
        "aafigure",
        "click",
        "click-repl",
        "jsx-lexer",
        "matplotlib",
        "myst-parser",
        "numpy",
        "pyyaml",
        "scipy",
        "sphinx-copybutton",
        "sphinxcontrib-drawio",
        "sphinxcontrib-mermaid",
        "sphinxcontrib-youtube",
        "sphinxemoji",
        "toolz",
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
        'console_scripts': [
            "glide = glide.cli.glidecmd:cli"
        ]
    },
    package_data={'themes': ['*']}
)
