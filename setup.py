#!/usr/bin/env python

# Since it dives deeply into the semi-public API of Sphinx, this
# product is very sensitive to Sphinx versions. If you use a
# version outside of the accepted ranges, expect problems.

from setuptools import setup

setup(name='Glide',
      version='1.4.1',
      description='Curriculum presentation system.',
      author='Joel Burton',
      author_email='joel@joelburton.com',
      url='https://github.com/joelburton/glide',
      packages=['glide', 'glide/directives', 'glide/writers'],
      python_requires=">= 3.6.0",
      install_requires=["Sphinx (>=2.1.2,<2.2)"],
      include_package_data=True,
      package_data={'themes': ['*']}
     )
