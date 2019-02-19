#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class GetSettings(ctmcommands.cmd.CSKCommand):

    Description = 'Gets all the configuration settings from the database in json format'
    API = 'get_settings'
    Examples = '''
_To get all config settings in text format_

    ctm-get-settings

_To get all config settings in json format_

    ctm-get-settings -F "json"

_To get the settings only for the messenger module_

    ctm-get-settings -m "Messenger"

_To get a list of the module names available in the settings configurations_
   
    ctm-get-settings |grep -v "^ "|grep -v "^$"
'''
    Options = [Param(name='module', short_name='m', long_name='module',
                     optional=True, ptype='string',
                     doc='Filter to a specific module.')
               ]

    def main(self):
        results = self.call_api(self.API, ['module'])
        print(results)
