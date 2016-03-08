#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class GetTaskInstances(ctmcommands.cmd.CSKCommand):

    Description = 'Get a list of Task Instances and their properties (status, dates, etc.).'
    API = 'get_task_instances'
    Examples = '''
_To retrieve the the last 200 task instances_

    ctm-get-task-instances

_To get all Processing and Submitted task instances, max 200_

    ctm-get-task-instances -s "Processing,Submitted"

_To get a set of task instances between two dates_

    ctm-get-task-instances --from "01/14/2014" --to "01/16/2014"

_To get the last 1000 task instances, overriding the default max of 200_

    ctm-get-task-instances -r 1000

_To get the last 10 task instance for any tasks with a particular string in the name_

    ctm-get-task-instances -r 10 -f "mytask01"
'''
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
            results = self.call_api(self.API, ['filter', 'status', 'from', 'to', 'records'])
            print(results)
        except Exception as ex:
            raise ex
