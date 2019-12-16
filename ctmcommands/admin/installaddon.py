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


class InstallAddOn(ctmcommands.cmd.CSKCommand):

    Description = """Installs an Add-On from the VS-Exchange

Returns success or an error message."""

    API = 'install_add_on'
    Examples = ''''''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='The name of the add-on to install from the VS-Exchange'),
               Param(name='team', short_name='t', long_name='team',
                     optional=True, ptype='string',
                     doc="""The name of the team in which to install any projects, packages, pipelines, and tasks included in this add-on.
                            Required if any any projects, packages, pipelines, or tasks exist in the add-on"""),
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'team'])
        print(results)
