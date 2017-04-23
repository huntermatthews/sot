#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from flask import Flask
from flask import g
from flask import current_app

from prog.routes import add_routes
from prog.config import get_config
from prog.connections import (
    add_before_request_calls,
    add_after_request_calls,
    add_before_first_request_calls,
    add_teardown_request_calls,
    )


def main():
    # Config happens first - a minor victory...
    config = get_config()

    app = Flask(__name__)
    add_routes(app)
    add_before_request_calls(app)
    add_after_request_calls(app)
    add_before_first_request_calls(app)
    add_teardown_request_calls(app)
    app.run(debug=True)


if __name__ == '__main__':
    main()

## END OF LINE ##
