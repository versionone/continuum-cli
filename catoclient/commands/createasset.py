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

class CreateAsset(catoclient.catocommand.CatoCommand):

    Description = 'Creates a new fixed address Asset in Cato.'
    API = 'create_asset'
    Examples = '''
    cato-create-asset -n "Test 123" -s "Active" -a "10.10.2.2" -d "test02" -t "1433" -u "appuser" -p "passw0rd"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the new Asset.'),
               Param(name='status', short_name='s', long_name='status',
                     optional=True, ptype='string',
                     doc='Status, either "Active" or "Inactive".  ("Active" if omitted.)'),
               Param(name='address', short_name='a', long_name='address',
                     optional=True, ptype='string',
                     doc='Network address of the Asset.'),
               Param(name='port', short_name='t', long_name='port',
                     optional=True, ptype='string',
                     doc='Service port of the Asset.'),
               Param(name='db_name', short_name='d', long_name='db_name',
                     optional=True, ptype='string',
                     doc='A database name.'),
               Param(name='user', short_name='u', long_name='user',
                     optional=True, ptype='string',
                     doc='A User ID.'),
               Param(name='password', short_name='p', long_name='password',
                     optional=True, ptype='string',
                     doc='A Password.'),
               Param(name='shared_credential', short_name='c', long_name='shared_credential',
                     optional=True, ptype='string',
                     doc='A Shared Credential.'),
               Param(name='conn_string', long_name='conn_string',
                     optional=True, ptype='string',
                     doc='A full connection string. (Not typical.)')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'status', 'address', 'port', 'db_name', 'user', 'password', 'shared_credential', 'conn_string'])
        print(results)
