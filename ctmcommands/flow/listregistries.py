#########################################################################
#
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import ctmcommands.cmd


class ListRegistries(ctmcommands.cmd.CSKCommand):

    Description = 'Lists all Registries.'
    API = 'list_registries'
    Examples = '''
_List all Registries

    ctm-list-registries
'''
    Options = []

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
