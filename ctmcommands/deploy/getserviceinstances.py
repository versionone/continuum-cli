#########################################################################
# 
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
# 
# 
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class GetServiceInstances(ctmcommands.cmd.CSKCommand):

    Description = 'Lists Service Instances from an Deployment Service'
    API = 'get_service_instances'
    Examples = '''
_To list all service instances for a deployment_

    ctm-get-service-instances -d "MyApp20"

_To list all service instances for a service on a deployment_

    ctm-get-service-instances -d "MyApp20" -s "Weblogic
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
