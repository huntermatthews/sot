# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from flask import g

from backend import (get_db, get_md)
from prog.config import get_config

def _assign_config():
    print('_assign_config() called')
    if not hasattr(g, 'config'):
        g.config = get_config()

def _assign_db():
    print('_assign_db() called')
    if not hasattr(g, 'db'):
        g.db = get_db()(g.config)

# def _assign_md():
#     print('_assign_md() called')
#     if not hasattr(g, 'md'):
#         g.md(g.config) = get_md()

def add_before_request_calls(app):
    """ As it says on the tin. """

    app.before_request(_assign_config)
    app.before_request(_assign_db)
#    app.before_request(_assign_md)

def _unassign_config(response):
    print('_unassign_config() called')
    print(response)
    return response

def add_after_request_calls(app):
    app.after_request(_unassign_config)

def _bf_first():
    print('before_first_request()')

def add_before_first_request_calls(app):
    app.before_first_request(_bf_first)

def _teardown_request_printer(response):
    print('_teardown_request_printer()')
    return response

def add_teardown_request_calls(app):
    app.teardown_request(_teardown_request_printer)


## END OF LINE ##
