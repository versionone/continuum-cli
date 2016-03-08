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


class ListPipelineGroups(ctmcommands.cmd.CSKCommand):

    Description = 'Lists all Pipeline Instance Groups.'
    API = 'list_pipelinegroups'
    Examples = '''
_List all Pipeline Instance Groups

    ctm-list-pipelinegroups
'''
    Options = [Param(name='pipeline', short_name='p', long_name='pipeline',
                     optional=True, ptype='string',
                     doc='Limit the results to a specific Pipeline.'),
               Param(name='project', short_name='r', long_name='project',
                     optional=True, ptype='string',
                     doc='Limit the results to a specific project.'),
               Param(name='group', short_name='g', long_name='group',
                     optional=True, ptype='string',
                     doc='Limit the results to a specific group.')]

    def main(self):
        results = self.call_api(self.API, ['pipeline', 'project', 'group'])
        print(results)
