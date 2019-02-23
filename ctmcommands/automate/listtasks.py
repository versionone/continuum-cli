#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class ListTasks(ctmcommands.cmd.CSKCommand):

    Description = 'Lists Tasks'
    API = 'list_tasks'
    Examples = '''
_List all tasks_

    ctm-list-tasks

_List all tasks with a particular string in the name

    ctm-list-tasks -f "Test Logging Level"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                    optional=True, ptype='string',
                    doc='''A string to use to filter the resulting data. Any row of data that has one field contains the string will be returned.''')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
