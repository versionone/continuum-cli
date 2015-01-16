#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class GetTaskInstanceStatus(cskcommands.cmd.CSKCommand):

    Description = 'Get the status of a Task Instance.'
    API = 'get_task_instance_status'
    Examples = '''
    csk-get-task-instance-status -i 43668
'''
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The Instance ID.')]

    def main(self):
        try:
            results = self.call_api(self.API, ['instance'])
            print(results)
        except Exception as ex:
            raise ex
