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

class ResubmitSequenceInstance(cskcommands.cmd.CSKCommand):

    Description = 'Resubmit a halted Sequence Instance.'
    API = 'resubmit_sequence'
    Examples = '''
    csk-resubmit-sequence-instance -i 514
'''
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The Instance ID to resubmit.')]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
