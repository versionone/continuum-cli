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

class AddDeploymentServiceState(catoclient.catocommand.CatoCommand):

    Description = 'Adds a State to a Deployment Service'
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a deployment id or deployment name.'),
               Param(name='service', short_name='v', long_name='service',
                     optional=False, ptype='string',
                     doc='Value can be either a service id or service name.'),
               Param(name='state', short_name='s', long_name='state',
                     optional=False, ptype='string',
                     doc='The name of this State.'),
               Param(name='nextstate', short_name='n', long_name='nextstate',
                     optional=True, ptype='string',
                     doc='The name of the State following this State.'),
               Param(name='task', short_name='t', long_name='task',
                     optional=True, ptype='string',
                     doc='ID, Name or Code of a Task.'),
               Param(name='version', short_name='tv', long_name='version',
                     optional=True, ptype='string',
                     doc='Optional Version of the Task. ("Default" if omitted.)')]

    def main(self):
        results = self.call_api('depMethods/add_deployment_service_state', ['deployment', 'service', 'state', 'nextstate', 'task', 'version'])
        print(results)
