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

import cskcommands.cmd
from cskcommands.param import Param

class ListProcesses(cskcommands.cmd.CSKCommand):

    Description = 'Lists server processes (poller, messenger, etc.) along with heartbeat information.'
    API = 'list_processes'
    Examples = '''
    cato-list-processes
'''
    Options = []

    def main(self):

        return self.call_api(self.API, [])

    def main_cli(self):
        results = self.main()
        print(results)

