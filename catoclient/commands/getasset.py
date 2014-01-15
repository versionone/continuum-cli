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

class GetAsset(catoclient.catocommand.CatoCommand):

    Description = 'Prints the properties of a Cato defined fixed asset'
    API = 'get_asset'
    Examples = '''
        cato-get-asset -a "database001"
    '''
    Options = [Param(name='asset', short_name='a', long_name='asset',
                     optional=False, ptype='string',
                     doc='The ID or Name of an Asset.')
               ]

    def main(self):
        results = self.call_api(self.API, ['asset'])
        print(results)
