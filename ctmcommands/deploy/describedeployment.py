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

class DescribeDeployment(ctmcommands.cmd.CSKCommand):

    Description = 'Gets all the high level properties about a Deployment such as status and health'
    API = 'describe_deployment'
    Examples = '''
    ctm-get-deployment -d "MyApp20"
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['deployment'])
        print(results)
