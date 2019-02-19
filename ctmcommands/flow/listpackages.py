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


class ListPackages(ctmcommands.cmd.CSKCommand):

    Description = 'Lists all Package Definitions.'
    API = 'list_packages'
    Examples = '''
_List all Package Definitions

    ctm-list-packages
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.'),
               Param(name='limit', short_name='l', long_name='limit',
                     optional=True, ptype='string',
                     doc='The number of packages to retrieve. Default limit is 100.')
               ]

    def main(self):
        results = self.call_api(self.API, ['filter', 'limit'])
        print(results)
