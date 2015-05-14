#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class TestVersionOne(cskcommands.cmd.CSKCommand):

    Description = "Test VersionOne connectivity"
    API = "test_versionone"
    Examples = """
    ccl-testversionone
"""

    def main(self):
        results = self.call_api(self.API, [])
        print(results)
