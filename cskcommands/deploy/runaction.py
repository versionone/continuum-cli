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

class RunAction(cskcommands.cmd.CSKCommand):

    Description = 'Runs a Deployment Action'
    API = 'run_action'
    Examples = '''
_To run an action on a service instance without parameters, no confirmation prompt_

    csk-run-action -d "MyApp20" -a "Trim Logfiles" -v "Weblogic" -i "Weblogic 1" --force

_To run an action on a service instance with a parameters file, no confirmation prompt_

    csk-run-action -d "MyApp20" -a "Trim Logfiles" -v "Weblogic" -i "Weblogic 1" -p "trimlog.json" --force

'''
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
               Param(name='parameters', short_name='p', long_name='parameters',
                     optional=True, ptype='string',
                     doc='JSON or XML formatted parameters, or a path to a file containing JSON or XML parameters.')
               ]

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
            # first, check if the "parameters" argument is json, xml, or a filename.
            if self.parameters:
                try:
                    import xml.etree.ElementTree as ET
                    ET.fromstring(self.parameters)
                except:  # couldn't parse it.  Maybe it's JSON
                    try:
                        import json
                        json.loads(self.parameters)
                    except:  # nope, last try, maybe it's a file path
                        try:
                            import os
                            fn = os.path.expanduser(self.parameters)
                            with open(fn, 'r') as f_in:
                                if not f_in:
                                    print("Unable to open parameters file [%s]." % fn)
                                self.parameters = f_in.read()
                        except:  # well, nothing worked so let's just whine
                            print ("'parameters' argument was provided, but unable to reconcile parameters as JSON, XML or a valid and existing file.")

            results = self.call_api(self.API, ['deployment', 'action', 'service', 'service_instance', 'log_level', 'parameters'])
            print(results)
