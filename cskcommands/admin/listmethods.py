#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class ListMethods(cskcommands.cmd.CSKCommand):

    Description = 'Retrieves a list of all REST API methods and their documentation.'
    API = ''
    Examples = '''
_To print a full listing of all api commands with documentation_

    csk-list-methods

_To print only the names with the api commands sorted_

    csk-list-methods -l
'''
    Options = [Param(name='listonly', short_name='l', long_name='listonly',
                     optional=True, ptype='boolean',
                     doc='List the methods without documentation.')]
               

    def main(self):
        # output format for this command is limited to text
        self.output_format = "text"
        
        results = self.call_api(self.API, ['listonly'])
        print(results)

