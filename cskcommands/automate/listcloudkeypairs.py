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

class ListCloudKeyPairs(cskcommands.cmd.CSKCommand):

    Description = 'Lists cloud endpoint key pairs (ssh private keys)'
    API = 'list_cloud_keypairs'
    Examples = '''
_List all keypair names associated with the AWS us-east-1 cloud endpoint_

    csk-list-cloud-keypairs -c "us-east-1"
'''
    Options = [Param(name='cloud', short_name='c', long_name='cloud',
                     optional=False, ptype='string',
                     doc='A Cloud ID or Name.')
               ]

    def main(self):
        results = self.call_api(self.API, ['cloud'])
        print(results)

