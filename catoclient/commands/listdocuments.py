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

class ListDocuments(catoclient.catocommand.CatoCommand):

    Description = 'Lists documents in the MongoDB datastore'
    API = 'list_documents'
    Examples = '''
_To list all documents in a specific collection_

    cato-list-documents -c "workflow_stages"

_To list all documents in a specific collection that have a string match_

    cato-list-documents -c "workflow_stages" -f "stage 1"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                    doc='''A string to use to filter the resulting data. Any row of
                            data that has one field contains the string will be returned.'''),
               Param(name='collection', short_name='c', long_name='collection',
                     optional=True, ptype='string',
                     doc='''A document collection.  "Default" collection will be used 
                        if omitted.''')]

    def main(self):
        results = self.call_api(self.API, ['collection', 'filter'])
        print(results)
