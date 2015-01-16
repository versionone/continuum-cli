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

class GetServiceInstanceDocument(cskcommands.cmd.CSKCommand):

    Description = 'Retrieves the json formatted datastore document for a service instance'
    API = 'get_service_instance_document'
    Examples = '''
_To get the datastore document for a service instance and output to a file_

    csk-get-instance-document -d "MyApp20" -i "Weblogic 3" > weblogic3.json
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
