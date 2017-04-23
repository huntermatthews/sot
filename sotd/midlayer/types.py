# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

def get_all_types(db):
    return db.get_types()

def create_type(db, new_type):
    return db.create_type(new_type)


## END OF LINE ##
