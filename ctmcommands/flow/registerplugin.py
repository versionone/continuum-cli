#########################################################################
#
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class RegisterPlugin(ctmcommands.cmd.CSKCommand):

    Description = 'Registers a new Flow Plugin.'
    API = 'register_plugin'
    Examples = '''
    ctm-register-plugin -n "PluginName"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='Name of the new plugin to register.')]

    def main(self):
        results = self.call_api(self.API, ['name'])
        print(results)
