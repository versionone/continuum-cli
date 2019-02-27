#########################################################################
#
# Copyright 2019 VersionOne
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
                     doc='Limit the results to a specific group.'),
               Param(name='since', short_name='s', long_name='since',
                     optional=True, ptype='string',
                     doc='Limit the results to Instances after the provided timestamp.'),
               Param(name='limit', short_name='l', long_name='limit',
                     optional=True, ptype='integer',
                     doc='Limit the number of results.  (0 for all results, 100 if omitted.')]

    def main(self):
        results = self.call_api(self.API, ['definition', 'project', 'group', 'since', 'limit'])
        print(results)
