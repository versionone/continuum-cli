#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class ListTasks(cskcommands.cmd.CSKCommand):

    Description = 'Lists Tasks'
    API = 'list_tasks'
    Examples = '''
_List all tasks_

    ccl-list-tasks

_List all tasks with a particular string in the name, all versions_

    ccl-list-tasks -f "Test Logging Level" -v
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

