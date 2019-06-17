#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class RemoveTeamUser(ctmcommands.cmd.CSKCommand):

    Description = 'Remove the specified User from a Team.'
    API = 'remove_team_user'
    Examples = '''
    ctm-remove-team-user -t "dev team" -u "bob"
'''
    Options = [Param(name='team', short_name='t', long_name='team',
                     optional=False, ptype='string',
                     doc='Name or ID of the Team to change.'),
               Param(name='user', short_name='u', long_name='user',
                     optional=False, ptype='string',
                     doc='Name or ID of the User to remove.'),
               Param(name='default', short_name='d', long_name='default',
                     optional=True, ptype='string',
                     doc='Users must be in at least one Team.  If the removal operation would leave this user Teamless, specify a new `Default` team for the User. Will attempt to use `Default` if omitted.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['team', 'user', 'default'])
        print(results)
