# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

# from app.config import get_config
from backend.mongodb import MongoDB as db

def get_db():
    """ Get a db object? or module going """

    # In the future, we'll look at our config and possibly user/auth
    # information and one of various db's.

    # For now? HHAHHAHAHAHA
    # we return mongodb and call it a day
    return db


def get_md():
    """ Get a md object or module going. """

    # in the future, we might split db and md (metadata) duties between
    # say genders AND mongo. Of course we do nothing of the sort in v1.

    return db


## END OF LINE ##
