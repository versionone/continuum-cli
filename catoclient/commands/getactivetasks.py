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

class GetActiveTasks(catoclient.catocommand.CatoCommand):

    Description = 'Gets a list of active Task Instances (Submitted, Staged, Pending, Processing).'
    API = 'get_task_instances'
    Examples = '''
_Get all active task instances_

    cato-get-active-tasks

_Get all active task instances that have a status of Processing_

    cato-get-active-tasks -f "Processing"

_Get all active task instance with a particular string in the name_

    cato-get-active-tasks -f "mytask01"

_Limit the number of task instances returned_

    cato-get-active-tasks -r 10
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.'),
               Param(name='records', short_name='r', long_name='records',
                     optional=True, ptype='string',
                     doc='Maximum number of records to return.')
               ]

    def main(self):
        try:
            self.status = "Processing"
            
            results = self.call_api(self.API, ['filter', 'status', 'records'])
            print(results)
        except Exception as ex:
            raise ex
