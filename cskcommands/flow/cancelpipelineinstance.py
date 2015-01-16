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


class CancelPipelineInstance(cskcommands.cmd.CSKCommand):

    Description = """Cancels a processing Pipeline Instance.
    
    Sets all Processing or Pending statuses to 'Canceled'.

Returns success or failure."""

    API = 'cancel_pipelineinstance'
    Examples = ''''''
    Options = [Param(name='rc', short_name='r', long_name='rc',
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
            results = self.call_api(self.API, ['rc'])
            print(results)
