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

class GetApplicationTemplate(commands.catocommand.CatoCommand):

    Description = 'Retrieves the properties of an application template'
    API = 'get_application_template'
    Examples = '''
_To get the high level properties of an application template_

    maestro-get-application-template -t "Spring Petclinic" -v 1

_To get the json formatted definition for the application template and redirect to a file_

    maestro-get-application-template -t "Spring Petclinic" -v 1 -d > petclinic.json

_To get retrieve a base64 encoded icon file for an application template and decode it_

    maestro-get-application-template -t "Spring Petclinic" -v 1 -i | base64 --decode > petclinic.png



'''
    Options = [Param(name='template', short_name='t', long_name='template',
                     optional=False, ptype='string',
                     doc='Name of the Application Template.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=False, ptype='string',
                     doc='The Application Template Version.'),
               Param(name='getdefinition', short_name='d', long_name='desc',
                     optional=True, ptype='boolean',
                     doc='Will only return the JSON definition file.'),
               Param(name='geticon', short_name='i', long_name='icon',
                     optional=True, ptype='boolean',
                     doc='Will only return the Base64 encoded icon.')
               ]

    def main(self):
        results = self.call_api(self.API, ['template', 'version', 'getdefinition', 'geticon'])
        print(results)
