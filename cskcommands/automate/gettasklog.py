#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class GetTaskLog(cskcommands.cmd.CSKCommand):

    Description = 'Retrieve the task instance log from the database'
    API = 'get_task_log'
    Examples = '''
    ccl-get-task-log -i 43667
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
