#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class TestJenkins(cskcommands.cmd.CSKCommand):

    Description = "Test Jenkins connectivity"
    API = "test_jenkins"
    Examples = """
    ccl-testjenkins -uusername -ppassword -sserver -c"dir c:"
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Jenkins instance name in the ClearCode configuration. Optional, do not use if testing default Jenkins instance.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
