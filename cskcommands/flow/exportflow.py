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


class ExportFlow(cskcommands.cmd.CSKCommand):

    Description = 'Exports everything in the Flow Pipeline definition catalog.'
    API = 'export_flow'
    Examples = '''
_Export everything.

    ccl-export-flow
'''
    Options = []

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
