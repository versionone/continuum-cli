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

import cskcommands.cmd
from cskcommands.param import Param

class ResubmitSequenceInstance(cskcommands.cmd.CSKCommand):

    Description = 'Resubmit a halted Sequence Instance.'
    API = 'resubmit_sequence'
    Examples = '''
    maestro-resubmit-sequence-instance -i 514
'''
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The Instance ID to resubmit.')]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
