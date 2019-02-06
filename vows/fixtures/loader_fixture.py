#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from os.path import join, abspath, dirname

IMAGE_ID = "image.jpg"
KEYSPACE = "general"
IMAGE_BYTES_ARRAY = []

IMAGE_PATH = join(abspath(dirname(__file__)), IMAGE_ID)
with open(IMAGE_PATH, 'r') as img:
    IMAGE_BYTES = img.read()
    IMAGE_BYTES_ARRAY = bytearray(IMAGE_BYTES)
