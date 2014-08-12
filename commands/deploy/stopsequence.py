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

import commands.catocommand
from commands.param import Param

class StopSequence(commands.catocommand.CatoCommand):

    Description = 'Stops a running Sequence Instance.'
    API = 'stop_sequence'
    Examples = '''
_To stop a running sequence instance without confirmation prompt_

    maestro-stop-sequence -i 514 --force

'''
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The sequence instance number to stop')]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
