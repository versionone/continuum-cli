#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class StopTask(cskcommands.cmd.CSKCommand):

    Description = 'Cancels a task instance in a runnning status'
    API = 'stop_task'
    Examples = '''
    ccl-stop-task -i 43675
'''
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The Task Instance ID to stop.')]

    def main(self):
        try:
            results = self.call_api(self.API, ['instance'])
            print(results)
        except Exception as ex:
            raise ex
