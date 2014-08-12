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
import glob
import json
import base64

import catoclient.catocommand
from catoclient.param import Param

class ImportApplicationTemplate(catoclient.catocommand.CatoCommand):

    Description = 'Imports an Application Template from a properly formatted directory.'
    API = ''
    Examples = ''''''
    Options = [Param(name='inputdirectory', short_name='i', long_name='inputdirectory',
                     optional=False, ptype='string',
                     doc='Directory where the Application Template files exist.'),
               Param(name='makeavailable', short_name='a', long_name='makeavailable',
                     optional=True, ptype='boolean',
                     doc='Flag this Application as "Available".'),
               Param(name='ignoreconflicts', long_name='ignoreconflicts',
                     optional=True, ptype='boolean',
                     doc="""If provided, the import process will handle Task and Report name conflicts aggressively.  
If Tasks or Reports with the same Name/Version exist, they will be overwritten.

Tasks do have an individual on_conflict option as well.  If 'ignoreconflicts' is set, 
but a Task also has explicitly set 'on_conflict=cancel', then that Task will be skipped
but the Template creation will complete.""")
               ]

    def main(self):
        """
        This command will make multiple API calls.
        
        Rollback on error requires additional API calls.
        
        Basic premise:
        1) spin all the files and create database objects
        2) be happy
        """
        rootdir = os.path.expanduser(self.inputdirectory)
        # the directory must exist
        if not os.path.exists(rootdir):
            print "The directory [%s] does not exist." % (rootdir)
            return
            
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("\nImporting an Application Template could possibly overwrite existing Tasks and Reports.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True
        if not go:
            return
        
        # subdirectories
        defdir = os.path.join(rootdir, "definition")
        icondir = os.path.join(rootdir, "icon")
        taskdir = os.path.join(rootdir, "tasks")
        reportdir = os.path.join(rootdir, "reports")

        
        app_details = None
        fn = os.path.expanduser(os.path.join(rootdir, "application.json"))
        with open(fn, 'r') as f_in:
            if not f_in:
                print("Unable to open file [%s]." % fn)
            data = f_in.read()
            if data:
                app_details = json.loads(data)

        if not app_details:
            print "Unable to read the Application Template details from application.json."
            return
        
        
        """
        OK, let's keep this clear in our heads... making an API call from a command
            assumes that all the properties of the call are defined as attributes of 'self'.
        
        Some of these property names will be reused across several calls, so be extra sure to keep them updated in context.
        """

        # we're gonna be taking all API responses as JSON
        self.output_format = "json"

        
        # this might seem backwards, but to keep it clean...
        # spin every task FIRST and stop if any of them exist, unless the plow flag is set.
        
        # get a list of all defined tasks
        self.show_all_versions = True
        existingtasks = self.call_api('list_tasks', ['filter', 'show_all_versions'])
        existingtasks = json.loads(existingtasks)
        existnames = [(x["Name"], x["Version"]) for x in existingtasks]

        # now load up the tasks in the import directory
        # we're gonna go ahead and read every file now.  
        # That's the only way to get the name/version/conflict out of each file.
        tasks2import = []
        possibleconflicts = []
        for fn in glob.glob(os.path.join(taskdir, "*.json")):
            with open(fn, 'r') as f_in:
                if not f_in:
                    print("Unable to open Task file [%s]." % fn)
                data = f_in.read()
                if data:
                    tasks2import.append(data)

                    # to see if a task *might* be a conflict, we first need a list of all the tasks
                    # we wanna import.  But if the task has an on_conflict other than 'cancel', 
                    # well that's not really a conflict, is it?
                    t = json.loads(data)
                    if "OnConflict" in t:
                        if t["OnConflict"] != "cancel":
                            continue
                    else:
                        possibleconflicts.append((t["Name"], t["Version"]))                    

        # if ignoreconflicts was not provided, we bail if there are conflicts
        # UNLESS those conflicts have an explicit OnConflict of "replace"
        
        # so, the set will match up the TWO ITEM tuples, and show conflicts.
        # Then, we'll spin it again looking at the THREE ITEM tuples and removing any that are set to 'replace'
        conflicts = list(set(existnames).intersection(possibleconflicts))
        
        if not self.ignoreconflicts and len(conflicts):
            # spin the full tasks2import looking 
            print "One or more Tasks in this Application Template already exist:"
            print "\n".join(["[%s] Version [%s]" % (t[0], t[1]) for t in conflicts])
            return


        # BUT, if ignoreconflicts WAS provided, we will plow tasks in even if they exist.
        # we did a return up above, so if we get here... we're plowing!

        # CREATE THE APPLICATION TEMPLATE
        self.name = app_details["Name"]
        self.version = app_details["Version"]
        self.description = app_details["Description"]
 
        self.template = None
        fn = os.path.expanduser(os.path.join(defdir, "definition.json"))
        with open(fn, 'r') as f_in:
            if not f_in:
                print("Unable to open file [%s]." % fn)
            self.template = f_in.read()
 
        self.icon = None
        try:
            fn = os.path.expanduser(os.path.join(icondir, "application.png"))
            with open(fn, 'r') as f_in:
                if not f_in:
                    print("Unable to open file [%s]." % fn)
                self.icon = base64.b64encode(f_in.read())
        except:
            pass
        
        response = self.call_api('create_application_template', ['name', 'version', 'description', 'template', 'icon', 'makeavailable', 'ignoreconflicts'])
        response = json.loads(response)
        if response.get("ID"):
            print "Application Template successfully created."
        
        # spin and create the tasks
        for tjson in tasks2import:
            self.json = tjson
            self.on_conflict = "replace"
            response = self.call_api('create_task_from_json', ['json', 'on_conflict'])
            response = json.loads(response)
            if response.get("Name"):
                print "Created/Updated Task [%s]" % response.get("Name")
                
        # and the canvas elements

        # importing canvas items is pretty easy.
        # 1) The first directory is the 'project'
        # 2) second directory is the component
        # 3) files below that.
        
        # a flat list of all the details
        everything = []
        projects = [ d for d in os.listdir(reportdir) if os.path.isdir(os.path.join(reportdir, d)) ]
        # filter out any invalid dirs
        projects = [ p for p in projects if "proj_" in p]
        if projects:
            for p in projects:
                pdir = os.path.join(reportdir, p)
                components = [ d for d in os.listdir(pdir) if os.path.isdir(os.path.join(pdir, d)) ]
                components = [ c for c in components if "comp_" in c]
                if components:
                    for c in components:
                        cdir = os.path.join(pdir, c)
                        files = [ f for f in os.listdir(cdir) if os.path.isfile(os.path.join(cdir, f)) ]
                        files = [ f for f in files if "item_" in f]
                        for f in files:
                            # open each file ...
                            fn = os.path.join(cdir, f)
                            with open(fn, 'r') as f_in:
                                if not f_in:
                                    print("Unable to open file [%s]." % fn)
                                data = f_in.read()
                            
                            everything.append((p.replace("proj_", ""), c.replace("comp_", ""), f.replace("item_", ""), data))
                            
        # finally, make the api call for each row (suboptimal I know, but whatever)
        for row in everything:
            self.project, self.component, self.name, self.data = row[:]        
            response = self.call_api('create_canvas_item', ['project', 'component', 'name', 'data', 'ignoreconflicts'])
            print response
        
        print "Success!"
        

            
