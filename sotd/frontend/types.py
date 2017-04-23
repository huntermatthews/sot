# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from pprint import pprint

from flask import Flask
from flask import jsonify
from flask import request
from flask import g

from midlayer import types

def list_types():
    # for GET /types, get a list of all types (tables, collections)
    return '{}'.format(types.get_all_types(g.db))

def create_types():
    pprint(request.is_json)
    new_type = request.get_json()
    pprint(new_type)
    types.create_type(g.db, new_type)
    return jsonify(new_type)

## END OF LINE ##
