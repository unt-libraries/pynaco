from setuptools import setup, find_packages
import re

version = ''
with open('pynaco/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

tests_require = [
    'ddt >= 1.0.0'
]

setup(
    name='pynaco',
    version=version,
    description='Python implementation of the NACO normalization rules',
    url='https://github.com/unt-libraries/pynaco',
    packages=find_packages(exclude=['tests.*', 'tests']),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    license='',
    tests_require=tests_require,
    test_suite='runtests',
)
