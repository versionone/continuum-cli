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

class UpdateCloud(catoclient.catocommand.CatoCommand):

    Description = 'Updates a Cloud.'
    API = 'update_cloud'
    Examples = ''''''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Cloud.'),
               Param(name='apiurl', short_name='u', long_name='apiurl',
                     optional=True, ptype='string',
                     doc='URL of the Cloud API endpoint.'),
               Param(name='apiprotocol', short_name='p', long_name='apiprotocol',
                     optional=True, ptype='string',
                     doc='Cloud API endpoint protocol.'),
               Param(name='default_account', short_name='d', long_name='default_account',
                     optional=True, ptype='string',
                     doc='A default Account to be associated with this Cloud.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'apiurl', 'apiprotocol', 'default_account'])
        print(results)
