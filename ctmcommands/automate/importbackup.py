#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class ImportBackup(ctmcommands.cmd.CSKCommand):

    Description = '''DEPRECATED: Please use `ctm-import-task`.
    
    Imports a task backup file into the system. This file can include one or
                    more tasks within it and must be XML or JSON formatted'''
    API = 'import_backup'
    Examples = '''
    ctm-import-backup -f ~/mytask01.xml
'''
    Options = [Param(name='file', short_name='f', long_name='file',
                     optional=False, ptype='string',
                     doc='The file name of the backup file.'),
               Param(name='on_conflict', short_name='c', long_name='on_conflict',
                     optional=True, ptype='string',
                     doc='Action to take if one or more Tasks have a conflict. "replace", "cancel".')]

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
            answer = input("\n\n\nDEPRECATION WARNING - This command is deprecated and will be removed soon.  Use `ctm-import-task` instead.\n\n\n\nImporting a backup file will add Tasks to your system, possibly updating existing Tasks.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['import_text', 'on_conflict'], verb='POST')
            print(results)
