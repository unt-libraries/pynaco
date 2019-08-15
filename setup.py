#!/usr/bin/env python
import os
import re
from setuptools import setup, find_packages

version = ''
with open('pynaco/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

readme = ''
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    readme = f.read()

tests_require = [
    'ddt >= 1.0.0'
]

setup(
    name='pynaco',
    version=version,
    maintainer='Mark Phillips',
    maintainer_email='mark.phillips@unt.edu',
    description='Python implementation of the NACO normalization rules.',
    long_description=readme,
    url='https://github.com/unt-libraries/pynaco',
    packages=find_packages(),
    include_package_data=True,
    license='OCLC Research Public License 2.0',
    tests_require=tests_require,
    test_suite='runtests',
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    )
)
