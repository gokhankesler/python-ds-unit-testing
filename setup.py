#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="Unit Testing Application",
      version="0.1.0",
      description="Unit Testing Application",
      author="Gokhan Kesler",
      packages=find_packages("src"),
      package_dir={"": "src"},
      author_email="gokhankesler@gmail.com",
      install_requires=["jupyter==1.0.0",
                        "matplotlib",
                        "numpy==1.17.3",
                        "pytest==5.2.2",
                        "pytest-mpl==0.10",
                        "pytest-mock==1.11.2",
                        "scipy",
                        ],
      )
