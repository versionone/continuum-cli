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

class RemoveServiceInstance(cskcommands.cmd.CSKCommand):

    Description = 'Remove a Service Instance from a Deployment.'
    API = 'remove_service_instance'
    Examples = '''
_To delete a service instance from a deployment without confirmation prompt_

    ccl-remove-service-instance -d "MyApp20" -i "Weblogic 2" --force
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='The Name or ID of a Deployment.'),
               Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The Name or ID of the Service Instance.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("WARNING: This is a utility function.\n\nRemoving a Service Instance removes references, but WILL NOT terminate any provisioned infrastructure. This cannot be undone.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['deployment', 'instance'])
            print(results)
