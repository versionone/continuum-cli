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


class CancelPipelineInstance(ctmcommands.cmd.CSKCommand):

    Description = """Cancels a processing Pipeline Instance.
    
    Sets all Processing or Pending statuses to 'Canceled'.

Returns success or failure."""

    API = 'cancel_pipelineinstance'
    Examples = ''''''
    Options = [Param(name='pi', short_name='i', long_name='pi',
                     optional=False, ptype='string',
                     doc='Name or ID of a Pipeline Instance.')
               ]

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
            results = self.call_api(self.API, ['pi'])
            print(results)
