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

class CreateTask(catoclient.catocommand.CatoCommand):

    Description = 'Creates a new Task.'
    API = 'create_task'
    Examples = ''''''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the new Task.'),
               Param(name='desc', short_name='d', long_name='desc',
                     optional=True, ptype='string',
                     doc='A description of the new Task.'),
               Param(name='code', short_name='c', long_name='code',
                     optional=True, ptype='string',
                     doc='A code for the new Task.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'code', 'desc'])
        print(results)
