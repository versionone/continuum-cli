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


class ExportPhases(cskcommands.cmd.CSKCommand):

    Description = 'Exports all Phases in the catalog.'
    API = 'export_phases'
    Examples = '''
_Export all Phases

    csk-export-phases
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
