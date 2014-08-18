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

import cskcommands.cmd
from cskcommands.param import Param

class ListApplicationTemplates(cskcommands.cmd.CSKCommand):

    Description = 'Lists application deployment template and their high level properties'
    API = 'list_application_templates'
    Examples = '''
_To list all application templates_
    
    maestro-list-application-templates

_To list all application templates with a certain string in the name or description_

    maestro-list-application-templates -f "sample app"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='matches if the filter string is in the result')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
