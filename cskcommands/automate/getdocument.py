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

class GetDocument(cskcommands.cmd.CSKCommand):

    Description = '''Gets a datastore document based on a MongoDB query. For query syntax, see the 
                    MongDB find() syntax http://docs.mongodb.org/manual/reference/method/db.collection.find'''
    API = 'get_document'
    Examples = '''
_To get the json document from a collection based on a specific query_

    ccl-get-document -c "workflow_stages" -q '{"stage" : "stage 1"}'
'''
    Options = [Param(name='query', short_name='q', long_name='query',
                     optional=False, ptype='string',
                     doc='A query in JSON format.'),
               Param(name='collection', short_name='c', long_name='collection',
                     optional=True, ptype='string',
                     doc='A document collection.  "Default" if omitted.')]

    def main(self):
        results = self.call_api(self.API, ['query', 'collection'])
        print(results)
