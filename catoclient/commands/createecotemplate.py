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

class CreateEcotemplate(catoclient.catocommand.CatoCommand):

    Description = 'Create an Ecosystem Template.'
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='A name for the new Ecotemplate.'),
               Param(name='description', short_name='d', long_name='description',
                     optional=True, ptype='string',
                     doc='A description of the new Ecotemplate.'),
               Param(name='storm_url', short_name=None, long_name='storm_url',
                     optional=True, ptype='string',
                     doc='The URL of a Storm template.'),
               Param(name='storm_file', short_name=None, long_name='storm_file',
                     optional=True, ptype='string',
                     doc='The file name of a Storm template.')
               ]

    def main(self):
        try:
            # So, you can't specify a storm_url AND a storm_file
            # if both are provided, the storm_file wins.
            
            self.storm_file_type = ""
            self.storm_file_text = ""

            if self.storm_url:
                self.storm_file_type = "URL"
                self.storm_file_text = self.storm_url
            
            if self.storm_file:
                fn = self.storm_file
                with open(fn, 'r') as f_in:
                    if not f_in:
                        print("Unable to open file [%s]." % fn)
                    data = f_in.read()
                    if data:
                        self.storm_file_type = "Text"
                        self.storm_file_text = data
            
            
            results = self.call_api('ecoMethods/create_ecotemplate', ['name', 'description', 'storm_file_type', 'storm_file_text'])
            print(results)
        except ValueError:
            # the results could not be parsed as JSON, just return them
            print(results)
        except Exception as ex:
            raise ex
