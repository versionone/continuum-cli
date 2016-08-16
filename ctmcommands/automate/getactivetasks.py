#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class GetActiveTasks(ctmcommands.cmd.CSKCommand):

    Description = 'Gets a list of active Task Instances (Submitted, Staged, Pending, Processing).'
    API = 'get_task_instances'
    Examples = '''
_Get all active task instances_

    ctm-get-active-tasks

_Get all active task instances that have a status of Processing_

    ctm-get-active-tasks -f "Processing"

_Get all active task instance with a particular string in the name_

    ctm-get-active-tasks -f "mytask01"

_Limit the number of task instances returned_

    ctm-get-active-tasks -r 10
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
