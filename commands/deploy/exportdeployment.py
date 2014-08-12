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

import commands.catocommand
from commands.param import Param

class ExportDeployment(commands.catocommand.CatoCommand):

    Description = 'Exports a Deployed Application as an Application Template.  Optionally create a new version of the source Template.'
    API = 'export_deployment'
    Examples = '''
_To export a json representation of a deloyed application to a file_

    maestro-export-deployment -d "MyApp20" > myapp.json 

_To create a new application template from a deployed application and immediately make it available in the app store_

    maestro-export-deployment -d "MyApp20" -v "3" -a
'''
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
        results = self.call_api(self.API, ['deployment', 'new_version', 'makeavailable'])
        print(results)
