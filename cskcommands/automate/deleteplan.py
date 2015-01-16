#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class DeletePlan(cskcommands.cmd.CSKCommand):

    Description = 'Deletes a specific queued execution plan for a scheduled task.'
    API = 'delete_plan'
    Examples = '''
    csk-delete-plan -p 55
'''
    Options = [Param(name='plan_id', short_name='p', long_name='plan_id',
                     optional=False, ptype='string',
                     doc='The integer ID of the Plan to delete.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("WARNING: This is a utility function.\n\nDeleting a Plan cannot be undone.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['plan_id'])
            print(results)
