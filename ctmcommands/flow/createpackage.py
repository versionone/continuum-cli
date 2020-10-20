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


class CreatePackage(ctmcommands.cmd.CSKCommand):

    Description = """Creates a Package Definition.

Returns a Package Definition Object."""

    API = 'create_package'
    Examples = ''''''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the Package Definition.'),
               Param(name='team', short_name='t', long_name='team',
                     optional=False, ptype='string',
                     doc='Team which the Package Definition should belong to'),
               Param(name='description', short_name='d', long_name='description',
                     optional=True, ptype='string',
                     doc='A description for the Package Definition.'),
               Param(name='progression', short_name='p', long_name='progression',
                     optional=True, ptype='string',
                     doc='Value can be either a Progression ID or Name.')               
               ]

    def main(self):
        results = self.call_api(self.API,
                                ['name', 'team', 'description', 'progression'])
        print(results)
