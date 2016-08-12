#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class CreateAsset(ctmcommands.cmd.CSKCommand):

    Description = 'Creates a new fixed address Asset.'
    API = 'create_asset'
    Examples = '''
    ctm-create-asset -n "Test 123" -s "Active" -a "10.10.2.2" -d "test02" -t "1433" -u "appuser" -p "passw0rd"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the new Asset.'),
               Param(name='status', short_name='s', long_name='status',
                     optional=True, ptype='string',
                     doc='Status, either "Active" or "Inactive".  ("Active" if omitted.)'),
               Param(name='address', short_name='a', long_name='address',
                     optional=True, ptype='string',
                     doc='Network address of the Asset.'),
               Param(name='port', short_name='t', long_name='port',
                     optional=True, ptype='string',
                     doc='Service port of the Asset.'),
               Param(name='db_name', short_name='d', long_name='db_name',
                     optional=True, ptype='string',
                     doc='A database name.'),
               Param(name='user', short_name='u', long_name='user',
                     optional=True, ptype='string',
                     doc='A User ID.'),
               Param(name='password', short_name='p', long_name='password',
                     optional=True, ptype='string',
                     doc='A Password.'),
               Param(name='shared_credential', short_name='c', long_name='shared_credential',
                     optional=True, ptype='string',
                     doc='A Shared Credential.'),
               Param(name='conn_string', long_name='conn_string',
                     optional=True, ptype='string',
                     doc='A full connection string. (Not typical.)')
               ]

    def main(self):
        results = self.call_api(self.API, ['name', 'status', 'address', 'port', 'db_name', 'user', 'password', 'shared_credential', 'conn_string'])
        print(results)
