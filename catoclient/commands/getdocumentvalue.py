#########################################################################
# 
# Copyright 2013 Cloud Sidekick
# __________________
# 
#  All Rights Reserved.
# 
# NOTICE:  All information contained herein is, and remains
# the property of Cloud Sidekick and its suppliers,
# if any.  The intellectual and technical concepts contained
# herein are proprietary to Cloud Sidekick
# and its suppliers and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Cloud Sidekick.
#
#########################################################################

import catoclient.catocommand
from catoclient.param import Param

class GetDocumentValue(catoclient.catocommand.CatoCommand):

    Description = 'Gets the value for a given key in a Datastore document stored in the MongoDB datastore.'
    API = 'get_document_value'
    Examples = '''
_To get a value from a document based on a specific query_

    cato-get-document-value -c "workflow_stages" -q '{"stage" : "stage 1"}' -k "status"
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
