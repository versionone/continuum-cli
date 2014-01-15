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

class SetDocumentValue(catoclient.catocommand.CatoCommand):

    Description = 'Sets the value for a given key in a document in the MongoDB datastore.'
    API = 'set_document_value'
    Examples = '''
    cato-set-document-value -c "workflow_stages" -q '{"stage" : "stage 1"}' -k "status" -v "running"
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
