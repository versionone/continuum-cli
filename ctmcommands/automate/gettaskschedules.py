#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class GetTaskSchedules(ctmcommands.cmd.CSKCommand):

    Description = 'Gets a list of schedule definitions for a given task.'
    API = 'get_task_schedules'
    Examples = '''
_To list the schedules for a particular task_

    ctm-get-task-schedules -t "mytask01"
'''
    Options = [Param(name='task', short_name='t', long_name='task',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Task.')]

    def main(self):
        results = self.call_api(self.API, ['task'])
        print(results)
