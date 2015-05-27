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
    ccl-testversionone -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='VersionOne instance name in the ClearCode configuration. Optional, do not use if testing default VersionOne instance.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
