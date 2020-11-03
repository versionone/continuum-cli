#########################################################################
#
# Copyright 2020 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class CreateProgression(ctmcommands.cmd.CSKCommand):

    Description = """Creates a Progression.

Returns a Progression Object."""

    API = 'create_progression'
    Examples = ''''''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the Progression.'),
               Param(name='description', short_name='d', long_name='description',
                     optional=True, ptype='string',
                     doc='A description for the Progression.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'description'])
        print(results)
