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

class RemoveServiceInstance(catoclient.catocommand.CatoCommand):

    Description = 'Remove a Service Instance from a Deployment.'
    API = 'remove_service_instance'
    Examples = '''
_To delete a service instance from a deployment without confirmation prompt_

    maestro-remove-service-instance -d "MyApp20" -i "Weblogic 2" --force
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
            answer = raw_input("WARNING: This is a utility function.\n\nRemoving a Service Instance removes Maestro records, but WILL NOT terminate any provisioned infrastructure. This cannot be undone.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['deployment', 'instance'])
            print(results)
