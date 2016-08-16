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


class AddSequence(ctmcommands.cmd.CSKCommand):

    Description = 'Creates a new Sequence on a Deployment.'
    API = 'add_sequence'
    Examples = ''''''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='sequencefile', short_name='s', long_name='sequencefile',
                     optional=False, ptype='string',
                     doc='File name of a JSON Sequence definition file.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("\nAdding a Sequence to a running Deployment makes it different from the source Application Template.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            self.sequence = None
            if self.sequencefile:
                import os
                fn = os.path.expanduser(self.sequencefile)
                with open(fn, 'r') as f_in:
                    if not f_in:
                        print("Unable to open file [%s]." % fn)
                    data = f_in.read()
                    if data:
                        self.sequence = data

        results = self.call_api(self.API, ['deployment', 'sequence'])
        print(results)
