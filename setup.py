#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.6.4'
long_description = '\n'.join([
    open('README.rst').read(),
    ])

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='pygments-style-prism-default',
    version=version,
    description='Pygments version of the prism.js default color scheme',
    long_description=long_description,
    classifiers=classifiers,
    keywords=['pygments', 'style', 'prism.js', 'syntax highlighting'],
    author='Pierre-Luc BLOT',
    author_email='pierreluc.blot@gmail.com',
    url='https://github.com/pierre-luc/pygments-style-prism-default',
    license='MIT',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],
    entry_points="""
        [pygments.styles]
        prism=pygments_style_prism:PrismStyle
    """,
    zip_safe=False,
)
