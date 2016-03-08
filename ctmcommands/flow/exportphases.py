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


class ExportPhases(ctmcommands.cmd.CSKCommand):

    Description = 'Exports all Phases in the catalog.'
    API = 'export_phases'
    Examples = '''
_Export all Phases

    ctm-export-phases
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
