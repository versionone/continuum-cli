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

import commands.catocommand
from commands.param import Param


class DeletePipelineInstance(commands.catocommand.CatoCommand):

    Description = """Permanently deletes a Pipeline Instance.
    
NOTE: at the moment, requires the '_id' of the Pipeline Instance.

Returns success or failure."""

    API = 'delete_pipelineinstance'
    Examples = ''''''
    Options = [Param(name='pi', short_name='i', long_name='i',
                     optional=False, ptype='string',
                     doc='ID of a Pipeline Instance.')
               ]

    def main(self):
        results = self.call_api(self.API, ['pi'])
        print(results)
