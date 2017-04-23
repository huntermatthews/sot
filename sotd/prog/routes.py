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

    # TYPES API
    app.add_url_rule('/types', 'list_types', frontend.list_types,
                     methods=['GET'])
    app.add_url_rule('/types', 'create_types', frontend.create_types,
                     methods=['POST'])


## END OF LINE ##
