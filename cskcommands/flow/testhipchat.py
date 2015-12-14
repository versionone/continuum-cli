#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class TestHipChat(cskcommands.cmd.CSKCommand):

    Description = "Test HipChat Server connectivity"
    API = "test_hipchat"
    Examples = """
    ccl-testhipchat -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='HipChat instance name in the Continuum configuration. Optional, do not use if testing default HipChat instance.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
