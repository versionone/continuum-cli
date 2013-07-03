#########################################################################
# 
# Copyright 2013 Cloud Sidekick
# __________________
# 
#  All Rights Reserved.
# 
# NOTICE:  All information contained herein is, and remains
# the property of Cloud Sidekick and its suppliers,
# if any.  The intellectual and technical concepts contained
# herein are proprietary to Cloud Sidekick
# and its suppliers and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Cloud Sidekick.
#
#########################################################################

import os
import json
import glob

import catoclient.catocommand
from catoclient.param import Param

class DeleteApplicationTemplate(catoclient.catocommand.CatoCommand):

    Description = """Deletes an Application Template.
        
        * If --deletetasks is provided, the command will delte Tasks *directly referenced* by the definition file.
            (Indirectly referenced Tasks, such at those included in 'Subtask' and 'Run Task' commands.) 
        
        * If --inputdirectory is provided, then ALL TASKS listed in the backup directory will be deleted from the target system.
        """
    Options = [Param(name='template', short_name='t', long_name='template',
                     optional=False, ptype='string',
                     doc='Name of the Application Template.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=False, ptype='string',
                     doc='The Application Template Version.'),
               Param(name='deletetasks', long_name='deletetasks',
                     optional=True, ptype='boolean',
                     doc='If provided, all referenced Tasks will be *forcibly deleted*!'),
               Param(name='inputdirectory', short_name='i', long_name='inputdirectory',
                     optional=True, ptype='string',
                     doc='Directory where the Application Template files exist.')
               ]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("WARNING: This is a utility function.\n\nDeleting an Application Template cannot be undone.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            # NOTE: since this command is capable of being run from a backup directory, it 
            # goes one step further when deleting tasks.
            #     if 'deletetasks' is provided, it will delete every task from the system that's listed in the backup directory.
            if self.inputdirectory:
                rootdir = os.path.expanduser(self.inputdirectory)
                # the directory must exist
                if not os.path.exists(rootdir):
                    print "The directory [%s] does not exist." % (rootdir)
                    return

                taskdir = os.path.join(rootdir, "tasks")
                for fn in glob.glob(os.path.join(taskdir, "*.csk")):
                    with open(fn, 'r') as f_in:
                        if not f_in:
                            print("Unable to open Task file [%s]." % fn)
                        data = f_in.read()
                        if data:
                            # we gotta read the task file to get the name and version so we can delete it
                            t = json.loads(data)
                            if "Name" in t and "Version" in t:
                                # inefficient at the moment, but hit the API to delete the task.
                                # there should be an API endpoint that deletes from a list of task name/version pairs.
                                self.task = t["Name"]
                                self.force_delete = True
                                print self.call_api('delete_task', ['task', 'force_delete'])

            # now, lets do the api call that deletes the template
            results = self.call_api('delete_application_template', ['template', 'version', 'deletetasks'])
            print(results)
