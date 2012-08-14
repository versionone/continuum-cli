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

class GetEcosystemObjects(catoclient.catocommand.CatoCommand):

    Description = 'Retrieves Ecosystem Objects'
    Options = [Param(name='ecosystem', short_name='e', long_name='ecosystem',
                     optional=False, ptype='string',
                     doc='Value can be either an ecosystem id or ecosystem name.')]

    def display_ecosystem_objects(self, results):
        result_dict = json.loads(results) if results else {}
        self.print_results(result_dict, ['EcosystemObjectType','EcosystemObjectID', 'CloudName', 'AddedDate'])

    def main(self):

        return self.call_api('ecoMethods/get_ecosystem_objects', ['ecosystem'])

    def main_cli(self):
        results = self.main()
        self.display_ecosystem_objects(results)

