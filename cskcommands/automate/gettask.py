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

class GetTask(cskcommands.cmd.CSKCommand):

    Description = 'Prints the properties of a Task'
    API = 'get_task'
    Examples = '''
_To print the high level properties of a specific Task version_

    cato-get-task -t "mytask01" -v "2.000"

_To print the properties and code of the default version of a Task_

    cato-get-task -t "new example" -i
'''
    Options = [Param(name='task', short_name='t', long_name='task',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Task.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=True, ptype='string',
                     doc='An optional specific Task Version. (Default if omitted.)'),
              Param(name='include_code', short_name='i', long_name='include_code',
                     optional=True, ptype='boolean',
                     doc='Include all task step code, if output_format is "json" or "xml".')]

    def main(self):
        results = self.call_api(self.API, ['task', 'version', 'include_code'])
        print(results)

