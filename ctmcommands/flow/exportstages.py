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


class ExportStages(ctmcommands.cmd.CSKCommand):

    Description = 'Exports all Stages in the catalog.'
    API = 'export_stages'
    Examples = '''
_Export all Stages

    ctm-export-stages
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
