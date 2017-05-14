# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from pprint import pprint

from flask import jsonify
from flask import request
from flask import g

from midlayer import items

def list_items(collection):
    # for GET /items, get all the items right now
    return '{}'.format(items.list_items(g.db, collection))

def create_items(collection):
    result = []
    new_items = request.get_json()
    pprint(new_items)
    if isinstance(new_items, dict):
        new_items = list(new_items)
    for item in new_items:
        result.append(items.create_item(g.db, item))
    return jsonify(result)

## END OF LINE ##
