#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class TestOctopus(cskcommands.cmd.CSKCommand):

    Description = "Test Octopus connectivity"
    API = "test_octopus"
    Examples = """
    ccl-testoctopus -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Octopus instance name in the Continuum configuration. Optional, do not use if testing default Octopus instance.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
