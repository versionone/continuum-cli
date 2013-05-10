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

class ResetPassword(catoclient.catocommand.CatoCommand):

    Description = 'Resets a User Password.'
    Options = [Param(name='password', short_name='p', long_name='password',
                     optional=True, ptype='string',
                     doc='The new password.'),
               Param(name='user', short_name='u', long_name='user',
                     optional=True, ptype='string',
                     doc='The ID or Name of a User Account.'),
               Param(name='generate', short_name='g', long_name='generate',
                     optional=True, ptype='boolean',
                     doc='Generate a new, random password.')
               ]

    def main(self):
        results = self.call_api('sysMethods/reset_password', ['user', 'password', 'generate'])
        print(results)
