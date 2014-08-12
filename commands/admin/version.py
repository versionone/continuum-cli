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

class Version(commands.catocommand.CatoCommand):

    Description = 'Displays the Version by request from the API.'
    API = 'version'
    Examples = '''
    cato-version
'''
    Options = []

    def main(self):
        results = self.call_api(self.API, [])
        print(results)
