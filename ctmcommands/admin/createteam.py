#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class CreateTeam(ctmcommands.cmd.CSKCommand):

    Description = 'Creates a new Team.'
    API = 'create_team'
    Examples = '''
    ctm-create-team -n "dev"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the new Team.'),
               Param(name='description', short_name='d', long_name='description',
                     optional=True, ptype='string',
                     doc='A description of the new Team'),
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'description'])
        print(results)
