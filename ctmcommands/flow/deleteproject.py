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


class DeleteProject(ctmcommands.cmd.CSKCommand):

    Description = 'Delete a Project object.'
    API = 'delete_project'
    Examples = '''
    ctm-delete-project -p "ProjectName"
'''
    Options = [Param(name='project', short_name='p', long_name='project',
                     optional=False, ptype='string',
                     doc='Value can be either a Project ID or Name.'),
               Param(name='preserve', long_name='preserve',
                     optional=True, ptype='boolean',
                     doc='If provided, will still delete all data, but the actual Project will be preserved.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = input("Are you sure (y/n)? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['project', 'preserve'])
            print(results)
