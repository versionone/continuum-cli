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

class GetServiceInstances(cskcommands.cmd.CSKCommand):

    Description = 'Lists Service Instances from an Deployment Service'
    API = 'get_service_instances'
    Examples = '''
_To list all service instances for a deployment_

    ccl-get-service-instances -d "MyApp20"

_To list all service instances for a service on a deployment_

    ccl-get-service-instances -d "MyApp20" -s "Weblogic
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
                 Param(name='service', short_name='s', long_name='service',
                     optional=True, ptype='string',
                     doc='Value can be either a Service ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['deployment', 'service'])
        print(results)
