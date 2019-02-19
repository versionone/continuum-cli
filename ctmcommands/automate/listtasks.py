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

_List all tasks with a particular string in the name, all versions_

    ctm-list-tasks -f "Test Logging Level" -v
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                    optional=True, ptype='string',
                    doc='''A string to use to filter the resulting data. Any row of data that has one field contains the string will be returned.'''),
              Param(name='show_all_versions', short_name='v', long_name='show_all_versions',
                     optional=True, ptype='boolean',
                     doc='Show all Versions, not just the "default".')]

    def main(self):
        results = self.call_api(self.API, ['filter', 'show_all_versions'])
        print(results)
