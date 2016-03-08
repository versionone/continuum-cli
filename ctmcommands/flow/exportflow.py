#########################################################################
#
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class ExportFlow(ctmcommands.cmd.CSKCommand):

    Description = 'Exports everything in the Flow Pipeline definition catalog.'
    API = 'export_flow'
    Examples = '''
_Export everything.

    ctm-export-flow
'''
    Options = []

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
