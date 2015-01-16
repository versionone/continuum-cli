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

class DeployApplication(cskcommands.cmd.CSKCommand):

    Description = 'Creates a deployment from deployment template. Does not run the start sequence'
    API = 'deploy_application'
    Examples = '''
_To create the deployment from an application template and give it a specific name_

    csk-deploy-application -t "MyApp" -v "1" -n "Test Actions Dev 12"

_To create the deployment from an application template accept the default name, with description_

    csk-deploy-application -t "MyApp" -v "1" -d "My Application"
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
