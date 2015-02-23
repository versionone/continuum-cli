#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class DeleteCredential(cskcommands.cmd.CSKCommand):

    Description = 'Deletes a Shared Credential.'
    API = 'delete_credential'
    Examples = '''
    ccl-delete-credential -c "adminuser"
'''
    Options = [Param(name='credential', short_name='c', long_name='credential',
                     optional=False, ptype='string',
                     doc='ID or Name of the Credential.')
               ]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("WARNING: This is a utility function.\n\nDeleting a Credential may affect automation connectivity and cannot be undone.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['credential'])
            print(results)
