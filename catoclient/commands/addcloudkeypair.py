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

class AddCloudKeypair(catoclient.catocommand.CatoCommand):

    Description = 'Adds a Key Pair to a Cloud'
    API = 'add_cloud_keypair'
    Examples = """"""
    Options = [Param(name='cloud', short_name='c', long_name='cloud',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Cloud.'),
               Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the Key Pair.'),
               Param(name='keyfile', short_name='k', long_name='keyfile',
                     optional=False, ptype='string',
                     doc='The Private Key.'),
               Param(name='passphrase', short_name='p', long_name='passphrase',
                     optional=True, ptype='string',
                     doc='A Passphrase for the Key Pair.')
               ]

    def main(self):
        self.private_key = None
        if self.keyfile:
            import os
            fn = os.path.expanduser(self.keyfile)
            with open(fn, 'r') as f_in:
                if not f_in:
                    print("Unable to open file [%s]." % fn)
                self.private_key = f_in.read()

        results = self.call_api(self.API, ['cloud', 'name', 'private_key', 'passphrase'])
        print(results)
