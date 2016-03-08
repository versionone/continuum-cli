#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

class TagObject(ctmcommands.cmd.CSKCommand):

    Description = 'Applies a security Tag to an object.'
    API = 'add_object_tag'
    Examples = '''
_To tag a task using task uuid and the task object type_
    
    ctm-tag-object -t "development" -o "7f17e600-794f-11e3-bb4c-c8bcc89d4845" -y 3
'''
    Options = [Param(name='tag', short_name='t', long_name='tag',
                     optional=False, ptype='string',
                     doc='The name of the Tag.'),
               Param(name='object_id', short_name='o', long_name='object_id',
                     optional=False, ptype='string',
                     doc='The uuid of the object to Tag.'),
               Param(name='object_type', short_name='y', long_name='object_type',
                     optional=False, ptype='string',
                     doc='''The numeric object type of the object to Tag. (User = 1, Asset = 2, Task = 3)''')]

    def main(self):
        results = self.call_api(self.API, ['tag', 'object_id', 'object_type'])
        print(results)
