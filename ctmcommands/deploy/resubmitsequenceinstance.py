#########################################################################
# 
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
# 
# 
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class ResubmitSequenceInstance(ctmcommands.cmd.CSKCommand):

    Description = 'Resubmit a halted Sequence Instance.'
    API = 'resubmit_sequence'
    Examples = '''
    ctm-resubmit-sequence-instance -i 514
'''
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The Instance ID to resubmit.')]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
