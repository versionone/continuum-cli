#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class ListUsers(cskcommands.cmd.CSKCommand):

    Description = 'Lists Users'
    API = 'list_users'
    Examples = '''
_List all users_

    csk-list-users

_List all users with Administrator role_

    csk-list-users -f "Administrator"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='''A string to use to filter the resulting data. Any row of data that has one field contains the string will be returned.''')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)

