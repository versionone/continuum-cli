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

class CreateEcosystem(catoclient.catocommand.CatoCommand):

    Description = 'Creates an empty Ecosystem.'
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the new Ecosystem.'),
               Param(name='ecotemplate', short_name='e', long_name='ecotemplate',
                     optional=False, ptype='string',
                     doc='The Ecotemplate this Ecosystem inherits from.'),
               Param(name='account', short_name='a', long_name='account',
                     optional=False, ptype='string',
                     doc='The ID or Name of Cloud Account credentials to use.'),
               Param(name='description', short_name='d', long_name='description',
                     optional=True, ptype='string',
                     doc='A description of the new Ecotemplate.')
               ]

    def main(self):
        try:
            
            results = self.call_api('ecoMethods/create_ecosystem', ['name', 'description', 'account', 'ecotemplate'])
            print(results)
        except ValueError:
            # the results could not be parsed as JSON, just return them
            print(results)
        except Exception as ex:
            raise ex
