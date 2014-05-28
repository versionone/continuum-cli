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

class CreateApplicationTemplate(catoclient.catocommand.CatoCommand):

    Description = """Creates a new Application Template.
    
Name and Version are required properties.

Specify a JSON definition file if desired.  

If no Template is provided, the Application Template will be created with an empty definition file."""
    
    API = 'create_application_template'
    Examples = '''
_To create an application template from an existing json definition and icon file_

    maestro-create-application-template -n "MyApp" -v "1" -d "MyApp description goes here" -t "myapp.json" -i "myapp.png"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the Application Template.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=False, ptype='string',
                     doc='The Application Template version.'),
               Param(name='description', short_name='d', long_name='description',
                     optional=True, ptype='string',
                     doc='Description of this Application definition.'),
               Param(name='templatefile', short_name='t', long_name='templatefile',
                     optional=True, ptype='string',
                     doc='A JSON document formatted as an Application definition.'),
               Param(name='iconfile', short_name='i', long_name='iconfile',
                     optional=True, ptype='string',
                     doc='An icon for the Application Template.'),
               Param(name='makeavailable', short_name='a', long_name='makeavailable',
                     optional=True, ptype='boolean',
                     doc='Flag this Application as "Available".')
               ]

    def main(self):
        import os
        import base64

        self.template = None
        if self.templatefile:
            fn = os.path.expanduser(self.templatefile)
            with open(fn, 'r') as f_in:
                if not f_in:
                    print("Unable to open file [%s]." % fn)
                self.template = f_in.read()

        self.icon = None
        if self.iconfile:
            fn = os.path.expanduser(self.iconfile)
            with open(fn, 'r') as f_in:
                if not f_in:
                    print("Unable to open file [%s]." % fn)
                self.icon = base64.b64encode(f_in.read())

        results = self.call_api(self.API, ['name', 'version', 'description', 'template', 'icon', 'makeavailable'])
        print(results)
