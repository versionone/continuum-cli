#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class GetAsset(ctmcommands.cmd.CSKCommand):

    Description = 'Prints the properties of an Asset'
    API = 'get_asset'
    Examples = '''
    ctm-get-asset -a "database001"
'''
    Options = [Param(name='asset', short_name='a', long_name='asset',
                     optional=False, ptype='string',
                     doc='The ID or Name of an Asset.')
               ]

    def main(self):
        results = self.call_api(self.API, ['asset'])
        print(results)
