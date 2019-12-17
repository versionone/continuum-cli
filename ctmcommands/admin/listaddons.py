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


class ListAddOns(ctmcommands.cmd.CSKCommand):

    Description = """Lists all Add-Ons installed in this Continuum instance.

Returns: A list of Add-On details."""

    API = 'list_add_ons'
    Examples = ''''''
    Options = [Param(name='include_contents', short_name='c', long_name='include_contents',
                     optional=True, ptype='string',
                     doc='If true, lists the names of all parts of each of the Add-Ons. Defaults to false'),
               ]

    def main(self):
        if self.include_contents == "true" and not hasattr(self, "output_format"):
            self.output_format = "json"
        results = self.call_api(self.API, ['include_contents'])
        print(results)
