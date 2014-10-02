#########################################################################
#
# Copyright 2013 Cloud Sidekick
# __________________
#
#  All Rights Reserved.
#
# NOTICE:  All information contained herein is, and remains
# the property of Cloud Sidekick and its suppliers,
# if any.  The intellectual and technical concepts contained
# herein are proprietary to Cloud Sidekick
# and its suppliers and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Cloud Sidekick.
#
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param


class InitiatePipeline(cskcommands.cmd.CSKCommand):

    Description = """Initiate a Pipeline Definition with matching 'key' information.

Returns a Release Candidate Object."""

    API = 'initiate_pipeline'
    Examples = ''''''
    Options = [Param(name='definition', short_name='d', long_name='definition',
                     optional=False, ptype='string',
                     doc='Pipeline Definition to initiate.'),
               Param(name='project', short_name='p', long_name='project',
                     optional=False, ptype='string',
                     doc='The Project name with which to associate this instance.'),
               Param(name='group', short_name='g', long_name='group',
                     optional=False, ptype='string',
                     doc='Descriptive label of a group to summarize multiple instances of this definition/project.'),
               Param(name='name', short_name='n', long_name='name',
                     optional=True, ptype='string',
                     doc='An explicit name for the unique instance. (Autogenerated if omitted.)'),
               Param(name='details', short_name='d', long_name='details',
                     optional=True, ptype='string',
                     doc='A JSON object with additional details about this instance.')
               ]

    def main(self):
        results = self.call_api(self.API, ['definition', 'project', 'group', 'name', 'details'])
        print(results)
