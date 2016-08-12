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


class CopyApplicationTemplate(ctmcommands.cmd.CSKCommand):

    Description = 'Copies an Application Template to a new name or version.'
    API = 'copy_application_template'
    Examples = '''
_To copy an application template to a new version, same name_

    ctm-copy-application-template -t "MyApp" -v "1" -n "MyApp" -r "2"
'''
    Options = [Param(name='template', short_name='t', long_name='template',
                     optional=False, ptype='string',
                     doc='The Application Template to copy.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=False, ptype='string',
                     doc='A version for the new Template.'),
               Param(name='newname', short_name='n', long_name='newname',
                     optional=False, ptype='string',
                     doc='A name for the new Template.'),
               Param(name='newversion', short_name='r', long_name='newversion',
                     optional=False, ptype='string',
                     doc='A version for the new Template.')
               ]

    def main(self):
        results = self.call_api(self.API, ['newname', 'newversion', 'template', 'version'])
        print(results)
