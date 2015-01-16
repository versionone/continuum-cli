#########################################################################
# 
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
# 
# 
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class GetSequenceInstanceStatus(cskcommands.cmd.CSKCommand):

    Description = 'Get a Deployment Sequence Instance Status.'
    API = 'get_sequence_instance_status'
    Examples = '''
_To get the status of a particular sequence instance_

    csk-get-sequence-instance-status -i 501
'''
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The sequence instance number.')]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
