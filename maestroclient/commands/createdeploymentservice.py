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

class CreateDeploymentService(catoclient.catocommand.CatoCommand):

    Description = 'Creates a new Deployment Service.'
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='The name of the new Service.'),
               Param(name='desc', short_name='a', long_name='description',
                     optional=True, ptype='string',
                     doc='The description for this Service..')
               ]

    def main(self):
        results = self.call_api('create_deployment_service', ['deployment', 'name', 'desc'])
        print(results)
