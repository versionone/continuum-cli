#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class ListCloudKeyPairs(ctmcommands.cmd.CSKCommand):

    Description = 'Lists cloud endpoint key pairs (ssh private keys)'
    API = 'list_cloud_keypairs'
    Examples = '''
_List all keypair names associated with the AWS us-east-1 cloud endpoint_

    ctm-list-cloud-keypairs -c "us-east-1"
'''
    Options = [Param(name='cloud', short_name='c', long_name='cloud',
                     optional=False, ptype='string',
                     doc='A Cloud ID or Name.')
               ]

    def main(self):
        results = self.call_api(self.API, ['cloud'])
        print(results)
