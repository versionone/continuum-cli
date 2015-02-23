#########################################################################
#
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#
#
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param


class ListProjects(cskcommands.cmd.CSKCommand):

    Description = 'Lists all Projects.'
    API = 'list_projects'
    Examples = '''
_List all Projects

    ccl-list-projects
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
