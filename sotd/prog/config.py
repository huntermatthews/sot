# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

G_CONFIG = {
    'db_host': 'localhost',
    'db_port': 27017,
    'db_database': 'sot_test',
}


def get_config():

    global G_CONFIG
    return G_CONFIG


## END OF LINE ##
