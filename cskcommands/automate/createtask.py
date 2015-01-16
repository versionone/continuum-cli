#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class CreateTask(cskcommands.cmd.CSKCommand):

    Description = 'Creates a new blank Task object.'
    API = 'create_task'
    Examples = '''
    csk-create-task -n "mytask" -d "This is a sample task" -c "test2001"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the new Task.'),
               Param(name='desc', short_name='d', long_name='desc',
                     optional=True, ptype='string',
                     doc='A description of the new Task.'),
               Param(name='code', short_name='c', long_name='code',
                     optional=True, ptype='string',
                     doc='A code for the new Task.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'code', 'desc'])
        print(results)
