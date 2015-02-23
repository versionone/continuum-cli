#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class GetCloud(cskcommands.cmd.CSKCommand):

    Description = 'Prints the properties of a Cloud endpoint'
    API = 'get_cloud'
    Examples = '''
    ccl-get-cloud -n "us-east-1"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Cloud.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name'])
        print(results)
