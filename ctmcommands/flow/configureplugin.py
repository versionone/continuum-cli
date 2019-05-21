#########################################################################
#
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class ConfigurePlugin(ctmcommands.cmd.CSKCommand):

    Description = """Configures the details of a specific plugin from a JSON document.

    WARNING: this command will OVERWRITE the existing plugin configuration!

    USE WITH CAUTION.
"""

    API = 'configure_plugin'
    Examples = ''''''
    Options = [Param(name='backupfile', short_name='b', long_name='backupfile',
                     optional=False, ptype='string',
                     doc='A JSON document formatted as a single Plugin Configuration.'),
               ]

    def main(self):
        import os

        self.plugins = None
        if self.backupfile:
            fn = os.path.expanduser(self.backupfile)
            with open(fn, 'r') as f_in:
                if not f_in:
                    print(("Unable to open file [%s]." % fn))
                self.plugin = f_in.read()

        results = self.call_api(self.API, ['plugin'], verb='POST')
        print(results)
