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


class SetPIDescription(ctmcommands.cmd.CSKCommand):

    Description = """Sets pipeline instance description"""

    API = 'set_pi_description'
    Examples = ''''''
    Options = [Param(name='pi', short_name='i', long_name='pi',
                     optional=False, ptype='string',
                     doc='Pipeline instance ID or name'),
               Param(name='description', short_name='d', long_name='description',
                     optional=False, ptype='string',
                     doc='Key name to set')
              ]

    def main(self):
        self.call_api(self.API, ['pi', 'description'])
