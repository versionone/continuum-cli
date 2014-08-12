#########################################################################
#
# Copyright 2013 Cloud Sidekick
# __________________
#
#  All Rights Reserved.
#
# NOTICE:  All information contained herein is, and remains
# the property of Cloud Sidekick and its suppliers,
# if any.  The intellectual and technical concepts contained
# herein are proprietary to Cloud Sidekick
# and its suppliers and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Cloud Sidekick.
#
#########################################################################

import commands.catocommand
from commands.param import Param


class ImportPipeline(commands.catocommand.CatoCommand):

    Description = """Imports a Pipeline definition from a JSON document.

Returns a Pipeline Object."""

    API = 'import_pipeline'
    Examples = ''''''
    Options = [Param(name='backupfile', short_name='b', long_name='backupfile',
                     optional=False, ptype='string',
                     doc='A JSON document formatted as a complete CSK Pipeline backup.'),
               Param(name='overwrite', short_name='o', long_name='overwrite',
                     optional=True, ptype='string',
                     doc="""Valid values: pipeline|phases|all|none (default).""")
               ]

    def main(self):
        import os

        self.backup = None
        if self.backupfile:
            fn = os.path.expanduser(self.backupfile)
            with open(fn, 'r') as f_in:
                if not f_in:
                    print("Unable to open file [%s]." % fn)
                self.backup = f_in.read()

        results = self.call_api(self.API, ['backup', 'overwrite'])
        print(results)
