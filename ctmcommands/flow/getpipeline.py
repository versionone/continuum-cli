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


class GetPipeline(ctmcommands.cmd.CSKCommand):

    Description = 'Gets a Pipeline Definition.'
    API = 'get_pipeline'
    Examples = '''
    ctm-get-pipeline -p "PipelineName"
'''
    Options = [Param(name='pipeline', short_name='p', long_name='pipeline',
                     optional=False, ptype='string',
                     doc='Value can be either a Definition ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['pipeline'])
        print(results)
