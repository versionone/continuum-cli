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

class RunTask(catoclient.catocommand.CatoCommand):

    Description = 'Runs a Cato Task.'
    Options = [Param(name='task', short_name='t', long_name='task',
                     optional=False, ptype='string',
                     doc='The ID or Name of the Task to run.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=True, ptype='string',
                     doc='An optional specific Task Version. (Default if omitted.)'),
               Param(name='log_level', short_name='l', long_name='log_level',
                     optional=True, ptype='string',
                     doc='An optional Logging level.  (Normal if omitted.)'),
               Param(name='account', short_name='a', long_name='account',
                     optional=True, ptype='string',
                     doc='The ID or Name of Cloud Account credentials for the Task.'),
               Param(name='service_instance', short_name='i', long_name='service_instance',
                     optional=True, ptype='string',
                     doc='The ID of a Service Instance.'),
               Param(name='parameterfile', short_name='p', long_name='parameterfile',
                     optional=True, ptype='string',
                     doc='The file name of a Parameter XML file.')
               ]

    def main(self):
        try:
            # first, we need to load the parameters xml from a file
            self.parameters = None
            if self.parameterfile:
                import os
                fn = os.path.expanduser(self.parameterfile)
                with open(fn, 'r') as f_in:
                    if not f_in:
                        print("Unable to open file [%s]." % fn)
                    self.parameters = f_in.read()

            results = self.call_api('taskMethods/run_task', ['task', 'version', 'log_level', 'account', 'service_instance', 'parameters'])
            print(results)
        except ValueError:
            # the results could not be parsed as JSON, just return them
            print(results)
        except Exception as ex:
            raise ex
