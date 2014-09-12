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


class GetReleaseCandidate(cskcommands.cmd.CSKCommand):

    Description = 'Gets a Release Candidate object.'
    API = 'get_releasecandidate'
    Examples = '''
    csk-get-releasecandidate -r "Release Candidate Name or ID"
'''
    Options = [Param(name='rc', short_name='r', long_name='rc',
                     optional=False, ptype='string',
                     doc='Value can be either a Release Candidate ID or Name.'),
               Param(name='include_stages', short_name='s', long_name='include_stages',
                     optional=True, ptype='boolean',
                     doc='If provided, include the Stages, Steps and Plugins - the whole enchilada.')]

    def main(self):
        results = self.call_api(self.API, ['rc', 'include_stages'])
        print(results)
