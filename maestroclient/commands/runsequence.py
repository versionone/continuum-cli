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
               Param(name='parameterfile', short_name='p', long_name='parameterfile',
                     optional=True, ptype='string',
                     doc='The file name of an optional Parameter definition file.')]

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

            results = self.call_api('run_sequence', ['deployment', 'sequence', 'onerror', 'params'])
            print(results)
