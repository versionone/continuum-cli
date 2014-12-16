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

class CreateTag(cskcommands.cmd.CSKCommand):

    Description = 'Creates a new Tag to be used to associate objects with one another.'
    API = 'create_tag'
    Examples = '''
    csk-create-tag -n "staging01" -d "staging environment 1"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='The name of the new Tag.  (AlphaNumeric ONLY. Cannot contain spaces, punctuation or special characters.)'),
               Param(name='description', short_name='d', long_name='description',
                     optional=True, ptype='string',
                     doc='Tag description.')]

    def main(self):
        results = self.call_api(self.API, ['name', 'description'])
        print(results)
