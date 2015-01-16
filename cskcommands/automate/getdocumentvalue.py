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

class GetDocumentValue(cskcommands.cmd.CSKCommand):

    Description = 'Gets the value for a given key in a Datastore document stored in the MongoDB datastore.'
    API = 'get_document_value'
    Examples = '''
_To get a value from a document based on a specific query_

    csk-get-document-value -c "workflow_stages" -q '{"stage" : "stage 1"}' -k "status"
'''
    Options = [Param(name='query', short_name='q', long_name='query',
                     optional=False, ptype='string',
                     doc='A query in JSON format to select the correct Document.'),
               Param(name='lookupkey', short_name='k', long_name='lookupkey',
                     optional=False, ptype='string',
                     doc='A key to look up.  Returns the entire document if omitted.'),
               Param(name='collection', short_name='c', long_name='collection',
                     optional=True, ptype='string',
                     doc='A document collection.  "Default" if omitted.')]

    def main(self):
        results = self.call_api(self.API, ['query', 'lookupkey', 'collection'])
        print(results)
