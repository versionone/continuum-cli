#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class ResetPassword(cskcommands.cmd.CSKCommand):

    Description = "Resets a User's login password."
    API = 'reset_password'
    Examples = '''
_Reset a User's password to a random password which will be emailed to the user_

    csk-reset-password -u "username1" bob -g

_Reset a User's password to a specified password_

    csk-reset-password -u "username1" -p "passw0rd"
'''
    Options = [Param(name='password', short_name='p', long_name='password',
                     optional=True, ptype='string',
                     doc='The new password.'),
               Param(name='user', short_name='u', long_name='user',
                     optional=True, ptype='string',
                     doc='The ID or Name of a User Account.'),
               Param(name='generate', short_name='g', long_name='generate',
                     optional=True, ptype='boolean',
                     doc='Generate a new, random password.')
               ]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("Are you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['user', 'password', 'generate'])
            print(results)
