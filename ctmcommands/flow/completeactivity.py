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


class CompleteActivity(ctmcommands.cmd.CSKCommand):

    Description = """Given a Package Name, Revision (or Full Version), and Activity Name - will complete that Activity with either 'success' or 'failure'.

Returns: `success` on success, errors otherwise."""

    API = 'complete_activity'
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
               Param(name='notes', short_name='n', long_name='notes',
                     optional=True, ptype='string',
                     doc='Notes to be placed on the Activity.'),
               Param(name='revision', short_name='r', long_name='revision',
                     optional=True, ptype='string',
                     doc='Revision of Package containing the Control. (Takes precedence over "fullversion" if both are provided.)'),
               Param(name='full_version', short_name='f', long_name='full_version',
                     optional=True, ptype='string',
                     doc='Full Version label of the Package containing the Control.'),
               Param(name='forcewith', long_name='forcewith',
                     optional=True, ptype='string',
                     doc='Force the completion.  (Will mark ALL Controls with the provided value - must be `pass` or `fail`.)'),
               Param(name='failure', long_name='failure',
                     optional=True, ptype='boolean',
                     doc='Mark the Activity as a Failure. (Will default to `success` if omitted.)'),
               Param(name='completion_time', short_name='t', long_name='completion_time',
                     optional=True, ptype='string',
                     doc='Mark the Activity complete at a specified time.'),
               Param(name='timezone', short_name='z', long_name='timezone',
                     optional=True, ptype='string',
                     doc='Optional modifier for "completion_time".'),
               ]

    def main(self):
        results = self.call_api(self.API, ['package', 'phase', 'activity', 'notes', 'revision', 'full_version', 'forcewith', 'failure', 'completion_time', 'timezone'])
        print(results)
