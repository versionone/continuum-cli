#########################################################################
#
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class GetPIWorkitems(ctmcommands.cmd.CSKCommand):

    Description = 'Gets the Workitems from the Manifest of a Pipeline Instance.'
    API = 'get_pi_workitems'
    Examples = '''
    ctm-get-piworkitems -i "Pipeline Instance Name or ID"
'''
    Options = [Param(name='pi', short_name='i', long_name='pi',
                     optional=False, ptype='string',
                     doc='Value can be either a Pipeline Instance ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['pi'])
        print(results)
