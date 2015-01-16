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

class DescribeDeployment(cskcommands.cmd.CSKCommand):

    Description = 'Gets all the high level properties about a Deployment such as status and health'
    API = 'describe_deployment'
    Examples = '''
    csk-get-deployment -d "MyApp20"
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['deployment'])
        print(results)
