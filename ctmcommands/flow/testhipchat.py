#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class TestHipChat(ctmcommands.cmd.CSKCommand):

    Description = "Test HipChat Server connectivity"
    API = "test_hipchat"
    Examples = """
    ctm-testhipchat -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='HipChat instance name in the Continuum configuration. Optional, do not use if testing default HipChat instance.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
