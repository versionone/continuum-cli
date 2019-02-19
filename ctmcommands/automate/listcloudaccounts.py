#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class ListCloudAccounts(ctmcommands.cmd.CSKCommand):

    Description = 'Lists Cloud Accounts.'
    API = 'list_cloud_accounts'
    Examples = '''
_List all cloud accounts with AWS in the name or cloud type_

    ctm-list-cloud-accounts -f "AWS"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='''A string to use to filter the resulting data. Any row of data that has one field contains the string will be returned.''')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
