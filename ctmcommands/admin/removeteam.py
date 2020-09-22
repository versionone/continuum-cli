#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class RemoveTeam(ctmcommands.cmd.CSKCommand):

    Description = 'Remove the specified Team from the Database.'
    API = 'remove_team'
    Examples = '''
    ctm-remove-team -t "dev team" 
'''
    Options = [Param(name='team', short_name='t', long_name='team',
                     optional=False, ptype='string',
                     doc='Name or ID of the Team to change. The team must not have any users associated with it.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['team',])
        print(results)
