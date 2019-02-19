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


class GetPipelineInstance(ctmcommands.cmd.CSKCommand):

    Description = 'Gets a Pipeline Instance object.'
    API = 'get_pipelineinstance'
    Examples = '''
    ctm-get-pipelineinstance -i "Pipeline Instance Name or ID"
'''
    Options = [Param(name='pi', short_name='i', long_name='pi',
                     optional=False, ptype='string',
                     doc='Value can be either a Pipeline Instance ID or Name.'),
               Param(name='include_stages', short_name='s', long_name='include_stages',
                     optional=True, ptype='boolean',
                     doc='If provided, include the Stages, Steps and Plugins - the whole enchilada.')]

    def main(self):
        results = self.call_api(self.API, ['pi', 'include_stages'])
        print(results)
