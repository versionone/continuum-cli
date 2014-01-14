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

class CreateDocument(catoclient.catocommand.CatoCommand):

    Description = 'Creates a new Datastore document in the Cato MongoDB datastore.'
    API = 'create_document'
    Examples = '''
        _Single quotes wrapping the json document, double inside_
        cato-create-document -c "inventory" -t '{ "type": "book", "item": "notebook", "qty": 40 }'

        _Double quotes wrapping the json document, double quotes escaped inside_
        cato-create-document -c "inventory" -t "{ \"type\": \"book\", \"item\": \"notebook\", \"qty\": 40 }"
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
