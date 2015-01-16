#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class ListAssets(cskcommands.cmd.CSKCommand):

    Description = 'Lists Assets'
    API = 'list_assets'
    Examples = '''
_List all Assets with test in the name_

    csk-list-assets -f "test"

_List all Assets that are active_

    csk-list-assets -f "Active"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='''A string to use to filter the resulting data. Any row of data that has one field contains the string will be returned.''')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)

