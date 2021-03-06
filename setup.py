#!/usr/bin/env python
from setuptools import find_packages, setup

__version__ = '0.1.1'

tests_require = [
    'unittest2',
]

install_requires = [
    'Pillow',
    'path.py',
]

setup(
    name='monsterid',
    version=__version__,
    author='Adam Hitchcock',
    author_email='adam@northisup.com',
    license='Apache License 2.0',
    url='http://github.com/NorthIsUp/monsterid',
    description='deterministically generated avatars in python',
    zip_safe=False,
    packages=find_packages('src', exclude=['tests']),
    package_dir={'':'src'},
    install_requires=install_requires,
    tests_require=tests_require,
    include_package_data=True,
)
