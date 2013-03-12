#!/usr/bin/env python
from setuptools import setup

long_description = open('README').read()

setup(name='corpcrawl',
      version='0.0.1',
      author="rozap",
      author_email="chrisd1891@gmail.com",
      license="MIT",
      url="none",
      description="Corpcrawl EDGAR Scraper",
      long_description=long_description,
      platforms=['any'],
      packages=["corpcrawl"]
)