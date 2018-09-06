#!/usr/bin/env python


from setuptools import setup

setup(name='Glide',
      version='1.1',
      description='Curriculum presentation system.',
      author='Joel Burton',
      author_email='joel@joelburton.com',
      url='https://github.com/joelburton/glide',
      packages=['glide', 'glide/directives', 'glide/writers'],
      python_requires=">= 3.6.0",
      install_requires=["Sphinx (>=1.7.5,<=1.8)"],
      include_package_data=True,
      package_data={'themes': ['*']}
     )
