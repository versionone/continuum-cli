#########################################################################
# Copyright 2011 Cloud Sidekick
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#########################################################################

import commands.catocommand
from commands.param import Param

class DeleteTask(commands.catocommand.CatoCommand):

    Description = 'Deletes a Task.'
    API = 'delete_task'
    Examples = '''
_To delete a task that does not have any runtime history_

    cato-delete-task -t "mytask01"

_To force a delete of a task that has runtime history_

    cato-delete-task -f "mytask01" -f
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
