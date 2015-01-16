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

class ExportPipeline(cskcommands.cmd.CSKCommand):

    Description = 'Exports a Pipeline Definition backup file.  Includes complete versions of all Phases and Stages.'
    API = 'export_pipeline'
    Examples = '''
_To export a Pipeline backup file._

    csk-export-pipeline -p "MyPipeline" > mypipeline.json 
'''
    Options = [Param(name='pipeline', short_name='p', long_name='pipeline',
                     optional=False, ptype='string',
                     doc='Value can be either a Definition ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['pipeline'])
        print(results)
