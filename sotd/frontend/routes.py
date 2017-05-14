# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import frontend

def add_routes(app):

    # Application level API
    app.add_url_rule('/', 'summary', frontend.summary,
                     methods=['GET'])

    # DEBUG API
    app.add_url_rule('/query', 'debug_query', frontend.debug_query,
                     methods=['GET'])

    # COLLECTIONS API
    app.add_url_rule('/collections', 'list_collections',
                     frontend.list_collections, methods=['GET'])
    app.add_url_rule('/collections', 'create_collections',
                     frontend.create_collections, methods=['POST'])

    # ITEMS API
    app.add_url_rule('/collections/<collection>/items', 'list_items',
                     frontend.list_items, methods=['GET'])
    app.add_url_rule('/collections/<collection>/items', 'create_items',
                     frontend.create_items, methods=['POST'])

    app.add_url_rule('/collections/<collection>/items/<item>/fields/<field>',
                     'get_field', frontend.get_field, methods=['GET'])

## END OF LINE ##
