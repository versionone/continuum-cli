#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class TestBamboo(cskcommands.cmd.CSKCommand):

    Description = "Test Bamboo connectivity"
    API = "test_bamboo"
    Examples = """
    ccl-testbamboo -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Bamboo instance name in the ClearCode configuration. Optional, do not use if testing default Bamboo instance.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
