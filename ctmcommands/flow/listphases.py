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


class ListPhases(ctmcommands.cmd.CSKCommand):

    Description = 'Lists all Phases in the catalog.'
    API = 'list_phases'
    Examples = '''
_List all Phases

    ctm-list-phases
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
