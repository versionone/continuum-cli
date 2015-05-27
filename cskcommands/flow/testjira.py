#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class TestJira(cskcommands.cmd.CSKCommand):

    Description = "Test Jira connectivity"
    API = "test_jira"
    Examples = """
    ccl-testjira -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Jira instance name in the ClearCode configuration. Optional, do not use if testing default Jira instance.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
