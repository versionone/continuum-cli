#########################################################################
# Copyright 2019 VersionOne
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
'''
    Options = [Param(name='task', short_name='t', long_name='task',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Task.')]

    def main(self):
        results = self.call_api(self.API, ['task'])
        print(results)
