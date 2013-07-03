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

import catoclient.catocommand
from catoclient.param import Param

class GetApplicationTemplate(catoclient.catocommand.CatoCommand):

    Description = 'Gets an Application Template.'
    Options = [Param(name='template', short_name='t', long_name='template',
                     optional=False, ptype='string',
                     doc='Name of the Application Template.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=False, ptype='string',
                     doc='The Application Template Version.'),
               Param(name='getdefinition', short_name='d', long_name='desc',
                     optional=True, ptype='boolean',
                     doc='Will only return the JSON definition file.'),
               Param(name='geticon', short_name='i', long_name='owner',
                     optional=True, ptype='boolean',
                     doc='Will only return the Base64 encoded icon.')
               ]

    def main(self):
        results = self.call_api('get_application_template', ['template', 'version', 'getdefinition', 'geticon'])
        print(results)
