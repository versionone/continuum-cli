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

class AddDeployment(cskcommands.cmd.CSKCommand):

    Description = 'Creates a new Deployment.'
    API = 'add_deployment'
    Examples = ''''''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='Name for the new Deployment.'),
               Param(name='description', short_name='d', long_name='description',
                     optional=True, ptype='string',
                     doc='Description of this Application.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'description'])
        print(results)
