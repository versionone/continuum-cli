#########################################################################
#
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class OverrideControl(ctmcommands.cmd.CSKCommand):

    Description = """Given a Package Revision, a Phase and a Control Name, will override that Control if it exists and is failed.

Returns: `success` on success, errors otherwise."""

    API = 'override_control'
    Examples = ''''''
    Options = [Param(name='package', short_name='p', long_name='package',
                     optional=False, ptype='string',
                     doc='Name of Package'),
               Param(name='phase', short_name='h', long_name='phase',
                     optional=False, ptype='string',
                     doc='Phase containing the Activity/Control to override..'),
               Param(name='activity', short_name='a', long_name='activity',
                     optional=False, ptype='string',
                     doc='Name of Activity'),
               Param(name='control', short_name='c', long_name='control',
                     optional=False, ptype='string',
                     doc='Name of Control.'),
               Param(name='reason', short_name='e', long_name='reason',
                     optional=False, ptype='string',
                     doc='Reason for overriding the Control.'),
               Param(name='revision', short_name='r', long_name='revision',
                     optional=True, ptype='string',
                     doc='Revision of Package containing the Control. (Takes precedence over "fullversion" if both are provided.)'),
               Param(name='full_version', short_name='f', long_name='full_version',
                     optional=True, ptype='string',
                     doc='Full Version label of the Package containing the Control.')
               ]

    def main(self):
        results = self.call_api(self.API, ['package', 'phase', 'activity', 'control', 'reason', 'revision', 'full_version'])
        print(results)
