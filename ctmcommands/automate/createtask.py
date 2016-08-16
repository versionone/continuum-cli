#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class CreateTask(ctmcommands.cmd.CSKCommand):

    Description = 'Creates a new blank Task object.'
    API = 'create_task'
    Examples = '''
    ctm-create-task -n "mytask" -d "This is a sample task" -c "test2001"
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
