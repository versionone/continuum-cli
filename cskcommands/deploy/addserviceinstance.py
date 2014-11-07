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

class AddServiceInstance(cskcommands.cmd.CSKCommand):

    Description = 'Creates a new Deployment Service Instance.'
    API = 'add_service_instance'
    Examples = ''''''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='service', short_name='s', long_name='service',
                     optional=False, ptype='string',
                     doc='Value can be either a Service ID or Name.'),
               Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='Name (Label) of the new Instance.'),
               Param(name='hostname', short_name='h', long_name='hostname',
                     optional=True, ptype='string',
                     doc='Real host name.'),
               Param(name='address', short_name='a', long_name='address',
                     optional=True, ptype='string',
                     doc='Host IP Address (required with `hostname`.')
               ]

    def main(self):
        results = self.call_api(self.API, ['deployment', 'service', 'name', 'hostname', 'address'])
        print(results)
