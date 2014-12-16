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

class GetDeploymentSequence(cskcommands.cmd.CSKCommand):

    Description = 'Displays a deployment sequences steps in an readable format'
    API = 'get_deployment_sequence'
    Examples = '''
_To display the sequence steps in plain text_

    csk-get-deployment-sequence -d "Spring Petclinic 11" -s "Start"

_To display the sequence steps in json format_

    csk-get-deployment-sequence -d "Spring Petclinic 11" -s "Start" -F json
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
