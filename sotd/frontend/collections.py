# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from pprint import pprint

from flask import jsonify
from flask import request
from flask import g

from midlayer import collections

def list_collections():
    # for GET /collections, get a list of all collections
    return '{}'.format(collections.list_collections(g.db))

def create_collections():
    new_collections = request.get_json()
    pprint(new_collections)
    collections.create_collection(g.db, new_collections)
    return jsonify(new_collections)

## END OF LINE ##
