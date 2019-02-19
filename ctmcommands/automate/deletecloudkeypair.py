#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class DeleteCloudKeypair(ctmcommands.cmd.CSKCommand):

    Description = 'Removes a key pair (ssh private key) from a Cloud endpoint definition.'
    API = 'delete_cloud_keypair'
    Examples = '''
    ctm-delete-cloud-keypair -c "us-east-1" -n "privatekey001"
'''
    Options = [Param(name='cloud', short_name='c', long_name='cloud',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Cloud.'),
               Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the Key Pair.')
               ]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("WARNING: Deleting a Cloud Key Pair cannot be undone.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['cloud', 'name'])
            print(results)
