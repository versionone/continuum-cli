#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class ListProcesses(cskcommands.cmd.CSKCommand):

    Description = 'Lists server processes (poller, messenger, etc.) along with heartbeat information.'
    API = 'list_processes'
    Examples = '''
    csk-list-processes
'''
    Options = []

    def main(self):

        return self.call_api(self.API, [])

    def main_cli(self):
        results = self.main()
        print(results)

