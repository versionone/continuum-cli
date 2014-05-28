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

class GetDocument(catoclient.catocommand.CatoCommand):

    Description = '''Gets a datastore document based on a MongoDB query. For query syntax, see the 
                    MongDB find() syntax http://docs.mongodb.org/manual/reference/method/db.collection.find'''
    API = 'get_document'
    Examples = '''
_To get the json document from a collection based on a specific query_

    cato-get-document -c "workflow_stages" -q '{"stage" : "stage 1"}'
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
