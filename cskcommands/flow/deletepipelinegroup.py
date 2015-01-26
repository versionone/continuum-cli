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


class DeletePipelineGroup(cskcommands.cmd.CSKCommand):

    Description = """Permanently deletes a Pipeline Instance Group.

Requires the '_id' of the Pipeline Instance Group.

Returns success or failure."""

    API = 'delete_pipelinegroup'
    Examples = ''''''
    Options = [Param(name='pg', short_name='i', long_name='pg',
                     optional=False, ptype='string',
                     doc='ID of a Pipeline Instance Group.')
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
            results = self.call_api(self.API, ['pg'])
            print(results)
