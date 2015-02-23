#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class GetAsset(cskcommands.cmd.CSKCommand):

    Description = 'Prints the properties of an Asset'
    API = 'get_asset'
    Examples = '''
    ccl-get-asset -a "database001"
'''
    Options = [Param(name='asset', short_name='a', long_name='asset',
                     optional=False, ptype='string',
                     doc='The ID or Name of an Asset.')
               ]

    def main(self):
        results = self.call_api(self.API, ['asset'])
        print(results)
