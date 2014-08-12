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


class CreatePipeline(commands.catocommand.CatoCommand):

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
                    print("Unable to open file [%s]." % fn)
                self.template = f_in.read()

        results = self.call_api(self.API, ['template'])
        print(results)
