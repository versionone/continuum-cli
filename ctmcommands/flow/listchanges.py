#########################################################################
#
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

from ctmcommands.cmd import CSKCommand
from ctmcommands.param import Param


class ListChanges(CSKCommand):

    Description = "Lists all Changes."
    API = "list_changes"
    Params = ['project', 'group', 'since', 'managed', 'unmanaged']
    Examples = '''
    ctm-list-changes
'''
    Options = [Param(name='project', short_name='r', long_name='project', optional=True,
                     doc='Limit the results to a specific project.'),
               Param(name='group', short_name='g', long_name='group', optional=True,
                     doc='Limit the results to a specific group.'),
               Param(name='since', short_name='s', long_name='since', optional=True,
                     doc='Limit the results to changes after the provided timestamp.'),
               Param(name='managed', short_name='m', long_name='managed', optional=True,
                     ptype='boolean', doc='List only the managed changes.'),
               Param(name='unmanaged', short_name='u', long_name='unmanaged', optional=True,
                     ptype='boolean', doc='List only the unmanaged changes, Ignored if managed flag is provided')]

    def main(self):
        changes = self.call_api(self.API, self.Params)
        print(changes)
