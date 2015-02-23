#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class UpdateCloud(cskcommands.cmd.CSKCommand):

    Description = 'Updates the properties of a Cloud Endpoint.'
    API = 'update_cloud'
    Examples = '''
_Update the address of a vCloud cloud endpoint_

    ccl-update-cloud -n "vcloud-test" -u "iad2.vcloudservice.vmware.com"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Cloud.'),
               Param(name='apiurl', short_name='u', long_name='apiurl',
                     optional=True, ptype='string',
                     doc='URL of the Cloud API endpoint.'),
               Param(name='apiprotocol', short_name='p', long_name='apiprotocol',
                     optional=True, ptype='string',
                     doc='Cloud API endpoint protocol.'),
               Param(name='default_account', short_name='d', long_name='default_account',
                     optional=True, ptype='string',
                     doc='A default Account to be associated with this Cloud.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'apiurl', 'apiprotocol', 'default_account'])
        print(results)
