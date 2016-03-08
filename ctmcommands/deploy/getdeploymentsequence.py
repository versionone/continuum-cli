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

class GetDeploymentSequence(ctmcommands.cmd.CSKCommand):

    Description = 'Displays a deployment sequences steps in an readable format'
    API = 'get_deployment_sequence'
    Examples = '''
_To display the sequence steps in plain text_

    ctm-get-deployment-sequence -d "Spring Petclinic 11" -s "Start"

_To display the sequence steps in json format_

    ctm-get-deployment-sequence -d "Spring Petclinic 11" -s "Start" -F json
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='sequence', short_name='s', long_name='sequence',
                     optional=False, ptype='string',
                     doc='A Sequence name on this Deployment.')]

    def main(self):
        results = self.call_api(self.API, ['deployment', 'sequence'])
        print(results)
