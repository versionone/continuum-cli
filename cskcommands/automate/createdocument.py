#########################################################################
# 
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
# 
# 
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class CreateDocument(cskcommands.cmd.CSKCommand):

    Description = 'Creates a new Datastore document in the MongoDB datastore.'
    API = 'create_document'
    Examples = r'''
_Single quotes wrapping the json document, double inside_

    csk-create-document -c "inventory" -t '{ "type": "book", "item": "notebook", "qty": 40 }'

_Double quotes wrapping the json document, double quotes escaped inside_

    csk-create-document -c "inventory" -t "{ \"type\": \"book\", \"item\": \"notebook\", \"qty\": 40 }"
'''
    Options = [Param(name='collection', short_name='c', long_name='collection',
                     optional=True, ptype='string',
                     doc='The MongoDB collection in which to store the data.  "Default" if omitted.'),
               Param(name='template', short_name='t', long_name='template',
                     optional=True, ptype='string',
                     doc='A valid JSON document.  A blank document will be created if omitted.')]

    def main(self):
        results = self.call_api(self.API, ['template', 'collection'])
        print(results)
