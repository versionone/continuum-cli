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

class GetDeploymentLog(cskcommands.cmd.CSKCommand):

    Description = 'Get the log for a Deployment.'
    API = 'get_deployment_log'
    Examples = ''''''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='service', short_name='s', long_name='service',
                     optional=True, ptype='string',
                     doc='Value can be either a Service ID or Name.'),
               Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Value can be either a Service Instance ID or Name.'),
               Param(name='seq_instance', short_name='q', long_name='seq_instance',
                     optional=True, ptype='string',
                     doc='Value must be a Sequence Instance ID.'),
               Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.'),
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
        results = self.call_api(self.API, ['deployment', 'service', 'instance', 'seq_instance', 'filter', 'from', 'to', 'records'])
        print(results)
