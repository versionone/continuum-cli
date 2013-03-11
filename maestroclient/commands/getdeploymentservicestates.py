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

class GetDeploymentServiceStates(catoclient.catocommand.CatoCommand):

    Description = 'List all States on a Deployment Service'
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a deployment id or deployment name.'),
               Param(name='service', short_name='v', long_name='service',
                     optional=False, ptype='string',
                     doc='Value can be either a service id or service name.')]

    def main(self):
        results = self.call_api('depMethods/get_deployment_service_states', ['deployment', 'service'])
        print(results)
