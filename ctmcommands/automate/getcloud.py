#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class GetCloud(ctmcommands.cmd.CSKCommand):

    Description = 'Prints the properties of a Cloud endpoint'
    API = 'get_cloud'
    Examples = '''
    ctm-get-cloud -n "us-east-1"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Cloud.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name'])
        print(results)
