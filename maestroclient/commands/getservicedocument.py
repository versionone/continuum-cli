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

class GetServiceDocument(catoclient.catocommand.CatoCommand):

    Description = 'Retrieves a json formatted datastore document for a service on a deployment'
    API = 'get_service_document'
    Examples = '''
_To retieve the datastore document for a service and output it to a file_

    maestro-get-service-document -d "MyApp20" -s "Weblogic" > weblogic.json
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
                 Param(name='service', short_name='s', long_name='service',
                     optional=False, ptype='string',
                     doc='Value can be either a Service ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['deployment', 'service'])
        print(results)
