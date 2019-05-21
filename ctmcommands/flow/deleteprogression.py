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


class DeleteProgression(ctmcommands.cmd.CSKCommand):

    Description = 'Delete a Progression.'
    API = 'delete_progression'
    Examples = '''
    ctm-delete-progression -p "Progression Name"
'''
    Options = [Param(name='progression', short_name='p', long_name='progression',
                     optional=False, ptype='string',
                     doc='Value can be either a Progression ID or Name.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = input("\nThis is a destructive operation.  All configuration and history of this Progression, including references to other objects, will be removed.\n\nAre you sure (y/n)? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['progression'])
            print(results)
