#########################################################################
# 
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
# 
# 
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class ListTemplateTasks(cskcommands.cmd.CSKCommand):

    Description = 'Lists all Tasks associated with an Application Template and the corresponding sequence or action'
    API = 'list_template_tasks'
    Examples = '''
_To list all tasks associated with an application template and version_

    csk-list-application-template-tasks -t "Sample Application" -v 5 
'''
    Options = [Param(name='template', short_name='t', long_name='template',
                     optional=False, ptype='string',
                     doc='Name of the Application Template.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=False, ptype='string',
                     doc='The Application Template Version.')]

    def main(self):
        results = self.call_api(self.API, ['template', 'version'])
        print(results)
