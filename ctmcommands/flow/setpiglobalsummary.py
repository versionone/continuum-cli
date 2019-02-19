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


class SetPIGlobalSummary(ctmcommands.cmd.CSKCommand):

    Description = """Sets pipeline instance global summary data"""

    API = 'set_pi_global_summary'
    Examples = ''''''
    Options = [Param(name='pi', short_name='i', long_name='pi',
                     optional=False, ptype='string',
                     doc='Pipeline instance ID or name'),
               Param(name='key', short_name='k', long_name='key',
                     optional=False, ptype='string',
                     doc='Key name to set'),
               Param(name='value', short_name='v', long_name='value',
                     optional=False, ptype='string',
                     doc='Value to set')
              ]

    def main(self):
        self.call_api(self.API, ['pi', 'key', 'value'])
