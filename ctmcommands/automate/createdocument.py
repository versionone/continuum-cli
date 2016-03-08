#########################################################################
# 
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
# 
# 
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class CreateDocument(ctmcommands.cmd.CSKCommand):

    Description = 'Creates a new Datastore document in the MongoDB datastore.'
    API = 'create_document'
    Examples = r'''
_Single quotes wrapping the json document, double inside_

    ctm-create-document -c "inventory" -t '{ "type": "book", "item": "notebook", "qty": 40 }'

_Double quotes wrapping the json document, double quotes escaped inside_

    ctm-create-document -c "inventory" -t "{ \"type\": \"book\", \"item\": \"notebook\", \"qty\": 40 }"
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
