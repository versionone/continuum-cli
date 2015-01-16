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


class CreateStage(cskcommands.cmd.CSKCommand):

    Description = """Create a new Stage in the Stages library.

Returns a Stage Object."""

    API = 'create_stage'
    Examples = ''''''
    Options = [Param(name='templatefile', short_name='t', long_name='templatefile',
                     optional=False, ptype='string',
                     doc='A JSON document formatted as a CSK Stage definition.')
               ]

    def main(self):
        import os

        self.template = None
        if self.templatefile:
            fn = os.path.expanduser(self.templatefile)
            with open(fn, 'r') as f_in:
                if not f_in:
                    print("Unable to open file [%s]." % fn)
                self.template = f_in.read()

        results = self.call_api(self.API, ['template'])
        print(results)
