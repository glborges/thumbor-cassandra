#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

import thumbor_cassandra.loader as loader

from os.path import abspath, join, dirname
from cassandra.cluster import Cluster
from pyvows import Vows, expect
from thumbor.context import Context
from thumbor.config import Config
from fixtures.loader_fixture import IMAGE_ID, IMAGE_BYTES_ARRAY, KEYSPACE


class CassandraContext(Vows.Context):
    def setup(self):
        self.cluster = Cluster(['127.0.0.1'], port=9042)
        self.session = self.cluster.connect()
        self.session.execute("""
            CREATE KEYSPACE IF NOT EXISTS %s
            WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
            """ % KEYSPACE)

        self.session.set_keyspace(KEYSPACE)

        self.session.execute("""
            CREATE TABLE IF NOT EXISTS images (
                image_id text,
                image_data blob,
                PRIMARY KEY (image_id)
            )
            """)

        self.image_path = join(abspath(dirname(__file__)), 'fixtures/image.jpg')

        with open(self.image_path, 'r') as img:
            image_byte = img.read()
            byte_array = bytearray(image_byte)

        self.session.execute("INSERT INTO images (image_id, image_data) VALUES (%s, %s)", [IMAGE_ID, byte_array])

    def teardown(self):
        self.session.execute("""
            DROP KEYSPACE IF EXISTS %s
            """ % KEYSPACE)


@Vows.batch
class CassandraLoaderVows(CassandraContext):
    class CanLoadImage(Vows.Context):
        @Vows.async_topic
        def topic(self, callback):
            config = Config(CASSANDRA_LOADER_KEYSPACE='general', CASSANDRA_LOADER_SERVER_PORT=9042,
                            CASSANDRA_LOADER_SERVER_HOST='localhost', CASSANDRA_LOADER_TABLE_NAME='images',
                            CASSANDRA_LOADER_TABLE_ID_COLUMN='image_id', CASSANDRA_LOADER_TABLE_BLOB_COLUMN='image_data')
            context = Context(config=config)

            return loader.load(context, IMAGE_ID, callback)

        def should_not_be_null(self, topic):
            expect(topic.args[0]).not_to_be_null()
            expect(topic.args[0]).not_to_be_an_error()

        def should_have_proper_bytes(self, topic):
            expect(topic.args[0]).to_equal(IMAGE_BYTES_ARRAY)

    class GettingReturnsNoneWhenImageDoesNotExist(Vows.Context):
        @Vows.async_topic
        def topic(self, callback):
            config = Config(CASSANDRA_LOADER_KEYSPACE='general', CASSANDRA_LOADER_SERVER_PORT=9042,
                            CASSANDRA_LOADER_SERVER_HOST='localhost', CASSANDRA_LOADER_TABLE_NAME='images',
                            CASSANDRA_LOADER_TABLE_ID_COLUMN='image_id', CASSANDRA_LOADER_TABLE_BLOB_COLUMN='image_data')

            return loader.load(Context(config=config), 'not_here', callback)

        def should_be_null(self, topic):
            expect(topic[0]).to_be_null()
