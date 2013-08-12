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

class RunAction(catoclient.catocommand.CatoCommand):

    Description = 'Runs a Deployment Action'
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='action', short_name='a', long_name='action',
                     optional=False, ptype='string',
                     doc='Name of the Action to run.'),
               Param(name='service', short_name='v', long_name='service',
                     optional=True, ptype='string',
                     doc='Value can be either a Service ID or Name.'),
               Param(name='service_instance', short_name='i', long_name='service_instance',
                     optional=True, ptype='string',
                     doc='The ID of a Service Instance.'),
               Param(name='log_level', short_name='l', long_name='log_level',
                     optional=True, ptype='string',
                     doc='An optional Logging level.  (Normal if omitted.)'),
               Param(name='parameterfile', short_name='p', long_name='parameterfile',
                     optional=True, ptype='string',
                     doc='The file name of an optional Parameter definition file.')]

    def main(self):
        
        if self.service_instance and not self.service:
            print "If a Service Instance is provided, a Service must also be specified."
            return
        
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("\nRunning an Action might change the condition of this Deployment and it's Services.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            # first, we need to load the parameters data from a file
            self.params = None
            if self.parameterfile:
                import os
                fn = os.path.expanduser(self.parameterfile)
                with open(fn, 'r') as f_in:
                    if not f_in:
                        print("Unable to open file [%s]." % fn)
                    data = f_in.read()
                    if data:
                        self.params = data

            results = self.call_api('run_action', ['deployment', 'action', 'service', 'service_instance', 'log_level', 'params'])
            print(results)
