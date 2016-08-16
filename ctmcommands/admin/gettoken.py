#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd


class GetToken(ctmcommands.cmd.CSKCommand):

    Description = 'Gets an API authentication token.'
    API = 'get_token'
    Examples = ''''''
    Options = []

    def main(self):
        results = self.call_api(self.API, [])
        print(results)
