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

class GetTaskPlans(cskcommands.cmd.CSKCommand):

    Description = 'Gets a list of queued schedule execution plans for a task.'
    API = 'get_task_plans'
    Examples = '''
_Get all scheduled execution plans for a particular task_

    cato-get-task-plans -t "mytask01"

_Get all scheduled execution plans for a specific verions of a task_

    cato-get-task-plans -t "mytask01" -v "2.000"
'''
    Options = [Param(name='task', short_name='t', long_name='task',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Task.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=True, ptype='string',
                     doc='An optional specific Task Version. (Default if omitted.)')]

    def main(self):
        results = self.call_api(self.API, ['task', 'version'])
        print(results)
