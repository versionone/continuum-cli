#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class DescribeTaskParameters(cskcommands.cmd.CSKCommand):

    Description = 'Describes the parameters defined for a task in a text readable format.'
    API = 'describe_task_parameters'
    Examples = '''
_Print the parameters of the default version of a task_

    csk-describe-task-parameters -t "mytask01"

_Print the parameters of a specific version of a task_

    csk-describe-task-parameters -t "new example" -v "2.000"
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

