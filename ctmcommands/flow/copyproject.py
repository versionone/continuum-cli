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


class CopyProject(ctmcommands.cmd.CSKCommand):

    Description = 'Copy a Project object.'
    API = 'copy_project'
    Examples = '''
    ctm-copy-project -p "ProjectName"
'''
    Options = [Param(name='project', short_name='p', long_name='project',
                     optional=False, ptype='string',
                     doc='Value can be either a Project ID or Name.'),
               Param(name='newname', short_name='n', long_name='newname',
                     optional=False, ptype='string',
                     doc='A name for the new Project.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("Are you sure (y/n)? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['project', 'newname'])
            print(results)
