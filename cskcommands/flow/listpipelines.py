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


class ListPipelines(cskcommands.cmd.CSKCommand):

    Description = 'Lists all Pipelines.'
    API = 'list_pipelines'
    Examples = '''
_List all Pipelines_

    csk-list-pipelines
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.')]

    def main(self):
        results = self.call_api(self.API, ['filter'])
        print(results)
