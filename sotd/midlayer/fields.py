# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime
from uuid import uuid4

from cerberus import Validator

def get_field(db, collection, item, field):
    # do some checking?
    # I have no idea.

    db.get_field(collection, item, field)


## END OF LINE ##
