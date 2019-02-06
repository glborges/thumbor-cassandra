#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2012 Damien Hardy dhardy@figarocms.fr

from distutils.core import setup

__version__ = None
execfile('thumbor_cassandra/_version.py')

setup(
    name = "thumbor_cassandra",
    packages = ["thumbor_cassandra"],
    version = __version__,
    description = "Cassandra loader for Thumbor (no GridFS)",
    author = "Guilherme Borges",
    author_email = "guilherme.lopes.borges@gmail.com",
    keywords = ["thumbor", "cassandra", "images"],
    license = 'MIT',
    url = 'https://github.com/dhardy92/thumbor_hbase',
    classifiers = ['Development Status :: 1 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: MacOSX :: Linux',
                   'Programming Language :: Python :: 2.6',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Multimedia :: Graphics :: Presentation'
    ],
    package_dir = {"thumbor_cassandra": "thumbor_cassandra"},
    install_requires=["thumbor", "cassandra-driver"],
    long_description = """\
Thumbor is a smart imaging service. It enables on-demand crop, resizing and flipping of images.
This module provide support for MongoDB loader for images. 
Image data is stored in one field of MongoDB document in a collection and addressed by its ObjectId('_id')
"""
)