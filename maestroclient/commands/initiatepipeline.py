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


class InitiatePipeline(catoclient.catocommand.CatoCommand):

    Description = """Creates a new Release Candidate in a Pipeline with matching 'key' information.

Returns a Release Candidate Object."""

    API = 'initiate_pipeline'
    Examples = ''''''
    Options = [Param(name='pipeline', short_name='p', long_name='pipeline',
                     optional=False, ptype='string',
                     doc='Value can be either a Pipeline ID or Name.'),
               Param(name='details', short_name='d', long_name='details',
                     optional=True, ptype='string',
                     doc='A JSON object with additional details for the Release Candidate.')
               ]

    def main(self):
        results = self.call_api(self.API, ['pipeline', 'details'])
        print(results)
