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
    ccl-testjira
"""

    def main(self):
        results = self.call_api(self.API, [])
        print(results)
