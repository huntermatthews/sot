# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime
from uuid import uuid4

from cerberus import Validator

def list_collections(db):
    return db.list_collections()

def create_collection(db, collection):
    # A sot collection is not a simple or single mongodb collection
    # we need:
    # check our incoming dict for required / optional fields
    # our name is valid for our backend
    # our name isn't already used
    # name itself - our main "data"
    # name.history for our history functions
    # name.sources for our last source updated
    # name.config for our customization (desc lives here)

    # check incoming collection description for completeness
    # TODO: should this happen in the midlayer or the frontend?
    schema = {'name': {'type': 'string',
                       'required': True,},
              'description': {'type': 'string'},
    }
    v = Validator(schema)
    if not v.validate(collection):
        print(v.errors)
        return False   # what goes here?

    # convienence
    name = collection['name']

    # different db allow/disallow different collection names)
    # I guess we could make them return "schema" to use with
    # cerberos...
    if not db.is_collection_name_valid(name):
        return False

    # Sot itself does not allow '_' - we use that for hiding
    # metadata and metacollections.
    if '_' in name:
        return False

    if name in db.list_collections():
        return False   # already created.

    # Finally, we can create our main collection and its
    # supporting "metadata" collections.
    db.create_collection(name)
    db.create_collection(name + '._history')
    db.create_collection(name + '._sources')
    db.create_collection(name + '._config')

    # Update our config support collection
    utc = datetime.utcnow()
    uuid = uuid4()
    config = {'name': 'metadata',
              'when': utc,
              'owner': 'admin',
              'description': collection.get('description', 'None.'),
              'uuid': uuid,
              }
    db.update_collection(name + '._config', config)

    # Update our source support collection
    #   No update to sources ??? is that only for fields?

    # Update our history support collection
    hist = {'object': 'collection',
            'operation': 'created',
            'name': name,
            'uuid': uuid,
            'owner': 'admin',
            }
    db.update_collection(name + '._history', hist)

## END OF LINE ##
