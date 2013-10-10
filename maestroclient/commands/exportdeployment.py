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

import catoclient.catocommand
from catoclient.param import Param

class ExportDeployment(catoclient.catocommand.CatoCommand):

    Description = 'Exports a Deployed Application as an Application Template.  Optionally create a new version of the source Template.'
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='new_version', short_name='v', long_name='new_version',
                     optional=True, ptype='string',
                     doc='A new Version number for the Template.'),
               Param(name='makeavailable', short_name='a', long_name='makeavailable',
                     optional=True, ptype='boolean',
                     doc='Flag this Application as "Available".')
               ]

    def main(self):
        results = self.call_api('export_deployment', ['deployment', 'new_version', 'makeavailable'])
        print(results)
