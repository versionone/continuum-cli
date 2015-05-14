#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class TestTeamCity(cskcommands.cmd.CSKCommand):

    Description = "Test TeamCity connectivity"
    API = "test_teamcity"
    Examples = """
    ccl-testteamcity -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='TeamCity instance name in the ClearCode configuration. Optional, do not use if testing default TeamCity instance.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
