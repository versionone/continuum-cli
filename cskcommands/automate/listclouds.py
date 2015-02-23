#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class ListClouds(cskcommands.cmd.CSKCommand):

    Description = 'Lists Cloud endpoints.'
    API = 'list_clouds'
    Examples = '''
_List all cloud endpoints_

    ccl-list-clouds

_List all vcloud cloud endpoints_

    ccl-list-clouds -f "vCloud"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='''A string to use to filter the resulting data. Any row of data that has one field contains the string will be returned.''')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)

