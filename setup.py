#!/usr/bin/env python3

import unittest

from setuptools import setup


def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='distributions',
    version='0.1',
    description='Descrete distribution probability package',
    long_description=readme(),
    author='Hoenir',
    author_email='hoenirvili@gmail.com',
    url='https://github.com/hoenirvili/distributions/',
    packages=['distributions'],
    install_requires=['click', 'numpy', 'matplotlib', 'scipy'],
    scripts=['bin/distributions'],
    test_suite='setup.my_test_suite',
    license='MIT',
    classifiers=[
        'Developmnet Status :: 4 - Beta',
        'License :: OSI Approved :: MIT license',
        'Operating System :: Linux',
    ])
