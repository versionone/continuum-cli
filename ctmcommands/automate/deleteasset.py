#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

from builtins import input


class DeleteAsset(ctmcommands.cmd.CSKCommand):

    Description = 'Deletes an asset.'
    API = 'delete_asset'
    Examples = '''
    ctm-delete-asset -a "testdb"
'''
    Options = [Param(name='asset', short_name='a', long_name='asset',
                     optional=False, ptype='string',
                     doc='The ID or Name of the Asset to delete.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = input("WARNING: This is a utility function.\n\nDeleting an Asset cannot be undone.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['asset'])
            print(results)
