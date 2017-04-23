# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import logging

from pymongo import MongoClient

class MongoDB(object):

    def __init__(self, config):
        self.host = config['db_host']
        self.port = config['db_port']
        self.database = config['db_database']

        self._clear()

    @property
    def _db(self):
        if self._db_ is None:
            try:
                self._client_ = MongoClient(self.host, self.port)
                self._db_ = self._client_[self.database]
            except Exception as e:
                raise e
            #atexit.register(self._disconnect)
        return self._db_

    def disconnect(self):
        if self._client_ is not None:
            self._client_.close()
            self._clear()

    def _clear(self):
        self._client_ = None
        self._db_ = None

    def list_collections(self):
        collections = self._db.collection_names()
        return collections

    def create_collection(self, new_collection):
        pass


## END OF LINE ##
