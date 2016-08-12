#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class DescribeTaskParameters(ctmcommands.cmd.CSKCommand):

    Description = 'Describes the parameters defined for a task in a text readable format.'
    API = 'describe_task_parameters'
    Examples = '''
_Print the parameters of the default version of a task_

    ctm-describe-task-parameters -t "mytask01"

_Print the parameters of a specific version of a task_

    ctm-describe-task-parameters -t "new example" -v "2.000"
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
