#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class GetTaskInstance(ctmcommands.cmd.CSKCommand):

    Description = 'Get the properties of a Task Instance such as status, submitted and completed dates, etc.'
    API = 'get_task_instance'
    Examples = '''
    ctm-get-task-instance -i 43669
'''
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The Task Instance number.')]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
