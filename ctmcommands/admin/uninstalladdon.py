#########################################################################
#
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class UninstallAddOn(ctmcommands.cmd.CSKCommand):

    Description = """Uninstalls an Add-On from the VS-Exchange

Returns success or an error message."""

    API = 'uninstall_add_on'
    Examples = ''''''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='The name of the Add-On to uninstall from Continuum'),
               ]

    def main(self):
        results = self.call_api(self.API, ['name'])
        print(results)
