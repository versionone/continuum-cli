#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class GetTaskPlans(ctmcommands.cmd.CSKCommand):

    Description = 'Gets a list of queued schedule execution plans for a task.'
    API = 'get_task_plans'
    Examples = '''
_Get all scheduled execution plans for a particular task_

    ctm-get-task-plans -t "mytask01"

_Get all scheduled execution plans for a specific verions of a task_

    ctm-get-task-plans -t "mytask01" -v "2.000"
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
