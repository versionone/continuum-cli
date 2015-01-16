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

class RemoveServiceFromSequenceStep(cskcommands.cmd.CSKCommand):

    Description = 'Removes a Service from a Deployment Sequence Step on a deployed application.'
    API = 'remove_service_from_sequence_step'
    Examples = '''
    csk-remove-service-from-sequence-step -d "MyApp" -s "Terminate" -t 1 -v "Database"
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='sequence', short_name='s', long_name='sequence',
                     optional=False, ptype='string',
                     doc='A Sequence name on this Deployment.'),
               Param(name='step', short_name='t', long_name='step',
                     optional=False, ptype='int',
                     doc='The step number on which to remove the Service.'),
               Param(name='service', short_name='v', long_name='service',
                     optional=False, ptype='string',
                     doc='The name or ID of the new Service.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("Are you sure (y/n)? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['deployment', 'sequence', 'step', 'service'])
            print(results)
