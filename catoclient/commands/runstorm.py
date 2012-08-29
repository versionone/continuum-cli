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

class RunStorm(catoclient.catocommand.CatoCommand):

    Description = 'Provisions resources using Cato Storm.'
    Options = [Param(name='ecotemplate', short_name='e', long_name='ecotemplate',
                     optional=False, ptype='string',
                     doc='The ID or Name of the source Ecotemplate.'),
               Param(name='ecosystem_name', short_name='n', long_name='ecosystem_name',
                     optional=False, ptype='string',
                     doc='A name for the new Ecosystem.'),
               Param(name='account', short_name='a', long_name='account',
                     optional=False, ptype='string',
                     doc='The ID or Name of Cloud Account credentials to use.'),
               Param(name='cloud', short_name='c', long_name='cloud',
                     optional=False, ptype='string',
                     doc='The ID or Name of Cloud where the resources will be provisioned.'),
               Param(name='parameterfile', short_name='p', long_name='parameterfile',
                     optional=True, ptype='string',
                     doc='The file name of a Parameter XML file.')
               ]

    def main(self):
        try:
            # first, we need to load the parameters xml from a file
            self.parameter_xml = None
            if self.parameterfile:
                fn = self.parameterfile
                with open(fn, 'r') as f_in:
                    if not f_in:
                        print("Unable to open file [%s]." % fn)
                    data = f_in.read()
                    if data:
                        self.parameter_xml = data
            
            results = self.call_api('stormMethods/runstorm', ['ecotemplate', 'ecosystem_name', 'account', 'cloud', 'parameter_xml'])
            print(results)
        except ValueError:
            # the results could not be parsed as JSON, just return them
            print(results)
        except Exception as ex:
            raise ex
