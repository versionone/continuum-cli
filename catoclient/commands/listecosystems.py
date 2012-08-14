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

import json

class ListEcosystems(catoclient.catocommand.CatoCommand):

    Description = 'Lists Ecosystems'
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.')]

    def display_ecosystems(self, ecosystems):

        ecosystems_dict = json.loads(ecosystems) if ecosystems else {}
        self.print_results(ecosystems_dict, ['ID','Name','StormStatus'])

    def main(self):

        return self.call_api('ecoMethods/list_ecosystems', ['filter'])

    def main_cli(self):
        ecosystems = self.main()
        self.display_ecosystems(ecosystems)

