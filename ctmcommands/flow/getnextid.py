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


class GetNextId(ctmcommands.cmd.CSKCommand):

    Description = """Get the next ID in an ID set"""
    API = 'get_next_id'
    Examples = ''''''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='ID set name'),
               Param(name='reseed', short_name='r', long_name='reseed',
                     optional=True, ptype='string',
                     doc='Reseed the ID set starting with this number'),
               Param(name='fallback', short_name='f', long_name='fallback',
                     optional=True, ptype='string',
                     doc='Fallback to this number if there is an exception')
              ]

    def main(self):
        results = self.call_api(self.API, ["name", "reseed", "fallback"])
        print (results)
