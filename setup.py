#!/usr/bin/env python
from setuptools import setup

long_description = open('README.rst').read()

setup(name='corpcrawl',
      version='0.0.35',
      author="rozap",
      author_email="chrisd1891@gmail.com",
      license="MIT",
      url="https://github.com/chrisd1891/corpcrawl/",
      description="Corpcrawl EDGAR Scraper",
      long_description=long_description,
      platforms=['any'],
      packages=[
      	'corpcrawl',
      	'corpcrawl.util',
      	'corpcrawl.models'
      ]
)