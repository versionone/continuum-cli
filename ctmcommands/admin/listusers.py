#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class ListUsers(ctmcommands.cmd.CSKCommand):

    Description = 'Lists Users, Authentication type will be set to SSO if SSO is enabled in this instance'
    API = 'list_users'
    Examples = '''
_List all users_

    ctm-list-users

_List all users with Administrator role_

    ctm-list-users -f "Administrator"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc=('A string to use to filter the resulting data. '
                          'Any row of data that has one field contains '
                          'the string will be returned.')),
               Param(name='limit', short_name='l', long_name='limit',
                     optional=True, ptype='string',
                     doc=('The maximum number of items to retrieve, or '
                          '0 for unlimited. (Default is unlimited.)'))]

    def main(self):
        results = self.call_api(self.API, ['filter', 'limit'])
        print(results)
