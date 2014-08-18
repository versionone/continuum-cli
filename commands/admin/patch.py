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

class Patch(commands.catocommand.CatoCommand):

    Description = """If enabled, allows remote patching of a source or configuration file."""
    API = 'patch'
    Examples = ''''''
    Options = [Param(name='path', short_name='p', long_name='path',
                     optional=False, ptype='string',
                     doc='Path of file to patch.'),
               Param(name='newfile', short_name='n', long_name='newfile',
                     optional=False, ptype='string',
                     doc='Replacement file.'),
               Param(name='authcode', short_name='a', long_name='authcode',
                     optional=False, ptype='string',
                     doc='Authorization code.')
               ]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("WARNING: This is a Administrator function.\n\nThis cannot be undone.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            if self.newfile:
                import os
                fn = os.path.expanduser(self.newfile)
                with open(fn, 'r') as f_in:
                    if not f_in:
                        print("Unable to open file [%s]." % fn)
                    self.content = f_in.read()
            results = self.call_api(self.API, ['path', 'content', 'authcode'])
            print(results)
