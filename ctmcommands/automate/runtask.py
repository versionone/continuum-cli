#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class RunTask(ctmcommands.cmd.CSKCommand):

    Description = 'Submits a Task for execution'
    API = 'run_task'
    Examples = '''
_To submit a particular task_

    ctm-run-task -t "mytask01"

_To submit a task the most verbose logging level_

    ctm-run-task -t "mytask01" -l 10

_To submit a task logging on critical errors only_

    ctm-run-task -t "mytask01" -l 50

_To submit a task to run one time in the future_

    ctm-run-task -t "mytask01" -r "1/16/2014 9:40"

_Initial runtime data as a JSON string. (Notice double quotes inside, single quote outside.)_

    ctm-run-task -t "mytask01" -d '{"ship":"Serenity","captain":"Malcolm Reynolds"}'

_Initial runtime data in a JSON file_

    ctm-run-task -t "mytask01" -d "~/mytask01_params.json"

'''
    Options = [Param(name='task', short_name='t', long_name='task',
                     optional=False, ptype='string',
                     doc='The ID or Name of the Task to run.'),
               Param(name='log_level', short_name='l', long_name='log_level',
                     optional=True, ptype='string',
                     doc='An optional Logging level.  One of 10,20 (default),30,40,50 with 10 most verbose, 50 no logging'),
               Param(name='options', short_name='o', long_name='options',
                     optional=True, ptype='string',
                     doc='A JSON object containing additional options for the Task.'),
               Param(name='run_later', short_name='r', long_name='run_later',
                     optional=True, ptype='string',
                     doc='The Task will be scheduled to run at the specified date/time.  ex. "7/4/1776 15:30".'),
               Param(name='parameters', short_name='p', long_name='parameters',
                     optional=True, ptype='string',
                     doc='JSON or XML formatted parameters, or a path to a file containing JSON or XML parameters.'),
               Param(name='initialdata', short_name='i', long_name='initialdata',
                     optional=True, ptype='string',
                     doc='JSON object initial runtime data, or a path to a file containing a JSON object.'),
               ]

    def main(self):
        try:
            # first validate any initial 'data'
            if self.initialdata:
                try:
                    import json
                    json.loads(self.initialdata)
                except:
                    # nope, maybe it's a file path
                    try:
                        import os
                        fn = os.path.expanduser(self.initialdata)
                        with open(fn, 'r') as f_in:
                            if not f_in:
                                print("Unable to open data file [%s]." % fn)
                            self.parameters = f_in.read()
                    except:
                        # well, nothing worked so let's just whine
                        print ("'initialdata' argument was provided, but unable to reconcile data as JSON or an existing and valid file.")

            # then, check if the "parameters" argument is json, xml, or a filename.
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

            results = self.call_api(self.API, ['task', 'log_level', 'options', 'parameters', 'run_later', 'initialdata'])
            print(results)
        except ValueError:
            # the results could not be parsed as JSON, just return them
            print(results)
        except Exception as ex:
            raise ex
