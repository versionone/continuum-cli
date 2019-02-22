#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class DescribeTaskParameters(ctmcommands.cmd.CSKCommand):

    Description = 'Describes the parameters defined for a task in a text readable format.'
    API = 'describe_task_parameters'
    Examples = '''
_Print the parameters of a task_

    ctm-describe-task-parameters -t "mytask01"
'''
    Options = [Param(name='task', short_name='t', long_name='task',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Task.'),
                     doc='An optional specific Task Version. (Default if omitted.)')]

    def main(self):
        results = self.call_api(self.API, ['task'])
        print(results)
