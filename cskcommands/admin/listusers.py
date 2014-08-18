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

class ListUsers(cskcommands.cmd.CSKCommand):

    Description = 'Lists Users'
    API = 'list_users'
    Examples = '''
_List all users_

    cato-list-users

_List all users with Administrator role_

    cato-list-users -f "Administrator"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='''A string to use to filter the resulting data. Any row of data that has one field contains the string will be returned.''')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)

