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

class AddService(cskcommands.cmd.CSKCommand):

    Description = 'Creates a new Deployment Service.'
    API = 'add_service'
    Examples = ''''''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='Name for the new Deployment.'),
               Param(name='servicefile', short_name='s', long_name='servicefile',
                     optional=True, ptype='string',
                     doc='Additional properties in JSON Service definition format.')
               ]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("\nAdding a Service to a running Deployment makes it different from the source Application Template.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            self.service = None
            if self.servicefile:
                import os
                fn = os.path.expanduser(self.servicefile)
                with open(fn, 'r') as f_in:
                    if not f_in:
                        print("Unable to open file [%s]." % fn)
                    data = f_in.read()
                    if data:
                        self.service = data

            results = self.call_api(self.API, ['deployment', 'name', 'service'])
            print(results)
