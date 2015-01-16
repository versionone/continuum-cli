#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class CreateCredential(cskcommands.cmd.CSKCommand):

    Description = 'Creates a new set of Shared Credentials that can be used to log into other systems.'
    API = 'create_credential'
    Examples = '''
    csk-create-credential -n "adminuser" -d "Administrator User" -u "root" -p "passw0rd"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the new Credential, must be unique.'),
               Param(name='description', short_name='d', long_name='description',
                     optional=False, ptype='string',
                     doc='Credential description or long name.'),
               Param(name='username', short_name='u', long_name='username',
                     optional=False, ptype='string',
                     doc='The user/login name.'),
               Param(name='password', short_name='p', long_name='password',
                     optional=False, ptype='string',
                     doc='The password/privatekey.'),
               Param(name='domain', short_name='o', long_name='domain',
                     optional=True, ptype='string',
                     doc='An optional domain name for the credential.'),
               Param(name='privileged', short_name='v', long_name='privileged',
                     optional=True, ptype='string',
                     doc='Additional password required to put certain Cisco IOS devices into "privileged" mode.')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'description', 'username', 'password', 'domain', 'privileged'])
        print(results)
