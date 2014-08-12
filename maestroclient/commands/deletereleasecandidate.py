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


class DeleteReleaseCandidate(catoclient.catocommand.CatoCommand):

    Description = """Permanently deletes a Release Candidate.

Returns success or failure."""

    API = 'delete_releasecandidate'
    Examples = ''''''
    Options = [Param(name='rc', short_name='r', long_name='rc',
                     optional=False, ptype='string',
                     doc='Name or ID of a Release Candidate.')
               ]

    def main(self):
        results = self.call_api(self.API, ['rc'])
        print(results)
