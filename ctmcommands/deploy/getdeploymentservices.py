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

class GetDeploymentServices(ctmcommands.cmd.CSKCommand):

    Description = 'Displays a list of service names for a given deployment'
    API = 'get_deployment_services'
    Examples = '''
_To get all service names on a deployment_

    ctm-get-deployment-services  -d "Spring Petclinic 11"

_To get all service names on a deployment with Balancer in the service name_

    ctm-get-deployment-services  -d "Spring Petclinic 11" -f "Balancer"

_To get all service names on a deployment associated with a particular host_

    ctm-get-deployment-services  -d "Spring Petclinic 11" -h "i-a653e588"
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='Filter results with part of the string in the service name'),
              Param(name='hostfilter', short_name='h', long_name='hostfilter',
                     optional=True, ptype='string',
                     doc='Will filter results by the ID, Name or Address of any associated Hosts.')
               ]

    def main(self):
        results = self.call_api(self.API, ['deployment', 'filter', 'hostfilter'])
        print(results)
