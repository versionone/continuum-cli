#########################################################################
# 
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
# 
# 
#########################################################################

import ctmcommands.cmd


class GetLicense(ctmcommands.cmd.CSKCommand):

    Description = 'Prints the license information including expiration date'
    API = 'get_license'
    Examples = '''
    ctm-get-license
'''
    Options = []

    def main(self):
        results = self.call_api(self.API, [])
        print(results)
