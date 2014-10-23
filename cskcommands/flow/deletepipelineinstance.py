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


class DeletePipelineInstance(cskcommands.cmd.CSKCommand):

    Description = """Permanently deletes a Pipeline Instance.

Returns success or failure."""

    API = 'delete_pipelineinstance'
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
