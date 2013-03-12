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

import catoclient.catocommand
from catoclient.param import Param

class GetActionParameters(catoclient.catocommand.CatoCommand):

    Description = 'Gets a Parameters template for an Action.'
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either an deployment id or deployment name.'),
               Param(name='action', short_name='a', long_name='action',
                     optional=False, ptype='string',
                     doc='Name of the Action.'),
               Param(name='service', short_name='v', long_name='service',
                     optional=True, ptype='string',
                     doc='Value can be either a service id or service name.'),
               Param(name='basic', short_name='b', long_name='basic',
                     optional=True, ptype='boolean',
                     doc='Get a basic template with no descriptive details or default values.')]
               

    def main(self):
        results = self.call_api('depMethods/get_action_parameters', ['deployment', 'action', 'basic'])
        print(results)

