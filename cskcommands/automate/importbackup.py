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

class ImportBackup(cskcommands.cmd.CSKCommand):

    Description = '''Imports a task backup file into the system. This file can include one or
                    more tasks within it and must be XML or JSON formatted'''
    API = 'import_backup'
    Examples = '''
    cato-import-backup -f ~/mytask01.xml
'''
    Options = [Param(name='file', short_name='f', long_name='file',
                     optional=False, ptype='string',
                     doc='The file name of the backup file.'),
               Param(name='on_conflict', short_name='c', long_name='on_conflict',
                     optional=True, ptype='string',
                     doc='Action to take if one or more Tasks have a conflict. "replace", "minor", "major", "cancel".')]

    def main(self):
        self.import_text = None
        if self.file:
            import os
            fn = os.path.expanduser(self.file)
            with open(fn, 'r') as f_in:
                if not f_in:
                    print("Unable to open file [%s]." % fn)
                data = f_in.read()
                if data:
                    self.import_text = data
                else:
                    print("File is empty.")
                    return

        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("\nImporting a backup file will add Tasks to your system, possibly updating existing Tasks.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['import_text', 'on_conflict'])
            print(results)

