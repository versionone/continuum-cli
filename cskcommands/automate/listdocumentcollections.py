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

class ListDocumentCollections(cskcommands.cmd.CSKCommand):

    Description = 'List all collections in the MongoDB datastore.'
    API = 'list_document_collections'
    Examples = '''
_List all datastore collections_

    csk-list-document-collections

_List all datastore collections, with workflow in the name_

    csk-list-document-collections -f "workflow"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='''A string to use to filter the resulting data. Any row of data that has one field contains the string will be returned.''')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
