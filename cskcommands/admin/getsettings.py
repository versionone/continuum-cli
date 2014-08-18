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

class GetSettings(cskcommands.cmd.CSKCommand):

    Description = 'Gets all the configuration settings from the database in json format'
    API = 'get_settings'
    Examples = '''
_To get all config settings in text format_

    cato-get-settings

_To get all config settings in json format_

    cato-get-settings -F "json"

_To get the settings only for the messenger module_

    cato-get-settings -m "Messenger"

_To get a list of the module names available in the settings configurations_
   
    cato-get-settings |grep -v "^ "|grep -v "^$"
'''
    Options = [Param(name='module', short_name='m', long_name='module',
                     optional=True, ptype='string',
                     doc='Filter to a specific module.')
               ]

    def main(self):
        results = self.call_api(self.API, ['module'])
        print(results)
