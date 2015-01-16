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

class GetDeploymentSequences(cskcommands.cmd.CSKCommand):

    Description = 'Displays all deployment sequences in a readable format.'
    API = 'get_deployment_sequences'
    Examples = '''
_To retrieve all sequences and their steps and display in text format_
    csk-get-deployment-sequences -d "Spring Petclinic 11"

_To retrieve all sequences  and their steps filtered by sequence name_
    csk-get-deployment-sequences -d "Spring Petclinic 11" -f "Terminate"
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.')]

    def main(self):
        results = self.call_api(self.API, ['deployment', 'filter'])
        print(results)
