# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from pprint import pprint

from flask import jsonify
from flask import request
from flask import g

from midlayer import fields

def list_fields(collection, item):
    return '{}'.format(fields.list_fields(g.db, collection, item))

def create_fields(collection, item):
    return False
    result = []
    print(request.is_json)
    print(request.data)
    new_fields = request.get_json()
    print(type(new_fields))
    pprint(new_fields)
    if isinstance(new_fields, dict):
        new_fields = list(new_fields)
    for coll in new_fields:
        result.append(fields.create_field(g.db, coll))
    return jsonify(result)

def get_field(collection, item, field):
    print(request.data)
    result = fields.get_field(g.db, collection, item, field)
    return jsonify(result)

## END OF LINE ##
