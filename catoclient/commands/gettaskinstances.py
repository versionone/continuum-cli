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

class GetTaskInstances(catoclient.catocommand.CatoCommand):

    Description = 'Get a list of Cato Task Instances.'
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.'),
               Param(name='status', short_name='s', long_name='status',
                     optional=True, ptype='string',
                     doc='A comma separated list of statuses.'),
               Param(name='from', short_name='', long_name='from',
                     optional=True, ptype='string',
                     doc='A "from" date.'),
               Param(name='to', short_name='', long_name='to',
                     optional=True, ptype='string',
                     doc='A "to" date.'),
               Param(name='records', short_name='r', long_name='records',
                     optional=True, ptype='string',
                     doc='Maximum number of records to return.')
               ]

    def main(self):
        try:
            results = self.call_api('get_task_instances', ['filter', 'status', 'from', 'to', 'records'])
            print(results)
        except Exception as ex:
            raise ex
