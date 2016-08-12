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


class AddServiceInstance(ctmcommands.cmd.CSKCommand):

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
