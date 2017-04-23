# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from pprint import pprint

from flask import Flask
from flask import jsonify
from flask import request

def debug_query():
    print('args')
    for key in request.args:
        print('{}: {}'.format(key, request.args[key]))
    print('is it json? {}'.format(request.is_json))
    if request.is_json:
        print('da json:')
        pprint(request.get_json())
    new_type = request.get_json()
    pprint(new_type)
    return jsonify(new_type)

## END OF LINE ##
