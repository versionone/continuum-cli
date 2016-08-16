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


class GetServiceDocument(ctmcommands.cmd.CSKCommand):

    Description = 'Retrieves a json formatted datastore document for a service on a deployment'
    API = 'get_service_document'
    Examples = '''
_To retieve the datastore document for a service and output it to a file_

    ctm-get-service-document -d "MyApp20" -s "Weblogic" > weblogic.json
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
                 Param(name='service', short_name='s', long_name='service',
                     optional=False, ptype='string',
                     doc='Value can be either a Service ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['deployment', 'service'])
        print(results)
