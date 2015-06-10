#########################################################################
#
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#
#
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param


class GetPIWorkitems(cskcommands.cmd.CSKCommand):

    Description = 'Gets the Workitems from the Manifest of a Pipeline Instance.'
    API = 'get_pi_workitems'
    Examples = '''
    ccl-get-piworkitems -i "Pipeline Instance Name or ID"
'''
    Options = [Param(name='pi', short_name='i', long_name='pi',
                     optional=False, ptype='string',
                     doc='Value can be either a Pipeline Instance ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['pi'])
        print(results)
