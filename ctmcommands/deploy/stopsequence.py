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


class StopSequence(ctmcommands.cmd.CSKCommand):

    Description = 'Stops a running Sequence Instance.'
    API = 'stop_sequence'
    Examples = '''
_To stop a running sequence instance without confirmation prompt_

    ctm-stop-sequence -i 514 --force

'''
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The sequence instance number to stop')]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
