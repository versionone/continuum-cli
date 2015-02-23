#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class DeleteTag(cskcommands.cmd.CSKCommand):

    Description = 'Deletes a Tag.'
    API = 'delete_tag'
    Examples = '''
    ccl-delete-tag -n "staging01"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='The Name of the Tag to delete.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("WARNING: This is a utility function.\n\nDeleting a Tag could leave Users without access to their content. This cannot be undone.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['name'])
            print(results)
