#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class Version(cskcommands.cmd.CSKCommand):

    Description = 'Displays the Version by request from the API.'
    API = 'version'
    Examples = '''
    ccl-version
'''
    Options = []

    def main(self):
        results = self.call_api(self.API, [])
        print(results)

