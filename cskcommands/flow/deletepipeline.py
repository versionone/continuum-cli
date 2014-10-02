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


class DeletePipeline(cskcommands.cmd.CSKCommand):

    Description = 'Delete a Pipeline Definition.'
    API = 'delete_pipeline'
    Examples = '''
    csk-delete-pipeline -p "PipelineName"
'''
    Options = [Param(name='pipeline', short_name='p', long_name='pipeline',
                     optional=False, ptype='string',
                     doc='Value can be either a Definition ID or Name.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("Are you sure (y/n)? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['pipeline'])
            print(results)
