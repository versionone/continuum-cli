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
import json

class ScheduleTasks(commands.catocommand.CatoCommand):

    Description = 'Schedules one or more Tasks using a json template file.'
    API = 'schedule_tasks'
    Examples = '''
    cato-schedule-tasks -s ./schedule_template.json
'''
    Options = [Param(name='schedulefile', short_name='s', long_name='schedulefile',
                     optional=False, ptype='string',
                     doc='''The path to a json formatted schedule definition file. See the schedule_tasks API documentation for the format of the file.''')
               ]

    def main(self):
        try:
            # first, we need to load the schedule definition
            self.tasks = None
            if self.schedulefile:
                import os
                fn = os.path.expanduser(self.schedulefile)
                with open(fn, 'r') as f_in:
                    if not f_in:
                        print("Unable to open file [%s]." % fn)
                    self.tasks = f_in.read()

            results = self.call_api(self.API, ['tasks'])
            print(results)
        except Exception as ex:
            raise ex
