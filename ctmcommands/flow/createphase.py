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


class CreatePhase(ctmcommands.cmd.CSKCommand):

    Description = """Create a new Phase in the Phases library.

Returns a Phase Object."""

    API = 'create_phase'
    Examples = ''''''
    Options = [Param(name='templatefile', short_name='t', long_name='templatefile',
                     optional=False, ptype='string',
                     doc='A JSON document formatted as a CSK Phase definition.')
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
