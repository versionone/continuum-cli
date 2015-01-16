#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class GetSettings(cskcommands.cmd.CSKCommand):

    Description = 'Gets all the configuration settings from the database in json format'
    API = 'get_settings'
    Examples = '''
_To get all config settings in text format_

    csk-get-settings

_To get all config settings in json format_

    csk-get-settings -F "json"

_To get the settings only for the messenger module_

    csk-get-settings -m "Messenger"

_To get a list of the module names available in the settings configurations_
   
    csk-get-settings |grep -v "^ "|grep -v "^$"
'''
    Options = [Param(name='module', short_name='m', long_name='module',
                     optional=True, ptype='string',
                     doc='Filter to a specific module.')
               ]

    def main(self):
        results = self.call_api(self.API, ['module'])
        print(results)
