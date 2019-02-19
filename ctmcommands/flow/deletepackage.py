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


class DeletePackage(ctmcommands.cmd.CSKCommand):

    Description = 'Delete a Project object.'
    API = 'delete_package'
    Examples = '''
    ctm-delete-package -p "Package Name"
'''
    Options = [Param(name='package', short_name='p', long_name='package',
                     optional=False, ptype='string',
                     doc='Value can be either a Package ID or Name.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("\nThis is a destructive operation.  All configuration and history of this Package, including references to other objects, will be removed.\n\nAre you sure (y/n)? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['package'])
            print(results)
