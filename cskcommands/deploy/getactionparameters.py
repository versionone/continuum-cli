#########################################################################
# Copyright 2011 Cloud Sidekick
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class GetActionParameters(cskcommands.cmd.CSKCommand):

    Description = 'Retreives a json formatted Parameters template for an Action.'
    API = 'get_action_parameters'
    Examples = '''
_To get a parameters template file for a particular action on a deployment, redirecting to a file_

    maestro-get-action-parameters -d "MyApp10" -v "Weblogic" -a "Trim Logfiles" > trim_logfiles.json
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

