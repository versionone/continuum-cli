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

import catoclient.catocommand
from catoclient.param import Param

class GetSequenceInstanceStatus(catoclient.catocommand.CatoCommand):

    Description = 'Get a Deployment Sequence Instance Status.'
    API = 'get_sequence_instance_status'
    Examples = '''
_To get the status of a particular sequence instance_

    maestro-get-sequence-instance-status -i 501
'''
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The sequence instance number.')]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
