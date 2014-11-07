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

import cskcommands.cmd
from cskcommands.param import Param

class AddDeployment(cskcommands.cmd.CSKCommand):

    Description = 'Creates a new Deployment.'
    API = 'add_deployment'
    Examples = ''''''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='Name for the new Deployment.'),
               Param(name='description', short_name='d', long_name='description',
                     optional=True, ptype='string',
                     doc='Description of this Application.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'description'])
        print(results)
