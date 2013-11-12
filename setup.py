#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="DevOps Bootcamp",
      version='0.0.1',
      description="OSU OSL's training curriculum",
      author='OSU OSL & OSU LUG',
      author_email='devopsbootcamp@osuosl.org',
      url='http://devopsbootcamp.osuosl.org',
      packages=find_packages(exclude=["contrib", "docs", "tests*"]),
      zip_safe=False,
)

def install():
    pass
