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

import catoclient.catocommand
from catoclient.param import Param

class DeleteSchedule(catoclient.catocommand.CatoCommand):

    Description = 'Deletes a Cato task schedule and all queued execution plans.'
    API = 'delete_schedule'
    Examples = '''
        cato-delete-schedule -s "157545d8-7df9-11e3-ab87-da5f4e6a2990"
    '''
    Options = [Param(name='schedule_id', short_name='s', long_name='schedule_id',
                     optional=False, ptype='string',
                     doc='The UUID of the Schedule to delete.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("WARNING: This is a utility function.\n\nDeleting a Schedule cannot be undone.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['schedule_id'])
            print(results)
