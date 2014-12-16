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
