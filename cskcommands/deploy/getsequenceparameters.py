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

class GetSequenceParameters(cskcommands.cmd.CSKCommand):

    Description = 'Gets the Parameters template for a Sequence which can be used to pass to a sequence.'
    API = 'get_sequence_parameters'
    Examples = '''
_To get the json formatted parameters for a particular sequence and redirect to a file_

    csk-get-sequence-parameters -d "MyApp20" -s "Start" > myapp_parms.json
    
    or 

    csk-get-sequence-parameters -t "MyTemplate" -v "1" -s "Start" > myapp_parms.json
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=True, ptype='string',
                     doc='Value can be either a Deployment ID or Name. Either deployment or template must be used'),
               Param(name='template', short_name='t', long_name='template',
                     optional=True, ptype='string',
                     doc='A deployment template name. Either deployment or template must be used'),
               Param(name='version', short_name='v', long_name='version',
                     optional=True, ptype='string',
                     doc='A deployment template version. Required if template used'),
               Param(name='sequence', short_name='s', long_name='sequence',
                     optional=False, ptype='string',
                     doc='A Sequence name on this Deployment.'),
               Param(name='basic', short_name='b', long_name='basic',
                     optional=True, ptype='boolean',
                     doc='Get a basic template with no descriptive details or default values.')]

    def main(self):
        results = self.call_api(self.API, ['deployment', 'template', 'version', 'sequence', 'basic'])
        print(results)
