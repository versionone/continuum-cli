#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class TestVersionOne(ctmcommands.cmd.CSKCommand):

    Description = "Test VersionOne connectivity"
    API = "test_versionone"
    Examples = """
    ctm-testversionone -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='VersionOne instance name in the Continuum configuration. Optional, do not use if testing default VersionOne instance.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
