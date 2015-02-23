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

class GetLicense(cskcommands.cmd.CSKCommand):

    Description = 'Prints the license information including expiration date'
    API = 'get_license'
    Examples = '''
    ccl-get-license
'''
    Options = []

    def main(self):
        results = self.call_api(self.API, [])
        print(results)
