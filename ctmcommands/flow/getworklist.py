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


class GetWorklist(ctmcommands.cmd.CSKCommand):

    Description = 'Gets a list of pending Pipeline Instances.'
    API = 'get_worklist'
    Examples = '''
    ctm-get-worklist -f "key:value"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='Limit the result to a specific key:value pair.')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
