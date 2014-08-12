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


class ListReleaseCandidates(catoclient.catocommand.CatoCommand):

    Description = 'Lists all Release Candidates.'
    API = 'list_releasecandidates'
    Examples = '''
_List all Release Candidates

    csk-list-releasecandidates
'''
    Options = [Param(name='pipeline', short_name='p', long_name='pipeline',
                     optional=True, ptype='string',
                     doc='Limit the results to a specific Pipeline.'),
               Param(name='project', short_name='r', long_name='project',
                     optional=True, ptype='string',
                     doc='Limit the results to a specific project.'),
               Param(name='story', short_name='s', long_name='story',
                     optional=True, ptype='string',
                     doc='Limit the results to a specific story.')]

    def main(self):
        results = self.call_api(self.API, ['pipeline', 'project', 'story'])
        print(results)
