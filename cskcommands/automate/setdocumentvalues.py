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

class SetDocumentValues(cskcommands.cmd.CSKCommand):

    Description = 'Sets the value for set of provided keys in a document in the MongoDB datastore.'
    API = 'set_document_values'
    Examples = '''
    ccl-set-document-values -c "workflow_stages" -q '{"stage" : "stage 1"}' -u '{"status" : "running", "foo.bar" : "baz"}'
'''
    Options = [Param(name='query', short_name='q', long_name='query',
                     optional=False, ptype='string',
                     doc='A query in JSON format to select the correct Document.'),
               Param(name='collection', short_name='c', long_name='collection',
                     optional=True, ptype='string',
                     doc='A document collection.  "Default" if omitted.'),
               Param(name='updatedoc', short_name='u', long_name='updatedoc',
                     optional=False, ptype='string',
                     doc='A key to look up in the document.')]

    def main(self):
        results = self.call_api(self.API, ['query', 'collection', 'updatedoc'])
        print(results)
