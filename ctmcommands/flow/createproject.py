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


class CreateProject(ctmcommands.cmd.CSKCommand):

    Description = """Creates a Project.

Returns a Project Object."""

    API = 'create_project'
    Examples = ''''''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the Project.'),
               Param(name='team', short_name='t', long_name='team',
                     optional=False, ptype='string',
                     doc='Team which the project should belong to'),
               Param(name='description', short_name='d', long_name='description',
                     optional=True, ptype='string',
                     doc='A description for the Project.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'team', 'description'])
        print(results)
