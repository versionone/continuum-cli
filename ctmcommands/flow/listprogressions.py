#########################################################################
#
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class ListProgressions(ctmcommands.cmd.CSKCommand):

    Description = 'Lists all Progressions.'
    API = 'list_progressions'
    Examples = '''
_List all Progressions

    ctm-list-progressions
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
