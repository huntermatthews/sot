# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from flask import Response
from flask import jsonify
from flask import request

import midlayer.summary

def summary():
    print(request.headers)
    now, utc = midlayer.summary.summary()
    res = {'now': now, 'utc': utc}
    return jsonify(res)

## END OF LINE ##
