#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class GetCloudAccount(cskcommands.cmd.CSKCommand):

    Description = 'Prints the properties of a Cloud Account'
    API = 'get_account'
    Examples = '''
    ccl-get-cloud-account -n "vclouddev"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Cloud Account.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name'])
        print(results)
