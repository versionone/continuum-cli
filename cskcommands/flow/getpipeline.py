#########################################################################
#
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#
#
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param


class GetPipeline(cskcommands.cmd.CSKCommand):

    Description = 'Gets a Pipeline Definition.'
    API = 'get_pipeline'
    Examples = '''
    ccl-get-pipeline -p "PipelineName"
'''
    Options = [Param(name='pipeline', short_name='p', long_name='pipeline',
                     optional=False, ptype='string',
                     doc='Value can be either a Definition ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['pipeline'])
        print(results)
