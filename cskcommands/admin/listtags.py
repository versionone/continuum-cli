#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class ListTags(cskcommands.cmd.CSKCommand):

    Description = 'Lists Tags and indicates whether they are in use or not.'
    API = 'list_tags'
    Examples = '''
_To print all tags_

    ccl-list-tags

_To print all tags containing a specific string in the name or description_

    ccl-list-tags -f "development"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                    optional=True, ptype='string',
                    doc='''A string to use to filter the resulting data. Any row of data that has one field contains the string will be returned.''')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)

