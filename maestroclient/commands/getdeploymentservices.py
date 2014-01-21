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

class GetDeploymentServices(catoclient.catocommand.CatoCommand):

    Description = 'Displays a list of service names for a given deployment'
    API = 'get_deployment_services'
    Examples = '''
_To get all service names on a deployment_

    maestro-get-deployment-services  -d "Spring Petclinic 11"

_To get all service names on a deployment with Balancer in the service name_

    maestro-get-deployment-services  -d "Spring Petclinic 11" -f "Balancer"

_To get all service names on a deployment associated with a particular host_

    maestro-get-deployment-services  -d "Spring Petclinic 11" -h "i-a653e588"
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.'),
              Param(name='hostfilter', short_name='h', long_name='hostfilter',
                     optional=True, ptype='string',
                     doc='Will filter results by the ID, Name or Address of any associated Hosts.')
               ]

    def main(self):
        results = self.call_api(self.API, ['deployment', 'filter', 'hostfilter'])
        print(results)
