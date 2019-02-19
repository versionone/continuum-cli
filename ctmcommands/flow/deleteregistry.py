#########################################################################
#
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class DeleteRegistry(ctmcommands.cmd.CSKCommand):

    Description = 'Delete a Registry.'
    API = 'delete_registry'
    Examples = '''
    ctm-delete-registry -p "Registry Name"
'''
    Options = [Param(name='registry', short_name='r', long_name='registry',
                     optional=False, ptype='string',
                     doc='Value is Registry Name.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("\nThis is a destructive operation.  This Registry, including references to other objects, will be removed.\n\nAre you sure (y/n)? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['registry'])
            print(results)
