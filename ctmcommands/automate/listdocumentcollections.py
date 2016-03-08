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

class ListDocumentCollections(ctmcommands.cmd.CSKCommand):

    Description = 'List all collections in the MongoDB datastore.'
    API = 'list_document_collections'
    Examples = '''
_List all datastore collections_

    ctm-list-document-collections

_List all datastore collections, with workflow in the name_

    ctm-list-document-collections -f "workflow"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='''A string to use to filter the resulting data. Any row of data that has one field contains the string will be returned.''')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
