#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class TestTeamCity(ctmcommands.cmd.CSKCommand):

    Description = "Test TeamCity connectivity"
    API = "test_teamcity"
    Examples = """
    ctm-testteamcity -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='TeamCity instance name in the Continuum configuration. Optional, do not use if testing default TeamCity instance.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
