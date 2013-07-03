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

class GetSystemLog(catoclient.catocommand.CatoCommand):

    Description = 'Get the System Log.'
    Options = [Param(name='object_id', short_name='i', long_name='object_id',
                     optional=True, ptype='string',
                     doc='An Object ID filter.'),
               Param(name='object_type', short_name='t', long_name='object_type',
                     optional=True, ptype='string',
                     doc='An Object Type filter.'),
               Param(name='user', short_name='u', long_name='user',
                     optional=True, ptype='string',
                     doc='A User filter.'),
               Param(name='log_type', short_name='l', long_name='log_type',
                     optional=True, ptype='string',
                     doc='A Log Type filter.'),
               Param(name='action', short_name='a', long_name='action',
                     optional=True, ptype='string',
                     doc='An Action filter.'),
               Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.'),
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
            results = self.call_api('get_system_log', ['object_id', 'object_type', 'log_type', 'action', 'filter', 'from', 'to', 'records', 'user'])
            print(results)
        except Exception as ex:
            raise ex
