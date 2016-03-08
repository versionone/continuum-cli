#########################################################################
#
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class ListPipelineInstances(ctmcommands.cmd.CSKCommand):

    Description = 'Lists all Pipeline Instances.'
    API = 'list_pipelineinstances'
    Examples = '''
_List all Pipeline Instances

    ctm-list-pipelineinstances
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
