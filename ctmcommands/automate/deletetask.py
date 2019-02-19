#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class DeleteTask(ctmcommands.cmd.CSKCommand):

    Description = 'Deletes a Task.'
    API = 'delete_task'
    Examples = '''
_To delete a task that does not have any runtime history_

    ctm-delete-task -t "mytask01"

_To force a delete of a task that has runtime history_

    ctm-delete-task -f "mytask01" -f
'''
    Options = [Param(name='task', short_name='t', long_name='task',
                     optional=False, ptype='string',
                     doc='The ID or Name of the Task to delete.'),
               Param(name='force_delete', short_name='f', long_name='force_delete',
                     optional=True, ptype='boolean',
                     doc='Force the deletion of a Task, even if it has history and references.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("WARNING: This is a utility function.\n\nDeleting a Task cannot be undone.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['task', 'force_delete'])
            print(results)
