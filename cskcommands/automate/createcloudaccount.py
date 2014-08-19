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

class CreateCloudAccount(cskcommands.cmd.CSKCommand):

    Description = 'Creates new Cloud Account credentials used to access a cloud endpoint.'
    API = 'create_account'
    Examples = '''
    cato-create-cloud-account -name "vcloudtest" -v "vCloud" -l "tom.thumb@example.com" -p "passw0rd" -d "vcloud-test"
'''
    Options = [Param(name='provider', short_name='v', long_name='provider',
                     optional=False, ptype='string',
                     doc='The name of a supported Cloud Provider. One of: Eucalyptus, vCloud, VMware, AWS, OpenStackAws'),
               Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the new Cloud Account.'),
               Param(name='login', short_name='l', long_name='login',
                     optional=False, ptype='string',
                     doc='Login name (Access Key) for the new Cloud Account.'),
               Param(name='password', short_name='p', long_name='password',
                     optional=False, ptype='string',
                     doc='Password for the new Cloud Account.'),
               Param(name='default_cloud', short_name='d', long_name='default_cloud',
                     optional=False, ptype='string',
                     doc='A default Cloud to be associated with this Account.'),
               Param(name='account_number', short_name='a', long_name='account_number',
                     optional=True, ptype='string',
                     doc='An account number for the New Cloud Account.')
               ]

    def main(self):
        results = self.call_api(self.API, ['provider', 'name', 'login', 'password', 'default_cloud', 'account_number'])
        print(results)
