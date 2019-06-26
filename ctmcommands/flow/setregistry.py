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


class SetRegistry(ctmcommands.cmd.CSKCommand):

    Description = """Sets values in a specific Registry document.

Returns `success` on success, errors otherwise."""

    API = 'set_registry'
    Examples = ''''''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='Name of the Registry document.'),
               Param(name='value', short_name='v', long_name='value',
                     optional=True, ptype='string',
                     doc="""Value to set at specified path, or entire document.
                       If omitted, target key or document will be cleared."""),
               Param(name='path', short_name='p', long_name='path',
                     optional=True, ptype='string',
                     doc="If specified, will place `value` at this path.  If omitted, will update the entire document."),
               Param(name='action', short_name='a', long_name='action',
                     optional=True, ptype='string',
                     doc="Valid values: set | unset | addtoset | push | pull | merge | merge_right_to_left"),
               Param(name='create', short_name='c', long_name='create',
                     optional=True, ptype='string',
                     doc="Create named Registry if it doesn't exist? Valid values: true | false")
               ]

    def main(self):
        try:
            self.value = json.loads(self.value)
        except:
            raise Exception("set_registry - provided type is not mergeable")
        args = {
            'name': self.name,
            'value': self.value,
            'path': self.path,
            'action': self.action,
            'create': self.create
        }
        results = self.call_api(self.API, data=json.dumps(args), verb='POST', content_type="application/json")
        print(results)
