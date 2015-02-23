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

class ExportDeployment(cskcommands.cmd.CSKCommand):

    Description = 'Exports a Deployed Application as an Application Template.  Optionally create a new version of the source Template.'
    API = 'export_deployment'
    Examples = '''
_To export a json representation of a deloyed application to a file_

    ccl-export-deployment -d "MyApp20" > myapp.json 

_To create a new application template from a deployed application and immediately make it available in the app store_

    ccl-export-deployment -d "MyApp20" -v "3" -a
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
