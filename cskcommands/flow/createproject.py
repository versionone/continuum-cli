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


class CreateProject(cskcommands.cmd.CSKCommand):

    Description = """Creates a Project.

Returns a Project Object."""

    API = 'create_project'
    Examples = ''''''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the Project.'),
               Param(name='description', short_name='d', long_name='description',
                     optional=True, ptype='string',
                     doc='A description for the Project.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'description'])
        print(results)
