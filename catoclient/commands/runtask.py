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

    Description = 'Submits a Cato task for execution'
    API = 'run_task'
    Examples = '''
_To submit a particular task_

    cato-run-task -t "mytask01" 

_To submit a particular version of a task_

    cato-run-task -t "mytask01" -v "2.000"

_To submit a task the most verbose logging level_

    cato-run-task -t "mytask01" -l 10

_To submit a task logging on critical errors only_

    cato-run-task -t "mytask01" -l 50

_To submit a task with a certain Cato defined cloud account_

    cato-run-task -t "mytask01" -a "vcloudaccount01"

_To submit a task to run one time in the future_

    cato-run-task -t "mytask01" -r "1/16/2014 9:40"

_To submit a task with parameters as a json string, notice double quotes inside, single quote outside_

    cato-run-task -t "mytask01" -p '[{"name":"param1","values":["hello"]},{"name":"param2","values":["world"]}]'

_To submit a task with parameters in a json file_

    cato-run-task -t "mytask01" -p "~/mytask01_params.json"

'''
    Options = [Param(name='task', short_name='t', long_name='task',
                     optional=False, ptype='string',
                     doc='The ID or Name of the Task to run.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=True, ptype='string',
                     doc='An optional specific Task Version. (Default if omitted.)'),
               Param(name='log_level', short_name='l', long_name='log_level',
                     optional=True, ptype='string',
                     doc='An optional Logging level.  One of 10,20 (default),30,40,50 with 10 most verbose, 50 no logging'),
               Param(name='account', short_name='a', long_name='account',
                     optional=True, ptype='string',
                     doc='The ID or Name of Cloud Account credentials for the Task.'),
               Param(name='options', short_name='o', long_name='options',
                     optional=True, ptype='string',
                     doc='A JSON object containing additional options for the Task.'),
               Param(name='run_later', short_name='r', long_name='run_later',
                     optional=True, ptype='string',
                     doc='The Task will be scheduled to run at the specified date/time.  ex. "7/4/1776 15:30".'),
               Param(name='parameters', short_name='p', long_name='parameters',
                     optional=True, ptype='string',
                     doc='JSON or XML formatted parameters, or a path to a file containing JSON or XML parameters.')
               ]

    def main(self):
        try:
            # first, check if the "parameters" argument is json, xml, or a filename.
            if self.parameters:
                try:
                    import xml.etree.ElementTree as ET
                    ET.fromstring(self.parameters)
                except:  # couldn't parse it.  Maybe it's JSON
                    try:
                        import json
                        json.loads(self.parameters)
                    except:  # nope, last try, maybe it's a file path
                        try:
                            import os
                            fn = os.path.expanduser(self.parameters)
                            with open(fn, 'r') as f_in:
                                if not f_in:
                                    print("Unable to open parameters file [%s]." % fn)
                                self.parameters = f_in.read()
                        except:  # well, nothing worked so let's just whine
                            print ("'parameters' argument was provided, but unable to reconcile parameters as JSON, XML or a valid and existing file.")

            results = self.call_api(self.API, ['task', 'version', 'log_level', 'account', 'service_instance', 'parameters', 'run_later'])
            print(results)
        except ValueError:
            # the results could not be parsed as JSON, just return them
            print(results)
        except Exception as ex:
            raise ex
