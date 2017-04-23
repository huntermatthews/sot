# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


def list_collections(db):
    return db.list_collections()

def create_collection(db, new_collection):
    return db.create_collection(new_collection)


## END OF LINE ##
