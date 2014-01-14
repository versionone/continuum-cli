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

class CreateCredential(catoclient.catocommand.CatoCommand):

    Description = 'Creates a new set of Shared Credentials in Cato that can be used to log into other systems.'
    API = 'create_credential'
    Examples = '''
        cato-create-credential -n "adminuser" -d "Administrator User" -u "root" -p "passw0rd"
    '''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the new Credential, must be unique.'),
               Param(name='description', short_name='d', long_name='description',
                     optional=False, ptype='string',
                     doc='Credential description or long name.'),
               Param(name='username', short_name='u', long_name='username',
                     optional=False, ptype='string',
                     doc='The user/login name.'),
               Param(name='password', short_name='p', long_name='password',
                     optional=False, ptype='string',
                     doc='The password/privatekey.'),
               Param(name='domain', short_name='o', long_name='domain',
                     optional=True, ptype='string',
                     doc='An optional domain name for the credential.'),
               Param(name='privileged', short_name='v', long_name='privileged',
                     optional=True, ptype='string',
                     doc='Additional password required to put certain Cisco IOS devices into "privileged" mode.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'description', 'username', 'password', 'domain', 'privileged'])
        print(results)
