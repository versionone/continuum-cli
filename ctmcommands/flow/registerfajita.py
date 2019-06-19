#########################################################################
#
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################
import json

import ctmcommands.cmd
from ctmcommands.param import Param


class RegisterFajita(ctmcommands.cmd.CSKCommand):

    Description = 'Registers a Fajita with this Continuum instance. Usually this command will not be called directly. Instead, you should call ctm-install-fajita'
    API = 'register_fajita'
    Examples = '''
    ctm-install-fajita "Fajita Name"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='Name of the Fajita to register.'),
               Param(name='catalog', short_name='c', long_name='catalog',
                     optional=False, ptype='string',
                     doc='Catalog imported as part of this fajita. This is expected to match the result of `ctm-import-catalog -h false`')
               ]

    def main(self):
        catalog_results = json.loads(self.catalog)

        import_dict = {
            "name": self.name,
            "tasks": [task_id for task_id, import_result in catalog_results["tasks"].viewitems() if import_result]
        }
        results = self.call_api(self.API, data=json.dumps(import_dict), verb='POST', content_type="application/json")
        print(results)
