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

class GetSystemLog(commands.catocommand.CatoCommand):

    Description = 'Get the System Log.'
    API = 'get_system_log'
    Examples = '''
_To get the last 100 denied login attempts_

    cato-get-system-log -l "Security" -a "UserLoginAttempt"

_To get any log entries attributed to the administrator user between two dates_

    cato-get-system-log -u "administrator" -l "Object" --from "1/6/2014" --to "1/7/2014"

_To get the last 300 task modifications_

    cato-get-system-log -t 3 -r 300
'''
    Options = [Param(name='object_id', short_name='i', long_name='object_id',
                     optional=True, ptype='string',
                     doc='An Object ID filter.'),
               Param(name='object_type', short_name='t', long_name='object_type',
                     optional=True, ptype='string',
                     doc='''The integer representation of an internal object type. Can be used with one of the following when log_type = Object: (User = 1, Asset = 2, Task = 3, Schedule = 4, Tag = 7, Image = 8, MessageTemplate = 18, Parameter = 34, Credential = 35, Domain = 36, CloudAccount = 40, Cloud = 41, CloudKeyPair = 45)'''),
               Param(name='user', short_name='u', long_name='user',
                     optional=True, ptype='string',
                     doc='A user name to filter result on.'),
               Param(name='log_type', short_name='l', long_name='log_type',
                     optional=True, ptype='string',
                     doc='The type of log, either Object or Security'),
               Param(name='action', short_name='a', long_name='action',
                     optional=True, ptype='string',
                     doc='''The action that triggered a log entry. One of the following:
(UserLogin, UserLogout, UserLoginAttempt, UserPasswordChange, UserSessionDrop, ObjectAdd, ObjectModify, ObjectDelete, bjectView, ObjectCopy, ConfigChange)'''),
               Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter whereby the results would contain this string'),
               Param(name='from', short_name='', long_name='from',
                     optional=True, ptype='string',
                     doc='A "from" date in the format of m/d/yyyy.'),
               Param(name='to', short_name='', long_name='to',
                     optional=True, ptype='string',
                     doc='A "to" date in the format of m/d/yyyy.'),
               Param(name='records', short_name='r', long_name='records',
                     optional=True, ptype='string',
                     doc='Maximum number of records to return, default is 100.')
               ]

    def main(self):
        try:
            results = self.call_api(self.API, ['object_id', 'object_type', 'log_type', 'action', 'filter', 'from', 'to', 'records', 'user'])
            print(results)
        except Exception as ex:
            raise ex
