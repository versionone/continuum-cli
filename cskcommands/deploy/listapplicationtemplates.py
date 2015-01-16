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

class ListApplicationTemplates(cskcommands.cmd.CSKCommand):

    Description = 'Lists application deployment template and their high level properties'
    API = 'list_application_templates'
    Examples = '''
_To list all application templates_
    
    csk-list-application-templates

_To list all application templates with a certain string in the name or description_

    csk-list-application-templates -f "sample app"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='matches if the filter string is in the result')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
