#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd


class ListProcesses(ctmcommands.cmd.CSKCommand):

    Description = 'Lists server processes (poller, messenger, etc.) along with heartbeat information.'
    API = 'list_processes'
    Examples = '''
    ctm-list-processes
'''
    Options = []

    def main(self):

        return self.call_api(self.API, [])

    def main_cli(self):
        results = self.main()
        print(results)
