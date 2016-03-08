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

class GetDeploymentDocument(ctmcommands.cmd.CSKCommand):

    Description = 'Retrieves the datastore data for a deployment in json format'
    API = 'get_deployment_document'
    Examples = '''
_To retrieve the data for a deployment and redirect to a file_

    ctm-get-deployment-document -d "Spring Petclinic 11" > petclinic11.json
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['deployment'])
        print(results)
