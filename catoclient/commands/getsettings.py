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

class GetSettings(catoclient.catocommand.CatoCommand):

    Description = 'Gets all the Cato settings.'
    Options = [Param(name='module', short_name='m', long_name='module',
                     optional=True, ptype='string',
                     doc='Filter to a specific Cato module.')
               ]

    def main(self):
        results = self.call_api('sysMethods/get_settings', ['module'])
        print(results)
