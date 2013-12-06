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

class RunSequence(catoclient.catocommand.CatoCommand):

    Description = 'Runs a Deployment Sequence'
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='sequence', short_name='s', long_name='sequence',
                     optional=False, ptype='string',
                     doc='A Sequence name on this Deployment.'),
               Param(name='onerror', short_name='e', long_name='onerror',
                     optional=True, ptype='string',
                     doc='The on_error directive for this Sequence. ("pause" or "halt", "pause" if omitted)'),
               Param(name='parameters', short_name='p', long_name='parameters',
                     optional=True, ptype='string',
                     doc='JSON or XML formatted parameters, or a path to a file containing JSON or XML parameters.')
               ]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("\nRunning a Sequence will change the condition of this Deployment and it's Services.\n\nAre you sure? ")
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

            results = self.call_api('run_sequence', ['deployment', 'sequence', 'onerror', 'parameters'])
            print(results)
