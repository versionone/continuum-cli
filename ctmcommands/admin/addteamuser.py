#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class AddTeamUser(ctmcommands.cmd.CSKCommand):

    Description = 'Add the specified User to a Team.'
    API = 'add_team_user'
    Examples = '''
    ctm-add-team-user -t "dev team" -u "bob" -r "User"
'''
    Options = [Param(name='team', short_name='t', long_name='team',
                     optional=False, ptype='string',
                     doc='Name or ID of the Team to change.'),
               Param(name='user', short_name='u', long_name='user',
                     optional=False, ptype='string',
                     doc='Name or ID of the User to add.'),
               Param(name='team_role', short_name='r', long_name='team_role',
                     optional=False, ptype='string',
                     doc='Name of the Role for new user to adopt on new team. Please specify either "Team Administrator", "Developer", or "User".'),
               ]

    def main(self):
        results = self.call_api(self.API, ['team', 'user', 'team_role'])
        print(results)
