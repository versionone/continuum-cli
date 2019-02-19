#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd


class Version(ctmcommands.cmd.CSKCommand):

    Description = 'Displays the Version by request from the API.'
    API = 'version'
    Examples = '''
    ctm-version
'''
    Options = []

    def main(self):
        results = self.call_api(self.API, [])
        print(results)
