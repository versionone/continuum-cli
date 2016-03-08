#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class CreateTag(ctmcommands.cmd.CSKCommand):

    Description = 'Creates a new Tag to be used to associate objects with one another.'
    API = 'create_tag'
    Examples = '''
    ctm-create-tag -n "staging01" -d "staging environment 1"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='The name of the new Tag.  (AlphaNumeric ONLY. Cannot contain spaces, punctuation or special characters.)'),
               Param(name='description', short_name='d', long_name='description',
                     optional=True, ptype='string',
                     doc='Tag description.')]

    def main(self):
        results = self.call_api(self.API, ['name', 'description'])
        print(results)
