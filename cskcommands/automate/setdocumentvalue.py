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

class SetDocumentValue(cskcommands.cmd.CSKCommand):

    Description = 'Sets the value for a given key in a document in the MongoDB datastore.'
    API = 'set_document_value'
    Examples = '''
    csk-set-document-value -c "workflow_stages" -q '{"stage" : "stage 1"}' -k "status" -v "running"
'''
    Options = [Param(name='query', short_name='q', long_name='query',
                     optional=False, ptype='string',
                     doc='A query in JSON format to select the correct Document.'),
               Param(name='collection', short_name='c', long_name='collection',
                     optional=True, ptype='string',
                     doc='A document collection.  "Default" if omitted.'),
               Param(name='lookupkey', short_name='k', long_name='lookupkey',
                     optional=False, ptype='string',
                     doc='A key to look up in the document.'),
               Param(name='value', short_name='v', long_name='value',
                     optional=True, ptype='string',
                     doc='A value to set.')]

    def main(self):
        results = self.call_api(self.API, ['query', 'collection', 'lookupkey', 'value'])
        print(results)
