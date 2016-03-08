#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class TestJira(ctmcommands.cmd.CSKCommand):

    Description = "Test Jira connectivity"
    API = "test_jira"
    Examples = """
    ctm-testjira -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Jira instance name in the Continuum configuration. Optional, do not use if testing default Jira instance.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
