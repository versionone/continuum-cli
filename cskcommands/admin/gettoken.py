#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class GetToken(cskcommands.cmd.CSKCommand):

    Description = 'Gets an API authentication token.'
    API = 'get_token'
    Examples = ''''''
    Options = []

    def main(self):
        results = self.call_api(self.API, [])
        print(results)
