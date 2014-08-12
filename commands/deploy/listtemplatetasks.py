#########################################################################
# 
# Copyright 2013 Cloud Sidekick
# __________________
# 
#  All Rights Reserved.
# 
# NOTICE:  All information contained herein is, and remains
# the property of Cloud Sidekick and its suppliers,
# if any.  The intellectual and technical concepts contained
# herein are proprietary to Cloud Sidekick
# and its suppliers and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Cloud Sidekick.
#
#########################################################################

import commands.catocommand
from commands.param import Param

class ListTemplateTasks(commands.catocommand.CatoCommand):

    Description = 'Lists all Tasks associated with an Application Template and the corresponding sequence or action'
    API = 'list_template_tasks'
    Examples = '''
_To list all tasks associated with an application template and version_

    maestro-list-application-template-tasks -t "Sample Application" -v 5 
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
