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

class GetSequenceInstances(cskcommands.cmd.CSKCommand):

    Description = 'Get a list of Deployment Sequence Instances.'
    API = 'get_sequence_instances'
    Examples = '''
_To get all past and present sequence instances for a given deployment_

    csk-get-sequence-instances -d "MyApp20"

_To get only completed sequence instances_

    csk-get-sequence-instances -d "MyApp20" -s "completed"

_To get all sequence instances for a particular sequence name_

    csk-get-sequence-instances -d "MyApp20" -f "Start"

_To get any sequence instance between two dates_

    csk-get-sequence-instances -d "MyApp20" --from "1/16/14" --to "0/17/14"
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='Filters the results if any part of the result contains the string.'),
               Param(name='status', short_name='s', long_name='status',
                     optional=True, ptype='string',
                     doc='A comma separated list of statuses.'),
               Param(name='from', short_name='', long_name='from',
                     optional=True, ptype='string',
                     doc='A "from" date.'),
               Param(name='to', short_name='', long_name='to',
                     optional=True, ptype='string',
                     doc='A "to" date.'),
               Param(name='records', short_name='r', long_name='records',
                     optional=True, ptype='string',
                     doc='Maximum number of records to return.')
               ]

    def main(self):
        results = self.call_api(self.API, ['deployment', 'filter', 'status', 'from', 'to', 'records'])
        print(results)
