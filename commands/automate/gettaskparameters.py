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

class GetTaskParameters(commands.catocommand.CatoCommand):

    Description = 'Gets a json formatted parameters template for a task.'
    API = 'get_task_parameters'
    Examples = '''
_To get the parameters of the default version of a task and redirect to a file_

    cato-get-task-parameters -t "mytask01" > mytask01_params.json

_To get the parameters of a specific version of a task_

    cato-get-task-parameters -t "new example" -v "2.000"

_To get the most basic parameter template of a task, minus descriptions and defaults_

    cato-get-task-parameters -t "new example" -b
'''
    Options = [Param(name='task', short_name='t', long_name='task',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Task.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=True, ptype='string',
                     doc='An optional specific Task Version. (Default if omitted.)'),
               Param(name='basic', short_name='b', long_name='basic',
                     optional=True, ptype='boolean',
                     doc='Get a basic template with no descriptive details or default values.')]
               

    def main(self):
        results = self.call_api(self.API, ['task', 'version', 'basic'])
        print(results)

