#########################################################################
#
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#
#
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param


class RegisterPlugin(cskcommands.cmd.CSKCommand):

    Description = 'Registers a new Flow Plugin.'
    API = 'register_plugin'
    Examples = '''
    ccl-register-plugin -n "PluginName"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='Name of the new plugin to register.')]

    def main(self):
        results = self.call_api(self.API, ['name'])
        print(results)
