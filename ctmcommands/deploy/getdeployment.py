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

class GetDeployment(ctmcommands.cmd.CSKCommand):

    Description = 'Prints the high level properties of a deployment such as state and health'
    API = 'get_deployment'
    Examples = '''
    ctm-get-deployment -d "MyApp20"
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['deployment'])
        print(results)

