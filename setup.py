#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2012 Damien Hardy dhardy@figarocms.fr

from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = None
execfile('thumbor_cassandra/_version.py')

setup(
    name = "thumbor_cassandra",
    packages = ["thumbor_cassandra"],
    version = __version__,
    description = "Apache Cassandra loader for Thumbor",
    author = "Guilherme Borges",
    author_email = "illidam.lopes@gmail.com",
    keywords = ["thumbor", "cassandra", "images"],
    license = 'MIT',
    url = 'https://github.com/glborges/thumbor-cassandra',
    classifiers = ['Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: Portuguese',
                   'Operating System :: MacOSX',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Multimedia :: Graphics :: Presentation'
    ],
    package_dir = {"thumbor_cassandra": "thumbor_cassandra"},
    install_requires=["thumbor", "cassandra-driver"],
    long_description = """\
Thumbor is a smart imaging service. It enables on-demand crop, resizing and flipping of images.
This module provide support for Apache Cassandra loader for images. 
Image data is stored in one column of a row in a table and addressed by its id in the table.)
"""
)