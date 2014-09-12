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


class GetRCData(cskcommands.cmd.CSKCommand):

    Description = 'Gets a Release Candidate Data object.'
    API = 'get_rc_data'
    Examples = '''
    csk-get-rcdata -r "Release Candidate Name or ID"
'''
    Options = [Param(name='rc', short_name='r', long_name='rc',
                     optional=False, ptype='string',
                     doc='Value can be either a Release Candidate ID or Name.'),
               Param(name='lookup', short_name='l', long_name='lookup',
                     optional=True, ptype='string',
                     doc='Lookup an expression that evaluates to a subsection of the document.')]

    def main(self):
        results = self.call_api(self.API, ['rc', 'lookup'])
        print(results)
