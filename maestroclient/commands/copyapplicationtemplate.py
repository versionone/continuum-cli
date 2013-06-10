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

class CopyApplicationTemplate(catoclient.catocommand.CatoCommand):

    Description = 'Copies an Application Template.'
    Options = [Param(name='template', short_name='t', long_name='template',
                     optional=False, ptype='string',
                     doc='The Application Template to copy.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=False, ptype='string',
                     doc='A version for the new Template.'),
               Param(name='newname', short_name='nn', long_name='newname',
                     optional=False, ptype='string',
                     doc='A name for the new Template.'),
               Param(name='newversion', short_name='nv', long_name='newversion',
                     optional=False, ptype='string',
                     doc='A version for the new Template.')
               ]

    def main(self):
        results = self.call_api('depMethods/copy_application_template', ['newname', 'newversion', 'template', 'version'])
        print(results)
