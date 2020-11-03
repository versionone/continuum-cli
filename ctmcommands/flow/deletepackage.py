#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

from builtins import input


class DeletePackage(ctmcommands.cmd.CSKCommand):

    Description = 'Delete a Package Definition.'
    API = 'delete_package'
    Examples = '''
    ctm-delete-package -p "Package Name"
'''
    Options = [Param(name='package', short_name='p', long_name='package',
                     optional=False, ptype='string',
                     doc='Value can be either a Package ID or Name.'),
               Param(name='preserve', long_name='preserve',
                     optional=True, ptype='boolean',
                     doc='If provided, will still delete all data, but the actual Package definition will be preserved.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = input("\nThis is a destructive operation.  All configuration and history of this Package, including references to other objects, will be removed.\n\nAre you sure (y/n)? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['package', 'preserve'])
            print(results)
