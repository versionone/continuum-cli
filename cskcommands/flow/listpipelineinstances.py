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


class ListPipelineInstances(cskcommands.cmd.CSKCommand):

    Description = 'Lists all Pipeline Instances.'
    API = 'list_pipelineinstances'
    Examples = '''
_List all Pipeline Instances

    csk-list-pipelineinstances
'''
    Options = [Param(name='definition', short_name='d', long_name='definition',
                     optional=True, ptype='string',
                     doc='Limit the results to a specific Pipeline Definition.'),
               Param(name='project', short_name='r', long_name='project',
                     optional=True, ptype='string',
                     doc='Limit the results to a specific project.'),
               Param(name='group', short_name='g', long_name='group',
                     optional=True, ptype='string',
                     doc='Limit the results to a specific group.')]

    def main(self):
        results = self.call_api(self.API, ['definition', 'project', 'group'])
        print(results)
