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

class ResetPassword(cskcommands.cmd.CSKCommand):

    Description = "Resets a User's login password."
    API = 'reset_password'
    Examples = '''
_Reset a User's password to a random password which will be emailed to the user_

    cato-reset-password -u "username1" bob -g

_Reset a User's password to a specified password_

    cato-reset-password -u "username1" -p "passw0rd"
'''
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
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("Are you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['user', 'password', 'generate'])
            print(results)
