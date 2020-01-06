#########################################################################
#
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class ConfigurePlugins(ctmcommands.cmd.CSKCommand):

    Description = """Configures the details of multiple plugins from a JSON document.
    
    WARNING: this command will OVERWRITE any existing plugin configuration!
    
    USE WITH CAUTION.
"""

    API = 'configure_plugins'
    Examples = ''''''
    Options = [Param(name='backupfile', short_name='b', long_name='backupfile',
                     optional=False, ptype='string',
                     doc='A JSON document formatted as a list of Plugin Configurations.'),
               ]

    def main(self):
        import os

        self.plugins = None
        if self.backupfile:
            fn = os.path.expanduser(self.backupfile)
            with open(fn, 'r') as f_in:
                if not f_in:
                    print("Unable to open file [%s]." % fn)
                self.plugins = f_in.read()

        results = self.call_api(self.API, ['plugins'], verb='POST')
        print(results)
