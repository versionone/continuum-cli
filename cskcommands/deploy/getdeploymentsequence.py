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

class GetDeploymentSequence(cskcommands.cmd.CSKCommand):

    Description = 'Displays a deployment sequences steps in an readable format'
    API = 'get_deployment_sequence'
    Examples = '''
_To display the sequence steps in plain text_

    ccl-get-deployment-sequence -d "Spring Petclinic 11" -s "Start"

_To display the sequence steps in json format_

    ccl-get-deployment-sequence -d "Spring Petclinic 11" -s "Start" -F json
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
