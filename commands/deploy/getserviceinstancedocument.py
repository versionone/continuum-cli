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

class GetServiceInstanceDocument(commands.catocommand.CatoCommand):

    Description = 'Retrieves the json formatted datastore document for a service instance'
    API = 'get_service_instance_document'
    Examples = '''
_To get the datastore document for a service instance and output to a file_

    maestro-get-instance-document -d "MyApp20" -i "Weblogic 3" > weblogic3.json
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
                 Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='Value can be either a Service Instance ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['deployment', 'instance'])
        print(results)
