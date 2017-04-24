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
    result = []
    print(request.is_json)
    print(request.data)
    new_collections = request.get_json()
    print(type(new_collections))
    pprint(new_collections)
    if isinstance(new_collections, dict):
        new_collections = list(new_collections)
    for coll in new_collections:
        result.append(collections.create_collection(g.db, coll))
    return jsonify(result)

## END OF LINE ##
