#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class ListCredentials(ctmcommands.cmd.CSKCommand):

    Description = 'Lists Shared Credentials.'
    API = 'list_credentials'
    Examples = '''
_List all shared credentials_

    ctm-list-credentials

_List all shared credentials with root in the name or description_

    ctm-list-credentials -f "root"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='''A string to use to filter the resulting data. Any row of data that has one field contains the string will be returned.''')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
