#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class GetTaskLog(ctmcommands.cmd.CSKCommand):

    Description = 'Retrieve the task instance log from the database'
    API = 'get_task_log'
    Examples = '''
    ctm-get-task-log -i 43667
'''
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The Task Instance number.')]

    def main(self):
        try:
            results = self.call_api(self.API, ['instance'])
            print(results)
        except Exception as ex:
            raise ex
