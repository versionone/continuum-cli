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

class ListApplicationTemplates(ctmcommands.cmd.CSKCommand):

    Description = 'Lists application deployment template and their high level properties'
    API = 'list_application_templates'
    Examples = '''
_To list all application templates_
    
    ctm-list-application-templates

_To list all application templates with a certain string in the name or description_

    ctm-list-application-templates -f "sample app"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='matches if the filter string is in the result')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
