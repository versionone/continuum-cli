#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class TestJenkins(ctmcommands.cmd.CSKCommand):

    Description = "Test Jenkins connectivity"
    API = "test_jenkins"
    Examples = """
    ctm-testjenkins -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Jenkins instance name in the Continuum configuration. Optional, do not use if testing default Jenkins instance.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
