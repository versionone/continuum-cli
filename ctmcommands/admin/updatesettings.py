#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param

from builtins import input


class UpdateSettings(ctmcommands.cmd.CSKCommand):

    Description = """Update the configuration settings of a specific module.
    
This command accepts a JSON object representing the settings for a module.
    
"""
    API = 'update_settings'
    Examples = '''
_To change the SMTPServerAddress of the Messenger_
    
    ctm-update-settings -m Messenger -s '{"SMTPServerAddress":"smtp.gmail.com"}'
    
_To update all settings for a particular module using a json formatted settings file__
    
    ctm-update-settings -m Messenger -f /tmp/messenger_settings.json
'''
    Options = [Param(name='module', short_name='m', long_name='module',
                     optional=False, ptype='string',
                     doc='Name of the module to update.'),
               Param(name='settings', short_name='s', long_name='settings',
                     optional=True, ptype='string',
                     doc='JSON Settings object.'),
               Param(name='settingsfile', short_name='f', long_name='settingsfile',
                     optional=True, ptype='string',
                     doc='A JSON file representing a module Settings object.')
               ]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = input("WARNING: This is a Administrator function.\n\nUpdating settings will change the operation of the system.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            if self.settingsfile:
                import os
                fn = os.path.expanduser(self.settingsfile)
                with open(fn, 'r') as f_in:
                    if not f_in:
                        print("Unable to open file [%s]." % fn)
                    self.settings = f_in.read()
            results = self.call_api(self.API, ['module', 'settings'])
            print(results)
