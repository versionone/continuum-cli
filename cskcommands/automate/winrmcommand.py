#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class WinRM(cskcommands.cmd.CSKCommand):

    Description = 'Test WinRM connections and issue commands.'
    API = "winrm_command"
    Examples = '''
    ccl-winrm -c"dir c:"
'''
    Options = [Param(name='server', short_name='s', long_name='server',
                     optional=True, ptype='string',
                     doc='Windows server address.'),
               Param(name='user', short_name='u', long_name='user',
                     optional=True, ptype='string',
                     doc='Windows User with WinRM permissions.'),
               Param(name='password', short_name='p', long_name='password',
                     optional=True, ptype='string',
                     doc='Windows User Password.'),
               Param(name='asset', short_name='a', long_name='asset',
                     optional=True, ptype='string',
                     doc='The ID or Name of an Asset to use instead of --server, --user and --password.'),
               Param(name='kerberos', short_name='k', long_name='kerberos',
                     optional=True, ptype='boolean',
                     doc='Use Kerberos (Domain) authentication.'),
               Param(name='powershell', long_name='powershell',
                     optional=True, ptype='boolean',
                     doc='Issue the provided --command as a PowerShell command.'),
               Param(name='command', short_name='c', long_name='command',
                     optional=True, ptype='string',
                     doc='A command to execute via WinRM.')
               ]

    def main(self):
        results = self.call_api(self.API, ['server', 'user', 'password', 'asset', 'kerberos', 'powershell', 'command'])
        print(results)

