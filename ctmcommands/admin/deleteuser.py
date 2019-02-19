#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class DeleteUser(ctmcommands.cmd.CSKCommand):

    Description = 'Deletes a new User.'
    API = 'delete_user'
    Examples = '''
    ctm-delete-user -u "dave.thomas"
'''
    Options = [Param(name='user', short_name='u', long_name='user',
                     optional=False, ptype='string',
                     doc='A login name for the user.')]

    def main(self):
        results = self.call_api(self.API, ['user'])
        print(results)
