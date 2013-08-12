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

class DeployApplication(catoclient.catocommand.CatoCommand):

    Description = 'Deploys an Application Template.'
    Options = [Param(name='template', short_name='t', long_name='template',
                     optional=False, ptype='string',
                     doc='The Application Template to use.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=False, ptype='string',
                     doc='The Application Template Version.'),
               Param(name='name', short_name='n', long_name='name',
                     optional=True, ptype='string',
                     doc='A name for the new Deployment.'),
               Param(name='desc', short_name='d', long_name='desc',
                     optional=True, ptype='string',
                     doc='A description of the new Deployment.'),
               Param(name='owner', short_name='o', long_name='owner',
                     optional=True, ptype='string',
                     doc='An owner of the new Deployment.')
               ]

    def main(self):
        results = self.call_api('deploy_application', ['name', 'template', 'version', 'owner', 'desc'])
        print(results)
