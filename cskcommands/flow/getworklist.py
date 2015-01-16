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


class GetWorklist(cskcommands.cmd.CSKCommand):

    Description = 'Gets a list of pending Pipeline Instances.'
    API = 'get_worklist'
    Examples = '''
    csk-get-worklist -f "key:value"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='Limit the result to a specific key:value pair.')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
