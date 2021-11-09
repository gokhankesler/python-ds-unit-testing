#!/usr/bin/env python

"""The setup script."""
from setuptools import setup, find_packages


setup(
    author="<Gokhan Kesler>",
    author_email='gokhankesler@gmail.com',
    description="A package for converting between imperial unit lengths and weights.",
    name='unitTest',
    packages=find_packages(include=["src", "src.*"]),
    install_requires=[
        'numpy',
        'pytest',
        'pytest-mock',
],
    version='0.0.1',
)
