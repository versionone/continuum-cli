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


class CreatePipeline(ctmcommands.cmd.CSKCommand):

    Description = """Creates a Pipeline definition from a JSON document.

Returns a Pipeline Object."""

    API = 'create_pipeline'
    Examples = ''''''
    Options = [Param(name='templatefile', short_name='t', long_name='templatefile',
                     optional=False, ptype='string',
                     doc='A JSON document formatted as a CSK Pipeline definition.')
               ]

    def main(self):
        import os

        self.template = None
        if self.templatefile:
            fn = os.path.expanduser(self.templatefile)
            with open(fn, 'r') as f_in:
                if not f_in:
                    print(("Unable to open file [%s]." % fn))
                self.template = f_in.read()

        results = self.call_api(self.API, ['template'])
        print(results)
