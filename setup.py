#!/usr/bin/env python
import os
import re
from setuptools import setup, find_packages

version = ''
with open('pynaco/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

tests_require = [
    'ddt >= 1.0.0'
]

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='pynaco',
    version=version,
    description='Python implementation of the NACO normalization rules.',
    long_description=README,
    url='https://github.com/unt-libraries/pynaco',
    packages=find_packages(),
    include_package_data=True,
    license='',
    tests_require=tests_require,
    test_suite='runtests',
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    )
)
