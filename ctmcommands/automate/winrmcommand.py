#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

"""
IMPORTANT NOTE:

Unlike most other commands, this file actually contains two classes.

One for issuing a Windows remote 'shell' command, and another very similar
one for issuing a Windows remote POWERSHELL command.
"""

import ctmcommands.cmd
from ctmcommands.param import Param


class WinRM(ctmcommands.cmd.CSKCommand):

    Description = 'Test WinRM connections and issue commands.'
    API = "winrm_command"
    Examples = '''
    ctm-winrm -uusername -ppassword -sserver -c"dir c:"
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
               Param(name='command', short_name='c', long_name='command',
                     optional=True, ptype='string',
                     doc='A command to execute via WinRM.')
               ]

    def main(self):
        results = self.call_api(self.API, ['server', 'user', 'password', 'asset', 'kerberos', 'command'])
        print(results)


class WinRMPS(ctmcommands.cmd.CSKCommand):

    Description = 'Test WinRM connections and issue commands.'
    API = "winrm_command"
    Examples = '''
    ctm-powershell -uusername -ppassword -sserver -c"write-host 'Hello World'"
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
               Param(name='command', short_name='c', long_name='command',
                     optional=True, ptype='string',
                     doc='A command to execute via WinRM.')
               ]

    def main(self):
        # important, flip a switch to tell the api function this is a powershell command
        self.powershell = True
        
        results = self.call_api(self.API, ['server', 'user', 'password', 'asset', 'kerberos', 'powershell', 'command'])
        print(results)
