#!/usr/bin/env python3

from distutils.core import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='Distributions',
      version='0.1',
      description='Simple package for computing different distributions',
      author='hoenir',
      maintainer='hoenir',
      long_description=readme(),
      install_requires=[
          "numpy",
          "matplotlib",
          "scipy"
      ],
      classifiers=[
          'Development Status :: 1 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Statistics :: Distributions',
      ],
      author_email='hoenirvili@gmail.com',
      url='https://github.com/hoenirvili/distributions',
      license='MIT',
      packages=['distributions'],
      zip_safe=False)
