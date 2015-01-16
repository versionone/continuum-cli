#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class GetTaskSchedules(cskcommands.cmd.CSKCommand):

    Description = 'Gets a list of schedule definitions for a given task.'
    API = 'get_task_schedules'
    Examples = '''
_To list the schedules for a particular task_

    csk-get-task-schedules -t "mytask01"

_To list the schedules for a particular version of a task_

    csk-get-task-schedules -t "new example" -v "2.000"
'''
    Options = [Param(name='task', short_name='t', long_name='task',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Task.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=True, ptype='string',
                     doc='An optional specific Task Version. (Default if omitted.)')]

    def main(self):
        results = self.call_api(self.API, ['task', 'version'])
        print(results)
