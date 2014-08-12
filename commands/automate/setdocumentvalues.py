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

import commands.catocommand
from commands.param import Param

class SetDocumentValues(commands.catocommand.CatoCommand):

    Description = 'Sets the value for set of provided keys in a document in the MongoDB datastore.'
    API = 'set_document_values'
    Examples = '''
    cato-set-document-values -c "workflow_stages" -q '{"stage" : "stage 1"}' -u '{"status" : "running", "foo.bar" : "baz"}'
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
