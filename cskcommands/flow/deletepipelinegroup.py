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


class DeletePipelineGroup(cskcommands.cmd.CSKCommand):

    Description = """Permanently deletes a Pipeline Instance Group.

Requires the '_id' of the Pipeline Instance Group.

Returns success or failure."""

    API = 'delete_pipelinegroup'
    Examples = ''''''
    Options = [Param(name='pig_id', short_name='i', long_name='pig_id',
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
            results = self.call_api(self.API, ['pi'])
            print(results)
