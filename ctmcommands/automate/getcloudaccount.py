#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class GetCloudAccount(ctmcommands.cmd.CSKCommand):

    Description = 'Prints the properties of a Cloud Account'
    API = 'get_account'
    Examples = '''
    ctm-get-cloud-account -n "vclouddev"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Cloud Account.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name'])
        print(results)
