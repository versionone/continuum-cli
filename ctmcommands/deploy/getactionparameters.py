#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class GetActionParameters(ctmcommands.cmd.CSKCommand):

    Description = 'Retreives a json formatted Parameters template for an Action.'
    API = 'get_action_parameters'
    Examples = '''
_To get a parameters template file for a particular action on a deployment, redirecting to a file_

    ctm-get-action-parameters -d "MyApp10" -v "Weblogic" -a "Trim Logfiles" > trim_logfiles.json
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='action', short_name='a', long_name='action',
                     optional=False, ptype='string',
                     doc='Name of the Action.'),
               Param(name='service', short_name='v', long_name='service',
                     optional=True, ptype='string',
                     doc='Value can be either a Service ID or Name.'),
               Param(name='basic', short_name='b', long_name='basic',
                     optional=True, ptype='boolean',
                     doc='Get a basic template with no descriptive details or default values.')]
               

    def main(self):
        results = self.call_api(self.API, ['deployment', 'action', 'service', 'basic'])
        print(results)

