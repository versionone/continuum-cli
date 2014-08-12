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

import commands.catocommand
from commands.param import Param

class DeployApplication(commands.catocommand.CatoCommand):

    Description = 'Creates a deployment from deployment template. Does not run the start sequence'
    API = 'deploy_application'
    Examples = '''
_To create the deployment from an application template and give it a specific name_

    maestro-deploy-application -t "MyApp" -v "1" -n "Test Actions Dev 12"

_To create the deployment from an application template accept the default name, with description_

    maestro-deploy-application -t "MyApp" -v "1" -d "My Application"
'''
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
                     doc='A description of the new Deployment.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'template', 'version', 'owner', 'desc'])
        print(results)
