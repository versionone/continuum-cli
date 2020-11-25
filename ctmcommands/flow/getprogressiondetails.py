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


class GetProgressionDetails(ctmcommands.cmd.CSKCommand):

    Description = 'Gets Progression Details.'
    API = 'get_progression_details'
    Examples = '''
'''
    Options = [Param(name='progression', short_name='p', long_name='progression',
                     optional=False, ptype='string',
                     doc='Value can be either a Progression ID or name.'),
               Param(name='packages', short_name='P', long_name='packages',
                     optional=True, ptype='string', cardinality='*',
                     doc='Filter response by a (comma-delimited) list of Package IDs.'),
               Param(name='teams', short_name='t', long_name='teams',
                     optional=True, ptype='string', cardinality='*',
                     doc='Filter response by a (comma-delimited) list of Team IDs or names.')]

    def main(self):
        results = self.call_api(self.API, ['progression', 'packages', 'teams'], verb='POST')
        print(results)
