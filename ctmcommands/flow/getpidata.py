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


class GetPIData(ctmcommands.cmd.CSKCommand):

    Description = 'Gets a Pipeline Instance Data object.'
    API = 'get_pi_data'
    Examples = '''
    ctm-get-pidata -i "Pipeline Instance Name or ID"
'''
    Options = [Param(name='pi', short_name='i', long_name='pi',
                     optional=False, ptype='string',
                     doc='Value can be either a Pipeline Instance ID or Name.'),
               Param(name='lookup', short_name='l', long_name='lookup',
                     optional=True, ptype='string',
                     doc='Lookup an expression that evaluates to a subsection of the document.')]

    def main(self):
        results = self.call_api(self.API, ['pi', 'lookup'])
        print(results)
