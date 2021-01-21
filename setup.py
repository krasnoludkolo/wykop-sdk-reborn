#!/usr/bin/env python
"""
Created on 18-12-2012

@author: maciag.artur
@author: jan.danecki
"""

from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()
with open('requirements_test.txt') as f:
    tests_requires = f.read().splitlines()

version = '0.6.1'

setup(
    name='wykop-sdk-reborn',
    version=version,
    packages=find_packages(),
    # PyPI metadata
    author='Jan Danecki',
    author_email='janek@projmen.pl',
    description='Client library for Wykop API v2',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/krasnoludkolo/wykop-sdk-reborn',
    install_requires=requirements,
    tests_require=requirements + tests_requires,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
