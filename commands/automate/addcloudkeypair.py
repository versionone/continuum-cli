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

import commands.catocommand
from commands.param import Param

class AddCloudKeypair(commands.catocommand.CatoCommand):

    Description = 'Adds a key pair (ssh private key) to a defined cloud endpoint'
    API = 'add_cloud_keypair'
    Examples = """
_To add a private key to the us-east-1 cloud endpoint_ 

    cato-add-cloud-keypair -c "us-east-1" -n "privatekey01" -k ~/privatekey01.pem

_To add a private key with a passphrase to the cloud endpoint_

    cato-add-cloud-keypair -c "us-east-1" -n "privatekey01" -k ~/.ssh/csk_www.pem -p "passw0rd"
"""
    Options = [Param(name='cloud', short_name='c', long_name='cloud',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Cloud endpoint.'),
               Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the Key Pair.'),
               Param(name='keyfile', short_name='k', long_name='keyfile',
                     optional=False, ptype='string',
                     doc='The path and filename for the private key pem file.'),
               Param(name='passphrase', short_name='p', long_name='passphrase',
                     optional=True, ptype='string',
                     doc='A Passphrase for the private key.')
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
